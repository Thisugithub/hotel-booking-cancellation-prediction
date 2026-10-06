import pandas as pd


def engineer_features(df):

    df = df.copy()

    df["total_nights"] = (
        df["stays_in_weekend_nights"]
        + df["stays_in_week_nights"]
    )

    df["total_guests"] = (
        df["adults"]
        + df["children"]
        + df["babies"]
    )


    # Family Feature

    df["is_family"] = (
        (df["children"] + df["babies"]) > 0
    ).astype(int)

    # Service Score

    df["service_score"] = (
        df["required_car_parking_spaces"]
        + df["total_of_special_requests"]
    )

    # Customer History

    df["customer_history"] = (
        df["previous_cancellations"]
        + df["previous_bookings_not_canceled"]
    )

    # Room Change Feature

    df["room_changed"] = (
        df["reserved_room_type"]
        != df["assigned_room_type"]
    ).astype(int)



    return df
