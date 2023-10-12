
# Elasticsearch CSV to Bulk JSON Converter

This script helps convert CSV files into a format suitable for Elasticsearch's `_bulk` API. It's designed to be dynamic, catering to various CSV structures by allowing users to define the columns they want to import.

## Prerequisites

-   Python 3.x
-  Movielens datasource csv file or any other csv structured file

## Usage

1.  Place your desired CSV file in an accessible directory.
    
2.  Run the script:
    
~~~    
    `python csv_to_bulk.py` 
~~~    
3.  Follow the interactive prompts:
    
    -   Provide the full path and filename of the source CSV.
    -   Specify the desired output filename for the converted data.
    -   Provide column titles based on the CSV structure or opt for generic titles.

## Features

-   **Dynamic Column Handling:** The script reads the CSV structure and asks the user to define titles. This means it's suitable for a variety of CSV files with different columns.
-   **Error Handling:** If the number of user-defined column titles doesn't match the CSV's structure, the script will generate generic titles for the missing columns.
-   **Elasticsearch-ready Output:** The produced output is formatted specifically for Elasticsearch's `_bulk` API, making data ingestion straightforward.

## Notes

-   Ensure your CSV file is properly structured, with a header row defining the columns.
-   For best results with Elasticsearch, make sure your CSV data is cleaned and preprocessed as needed before using this script.


# MovieLens data
To download the movielens data please run the following commands:
~~~
wget -P /tmp/mleans/ https://jb-workshop.s3.eu-west-1.amazonaws.com/ml-25m.zip
~~~

Install unzip if not already installed:
**ubuntu:**
~~~
sudo apt install -y unzip
~~~
**unzip the file**
~~~
cd /tmp/mleans
unzip ml-25m.zip
~~~ 

**Run the conversion process**
~~~ 
python3 [script_location]/csv_to_bulk.py
~~~ 
When asked for file location provide:
source file: /tmp/mleans/ml-25m/movies.csv
target file: /tmp/mleans/ml-25m/movies.json

When asked for titles provide:
movieId,title,genres
~~~
**DO NOT SAVE THE FILE OR FILES IN YOUR GIT WORKDIR - ONLY IN /TMP**