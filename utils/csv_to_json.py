import csv
import json
from typing import List
import pandas as pd 

def csv_to_json(src: str, dest: str, fields: List[str]):
    csv_df = pd.read_csv(src, encoding='unicode_escape', names=fields)
    csv_df.to_json(dest, orient='records')

if __name__ == "__main__":
    fields: List[str] = [
        "InvoiceNo",	
        "StockCode",	
        "Description", 	
        "Quantity", 	
        "InvoiceDate", 	
        "UnitPrice", 
        "CustomerID", 
        "Country"
    ]

    csv_to_json(
        "./datasets/ecommerce_data.csv", 
        "./datasets/ecommerce_data.json", 
        fields
    )

