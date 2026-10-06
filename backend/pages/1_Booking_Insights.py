import streamlit as st
import pandas as pd
import altair as alt


# ==================================================
# Page Setup
# ==================================================

st.set_page_config(
    page_title="Booking Insights",
    page_icon="📊",
    layout="wide"
)

with st.spinner("Loading Booking Insights..."):
    pass


# ==================================================
# Styling
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
        background:
            radial-gradient(
            circle at top right,
            rgba(124,58,237,.15),
            transparent 30%),

            #000000;
    }

    .block-container {
        max-width: 1300px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    /* Hero */
    .hero {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        border-radius: 24px;
        padding: 50px 45px;
        text-align: center;
        color: white;
        margin-bottom: 32px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.18);
        position: relative;
        overflow: hidden;
    }

    .hero::after {
        content: "";

        position: absolute;

        width: 300px;
        height: 300px;

        background:
            rgba(255,255,255,.08);

        border-radius: 50%;

        top: -100px;
        right: -80px;
    }

    .hero h1 {
        font-size: 43px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .hero p {
        font-size: 17px;
        color: #eef2ff;
        max-width: 760px;
        margin: auto;
        line-height: 1.7;
    }

    /* Section heading */
    .section-title {
        color: white;
        font-size: 29px;
        font-weight: 750;
        margin-top: 32px;
        margin-bottom: 7px;
    }

    .section-subtitle {
        color: #cbd5e1;
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 22px;
    }

    .analytics-heading {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 14px;
        margin: 80px 0 80px;
        padding: 18px 22px;
        border-radius: 16px;
        background: linear-gradient(
            110deg,
            rgba(37,99,235,.20),
            rgba(124,58,237,.16)
        );
        border: 1px solid rgba(96,165,250,.28);
        box-shadow: 0 10px 28px rgba(0,0,0,.22);
        color: white;
        text-align: center;
    }

    .analytics-heading-title {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        font-size: 26px;
        font-weight: 750;
    }

    .analytics-heading-note {
        width: 100%;
        margin: 0;
        padding-top: 14px;
        border-top: 1px solid rgba(251,191,36,.35);
        color: #f8fafc;
        line-height: 1.6;
    }

    /* Summary cards */
    .summary-card {
    background: linear-gradient(
        145deg,
        #2b4162 0%,
        #1f3553 45%,
        #172b45 100%
    );

    border: 1px solid rgba(96, 165, 250, 0.28);
    border-top: 1px solid rgba(255, 255, 255, 0.18);

    border-radius: 18px;
    padding: 26px 15px;
    text-align: center;
    min-height: 125px;

    box-shadow:
        0 14px 28px rgba(0, 0, 0, 0.50),
        0 6px 10px rgba(0, 0, 0, 0.35),
        inset 0 1px 1px rgba(255, 255, 255, 0.12),
        inset 0 -3px 8px rgba(0, 0, 0, 0.22);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease;

    position: relative;
    overflow: hidden;
}

    .summary-card:hover {

        transform: translateY(-10px);

        border-color:#60a5fa;

        box-shadow:
            0 0 30px rgba(96,165,250,.25),
            0 0 40px rgba(124,58,237,.15);
    }

    .summary-number {
        color: white;
        font-size: 30px;
        font-weight: 800;
    }

    .summary-label {
        color: #cbd5e1;
        font-size: 14px;
        margin-top: 7px;
    }

    /* Chart header */
    .chart-header {
        background:
            linear-gradient(
                145deg,
                #24395d,
                #1b2b45
            );

        border-radius: 18px;
        border: 1px solid #fbbf24;

        box-shadow:
            0 10px 25px rgba(0,0,0,.25);

        padding: 18px 20px;
        margin-bottom: 10px;
        min-height: 135px;
        text-align: center;
    }

    .chart-number {
        display: block;
        width: max-content;
        margin: 0 auto 10px;

        background:
            rgba(99,102,241,.15);

        padding:4px 10px;

        border-radius:20px;

        border:1px solid #6366f1;

        color:#a5b4fc;

        font-size:11px;
    }

    .chart-title {
        color: white;
        font-size: 19px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .chart-description {
        color: #cbd5e1;
        font-size: 13px;
        line-height: 1.5;
    }

    /* Finding box */
    .insight-box {
        background: #24364f;
        border-left: 4px solid #fbbf24;
        padding: 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        transition:.3s ease;
    }

    .insight-box:hover {
        transform:translateY(-4px);

        box-shadow:
            0 0 20px rgba(
            96,165,250,
            .15);
    }

    .insight-heading {
        color: #93c5fd;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 5px;
    }

    .insight-text {
        color: #e2e8f0;
        font-size: 13px;
        line-height: 1.55;
    }

    /* Closing */
    .closing-box {
        background:
            linear-gradient(
            135deg,
            #1e3a8a,
            #4338ca);

        padding: 45px;
        border-radius: 25px;

        box-shadow:
            0 0 35px rgba(
            79,70,229,
            0.25);

        border: 1px solid #3b4c65;
        text-align: center;
        margin-top: 35px;
    }

    .closing-box h2 {
        color: white;
        font-size: 24px;
        margin-bottom: 8px;
    }

    .closing-box p {
        color: #cbd5e1;
        font-size: 15px;
        margin-bottom: 0;
    }

    div.stButton > button {
        width: auto;
        background: #ff4b00;
        color: white;
        border: none;
        border-radius: 12px;
        min-height: 45px;
        font-weight: 650;
    }

    .st-key-open_booking_checker {
        width: 100% !important;
    }

    .st-key-open_booking_checker div[data-testid="stButton"] {
        display: flex;
        justify-content: center;
        width: 100%;
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
# Chart Theme Helper
# ==================================================

def style_chart(chart):
    return (
        chart
        .configure_view(
            stroke=None,
            fill="#111827"
        )
        .configure_axis(
            labelColor="#cbd5e1",
            titleColor="#cbd5e1",
            gridColor="#293548",
            domainColor="#475569",
            tickColor="#475569",
            labelFontSize=11,
            titleFontSize=12
        )
        .configure_legend(
            labelColor="#cbd5e1",
            titleColor="#e2e8f0"
        )
    )


# ==================================================
# Hero
# ==================================================

st.markdown(
    """
    <div class="hero">
        <h1>♕ Booking Insights Dashboard</h1>
        <p>
            Explore booking trends, cancellation patterns,
            hotel performance and reservation behaviour.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# Booking Overview
# ==================================================

st.markdown(
    """
<div style="text-align:center;">
<div class="section-title">Booking Overview</div>
<div class="section-subtitle">A quick summary of the booking records used to explore cancellation patterns.</div>
</div>
    """,
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4, gap="medium")

summary = [
    (c1, "119,390", "Total Bookings"),
    (c2, "75,166", "Not Cancelled"),
    (c3, "44,224", "Cancelled"),
    (c4, "37.0%", "Cancellation Rate")
]

for column, number, label in summary:
    with column:
        st.markdown(
            f"""
            <div class="summary-card">
                <div class="summary-number">{number}</div>
                <div class="summary-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown("""
<div class="analytics-heading">
    <div class="analytics-heading-title">
        <span>♨</span>
        <span>Booking Performance Analytics</span>
    </div>
    <p class="analytics-heading-note">
         Cancellations increase significantly for bookings made far in advance
        and for non-refundable reservations.
    </p>
</div>
""", unsafe_allow_html=True)


# ==================================================
# Data
# ==================================================

lead_time_data = pd.DataFrame(
    {
        "Booking Lead Time": [
            "0-7 days",
            "8-30 days",
            "31-90 days",
            "91-180 days",
            "181-365 days",
            "365+ days"
        ],
        "Cancellation Rate": [
            9.6,
            27.9,
            37.7,
            44.7,
            55.5,
            67.7
        ]
    }
)

deposit_data = pd.DataFrame(
    {
        "Deposit Type": [
            "Refundable",
            "No Deposit",
            "Non Refund"
        ],
        "Cancellation Rate": [
            22.2,
            28.4,
            99.4
        ]
    }
)

market_segment_data = pd.DataFrame(
    {
        "Market Segment": [
            "Complementary",
            "Direct",
            "Corporate",
            "Aviation",
            "Offline TA/TO",
            "Online TA",
            "Groups"
        ],
        "Cancellation Rate": [
            13.1,
            15.3,
            18.7,
            21.9,
            34.3,
            36.7,
            61.1
        ]
    }
)

monthly_data = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec"
        ],
        "Cancellation Rate": [
            30.5,
            33.4,
            32.1,
            40.8,
            39.7,
            41.5,
            37.5,
            37.8,
            39.2,
            38.0,
            31.2,
            35.0
        ]
    }
)


# ==================================================
# ROW 1
# Lead Time + Deposit Type
# ==================================================

row1_col1, row1_col2 = st.columns(2, gap="large")


# --------------------------------------------------
# GRAPH 1 - Lead Time
# --------------------------------------------------

with row1_col1:

    st.markdown(
        """
        <div class="chart-header">
            <div class="chart-number">INSIGHT 01</div>
            <div class="chart-title">
                ▦ Cancellation Rate by Booking Lead Time
            </div>
            <div class="chart-description">
                How cancellation rates changed depending on how far
                in advance a booking was made.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    lead_order = [
        "0-7 days",
        "8-30 days",
        "31-90 days",
        "91-180 days",
        "181-365 days",
        "365+ days"
    ]

    lead_bars = (
        alt.Chart(lead_time_data)
        .mark_bar(
            cornerRadiusEnd=6,
            color="#8b5cf6"
        )
        .encode(
            x=alt.X(
                "Cancellation Rate:Q",
                title="Cancellation Rate (%)",
                scale=alt.Scale(domain=[0, 75])
            ),
            y=alt.Y(
                "Booking Lead Time:N",
                title=None,
                sort=lead_order
            ),
            tooltip=[
                alt.Tooltip(
                    "Booking Lead Time:N",
                    title="Lead Time"
                ),
                alt.Tooltip(
                    "Cancellation Rate:Q",
                    title="Cancellation Rate",
                    format=".1f"
                )
            ]
        )
    )

    lead_labels = (
        alt.Chart(lead_time_data)
        .mark_text(
            align="left",
            baseline="middle",
            dx=5,
            color="#f8fafc",
            fontSize=12,
            fontWeight="bold"
        )
        .encode(
            x="Cancellation Rate:Q",
            y=alt.Y(
                "Booking Lead Time:N",
                sort=lead_order
            ),
            text=alt.Text(
                "Cancellation Rate:Q",
                format=".1f"
            )
        )
    )

    lead_chart = (
        lead_bars + lead_labels
    ).properties(
        height=285
    )

    st.altair_chart(
        style_chart(lead_chart),
        use_container_width=True
    )

    st.markdown(
        """
        <div class="insight-box">
            <div class="insight-heading">KEY FINDING</div>
            <div class="insight-text">
                Cancellation rates rose steadily as booking lead time
                increased, from 9.6% within seven days to 67.7% for
                bookings made more than a year ahead.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# GRAPH 2 - Deposit Type
# --------------------------------------------------

with row1_col2:

    st.markdown(
        """
        <div class="chart-header">
            <div class="chart-number">INSIGHT 02</div>
            <div class="chart-title">
                ▰ Cancellation Rate by Deposit Type
            </div>
            <div class="chart-description">
                How cancellation rates differed across the recorded
                deposit arrangements.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    deposit_order = [
        "Refundable",
        "No Deposit",
        "Non Refund"
    ]

    deposit_bars = (
        alt.Chart(deposit_data)
        .mark_bar(
            cornerRadiusEnd=6
        )
        .encode(
            x=alt.X(
                "Cancellation Rate:Q",
                title="Cancellation Rate (%)",
                scale=alt.Scale(domain=[0, 105])
            ),
            y=alt.Y(
                "Deposit Type:N",
                title=None,
                sort=deposit_order
            ),
            color=alt.Color(
                "Deposit Type:N",
                scale=alt.Scale(
                    domain=deposit_order,
                    range=[
                        "#fbbf24",
                        "#38bdf8",
                        "#8b5cf6"
                    ]
                ),
                legend=None
            ),
            tooltip=[
                alt.Tooltip(
                    "Deposit Type:N",
                    title="Deposit Type"
                ),
                alt.Tooltip(
                    "Cancellation Rate:Q",
                    title="Cancellation Rate",
                    format=".1f"
                )
            ]
        )
    )

    deposit_labels = (
        alt.Chart(deposit_data)
        .mark_text(
            align="left",
            baseline="middle",
            dx=5,
            color="#f8fafc",
            fontSize=12,
            fontWeight="bold"
        )
        .encode(
            x="Cancellation Rate:Q",
            y=alt.Y(
                "Deposit Type:N",
                sort=deposit_order
            ),
            text=alt.Text(
                "Cancellation Rate:Q",
                format=".1f"
            )
        )
    )

    deposit_chart = (
        deposit_bars + deposit_labels
    ).properties(
        height=285
    )

    st.altair_chart(
        style_chart(deposit_chart),
        use_container_width=True
    )

    st.markdown(
        """
        <div class="insight-box">
            <div class="insight-heading">KEY FINDING</div>
            <div class="insight-text">
                Cancellation behaviour differed strongly across deposit
                types. Non-refundable bookings recorded the highest
                cancellation rate at 99.4%.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# ROW 2
# Market Segment + Monthly Rate
# ==================================================

st.markdown(
    '<div style="height: 50px;"></div>',
    unsafe_allow_html=True
)

row2_col1, row2_col2 = st.columns(2, gap="large")


# --------------------------------------------------
# GRAPH 3 - Market Segment
# --------------------------------------------------

with row2_col1:

    st.markdown(
        """
        <div class="chart-header">
            <div class="chart-number">INSIGHT 03</div>
            <div class="chart-title">
                🌐 Cancellation Rate by Market Segment
            </div>
            <div class="chart-description">
                How cancellation behaviour differed across the main
                booking segments.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    segment_order = [
        "Complementary",
        "Direct",
        "Corporate",
        "Aviation",
        "Offline TA/TO",
        "Online TA",
        "Groups"
    ]

    segment_bars = (
        alt.Chart(market_segment_data)
        .mark_bar(
            cornerRadiusEnd=6
        )
        .encode(
            x=alt.X(
                "Cancellation Rate:Q",
                title="Cancellation Rate (%)",
                scale=alt.Scale(domain=[0, 70])
            ),
            y=alt.Y(
                "Market Segment:N",
                title=None,
                sort=segment_order
            ),
            color=alt.value("#6366f1"),
            tooltip=[
                alt.Tooltip(
                    "Market Segment:N",
                    title="Market Segment"
                ),
                alt.Tooltip(
                    "Cancellation Rate:Q",
                    title="Cancellation Rate",
                    format=".1f"
                )
            ]
        )
    )

    segment_labels = (
        alt.Chart(market_segment_data)
        .mark_text(
            align="left",
            baseline="middle",
            dx=5,
            color="#f8fafc",
            fontSize=11,
            fontWeight="bold"
        )
        .encode(
            x="Cancellation Rate:Q",
            y=alt.Y(
                "Market Segment:N",
                sort=segment_order
            ),
            text=alt.Text(
                "Cancellation Rate:Q",
                format=".1f"
            )
        )
    )

    segment_chart = (
        segment_bars + segment_labels
    ).properties(
        height=310
    )

    st.altair_chart(
        style_chart(segment_chart),
        use_container_width=True
    )

    st.markdown(
        """
        <div class="insight-box">
            <div class="insight-heading">KEY FINDING</div>
            <div class="insight-text">
                Cancellation rates varied across booking segments.
                Group bookings recorded the highest rate among the main
                identified segments at 61.1%.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# GRAPH 4 - Monthly Cancellation Rate
# --------------------------------------------------

with row2_col2:

    st.markdown(
        """
        <div class="chart-header">
            <div class="chart-number">INSIGHT 04</div>
            <div class="chart-title">
                ♧ Monthly Cancellation Rate
            </div>
            <div class="chart-description">
                How cancellation rates changed across the months
                of the year.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    month_order = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    ]

    monthly_line = (
        alt.Chart(monthly_data)
        .mark_line(
            color="#ef4444",
            strokeWidth=3,
            point=alt.OverlayMarkDef(
                filled=True,
                fill="#ef4444",
                size=75
            )
        )
        .encode(
            x=alt.X(
                "Month:N",
                title="Month",
                sort=month_order
            ),
            y=alt.Y(
                "Cancellation Rate:Q",
                title="Cancellation Rate (%)",
                scale=alt.Scale(
                    domain=[25, 45],
                    zero=False
                )
            ),
            tooltip=[
                alt.Tooltip(
                    "Month:N",
                    title="Month"
                ),
                alt.Tooltip(
                    "Cancellation Rate:Q",
                    title="Cancellation Rate",
                    format=".1f"
                )
            ]
        )
    )

    monthly_labels = (
        alt.Chart(monthly_data)
        .mark_text(
            dy=-11,
            color="#e2e8f0",
            fontSize=10,
            fontWeight="bold"
        )
        .encode(
            x=alt.X(
                "Month:N",
                sort=month_order
            ),
            y="Cancellation Rate:Q",
            text=alt.Text(
                "Cancellation Rate:Q",
                format=".1f"
            )
        )
    )

    monthly_chart = (
        monthly_line + monthly_labels
    ).properties(
        height=310
    )

    st.altair_chart(
        style_chart(monthly_chart),
        use_container_width=True
    )

    st.markdown(
        """
        <div class="insight-box">
            <div class="insight-heading">KEY FINDING</div>
            <div class="insight-text">
                Cancellation rates varied during the year. June recorded
                the highest rate at 41.5%, while January recorded the
                lowest at 30.5%.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# Closing Section
# ==================================================

st.markdown(
    """
    <div class="closing-box">
        <h2>Want to review a specific booking?</h2>
        <p>
            Use the booking checker to assess the cancellation
            risk of an individual reservation.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

left_col, center_col, right_col = st.columns([1, 1, 1])

with center_col:
    if st.button(
        "◉ Check a Booking",
        key="open_booking_checker"
    ):
        st.switch_page("pages/app.py")