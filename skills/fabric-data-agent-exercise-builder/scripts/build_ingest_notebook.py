#!/usr/bin/env python3
"""Build a Fabric-compatible PySpark ingestion notebook (.ipynb) from a data manifest.

Input: manifest.json written by generate_synthetic_data.py (table names, typed columns,
expected row counts, lakehouse folder). Output: one .ipynb that, attached to a default
lakehouse, reads each CSV from the lakehouse Files area with an explicit schema, writes
it to a Delta table in overwrite mode, validates row counts, and returns a JSON summary
through mssparkutils.notebook.exit. The first code cell is tagged as the parameters
cell so the folder path can be overridden from a pipeline Notebook activity.

Usage:
  python build_ingest_notebook.py --manifest working/<slug>/authoring/manifest.json \
      --out working/<slug>/package/<Name>_Ingest.ipynb [--title "Load maintenance export"]

Deterministic: the same manifest always yields byte-identical output.
Standard library only. The notebook itself is never executed by this script.
"""
import argparse
import json
import sys

SPARK_TYPE = {
    "string": "StringType()",
    "int": "IntegerType()",
    "double": "DoubleType()",
    "date": "DateType()",
    "timestamp": "TimestampType()",
    "boolean": "BooleanType()",
}


def src(text):
    lines = text.strip("\n").split("\n")
    return [ln + "\n" for ln in lines[:-1]] + [lines[-1]]


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": src(text)}


def code(text, tags=None):
    meta = {"microsoft": {"language": "python", "language_group": "synapse_pyspark"}}
    if tags:
        meta["tags"] = tags
    return {"cell_type": "code", "execution_count": None, "metadata": meta,
            "outputs": [], "source": src(text)}


def build(manifest, title):
    tables = manifest["tables"]
    folder = manifest.get("lakehouse_folder", "Files/raw")
    cells = [md(f"# {title}\n\n"
                f"Loads the {len(tables)} exported files in `{folder}` into Delta tables in the "
                "default lakehouse. Each run replaces the tables with the current files and "
                "checks the row counts.")]

    cells.append(code(
        "# Parameters\n"
        f'source_folder = "{folder}"\n'
        "validate_row_counts = True",
        tags=["parameters"]))

    schema_lines = ["from pyspark.sql.types import (StructType, StructField, StringType, IntegerType,",
                    "                               DoubleType, DateType, TimestampType, BooleanType)",
                    "", "TABLES = {"]
    for t in tables:
        schema_lines.append(f'    "{t["name"]}": {{')
        schema_lines.append(f'        "file": "{t["csv"]}",')
        schema_lines.append(f'        "expected_rows": {t["row_count"]},')
        schema_lines.append('        "schema": StructType([')
        for c in t["columns"]:
            schema_lines.append(f'            StructField("{c["name"]}", {SPARK_TYPE[c["type"]]}, True),')
        schema_lines.append("        ]),")
        schema_lines.append("    },")
    schema_lines.append("}")
    cells.append(md("## Table definitions\n\nExplicit schemas keep column types stable from run to run."))
    cells.append(code("\n".join(schema_lines)))

    cells.append(md("## Load each file into a Delta table"))
    cells.append(code(
        "results = []\n"
        "for table_name, spec in TABLES.items():\n"
        "    path = f\"{source_folder.rstrip('/')}/{spec['file']}\"\n"
        "    df = (spark.read.format(\"csv\")\n"
        "          .option(\"header\", \"true\")\n"
        "          .option(\"dateFormat\", \"yyyy-MM-dd\")\n"
        "          .option(\"timestampFormat\", \"yyyy-MM-dd HH:mm:ss\")\n"
        "          .option(\"mode\", \"FAILFAST\")\n"
        "          .schema(spec[\"schema\"])\n"
        "          .load(path))\n"
        "    (df.write.format(\"delta\")\n"
        "       .mode(\"overwrite\")\n"
        "       .option(\"overwriteSchema\", \"true\")\n"
        "       .saveAsTable(table_name))\n"
        "    loaded = spark.read.table(table_name).count()\n"
        "    results.append({\"table\": table_name, \"rows\": loaded, \"expected\": spec[\"expected_rows\"]})\n"
        "    print(f\"{table_name}: {loaded} rows\")"))

    cells.append(md("## Validate row counts and return a run summary"))
    cells.append(code(
        "import json\n"
        "mismatches = [r for r in results if r[\"rows\"] != r[\"expected\"]]\n"
        "if validate_row_counts and mismatches:\n"
        "    raise ValueError(f\"Row count check did not match: {mismatches}\")\n"
        "summary = {\"status\": \"succeeded\", \"tables\": results}\n"
        "display(spark.createDataFrame(results))\n"
        "mssparkutils.notebook.exit(json.dumps(summary))"))

    for n, cell in enumerate(cells, 1):
        cell["id"] = f"cell-{n:02d}"   # nbformat 4.5 requires stable cell ids
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Synapse PySpark", "language": "Python", "name": "synapse_pyspark"},
            "language_info": {"name": "python"},
            "microsoft": {"language": "python", "language_group": "synapse_pyspark"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", default="Load source files into lakehouse tables")
    a = ap.parse_args()
    with open(a.manifest, encoding="utf-8") as f:
        manifest = json.load(f)
    for t in manifest["tables"]:
        for c in t["columns"]:
            if c["type"] not in SPARK_TYPE:
                sys.exit(f"unsupported type {c['type']} in {t['name']}.{c['name']}")
    nb = build(manifest, a.title)
    # every code cell must at least compile as Python
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            compile("".join(cell["source"]), "<cell>", "exec")
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(nb, f, indent=1, ensure_ascii=True)
        f.write("\n")
    print(json.dumps({"ok": True, "out": a.out, "tables": [t["name"] for t in manifest["tables"]],
                      "code_cells": sum(c["cell_type"] == "code" for c in nb["cells"])}))


if __name__ == "__main__":
    main()
