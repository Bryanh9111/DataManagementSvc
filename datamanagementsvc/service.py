# Databricks notebook source
import requests
from datamanagementsvc.models import UpdatedDataModel

def get_updated_data():
    # Call the DataSvc API to get the original data
    response = requests.get('http://127.0.0.1:5000/data/read') 
    original_data = response.json()

    updated_data = []
    for item in original_data:
        updated_item = UpdatedDataModel(
            item['H1'],
            item['H2'],
            item['H3'],
            item['H4'],
            item['H5'],
            item['H6'],
            processed_flag=True
        )
        updated_data.append(updated_item.to_dict())
    
    return updated_data