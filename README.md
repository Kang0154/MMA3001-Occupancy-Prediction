# MMA3001 - Building Occupancy Prediction

## Project Overview
This project predicts building occupancy five minutes ahead
using historical occupancy sensor data.

## Dataset
Monash Smart Infrastructure Occupancy Dataset.
Input: timestamp, device ID, zone ID and headcount.
The original dataset is not included in this repository.

## Methods
- Baseline: current headcount
- Linear Regression
- Decision Tree Regression

Data is split chronologically into:
60% training, 20% validation and 20% testing.

Decision Tree depth is selected using validation MAE.
Models are evaluated using MAE and RMSE.

## Running the Project
1. Open MMA3001_Project.ipynb in Google Colab.
2. Upload the course-provided occupancy ZIP file.
3. Run all notebook cells in order.

## Project Files
- MMA3001_Project.ipynb: Main analysis
- project_utils.py: Feature preparation
- test_project_utils.py: Unit tests
- test_report.txt: Test results
- docs/: HTML documentation
- results.csv: Model comparison
- *.png: Result figures

## Limitations
Predictions are evaluated only where consecutive
five-minute intervals have observed headcounts.
Results may not generalise to other zones or devices.
