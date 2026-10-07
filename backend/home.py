import streamlit as st
import streamlit.components.v1 as components

# ==================================================
# Page Configuration
# ==================================================

st.set_page_config(
    page_title="Hotel Booking Cancellation Assistant",
    page_icon="🏨",
    layout="wide"
)


# ==================================================
# Custom Styling
# ==================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #000000;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    .hero {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        border-radius: 24px;
        padding: 65px 50px;
        text-align: center;
        color: white;
        margin-bottom: 35px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.18);
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
        background-color: #1e2d45;
        border: 1px solid #334155;
        border-radius: 18px;
        padding: 28px;
        min-height: 210px;
    }

    .feature-icon {
        font-size: 34px;
        margin-bottom: 14px;
    }

    .feature-card h3 {
        color: white;
        font-size: 21px;
        margin-bottom: 10px;
    }

    .feature-card p {
        color: #cbd5e1;
        font-size: 15px;
        line-height: 1.6;
    }

    .step-number {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        font-weight: 700;
        margin: auto;
        margin-bottom: 16px;
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
        background-color: #1e2d45;
        border-radius: 20px;
        padding: 35px;
        text-align: center;
        margin-top: 45px;
        border: 1px solid #334155;
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
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        width: 100%;
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        color: white;
        border: none;
        transform: translateY(-1px);
    }


    </style>
    """,
    unsafe_allow_html=True
)




# ==================================================
# Hero Section
# ==================================================

st.markdown(
    """
    <div class="hero">
        <h1>🏨 Hotel Booking Cancellation Assistant</h1>
        <p>
            Identify bookings that may be at risk of cancellation, explore past booking patterns,
             and support better reservation planning and follow-up.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


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
                <div class="journey-icon">🧳</div>
                <div class="journey-label">Booking</div>
                <div class="journey-sub">Reservation received</div>
            </div>

            <div class="journey-line"></div>

            <div class="journey-step step-two">
                <div class="journey-icon">📅</div>
                <div class="journey-label">Review</div>
                <div class="journey-sub">Booking details reviewed</div>
            </div>

            <div class="journey-line"></div>

            <div class="journey-step step-three">
                <div class="journey-icon">🏨</div>
                <div class="journey-label">Risk Check</div>
                <div class="journey-sub">Cancellation risk checked</div>
            </div>

            <div class="journey-line"></div>

            <div class="journey-step step-four">
                <div class="journey-icon">✅</div>
                <div class="journey-label">Decision</div>
                <div class="journey-sub">Plan the next step</div>
            </div>

        </div>

    </div>
    """,
    height=185,
    scrolling=False
)


# ==================================================
# Main Actions
# ==================================================

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
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
            <div class="feature-icon">📊</div>
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
            <div class="feature-icon">⚡</div>
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
            <div class="feature-icon">📅</div>
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
            <div class="feature-icon">📈</div>
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

st.write("")

left, center, right = st.columns([1, 2, 1])

with center:
    if st.button(
        "🔍 Check Cancellation Risk",
        key="bottom_prediction_button"
    ):
        st.switch_page("pages/app.py")