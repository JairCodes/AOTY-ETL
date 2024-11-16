# AOTY ETL Pipeline

## Dataset

This project uses the **Album of the Year (AOTY) dataset**, available on Kaggle.
You can download the dataset from the following link:

- [Album of the Year Dataset on Kaggle](https://www.kaggle.com/datasets/tabibyte/aoty-5000-highest-user-rated-albums/data)

### Instructions to Download
1. Visit the dataset page on Kaggle.
2. Log in or create a Kaggle account.
3. Download the dataset as a CSV file.
4. Place the downloaded file in the appropriate directory.
   - Default file path: `C:\Users\mouse\Desktop\Data\csv\aoty.csv`
5. Update the `file_path` variable in the script.


## Project Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline using Python. 
The pipeline processes album data from a CSV file, transforms it to clean and filter the data, and loads
it into a SQLite database. Additionally, it includes visualizations for user score distribution and most common genres.

## Features
- Extracts album data from a CSV file.
- Cleans and filters data to remove missing or irrelevant entries.
- Loads the processed data into a SQLite databse.
- Visualizes:
    - Distribution of user scores.
    - Top 10 most common genres.

## Technologies Used
- Python
- Pandas
- SQLite
- Matplotlib
- Seaborn

## Author
- Jair Ramirez ([Github Profile](https://github.com/JairCodes)) 😊