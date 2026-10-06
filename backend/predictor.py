import joblib
import pandas as pd

# Import preprocessing and feature engineering functions

from preprocessing import preprocess_data
from feature_engineering import engineer_features


# ==================================================
# Load Trained Random Forest Pipeline
# ==================================================

MODEL_PATH = "./models/random_forest_pipeline.pkl"

model = joblib.load(MODEL_PATH)


# ==================================================
# Validate Required Fields
# ==================================================

def validate_required_fields(data):

    required_fields = [

        "hotel",

        "lead_time",

        "arrival_date_year",

        "arrival_date_month",

        "arrival_date_week_number",

        "arrival_date_day_of_month",

        "stays_in_weekend_nights",

        "stays_in_week_nights",

        "adults",

        "meal",

        "market_segment",

        "distribution_channel",

        "reserved_room_type",

        "assigned_room_type",

        "deposit_type",

        "customer_type",

        "adr"
    ]

    for field in required_fields:

        if (
            field not in data
            or data[field] is None
            or str(data[field]).strip() == ""
        ):

            raise ValueError(
                f"{field} is required."
            )


# ==================================================
# Fill Optional Fields
# ==================================================

def fill_optional_fields(data):

    optional_defaults = {

        # median replacement during training
        "children": 0,

        # logical defaults
        "babies": 0,

        # mode replacement during training
        "country": "PRT",

        # filled with 0 during training
        "agent": 0,

        "is_repeated_guest": 0,

        "previous_cancellations": 0,

        "previous_bookings_not_canceled": 0,

        "booking_changes": 0,

        "days_in_waiting_list": 0,

        "required_car_parking_spaces": 0,

        "total_of_special_requests": 0
    }

    for field, default_value in optional_defaults.items():

        if (
            field not in data
            or data[field] is None
            or str(data[field]).strip() == ""
        ):

            data[field] = default_value

    return data


# ==================================================
# Validate Business Rules
# ==================================================

def validate_values(data):

    numeric_fields = [

        "lead_time",

        "arrival_date_year",

        "arrival_date_week_number",

        "arrival_date_day_of_month",

        "stays_in_weekend_nights",

        "stays_in_week_nights",

        "adults",

        "children",

        "babies",

        "adr",

        "booking_changes",

        "days_in_waiting_list",

        "required_car_parking_spaces",

        "total_of_special_requests",

        "previous_cancellations",

        "previous_bookings_not_canceled",

        "agent"
    ]

    for field in numeric_fields:

        if float(data[field]) < 0:

            raise ValueError(
                f"{field} cannot be negative."
            )

    if int(data["adults"]) <= 0:

        raise ValueError(
            "At least one adult is required."
        )

    if float(data["adr"]) < 0:

        raise ValueError(
            "ADR cannot be negative."
        )


# ==================================================
# Main Prediction Function
# ==================================================

def predict_booking(data):

    try:

        # ------------------------------------------
        # Validate mandatory inputs
        # ------------------------------------------

        validate_required_fields(data)

        # ------------------------------------------
        # Fill optional inputs
        # ------------------------------------------

        data = fill_optional_fields(data)

        # ------------------------------------------
        # Validate values
        # ------------------------------------------

        validate_values(data)

        # ------------------------------------------
        # Convert input to DataFrame
        # ------------------------------------------

        input_df = pd.DataFrame([data])

        # ------------------------------------------
        # Apply preprocessing used in training
        # ------------------------------------------

        input_df = preprocess_data(
            input_df
        )

        # ------------------------------------------
        # Apply feature engineering used in training
        # ------------------------------------------

        input_df = engineer_features(
            input_df
        )

        # ------------------------------------------
        # Generate prediction
        # ------------------------------------------

        prediction = model.predict(
            input_df
        )[0]

        probability = (
            model.predict_proba(
                input_df
            )[0, 1]
        )

        # ------------------------------------------
        # Build response
        # ------------------------------------------

        if prediction == 1:

            return {

                "status": "success",

                "prediction":
                    "Likely To Cancel",

                "cancellation_probability":
                    round(
                        probability * 100,
                        2
                    ),

                "message":
                    "This booking shows a high risk of cancellation."
            }

        else:

            return {

                "status": "success",

                "prediction":
                    "Likely To Not Cancel",

                "cancellation_probability":
                    round(
                        probability * 100,
                        2
                    ),

                "message":
                    "This booking is likely to be maintained."
            }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)
        }
