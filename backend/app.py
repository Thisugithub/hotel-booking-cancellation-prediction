import streamlit as st

from predictor import predict_booking


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Hotel Booking Cancellation Predictor",
    page_icon="🏨",
    layout="wide"
)

st.title(
    "🏨 Hotel Booking Cancellation Prediction System"
)

st.markdown("""
Enter booking details below.

Fields marked with * are required.

Optional fields may be left empty and
will automatically use default values.
""")


# ==========================================
# Required Fields
# ==========================================

st.header("Booking Information")

hotel = st.selectbox(
    "Hotel *",
    [
        "Resort Hotel",
        "City Hotel"
    ]
)

lead_time = st.number_input(
    "Lead Time *",
    min_value=0,
    value=0
)

arrival_date_year = st.number_input(
    "Arrival Year *",
    min_value=2015,
    value=2017
)

arrival_date_month = st.selectbox(
    "Arrival Month *",
    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
)

arrival_date_week_number = st.number_input(
    "Arrival Week Number *",
    min_value=1,
    max_value=53,
    value=1
)

arrival_date_day_of_month = st.number_input(
    "Arrival Day *",
    min_value=1,
    max_value=31,
    value=1
)

stays_in_weekend_nights = st.number_input(
    "Weekend Nights *",
    min_value=0,
    value=0
)

stays_in_week_nights = st.number_input(
    "Week Nights *",
    min_value=0,
    value=1
)

adults = st.number_input(
    "Adults *",
    min_value=1,
    value=2
)

meal = st.selectbox(
    "Meal Type *",
    [
        "BB",
        "HB",
        "FB",
        "SC"
    ]
)

market_segment = st.selectbox(
    "Market Segment *",
    [
        "Direct",
        "Corporate",
        "Online TA",
        "Offline TA/TO",
        "Groups",
        "Complementary",
        "Aviation"
    ]
)

distribution_channel = st.selectbox(
    "Distribution Channel *",
    [
        "Direct",
        "Corporate",
        "TA/TO",
        "GDS"
    ]
)

reserved_room_type = st.selectbox(
    "Reserved Room Type *",
    ["A","B","C","D","E","F","G","H","L"]
)

assigned_room_type = st.selectbox(
    "Assigned Room Type *",
    ["A","B","C","D","E","F","G","H","L"]
)

deposit_type = st.selectbox(
    "Deposit Type *",
    [
        "No Deposit",
        "Non Refund",
        "Refundable"
    ]
)

customer_type = st.selectbox(
    "Customer Type *",
    [
        "Transient",
        "Contract",
        "Transient-Party",
        "Group"
    ]
)

adr = st.number_input(
    "Average Daily Rate (ADR) *",
    min_value=0.0,
    value=100.0
)

# ==========================================
# Optional Fields
# ==========================================

with st.expander("Optional Fields"):

    country = st.text_input("Country")

    children = st.number_input(
        "Children",
        min_value=0,
        value=0
    )

    babies = st.number_input(
        "Babies",
        min_value=0,
        value=0
    )

    agent = st.number_input(
        "Agent",
        min_value=0,
        value=0
    )

    is_repeated_guest = st.selectbox(
        "Repeated Guest",
        [0,1]
    )

    previous_cancellations = st.number_input(
        "Previous Cancellations",
        min_value=0,
        value=0
    )

    previous_bookings_not_canceled = st.number_input(
        "Previous Non-Cancelled Bookings",
        min_value=0,
        value=0
    )

    booking_changes = st.number_input(
        "Booking Changes",
        min_value=0,
        value=0
    )

    days_in_waiting_list = st.number_input(
        "Days In Waiting List",
        min_value=0,
        value=0
    )

    required_car_parking_spaces = st.number_input(
        "Parking Spaces",
        min_value=0,
        value=0
    )

    total_of_special_requests = st.number_input(
        "Special Requests",
        min_value=0,
        value=0
    )


# ==========================================
# Predict Button
# ==========================================

if st.button("Predict Cancellation Risk"):

    data = {

        "hotel": hotel,

        "lead_time": lead_time,

        "arrival_date_year":
            arrival_date_year,

        "arrival_date_month":
            arrival_date_month,

        "arrival_date_week_number":
            arrival_date_week_number,

        "arrival_date_day_of_month":
            arrival_date_day_of_month,

        "stays_in_weekend_nights":
            stays_in_weekend_nights,

        "stays_in_week_nights":
            stays_in_week_nights,

        "adults": adults,

        "meal": meal,

        "market_segment":
            market_segment,

        "distribution_channel":
            distribution_channel,

        "reserved_room_type":
            reserved_room_type,

        "assigned_room_type":
            assigned_room_type,

        "deposit_type":
            deposit_type,

        "customer_type":
            customer_type,

        "adr": adr,

        # Optional

        "country": country,

        "children": children,

        "babies": babies,

        "agent": agent,

        "is_repeated_guest":
            is_repeated_guest,

        "previous_cancellations":
            previous_cancellations,

        "previous_bookings_not_canceled":
            previous_bookings_not_canceled,

        "booking_changes":
            booking_changes,

        "days_in_waiting_list":
            days_in_waiting_list,

        "required_car_parking_spaces":
            required_car_parking_spaces,

        "total_of_special_requests":
            total_of_special_requests
    }

    result = predict_booking(data)

    if result["status"] == "success":

        st.success(
            "Prediction Generated Successfully"
        )

        if result["prediction"] == "Likely To Cancel":

            st.error(
                result["prediction"]
            )

        else:

            st.success(
                result["prediction"]
            )

        st.metric(
            "Cancellation Probability",
            f"{result['cancellation_probability']}%"
        )

        st.info(
            result["message"]
        )

    else:

        st.error(
            result["message"]
        )
