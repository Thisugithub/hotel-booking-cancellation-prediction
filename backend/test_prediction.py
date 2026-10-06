from predictor import predict_booking

sample_data = {

    "hotel": "Resort Hotel",

    "lead_time": 100,

    "arrival_date_year": 2017,
    "arrival_date_month": "July",
    "arrival_date_week_number": 28,
    "arrival_date_day_of_month": 12,

    "stays_in_weekend_nights": 2,
    "stays_in_week_nights": 5,

    "adults": 2,
    "children": 1,
    "babies": 0,

    "meal": "BB",

    "country": "PRT",

    "market_segment": "Online TA",

    "distribution_channel": "TA/TO",

    "is_repeated_guest": 0,

    "previous_cancellations": 0,

    "previous_bookings_not_canceled": 0,

    "reserved_room_type": "A",

    "assigned_room_type": "A",

    "booking_changes": 0,

    "deposit_type": "No Deposit",

    "agent": 240,

    "days_in_waiting_list": 0,

    "customer_type": "Transient",

    "adr": 150,

    "required_car_parking_spaces": 0,

    "total_of_special_requests": 2
}

result = predict_booking(
    sample_data
)

print(result)
