import pandas as pd # Import the pandas library
import sqlite3 # Import the sqlite3 library
import seaborn as sns # Import the seaborn library
import matplotlib.pyplot as plt # Import the matplotlib library

"""
First, we'll extract the data from the CSV file and load it into
a DataFrame. We'll use the pandas library to read the CSV file.
"""

# Step 1: Extract the data
def extract_data(file_path):
    print("Extracting data...")
    # Read the csv file using the pandas library
    return pd.read_csv(file_path)

"""
Secondly, we'll tranform the extracted dataset by applying data cleaning, formatting,
and filtering operations. We'll fill missing values, conver data types, and filter the
data based on specific criteria.

Returns:
pd.DataFrame: The transformed DataFrame after applying all cleaning and filtering steps.
"""

# Step 2: Transform the data
def transform_data(data):
    print("Transforming data...")
        
    # Fill missing values in 'user_score' with the mean
    data['user_score'] = data['user_score'].fillna(data['user_score'].mean())
        
    # Ensure 'release_data' is in datetime format
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    
    # Drop rows with missing 'release_date' after conversion
    data = data.dropna(subset=['release_date'])
    
    # Filter albums with a user score greater than set threshold
    data = data[data['user_score'] > 75]
    
    # Filter albums released date
    data = data[data['release_date'].dt.year > 2013]
    
    # Filter albums by a specific artist
    #data = data[data['artist'] == 'Kendrick Lamar']
    
    print("Data after transformation:")
    print(data.head())
    return data

"""
We'll load the transformed dataset into a SQLite databse. We'll create a new SQLite
database file and write the DataFrame to a new table in the database.

Returns:
None: The function does not return a value, but prints a success message upon completion.
"""

# Step 3: Load the data
def load_data(data, db_name, table_name):
    print("Loading data into the database...")
    
    # Connect to SQLite databse (it will create the file if it doesn't exist)
    conn = sqlite3.connect(db_name)
    
    # Write the DataFrame to a SQLite table
    data.to_sql(table_name, conn, if_exists="replace", index=False)
    
    # Close the connection
    conn.close()
    print(f"Data successfully loaded into {db_name}, table: {table_name}")
    
"""
Here we visualize the distribution of user scores in the dataset using a histogram.
We'll use the seaborn library to create the histogram plot.

Returns: 
None: The function does not return a value, but displays the histogram plot.
"""
    
# Part 4: Distribution of user scores
def user_score_distribution(data):
    plt.figure(figsize=(10,6))
    sns.histplot(data['user_score'], bins=20, kde=True, color='skyblue')
    plt.title("Distribution of User Scores", fontsize=16, fontweight='bold', pad=15)
    plt.xlabel("User Score", fontsize=12)
    plt.ylabel("Frequency", fontsize =12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Display the plot
    plt.tight_layout()
    plt.show()
    
"""
Finally, we'll analyze and visualize the most common genres in the dataset. We'll
split the 'genres' column into individual genres, count the occurrences of each genre,
and display the top 10 most common genres using a bar plot.

Returns:
None: The function does not return a value, but displays the bar plot of the most common genres.
"""
    
# Part 5: Most common genres
def most_common_genres(data):
    genre_counts = data['genres'].str.split(',').explode().value_counts().head(10)
    plt.figure(figsize=(14,8))
    barplot = sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='viridis')
    plt.title('Top 10 Most Common Genres', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Number of Albums', fontsize=12)
    plt.ylabel('Genre', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    
    # Add data labels to each bar
    for i, count in enumerate(genre_counts.values):
        barplot.text(count + 1, i, str(count), color='black', va='center', fontsize=12)
    
    # Removes unnecessary spines and ticks from the plot
    sns.despine(left=True, bottom=True)
    
    # Display the plot
    plt.tight_layout()
    plt.show()
    

# Main function to test the extraction step
def main():
    # Set the path to the csv file
    file_path = r"C:\Users\mouse\Desktop\Data\csv\aoty.csv"
    db_name = "aoty_data.db"  # Name of th SQLite database file
    table_name = "albums"       # Name of the table to create
    
    # Extract the data
    data = extract_data(file_path)
    
    # Transform the extracted data
    transformed_data = transform_data(data)
    
    # Load the transformed data into a SQLite database
    load_data(transformed_data, db_name, table_name)
    
    # Display the distribution of user scores in the original data
    user_score_distribution(data)
    
    # Display the distribution of user scores in the transformed data
    user_score_distribution(transformed_data)
    
    # Display the most common genres in the original data
    most_common_genres(data)
    
    # Display the most common genres in the transformed data
    most_common_genres(transformed_data)
    
    
if __name__ == "__main__":
    main()
    