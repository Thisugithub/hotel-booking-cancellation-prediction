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

st.markdown("""
<style>

/* Navigation sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #0b1220 100%);
    border-right: 1px solid #263449;
}

[data-testid="stSidebarNav"] {
    padding: 1rem 0.7rem 0.5rem;
}

[data-testid="stSidebarNav"]::before {
    content: "HOTEL BOOKING\\A CANCELLATION ANALYTICS";
    display: block;
    white-space: pre-wrap;
    color: #e2e8f0;
    font-size: 0.72rem;
    font-weight: 750;
    letter-spacing: 0.09em;
    line-height: 1.7;
    text-align: center;
    padding: 0.65rem 0.8rem 1rem;
    margin: 0 0.25rem 0.8rem;
    border-bottom: 1px solid #263449;
}

[data-testid="stSidebarNav"] ul {
    gap: 0.35rem;
}

[data-testid="stSidebarNav"] a {
    display: flex;
    justify-content: center;
    color: #cbd5e1 !important;
    border: 1px solid transparent;
    border-radius: 10px;
    padding: 0.65rem 0.8rem;
    font-weight: 600;
    transition: background 0.18s ease, color 0.18s ease, border-color 0.18s ease;
}

[data-testid="stSidebarNav"] a p {
    color: #cbd5e1 !important;
    width: 100%;
    margin: 0;
    text-align: center;
}

[data-testid="stSidebarNav"] a:hover {
    color: #ffffff !important;
    background: rgba(148, 163, 184, 0.1);
    border-color: rgba(148, 163, 184, 0.12);
}

[data-testid="stSidebarNav"] a:hover p {
    color: #ffffff !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    color: #ffffff !important;
    background: linear-gradient(90deg, rgba(37, 99, 235, 0.24), rgba(124, 58, 237, 0.2));
    border-color: rgba(96, 165, 250, 0.3);
}

[data-testid="stSidebarNav"] a[aria-current="page"] p {
    color: #ffffff !important;
}

[data-testid="stSidebarNav"] a[href="/"] p,
[data-testid="stSidebarNav"] a[href$="/"] p {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"] a[href="/"] p::after,
[data-testid="stSidebarNav"] a[href$="/"] p::after {
    content: "Home";
    font-size: 0.9rem;
}

[data-testid="stSidebarNav"] a[href="/app"] p,
[data-testid="stSidebarNav"] a[href$="/app"] p {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"] a[href="/app"] p::after,
[data-testid="stSidebarNav"] a[href$="/app"] p::after {
    content: "Cancellation Risk Predictor";
    font-size: 0.9rem;
}

.sidebar-note {
    margin: 0.75rem 0.9rem;
    padding: 0.9rem;
    border: 1px solid #263449;
    border-radius: 12px;
    background: rgba(30, 41, 59, 0.72);
    text-align: center;
}

.sidebar-note-title {
    color: #f8fafc;
    font-size: 0.76rem;
    font-weight: 700;
    margin: 0 0 0.35rem;
}

.sidebar-note-copy {
    color: #94a3b8;
    font-size: 0.66rem;
    line-height: 1.5;
    margin: 0;
}

/* Main background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

/* Header card */
.hero {
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}

.high-risk-banner {
    background: linear-gradient(135deg, #991b1b, #dc2626);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    animation: riskPulse 2s ease-in-out infinite;
}

@keyframes riskPulse {
    0%, 100% {
        box-shadow: 0 0 0 rgba(220, 38, 38, 0.25);
    }
    50% {
        box-shadow: 0 0 28px rgba(220, 38, 38, 0.65);
    }
}

/* Section cards */
.card {
    background: #172033;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    border: 1px solid #334155;
}

/* Labels */
label {
    font-weight: bold !important;
}

/* Predict Button */
.stButton{
    display:flex;
    justify-content:center;
}

.stButton > button {
    width: 350px;
    height: 60px;
    border-radius: 18px;
    font-size: 20px;
    font-weight: 700;
    background: #ff4b00;
    box-shadow: 0 4px 12px rgba(255,75,0,.12);
    color: white;
    border: none;
    cursor: pointer;
    transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
}

.stButton > button:hover {
    background: #e04300;
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(255,75,0,.18);
    filter: brightness(1.04);
}

.stButton > button:active {
    transform: translateY(0) scale(.98);
}

.stButton > button:focus-visible {
    outline: 3px solid rgba(147,197,253,.9);
    outline-offset: 3px;
}

/* Metric cards */
[data-testid="metric-container"]{
    background: #172033;
    border-radius: 15px;
    padding: 15px;
    border: 1px solid #334155;
}

.stNumberInput,
.stSelectbox,
.stTextInput {
    background: #172033;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-note">
    <p class="sidebar-note-title">AI booking insights</p>
    <p class="sidebar-note-copy">
        Explore reservation trends and assess cancellation risk.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>♕ Hotel Booking Cancellation Predictor</h1>
    <p>
        Review booking details and receive an AI-powered
        cancellation risk assessment in seconds.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card" style="text-align:center;">
    🛎 Booking Details
    &nbsp;&nbsp; ➜ &nbsp;&nbsp;
    📜 Reservation Information
    &nbsp;&nbsp; ➜ &nbsp;&nbsp;
    🤖 AI Analysis
    &nbsp;&nbsp; ➜ &nbsp;&nbsp;
    ✔ Risk Decision
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h1 style="color:#60a5fa;">26</h1>
        <p>Features</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h1 style="color:#a78bfa;">Random Forest</h1>
        <p>Model</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h1 style="color:#34d399;">88%</h1>
        <p>Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<p style="font-size:13px;font-style:italic;color:#cbd5e1;margin:0 0 16px;">
    <strong>#</strong> Enter booking details below.
    <strong>#</strong> Fields marked with * are required.
    <strong>#</strong> Optional fields may be left empty and will automatically use default values.
</p>
""", unsafe_allow_html=True)


