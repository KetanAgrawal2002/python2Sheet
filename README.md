
# **SheetSync**: CSV Import & Filter
**SheetSync** is a web application that allows users to upload a CSV file, select specific columns from it, and add the selected data to a Google Sheet. Users can also provide a Google Sheet link to append their data to an existing sheet.Users can also apply filters based on their specific requirements before appending a data and append only required data.

### Table of Contents
- [Problem Statement](#problem-statement-crafting-a-csv-importer-for-google-sheets)
- [Trailer](#trailer)
- [Approach](#Approach)
- [Prerequisites](#prerequisites)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Checklist](#checklist)
- [Credits](#credits)


### Problem Statement: Crafting a CSV Importer for Google Sheets

**Context**:
Data analysts around the world 🌍, handle massive amounts of data to derive meaningful insights for their organization 📊. Among the tools they use, Google Sheets 📈 stands out due to its ease of use, accessibility, and collaborative features. However, many analysts have identified a recurring pain point: the cumbersome process of importing CSV files into Google Sheets repeatedly.

A typical week of an analyst in an e-commerce company 🛒 involves receiving multiple CSV files 📁 containing sales, inventory, customer feedback, and more. The data from these files needs to be meticulously analyzed and presented in the company’s weekly meetings. However, instead of diving directly into analysis, most analysts need to spend an inordinate amount of time just importing and structuring these CSV files into Google Sheets ⏳. This repetitive, time-consuming task reduces the efficiency of these professionals and delays the extraction of crucial insights 😫.

**Today, I am going to make their lives better.**

**Problem Statement**:
Make a CSV Importer for Google Sheets that lets users drag and drop CSV files onto the Google Sheet. The moment they drop the CSV file, allow them to select which columns to import 🗂️.


### Approach
In this project, I begin by developing a Streamlit web application to serve as the user interface, leveraging Streamlit's simplicity for creating interactive web applications using Python. To ensure secure access to Google Sheets, user authentication is implemented using Google OAuth2. Users log in with their Google accounts, granting authorization for the application to interact with their Google Sheets.

The backbone of this project's functionality relies on the seamless integration with the Google Sheets API, facilitated by the googleapiclient.discovery module from the Google API client library. This module empowers the application to create, access, and manipulate Google Sheets programmatically, offering a high degree of flexibility and control.

The application offers two primary data input functionalities. Firstly, users can create new Google Sheets, specifying the sheet's name and CSV file they wish to include. Secondly, users can give a link to an existing Google Sheet, and append additional data to the selected sheet.

To enhance data management, a data filtering feature is also implemented. Users have the ability to define filter criteria based on column values, ensuring that only data meeting the specified conditions is added to Google Sheets. This functionality empowers users to tailor their data uploads to suit their precise needs, adding a layer of customization to the application's data management capabilities.


### Prerequisites
- [Python](https://www.python.org/) Ensure that Python is installed on your computer.
- [Google Cloud Platform](https://cloud.google.com/) project with the Google Sheets API enabled.
- OAuth 2.0 credentials (client ID and client secret) for your Google Cloud project.


###  **Requirements**
- Windows Machine, Linux Machine, or Macintosh
- 7z, WinRAR or similar alternative
- Python3 and the necessary modules
- A Modern Web-Browser


### Installation
1. Clone the repository:

    Open your terminal or command prompt and navigate to the directory where you want to clone the project. 

    Then, run the following command to clone the repository:
    ```ruby
    git clone https://github.com/StackItHQ/stackit-hiring-assignment-KetanAgrawal2002.git
    ```

2. Navigate to the project directory:
   
    ```ruby
    cd stackit-hiring-assignment-KetanAgrawal2002
    ```

3. Install the required dependencies:

     Run requirements.bat

### Usage
Once you have all the prerequisites ready, you can run the project locally by executing the index.py file using the command:  

```ruby
streamlit run index.py
```

### Features
- **Drag and Drop capabilities** - Users can drag and drop CSV files onto the application.
- **Selection of columns** - Users can select which columns to import from the CSV file.
- **Usage of Google Sheets API** - The application uses the Google Sheets API to create, access, and manipulate Google Sheets programmatically.
- **Add data to existing files** - Users can add data to existing Google Sheets by providing a link to the sheet.
- **Custom Filters** - Users can apply custom filters to the data before adding it to Google Sheets.
- **Optimized for large files** - The application is optimized to handle large CSV files with thousands of rows and columns without causing performance issues or prolonged loading times.


### Credits
- Ketan Agrawal - <a href="https://www.linkedin.com/in/ketan-agrawal-b61a40205/">LinkedIn</a>, <a href="https://www.instagram.com/ketanagrawal_2002/">Instagram</a>, <a href="https://github.com/KetanAgrawal2002">GitHub</a>


<hr>
<center>
    Made with &#10084;&#65039; by Ketan Agrawal.
</center>
