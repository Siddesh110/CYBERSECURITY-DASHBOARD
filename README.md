# Cybersecurity Cases in India: Power BI Dashboard

A Power BI dashboard that analyses 1,200 cybersecurity cases across 10 Indian cities from 2019 to 2024. The data was cleaned first (Excel, Power Query and a Python script), then the dashboard and DAX measures were built in Power BI.

![Dashboard](cybersecurity%20dashboard.png)
   ## Project Goal
Find out which attack types, cities and sectors have the most cases and the highest money lost.

## Tools Used
- Excel and Power Query: data cleaning
- Python (pandas): data cleaning script
- Power BI: dashboard
- DAX: measures

## Dataset
File: `data/raw/cybersecurity_cases_india_combined.csv` (1,200 rows)

| Column | Meaning |
|---|---|
| Year | 2019 to 2024 |
| Day | Day of the month |
| Amount_Lost_INR | Money lost in the case (INR) |
| Incident_Type | Type of attack (Ransomware, Phishing, etc.) |
| City | 10 Indian cities |
| Category | Sector affected (Corporate, Health, Government, etc.) |

Note: the data has no month column and no source, so it may be sample data. This is a practice project, not official statistics.

## Step 1: Data Cleaning
Script: [`scripts/clean_data.py`](scripts/clean_data.py)

1. Made column names UPPER_CASE
2. Removed extra spaces from text columns
3. Merged `Malware_Attacks` into `Malware` (same attack type)
4. Checked for missing values and duplicates (none found, 1,200 rows kept)
5. Added an `INDEX` column as a unique case ID

Result: 1,200 clean rows and 9 incident types.
Cleaned file: `data/cleaned/cybersecurity_cases_india_cleaned.csv`

To run the script:
```bash
pip install pandas
python scripts/clean_data.py
```

## Step 2: Dashboard
File: `dashboard/CYBERSECURITY_DASHBOARD.pbix` (open with Power BI Desktop)

- 3 cards: Total Cases, Total Amount Lost, Average Amount Lost
- Column chart: number of cases by sector
- Bar chart: share of total money lost by city
- Pie chart: money lost by incident type
- Year slicer: filters the whole page
- Dark theme, one page

## Step 3: DAX Measures
File: [`dax/measures.dax`](dax/measures.dax)

```DAX
TOTAL CASES = COUNTROWS ( cybersecurity_cases_india_combined )

TOTAL AMOUNT LOST = SUM ( cybersecurity_cases_india_combined[AMOUNT_LOST_INR] )

AVERAGE AMOUNT LOST = DIVIDE ( [TOTAL AMOUNT LOST], [TOTAL CASES] )
```

## Key Findings
- 1,200 cases with a total loss of about INR 27.78 crore
- Average loss per case is about INR 2.32 lakh
- Ransomware has the most cases (189) and the highest total loss (about INR 4.11 crore)
- Delhi, Mumbai and Chennai have the biggest share of losses (about 12% each)
- Differences between cities are small (7.8% to 12.2%), so no city is a clear outlier

## Folder Structure
```
data/raw/        original CSV file
data/cleaned/    cleaned CSV file
scripts/         clean_data.py
dax/             measures.dax
dashboard/       Power BI file
images/          dashboard screenshot
```

## How to Use
1. Download or clone this repo
2. Open `dashboard/CYBERSECURITY_DASHBOARD.pbix` in Power BI Desktop
3. Use the Year slicer to filter the dashboard

## Author
Siddesh Valmiki
- GitHub: [Siddesh110](https://github.com/Siddesh110)
- LinkedIn: [siddesh-valmiki](https://linkedin.com/in/siddesh-valmiki)
- Portfolio: https://siddesh-valmiki-portfolio.netlify.app/