# ==========================================
# Stay Information
# ==========================================

st.markdown("""
<div style="
    background:linear-gradient(145deg,#1e2d45,#172437);
    padding:20px;
    border-radius:18px;
    border:1px solid rgba(96,165,250,.25);
    margin-bottom:25px;
    text-align:center;">
    <h2 style="
        color:white;
        margin:0;
        font-size:24px;">
        🛏 Stay Information
    </h2>
    <p style="
        color:#cbd5e1;
        margin-top:8px;">
        Provide the reservation and guest stay details required for risk analysis.
    </p>
</div>
""", unsafe_allow_html=True)

stay_left, stay_right = st.columns(2)

with stay_left:
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

with stay_right:
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

adults_left, adults_center, adults_right = st.columns([1, 2, 1])

with adults_center:
    adults = st.number_input(
        "Adults *",
        min_value=1,
        value=2
    )

# ==========================================
# Reservation Details
# ==========================================

st.markdown("""
<div style="
    background:linear-gradient(145deg,#1e2d45,#172437);
    padding:20px;
    border-radius:18px;
    border:1px solid rgba(96,165,250,.25);
    margin-top:20px;
    margin-bottom:25px;
    text-align:center;">
    <h2 style="
        color:white;
        margin:0;
        font-size:24px;">
        📜 Reservation Details
    </h2>
    <p style="
        color:#cbd5e1;
        margin-top:8px;">
        Provide the reservation, room, and pricing details required for risk analysis.
    </p>
</div>
""", unsafe_allow_html=True)

reservation_left, reservation_right = st.columns(2)

with reservation_left:
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

with reservation_right:
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

with st.expander("⚙ Advanced Booking Details"):

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

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    predict = st.button(
        "✦ Predict Cancellation Risk",
        use_container_width=True
    )

if predict:

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
            st.markdown("""
            <div class="high-risk-banner">
                <h2>⚠ High Cancellation Risk</h2>
                <p>
                    This booking shows characteristics commonly associated
                    with cancellations.
                </p>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div style="
                background:#14532d;
                padding:20px;
                border-radius:15px;
                text-align:center;">
                <h2>✅ BOOKING IS STABLE</h2>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card">
            <h3>Booking Assessment</h3>
            <p>Risk Level: {result["prediction"]}</p>
            <p>Probability: {result["cancellation_probability"]}%</p>
        </div>
        """, unsafe_allow_html=True)

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
