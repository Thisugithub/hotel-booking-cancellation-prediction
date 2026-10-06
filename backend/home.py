import streamlit as st
import streamlit.components.v1 as components

# ==================================================
# Page Configuration
# ==================================================

st.set_page_config(
    page_title="Hotel Booking Cancellation Assistant",
    page_icon="♕",
    layout="wide"
)


# ==================================================
# Custom Styling
# ==================================================

st.markdown(
    """
    <style>

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

    .stApp {
        background-color: #000000;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    .hero {
        background: linear-gradient(
            135deg,
            #2563eb,
            #7c3aed
        );

        border-radius: 24px;
        padding: 65px 50px;
        text-align: center;
        color: white;
        margin-bottom: 35px;
        position: relative;
        overflow: hidden;

        box-shadow:
            0 0 20px rgba(59,130,246,0.18),
            0 0 32px rgba(124,58,237,0.12);
    }

    .hero::before {
        content: "";
        position: absolute;

        width: 300px;
        height: 300px;

        background: rgba(255,255,255,0.12);

        border-radius: 50%;

        top: -100px;
        right: -100px;

        animation: pulseHero 6s infinite;
    }

    @keyframes pulseHero {
        0% {
            transform: scale(1);
        }

        50% {
            transform: scale(1.4);
        }

        100% {
            transform: scale(1);
        }
    }

    .hero h1 {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 15px;
    }

    .hero p {
        font-size: 19px;
        color: #f1f5f9;
        max-width: 760px;
        margin: auto;
        line-height: 1.7;
    }

    .section-title {
        text-align: center;
        color: white;
        font-size: 32px;
        font-weight: 700;
        margin-top: 45px;
        margin-bottom: 10px;
    }

    .section-subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .feature-card {
        background: linear-gradient(
            145deg,
            #223554,
            #192841
        );

        border: 1px solid rgba(96,165,250,0.20);
        border-radius: 22px;
        padding: 30px;

        height: 330px;

        display: flex;
        flex-direction: column;

        transition: all 0.35s ease;

        position: relative;
        overflow: hidden;

        box-shadow:
            0 8px 25px rgba(0,0,0,0.25);
    }

    .feature-card::before {
        content: "";

        position: absolute;

        width: 180px;
        height: 180px;

        background: rgba(124,58,237,0.08);

        border-radius: 50%;

        top: -70px;
        right: -70px;

        transition: all 0.4s ease;
    }

    .feature-card:hover {

        transform: translateY(-10px);

        border-color: #60a5fa;

        box-shadow:
            0 0 25px rgba(96,165,250,0.25),
            0 0 40px rgba(124,58,237,0.18);
    }

    .feature-card:hover::before {
        transform: scale(1.3);
    }

    .feature-icon {
        font-size: 42px;
        margin-bottom: 18px;
    }

    .feature-card h3 {
        font-size: 26px;
        font-weight: 700;
        color: white;
    }

    .feature-card p {
        color: #cbd5e1;
        line-height: 1.8;
        font-size: 16px;
        flex-grow: 1;
    }

    .step-number {
        width: 60px;
        height: 60px;
        border-radius: 50%;

        background:
        linear-gradient(
        135deg,
        #2563eb,
        #7c3aed);

        color: white;

        display: flex;
        align-items: center;
        justify-content: center;

        font-size: 24px;
        font-weight: 800;

        margin: auto;
        margin-bottom: 18px;

        box-shadow:
            0 0 20px rgba(96,165,250,0.3),
            0 0 35px rgba(124,58,237,0.3);
    }

    .step-card {
        text-align: center;
        padding: 22px;
    }

    .step-card h3 {
        color: white;
        font-size: 19px;
    }

    .step-card p {
        color: #cbd5e1;
        font-size: 14px;
        line-height: 1.6;
    }

    .final-section {
        background:
            linear-gradient(
            135deg,
            #1e3a8a,
            #312e81);

        border-radius: 24px;
        padding: 50px;

        text-align: center;
        margin-top: 80px;

        border: 1px solid rgba(96,165,250,0.3);

        box-shadow:
            0 0 30px rgba(96,165,250,0.2);
    }

    .final-section h2 {
        color: white;
        margin-bottom: 10px;
    }

    .final-section p {
        color: #cbd5e1;
        font-size: 16px;
    }

    div.stButton > button {
        background: #ff4b00;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        width: 100%;
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        background: #e04300;
        color: white;
        border: none;
        transform: translateY(-1px);
    }


    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div class="sidebar-note">
        <p class="sidebar-note-title">AI booking insights</p>
        <p class="sidebar-note-copy">
            Explore reservation trends and assess cancellation risk.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)




# ==================================================
# Hero Section
# ==================================================

st.markdown(
    """
    <div class="hero">
        <h1>♕ Hotel Booking Cancellation Assistant</h1>
        <p>
            Identify bookings that may be at risk of cancellation, explore past booking patterns,
             and support better reservation planning and follow-up.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<h3 style="
text-align:center;
color:white;
margin-top:10px;
margin-bottom:25px;">
⟡ AI-Powered Booking Risk Analysis & Smart Reservation Insights
</h3>
""", unsafe_allow_html=True)


# ==================================================
# Animated Booking Journey
# ==================================================

components.html(
    """
    <style>
        body {
            margin: 0;
            padding: 0;
            background: transparent;
            font-family: Arial, sans-serif;
        }

        .booking-journey {
            background: linear-gradient(
                145deg,
                #1e2d45,
                #121e30
            );

            border: 1px solid rgba(96, 165, 250, 0.25);
            border-radius: 20px;

            padding: 25px 30px 20px 30px;

            box-shadow:
                0 12px 30px rgba(0, 0, 0, 0.35),
                inset 0 1px 0 rgba(255, 255, 255, 0.05);
        }

        .journey-title {
            color: white;
            text-align: center;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 27px;
        }

        .journey-wrapper {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
        }

        .journey-step {
            width: 120px;
            text-align: center;
            position: relative;
            z-index: 2;
        }

        .journey-icon {
            width: 56px;
            height: 56px;
            margin: 0 auto 9px auto;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 50%;

            background: linear-gradient(
                135deg,
                #2563eb,
                #7c3aed
            );

            border: 1px solid rgba(255, 255, 255, 0.18);

            box-shadow:
                0 8px 20px rgba(37, 99, 235, 0.28),
                0 0 18px rgba(124, 58, 237, 0.18);

            font-size: 26px;

            animation: journeyFloat 3s ease-in-out infinite;
        }

        .step-two .journey-icon {
            animation-delay: 0.35s;
        }

        .step-three .journey-icon {
            animation-delay: 0.70s;
        }

        .step-four .journey-icon {
            animation-delay: 1.05s;
        }

        .journey-label {
            color: white;
            font-size: 14px;
            font-weight: 700;
        }

        .journey-sub {
            color: #94a3b8;
            font-size: 11px;
            margin-top: 3px;
        }

        .journey-line {
            flex: 1;
            max-width: 120px;
            height: 3px;

            position: relative;
            overflow: hidden;

            background: #475569;
            border-radius: 20px;

            margin: 0 8px 30px 8px;
        }

        .journey-line::after {
            content: "";

            position: absolute;
            top: 0;
            left: -45%;

            width: 45%;
            height: 100%;

            background: linear-gradient(
                90deg,
                transparent,
                #38bdf8,
                #8b5cf6,
                transparent
            );

            box-shadow:
                0 0 8px #38bdf8,
                0 0 14px #8b5cf6;

            animation: journeyMove 2.2s linear infinite;
        }

        @keyframes journeyFloat {
            0%, 100% {
                transform: translateY(0);
            }

            50% {
                transform: translateY(-7px);
            }
        }

        @keyframes journeyMove {
            0% {
                left: -45%;
            }

            100% {
                left: 110%;
            }
        }
    </style>


    <div class="booking-journey">

        <div class="journey-title">
            From Booking to Better Decisions
        </div>

        <div class="journey-wrapper">

            <div class="journey-step">
                <div class="journey-icon">🛎</div>
                <div class="journey-label">Booking</div>
                <div class="journey-sub">Reservation received</div>
            </div>

            <div class="journey-line"></div>

            <div class="journey-step step-two">
                <div class="journey-icon">▦</div>
                <div class="journey-label">Review</div>
                <div class="journey-sub">Booking details reviewed</div>
            </div>

            <div class="journey-line"></div>

            <div class="journey-step step-three">
                <div class="journey-icon">⌂</div>
                <div class="journey-label">Risk Check</div>
                <div class="journey-sub">Cancellation risk checked</div>
            </div>

            <div class="journey-line"></div>

            <div class="journey-step step-four">
                <div class="journey-icon">✔</div>
                <div class="journey-label">Decision</div>
                <div class="journey-sub">Plan the next step</div>
            </div>

        </div>

    </div>
    """,
    height=230,
    scrolling=False
)

st.markdown("""
<div style="
background:#1e2d45;
padding:25px;
border-radius:20px;
border:1px solid #334155;
margin-top:20px;
margin-bottom:25px;">

<h2 style="text-align:center;color:white;">
🍽 Hotel Reservation Overview
</h2>

<div style="
display:flex;
justify-content:space-around;
margin-top:20px;">

<div>
<h1 style="color:#60a5fa;text-align:center;">119K+</h1>
<p style="color:white;text-align:center;">Bookings Analysed</p>
</div>

<div>
<h1 style="color:#8b5cf6;text-align:center;">37%</h1>
<p style="color:white;text-align:center;">Historical Cancel Rate</p>
</div>

<div>
<h1 style="color:#22c55e;text-align:center;">24/7</h1>
<p style="color:white;text-align:center;">Prediction Support</p>
</div>

</div>
</div>
""", unsafe_allow_html=True)


# ==================================================
# Main Actions
# ==================================================

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">⌕</div>
            <h3>Check a Booking</h3>
            <p>
                Review a reservation and quickly understand its cancellation
                risk to support better booking decisions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

   

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🗝</div>
            <h3>Booking Insights</h3>
            <p>
                Explore useful booking patterns and trends to better understand
                guest behaviour and cancellation activity.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    


# ==================================================
# How It Works
# ==================================================

st.markdown(
    """
    <div class="section-title">Check Cancellation Risk in Three Steps</div>
    <div class="section-subtitle">
        Review a reservation and get a clear indication of its cancellation risk.
    </div>
    """,
    unsafe_allow_html=True
)

step1, step2, step3 = st.columns(3, gap="large")

with step1:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">1</div>
            <h3>Enter Booking Details</h3>
            <p>
                Provide the reservation information needed
                 to review the booking.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with step2:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">2</div>
            <h3>Check Cancellation Risk</h3>
            <p>
                Review the booking and receive a clear indication
                of its cancellation risk.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with step3:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-number">3</div>
            <h3>Support Your Decision</h3>
            <p>
                Use the result to support reservation follow-up
                 and planning.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# Everyday Hotel Operations Section
# ==================================================

st.markdown(
    """
    <div class="section-title">
        Supporting Better Reservation Decisions
    </div>

    <div class="section-subtitle">
        Useful cancellation insights to help staff review and manage reservations with confidence.
    </div>
    """,
    unsafe_allow_html=True
)

benefit1, benefit2, benefit3 = st.columns(3, gap="large")

with benefit1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">↯</div>
            <h3>Quick Booking Checks</h3>
            <p>
                Use cancellation insights to support room planning,
                 reservation follow-up, and availability decisions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with benefit2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">▦</div>
            <h3>Better Planning</h3>
            <p>
                Use cancellation insights to support reservation,
                occupancy, and room planning activities.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with benefit3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">◩</div>
            <h3>Understand Booking Patterns</h3>
            <p>
                Explore past booking patterns to understand
                 when and where cancellations were more common.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# Final Call to Action
# ==================================================

st.markdown(
    """
    <div class="final-section">
        <h2>Ready to check a booking?</h2>
        <p>
            Review a reservation and get a clear cancellation risk result.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 2, 3])

with col2:
    if st.button(
        "◉ Check Cancellation Risk",
        key="bottom_prediction_button"
    ):
        st.switch_page("pages/app.py")