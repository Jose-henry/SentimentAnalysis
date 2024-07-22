import openai  # OpenAI Python library for using GPT-3 language model
import csv  # CSV module for reading and writing CSV files
import pandas as pd  # Pandas library for data manipulation and analysis
from dotenv import load_dotenv  # python-dotenv package for loading .env files
import os

# Load environment variables from .env file
load_dotenv()

# Set the OPENAI_API_KEY from the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

# Read the file contents into a list of rows
filename = r"C:\Users\cherub\OneDrive\Desktop\TE-L Language files\Sentiment Model\Sentiment analysis with Openai\textcomment_utf8.csv"

# Initialize an empty list to store rows
rows = []

# Open the file in read mode with UTF-8 encoding
with open(filename, "r", encoding='utf-8') as f:
    # Create a CSV reader object
    reader = csv.reader(f)
    # Read the header row and store it separately
    header = next(reader)
    # Iterate over each row in the file and append it to the rows list
    for row in reader:
        rows.append(row)

# Add a new header for the sentiment column
header.append("Sentiment")

# Create a list to store the updated rows
updated_rows = []

# Perform sentiment analysis on each row
for row in rows:
    # Extract the text to be analyzed from the Second column of the row
    text = row[0]
    # Create a prompt for the sentiment analysis API with the text
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Please analyze the sentiment of the following text: {text} and decide whether the text has a positive, negative, or neutral sentiment."},
    ]
    # Call the sentiment analysis API with the prompt
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=messages,
    )
    # Extract the sentiment from the API response
    sentiment = response['choices'][0]['message']['content'].strip()
    # Append the sentiment to the row
    row.append(sentiment)
    # Add the updated row to the list
    updated_rows.append(row)

# Write the updated rows back to a CSV file
output_filename = r"C:\Users\cherub\OneDrive\Desktop\TE-L Language files\Sentiment Model\Sentiment analysis with Openai\textcomment_utf8_with_sentiment.csv"

# Open the file in write mode with UTF-8 encoding
with open(output_filename, "w", encoding='utf-8', newline='') as f:
    # Create a CSV writer object
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(header)
    # Write the updated rows
    writer.writerows(updated_rows)

print("Sentiment analysis completed and saved to", output_filename)
