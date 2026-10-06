import pandas as pd


def preprocess_data(df):

    df = df.copy()

    # Remove privacy columns

    drop_columns = [
        "name",
        "email",
        "phone-number",
        "credit_card",
        "company"
    ]

    df = df.drop(
        columns=drop_columns,
        errors="ignore"
    )

    # Remove leakage columns

    leakage_columns = [
        "reservation_status",
        "reservation_status_date"
    ]

    df = df.drop(
        columns=leakage_columns,
        errors="ignore"
    )

    


    return df
