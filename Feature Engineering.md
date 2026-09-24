# Hotel Booking Cancellation Prediction - Feature Engineering

## Project Overview

This project is part of the Hotel Booking Cancellation Prediction system developed for the IT3051 Fundamentals of Data Mining Mini Project.

The objective of this stage is to create new meaningful features from the existing dataset, perform feature selection, and identify the most important variables that influence hotel booking cancellations.

---

## Member Information

**Member 04 - Feature Engineering**

# Methodology

The feature engineering process followed the steps below:

1. Load and understand the preprocessed dataset.
2. Analyze available features and identify opportunities for creating meaningful variables.
3. Create new features that better represent customer behavior.
4. Perform feature selection using correlation analysis.
5. Evaluate feature importance using Random Forest Classifier.
6. Save the final engineered dataset for future machine learning model development.

---

# Workflow

Raw Dataset
↓
Data Understanding
↓
Data Quality Analysis
↓
Data Preprocessing
↓
Feature Engineering
↓
Feature Selection
↓
Feature Importance Analysis
↓
Final Engineered Dataset
↓
Machine Learning Model Development

---

# Newly Created Features

## is_family

Represents whether a booking includes family members such as children or babies.

Business Value:
- Helps identify family travel patterns.
- Family bookings may behave differently from individual bookings.

---

## service_score

Combines parking requests and special requests into a single metric.

Business Value:
- Indicates customer engagement.
- Customers requesting more services may have lower cancellation risk.

---

## customer_history

Combines previous successful bookings and previous cancellations.

Business Value:
- Measures customer loyalty and booking behavior.
- Useful for identifying repeat customers.

---

## room_changed

Shows whether the assigned room differs from the originally reserved room.

Business Value:
- Room allocation changes can influence customer satisfaction.
- May contribute to booking cancellation behavior.

---

# Feature Importance Results

The Random Forest algorithm identified the following important features:

1. lead_time
2. deposit_type
3. adr
4. country
5. service_score
6. total_nights
7. previous_cancellations
8. room_changed
9. market_segment

These features provide the strongest contribution to booking cancellation predictions.

---

# Visualizations Generated

During feature engineering the following visualizations were created:

- Correlation Heatmap
- Feature Importance Ranking

These visualizations helped identify relationships between variables and determine the most influential features.

---

# Challenges Faced

Several challenges were addressed during this stage:

- Understanding relationships between booking attributes.
- Creating meaningful features without causing data leakage.
- Handling categorical variables.
- Selecting features that improve prediction capability.
- Interpreting feature importance results.

---

# Data Leakage Prevention

To ensure model reliability:

- Target information was not used during feature creation.
- Engineered features were created only from existing input variables.
- Future information was not included in feature calculations.

This helps maintain fair and realistic prediction performance.

---

# Output Dataset

The final dataset contains:

- Original cleaned features
- Newly engineered features
- Selected predictive features

Output file:

```text
data/processed/feature_engineered_dataset.csv
``