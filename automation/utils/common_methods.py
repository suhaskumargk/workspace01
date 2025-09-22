import json
import openpyxl
import os
from typing import List
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class common_methods:
    @staticmethod
    def get_json_payload(path):
        """Get the data from json file."""
        with open(os.path.join(DATA_DIR, path), 'r') as f:
            payload = json.load(f)
        return payload
    
    @staticmethod
    def get_credentials_from_xlsx(path):
        """Get the data from xlsx file."""
        file_path = os.path.join(DATA_DIR, path)
        wb = openpyxl.load_workbook(file_path)
        try:
            ws = wb.active
            usernames = []
            passwords = []
            for row in ws.iter_rows(min_row=2, values_only=True):
                usernames.append(row[0])
                passwords.append(row[1])
            return usernames, passwords
        finally:
            wb.close()