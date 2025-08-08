import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import os

# Set the file path from the Kaggle dataset
file_path = "chatgpt_reviews.csv"

# Load the dataset using kagglehub
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "ashishkumarak/chatgpt-reviews-daily-updated",
    file_path,
)


# Save it as CSV to be consumed by Power BI
output_path = os.path.join(os.getcwd(), "chatgpt_reviews_latest.csv")
df.to_csv(output_path, index=False)

print(f"Saved latest dataset to: {output_path}")
