      
# 一次性测所有的asset

import csv
import requests
from dagster import asset


@asset
def cereals():
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    return list(csv.DictReader(lines))


@asset
def nabisco_cereals(cereals):
    """Cereals manufactured by Nabisco"""
    return [row for row in cereals if row["mfr"] == "N"]


@asset
def cereal_protein_fractions(cereals):
    """
    For each cereal, records its protein content as a fraction of its total mass.
    """
    result = {}
    for cereal in cereals:
        total_grams = float(cereal["weight"]) * 28.35
        result[cereal["name"]] = float(cereal["protein"]) / total_grams

    return result


@asset
def highest_protein_nabisco_cereal(nabisco_cereals, cereal_protein_fractions):
    """
    The name of the nabisco cereal that has the highest protein content.
    """
    sorted_by_protein = sorted(
        nabisco_cereals, key=lambda cereal: cereal_protein_fractions[cereal["name"]]
    )
    return sorted_by_protein[-1]["name"]


from dagster import materialize

def test_cereal_assets():
    assets = [
        nabisco_cereals,
        cereals,
        cereal_protein_fractions,
        highest_protein_nabisco_cereal,
    ]
    
    # 物化所有的asset，允许详细查看执行的成败、计算产生的值
    result = materialize(assets)
    
    assert result.success
    assert result.output_for_node("highest_protein_nabisco_cereal") == "100% Bran"

