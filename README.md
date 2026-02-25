# Gandhinagar Weather Analysis

## Overview
This project performs basic statistical analysis on the last 10 days of weather data for Gandhinagar.

The program calculates:
- Average (Mean)
- Median

For:
- Temperature (°C)
- Humidity (%)
- AQI

---

## File Included

- `weather_analysis.py` — Python script that performs analysis and generates a results file.

---

## How It Works

1. Synthetic Weather data is stored as a list of tuples.
2. The `statistics` library is used to compute average and median.
3. Results are:
   - Printed to the console
   - Saved to `analysis_results.txt`

---

## How to Run

Make sure Python is installed, then run:

```bash
python weather_analysis.py