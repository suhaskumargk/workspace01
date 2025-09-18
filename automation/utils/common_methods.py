import json
import openpyxl
import os
from typing import List

class common_methods:
    @staticmethod
    def get_json_payload(path):
        with open("./automation/data/" + path, 'r') as f:
            payload = json.load(f)
        return payload
    
    @staticmethod
    def get_credentials_from_xlsx(path):
        file_path = os.path.join("./automation/data/", path)
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