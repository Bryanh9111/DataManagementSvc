# Databricks notebook source
from flask import jsonify
from datamanagementsvc import app, api
from datamanagementsvc.service import get_updated_data
from flask_restx import Resource
from flask_cors import CORS 

# Enable CORS for the Flask app
CORS(app)

ns = api.namespace('updated-data', description='Operations on updated data')

@ns.route('/process')
class DataProcess(Resource):
    def get(self):
        """
        Call DataSvc API, process data, and return updated data as JSON
        """
        data = get_updated_data()
        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)