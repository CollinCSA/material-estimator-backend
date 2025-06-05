import os
import json
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheet config
SHEET_NAME = 'Estimator'
TAB_NAME = 'Projects'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

def authorize():
    creds_dict = json.loads(os.environ['GOOGLE_CREDS'])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, SCOPES)
    client = gspread.authorize(creds)
    
    print([s.title for s in client.opena11()])
    
    sheet = client.open(SHEET_NAME).worksheet(TAB_NAME)
    return sheet
    
def get_all_projects():
    sheet = authorize()
    return sheet.get_all_records()

def save_project(data):
    sheet = authorize()
    row = [
        data.get('Project ID', ''),
        data.get('Project Name', ''),
        data.get('Structure Type', ''),
        data.get('Materials', ''),
        data.get('Total Cost', ''),
        data.get('Best Vendor Map', ''),
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        data.get('Notes', '')
    ]
    sheet.append_row(row)
    return {"status": "success", "message": "Project saved."}
