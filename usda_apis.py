# -*- coding: utf-8 -*-
"""USDA APIs.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OCcaObvXpp5WuXfLiDWxo8lclmOKStHu
"""

# @title USDA API (first version)


import requests
import streamlit as st
from prettytable import PrettyTable

# Set up the API endpoints and your API key
base_url = "https://api.nal.usda.gov/fdc/v1"
api_key = "QeMl3zbVBqDHTwy9nsjhjfiehADeE1CAlNPRYPfF"

# Function to search for a food by name
def search_food(query):
    endpoint = f"{base_url}/foods/search"
    params = {
        "api_key": api_key,
        "query": query
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data.get("foods", [])

# Function to get nutrient information for a food
def get_food_nutrients(food_id):
    endpoint = f"{base_url}/food/{food_id}"
    params = {
        "api_key": api_key
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data.get("foodNutrients", [])

# Function to calculate nutrient content for a given amount of food
def calculate_nutrients(food_id, amount):
    nutrients = get_food_nutrients(food_id)
    nutrient_content = {}
    for nutrient in nutrients:
        nutrient_name = nutrient.get("nutrient", {}).get("name")
        nutrient_value = nutrient.get("amount")
        nutrient_unit = nutrient.get("nutrient", {}).get("unitName")
        if nutrient_name and nutrient_value is not None:
            if nutrient_name in nutrient_content:
                nutrient_content[nutrient_name]["value"] += (nutrient_value / 100) * amount
            else:
                nutrient_content[nutrient_name] = {"value": (nutrient_value / 100) * amount, "unit": nutrient_unit}
    return nutrient_content

# Example usage
foods_consumed = [
    {"name": "Bread", "amount": 150},  # Amount in grams
    {"name": "Yogurt", "amount": 100},   # Amount in grams
    {"name": "Chicken Breast", "amount": 120}  # Amount in grams
]

total_nutrients = {}

# Initialize the PrettyTable
table = PrettyTable()
table.field_names = ["Nutrient"] + [food["name"] for food in foods_consumed] + ["Total"]

# Collect and sum the nutrient data for each food
for food in foods_consumed:
    search_results = search_food(food["name"])
    if search_results:
        food_id = search_results[0]["fdcId"]
        food_nutrients = calculate_nutrients(food_id, food["amount"])
        for nutrient, data in food_nutrients.items():
            if nutrient not in total_nutrients:
                total_nutrients[nutrient] = {"value": 0, "unit": data["unit"]}
            total_nutrients[nutrient]["value"] += data["value"]
            total_nutrients[nutrient][food["name"]] = data["value"]

# Populate the table with nutrient data for each food
for nutrient in total_nutrients.keys():
    row = [nutrient]
    total_value = 0
    for food in foods_consumed:
        value = total_nutrients[nutrient].get(food["name"], 0)
        row.append(f"{value:.2f}")
        total_value += value
    row.append(f"{total_value:.2f} {total_nutrients[nutrient]['unit']}")
    table.add_row(row)

# Print the table
print(table)

# @title USDA API (second version)

import requests
from prettytable import PrettyTable

# Set up the API endpoints and your API key
base_url = "https://api.nal.usda.gov/fdc/v1"
api_key = "QeMl3zbVBqDHTwy9nsjhjfiehADeE1CAlNPRYPfF"

# List of nutrients to include
nutrients_list = [
    "Carbohydrate, by difference", "Protein", "Total lipid (fat)", "Fatty acids, total saturated",
    "Fatty acids, total monounsaturated", "Fatty acids, total polyunsaturated", "Fatty acids, total trans",
    "Fiber, total dietary", "Sugars, total including NLEA", "Sugars, added", "Vitamin A, RAE",
    "Thiamin", "Riboflavin", "Niacin", "Pantothenic acid", "Vitamin B-6", "Biotin",
    "Folate, total", "Vitamin B-12", "Vitamin C, total ascorbic acid", "Vitamin D (D2 + D3)",
    "Vitamin E (alpha-tocopherol)", "Vitamin K (phylloquinone)", "Calcium, Ca", "Iron, Fe",
    "Magnesium, Mg", "Phosphorus, P", "Potassium, K", "Sodium, Na", "Zinc, Zn",
    "Copper, Cu", "Manganese, Mn", "Selenium, Se", "Cholesterol",
    "Alcohol, ethyl", "Caffeine", "Water", "Ash"
]

# Function to search for a food by name
def search_food(query):
    endpoint = f"{base_url}/foods/search"
    params = {
        "api_key": api_key,
        "query": query
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data.get("foods", [])

# Function to get nutrient information for a food
def get_food_nutrients(food_id):
    endpoint = f"{base_url}/food/{food_id}"
    params = {
        "api_key": api_key
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data.get("foodNutrients", [])

# Function to calculate nutrient content for a given amount of food
def calculate_nutrients(food_id, amount):
    nutrients = get_food_nutrients(food_id)
    nutrient_content = {}
    for nutrient in nutrients:
        nutrient_name = nutrient.get("nutrient", {}).get("name")
        nutrient_value = nutrient.get("amount")
        nutrient_unit = nutrient.get("nutrient", {}).get("unitName")
        if nutrient_name and nutrient_value is not None:
            if nutrient_name in nutrient_content:
                nutrient_content[nutrient_name]["value"] += (nutrient_value / 100) * amount
            else:
                nutrient_content[nutrient_name] = {"value": (nutrient_value / 100) * amount, "unit": nutrient_unit}
    return nutrient_content

# Example usage
foods_consumed = [
    {"name": "Banana", "amount": 150},  # Amount in grams
    {"name": "Yogurt", "amount": 200},   # Amount in grams
    {"name": "Chicken Breast", "amount": 100}  # Amount in grams
]

total_nutrients = {nutrient: {"value": None, "unit": "g"} for nutrient in nutrients_list}

# Initialize the PrettyTable
table = PrettyTable()
table.field_names = ["Nutrient"] + [food["name"] for food in foods_consumed] + ["Total"]

# Collect and sum the nutrient data for each food
for food in foods_consumed:
    search_results = search_food(food["name"])
    if search_results:
        food_id = search_results[0]["fdcId"]
        food_nutrients = calculate_nutrients(food_id, food["amount"])
        for nutrient in nutrients_list:
            if nutrient in food_nutrients:
                nutrient_value = food_nutrients[nutrient]["value"]
                total_nutrients[nutrient]["value"] = 0.0 if total_nutrients[nutrient]["value"] is None else total_nutrients[nutrient]["value"]
                total_nutrients[nutrient]["value"] += nutrient_value
                total_nutrients[nutrient][food["name"]] = nutrient_value
                total_nutrients[nutrient]["unit"] = food_nutrients[nutrient]["unit"]
            else:
                total_nutrients[nutrient][food["name"]] = "NP"

# Populate the table with nutrient data for each food
for nutrient in nutrients_list:
    row = [nutrient]
    total_value = 0
    for food in foods_consumed:
        value = total_nutrients[nutrient].get(food["name"], "NP")
        if isinstance(value, (int, float)):
            row.append(f"{value:.2f}" if value != 0.0 else "0.00")
            if value != "NP":
                total_value += value
        else:
            row.append(value)
    row.append(f"{total_value:.2f} {total_nutrients[nutrient]['unit']}" if total_value > 0 else "NP")
    table.add_row(row)

# Print the table
print(table)

"""**NOTE on the last version:**
I am still not sure that all available data from USDA APIs is extracted, since the number of nutrients is different from when a fixed number of nutrients is requested (in the format of a list named 'nutrients_list' in the prevoius code). Moreover, there are some discrepancies in the data, for instance the above code does not provdie any information regarding Vit A, but the code below does. It seems that the list in the above code is not sycronized with the actual information provided by USDA APIs. Also, the code below only provides the sum, whereas, the above below provides information with nutrient content of each individual food.
"""

# @title USDA API (third version)

import requests
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# Set up the API endpoints and your API key
base_url = "https://api.nal.usda.gov/fdc/v1"
api_key = "QeMl3zbVBqDHTwy9nsjhjfiehADeE1CAlNPRYPfF"

# Function to search for a food by name
def search_food(query):
    endpoint = f"{base_url}/foods/search"
    params = {
        "api_key": api_key,
        "query": query
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data.get("foods", [])

# Function to get nutrient information for a food
def get_food_nutrients(food_id):
    endpoint = f"{base_url}/food/{food_id}"
    params = {
        "api_key": api_key
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    return data.get("foodNutrients", [])

# Function to calculate nutrient content for a given amount of food
def calculate_nutrients(food_id, amount):
    nutrients = get_food_nutrients(food_id)
    nutrient_content = {}
    for nutrient in nutrients:
        nutrient_name = nutrient.get("nutrient", {}).get("name")
        nutrient_value = nutrient.get("amount")
        nutrient_unit = nutrient.get("nutrient", {}).get("unitName")
        if nutrient_name and nutrient_value is not None:
            if nutrient_name in nutrient_content:
                nutrient_content[nutrient_name]["value"] += (nutrient_value / 100) * amount
            else:
                nutrient_content[nutrient_name] = {"value": (nutrient_value / 100) * amount, "unit": nutrient_unit}
    return nutrient_content

# Example usage
patient_id = input("Enter Patient ID: ")
foods_consumed = [
    {"name": "Banana", "amount": 150},  # Amount in grams
    {"name": "Yogurt", "amount": 200},   # Amount in grams
    {"name": "Chicken Breast", "amount": 100}  # Amount in grams
]

total_nutrients = {}

# Collect and sum the nutrient data for each food
for food in foods_consumed:
    search_results = search_food(food["name"])
    if search_results:
        food_id = search_results[0]["fdcId"]
        food_nutrients = calculate_nutrients(food_id, food["amount"])
        for nutrient_name, nutrient_data in food_nutrients.items():
            if nutrient_name in total_nutrients:
                total_nutrients[nutrient_name]["value"] += nutrient_data["value"]
            else:
                total_nutrients[nutrient_name] = nutrient_data

# Create DataFrame for nutrient content
nutrient_df = pd.DataFrame(list(total_nutrients.items()), columns=["Nutrient", "Value"])
nutrient_df["Value"] = nutrient_df["Value"].apply(lambda x: x["value"]).round(2)

# Save DataFrame to Excel file
excel_file_name = f"{patient_id}_nutrient_data.xlsx"
nutrient_df.to_excel(excel_file_name, index=False)

# Print the nutrient data
print("Nutrient Data:")
print(nutrient_df)

# Plot pie chart for energy contributions
carbohydrate_value = total_nutrients.get("Carbohydrate, by difference", {"value": 0})["value"]
fat_value = total_nutrients.get("Total lipid (fat)", {"value": 0})["value"]
protein_value = total_nutrients.get("Protein", {"value": 0})["value"]

plt.figure(figsize=(10, 8))
plt.pie([carbohydrate_value, fat_value, protein_value],
        labels=["Carbohydrate", "Fat", "Protein"], autopct='%1.1f%%', startangle=140)
plt.title("Nutrient Composition")
plt.axis('equal')
plt.show()

# Download the Excel file
files.download(excel_file_name)
