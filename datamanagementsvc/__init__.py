# Databricks notebook source
from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app, doc='/swagger/')

from datamanagementsvc import main
