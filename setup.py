# Databricks notebook source
from setuptools import setup, find_packages

setup(
    name='datamanagementsvc',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-RESTX',
        'requests',
    ],
)
