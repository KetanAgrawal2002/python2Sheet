## SheetSync: CSV Import & Filter
SheetSync is a web application that allows users to upload a CSV file, select specific columns from it, and add the selected data to a Google Sheet. Users can also provide a Google Sheet link to append their data to an existing sheet.Users can also apply filters based on their specific requirements before appending a data and append only required data.
### Table of Contents

- [Features](#features)
- [Approach](#Approach)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Video](#Video)


### Features

- Upload a CSV file.
- Select specific columns from the CSV file.
- Create a new Google Sheet and add the selected data.
- Append data to an existing Google Sheet using a provided link.
- Allows user to filter data based on their requirements.
- Utilizes the Google Sheets API for seamless integration with Google Sheets.


### Approach
In this project, I begin by developing a Streamlit web application to serve as the user interface, leveraging Streamlit's simplicity for creating interactive web applications using Python. To ensure secure access to Google Sheets, user authentication is implemented using Google OAuth2. Users log in with their Google accounts, granting authorization for the application to interact with their Google Sheets.

The backbone of this project's functionality relies on the seamless integration with the Google Sheets API, facilitated by the googleapiclient.discovery module from the Google API client library. This module empowers the application to create, access, and manipulate Google Sheets programmatically, offering a high degree of flexibility and control.

The application offers two primary data input functionalities. Firstly, users can create new Google Sheets, specifying the sheet's name and CSV file they wish to include. Secondly, users can give a link to an existing Google Sheet, and append additional data to the selected sheet.

To enhance data management, a data filtering feature is also implemented. Users have the ability to define filter criteria based on column values, ensuring that only data meeting the specified conditions is added to Google Sheets. This functionality empowers users to tailor their data uploads to suit their precise needs, adding a layer of customization to the application's data management capabilities.
  

### Prerequisites

- [Python](https://www.python.org/) Ensure that you have Python installed on your computer.
- [Google Cloud Platform](https://cloud.google.com/) project with the Google Sheets API enabled.
- OAuth 2.0 credentials (client ID and client secret) for your Google Cloud project.

### Installation

1. Clone the repository:

    Open your terminal or command prompt and navigate to the directory where you want to clone the project. 

    Then, run the following command to clone the repository:
    ```ruby
    git clone https://github.com/StackItHQ/stackit-hiring-assignment-KetanAgrawal2002.git
    ```

3. Navigate to the project directory:
   
    ```ruby
    cd stackit-hiring-assignment-KetanAgrawal2002
    ```

4. Install the required dependencies:

     Run requirements.bat


6. Set up the Google Calendar credentials:
     
    Download and place the credentials.json file (which contains your Google Sheet API credentials) in the project root directory and also add the access token and refresh token in token.json

### Usage
5. Start the application:

     Once you have all the prerequisites ready, you can run the project locally by executing the index.py file using the command:  

    ```ruby
    streamlit run index.py
    ```


### Video





