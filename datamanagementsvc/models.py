# Databricks notebook source
class UpdatedDataModel:
    def __init__(self, H1, H2, H3, H4, H5, H6, processed_flag):
        self.H1 = H1
        self.H2 = H2
        self.H3 = H3
        self.H4 = H4
        self.H5 = H5
        self.H6 = H6
        self.processed_flag = processed_flag 

    def to_dict(self):
        return {
            "H1": self.H1,
            "H2": self.H2,
            "H3": self.H3,
            "H4": self.H4,
            "H5": self.H5,
            "H6": self.H6,
            "processed_flag": self.processed_flag,
        }