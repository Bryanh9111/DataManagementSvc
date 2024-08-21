# Databricks notebook source
import unittest
from datamanagementsvc import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_process_data(self):
        response = self.app.get('/updated-data/process')
        self.assertEqual(response.status_code, 200)
        self.assertIn('processed_flag', response.json[0])

if __name__ == "__main__":
    unittest.main()
