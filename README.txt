# Power BI Daily Auto-Refresh from Kaggle

This setup fetches the latest version of the Kaggle dataset `chatgpt-reviews-daily-updated` and exports it as a CSV that Power BI can read and refresh daily.

## 🧩 Files

- `download_kaggle_reviews.py` — Python script to fetch the dataset using `kagglehub`.
- `run_daily.bat` — Batch file to automate execution.
- `chatgpt_reviews_latest.csv` — Auto-updated CSV for Power BI.
- `README.txt` — Instructions.

## 🛠️ Requirements

- Python 3.x installed
- `pip install kagglehub pandas`
- Optional: Add to Task Scheduler for daily auto-refresh.

## ⚙️ How to Use

1. Run `download_kaggle_reviews.py` once to create the CSV.
2. In Power BI, connect to `chatgpt_reviews_latest.csv` using **Get Data > CSV**.
3. Schedule `run_daily.bat` in Windows Task Scheduler to run every day.
4. (Optional) Publish the report to Power BI Service and configure refresh.