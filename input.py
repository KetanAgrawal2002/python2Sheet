from __future__ import print_function
import streamlit as st
import pandas as pd
import os.path
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow



def addData(data,title):
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    
    try:
        # records = data.to_records(index=False)
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                        fields='spreadsheetId') \
                .execute()

        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        
        body = {
            'values': data.values.tolist()
        }
        range_name = "Sheet1"
        result = service.spreadsheets().values().update(
                    spreadsheetId=spreadsheet.get('spreadsheetId'),
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                    ).execute()
        return "Data Added successfully"
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
            
            

    
    




# Set the title of the app
st.title("CSV File Upload App")

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
custom_title = st.text_input("Enter a custom title for the file (optional)")
# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the uploaded data
    # st.write("Uploaded CSV data:")
    # st.write(df)
    title = custom_title.strip() if custom_title else uploaded_file.name

    selected_columns = st.multiselect("Select columns to display", df.columns.tolist())

    # Check if any columns are selected
    if selected_columns:
        # Filter the DataFrame to display only the selected columns
        selected_df = df[selected_columns]
        st.write("Selected columns:")
        st.write(selected_df)
        
        
    else:
        st.warning("Please select at least one column to display.")
    
    if st.button("Add Data"):
        st.write(addData(selected_df,title))

    

