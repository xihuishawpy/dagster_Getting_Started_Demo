
import csv

import requests

from dagster import asset


@asset
def cereals():
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    return list(csv.DictReader(lines))


# 上游资产名称作为参数传入

@asset
def nabisco_cereals(cereals):
    # nabisco_cereals 依赖于 cereals
    return [row for row in cereals if row["mfr"] == "N"]
