import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="Temperature Analysis",
    page_icon="🌡️",
    layout="wide"
)
# ==========================================
# CUSTOM STYLING
# ==========================================

st.markdown("""
<style>

    /* Main page */
    .main {
        background-color: #0e1117;
    }

    /* Main headings */
    h1 {
        font-size: 42px !important;
        font-weight: 700 !important;
    }

    h2 {
        font-size: 30px !important;
        font-weight: 650 !important;
    }

    h3 {
        font-size: 24px !important;
        font-weight: 600 !important;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
    }

</style>
""", unsafe_allow_html=True)


# ==========================================
# DATA
# ==========================================


# Convert data into Pandas DataFrame
df = pd.read_csv("Test_data.csv", index_col=0)

df["month"] = df["month"].str.title()



# ==========================================
# MATHEMATICAL CALCULATIONS
# ==========================================

temperature = df["Temperature"]

mean_temperature = temperature.mean()

median_temperature = temperature.median()

maximum_temperature = temperature.max()

minimum_temperature = temperature.min()

temperature_range = (
    maximum_temperature - minimum_temperature
)

# NumPy calculation
temperature_array = np.array(temperature)

standard_deviation = np.std(temperature_array)

# Month-to-month temperature change
temperature_change = temperature.diff()

# Overall change from January to December
overall_change = temperature.iloc[-1] - temperature.iloc[0]

# Average monthly change
average_change = temperature_change.mean()

# Find hottest month
hottest_index = df["Temperature"].idxmax()

hottest_month = df.loc[
    hottest_index,
    "month"
]


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🌡️ Temperature Analysis")

st.sidebar.write(
    "Diploma Mathematics Project"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📋 Data",
        "🧮 Mathematics",
        "📈 Graphs",
        "ℹ️ About"
    ]
)


# ==========================================
# DASHBOARD
# ==========================================

if page == "🏠 Dashboard":

    st.title("🌡️ Monthly Temperature Analysis")

    st.write(
        "Diploma First Semester Mathematics Project"
    )

    st.divider()

    st.subheader("📊 Key Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Mean",
        f"{mean_temperature:.2f} °C"
    )

    col2.metric(
        "Median",
        f"{median_temperature:.2f} °C"
    )

    col3.metric(
        "Maximum",
        f"{maximum_temperature} °C"
    )

    col4.metric(
        "Minimum",
        f"{minimum_temperature} °C"
    )


    st.divider()

    st.subheader("🔥 Temperature Information")

    st.success(
        f"Hottest Month: {hottest_month} "
        f"({maximum_temperature} °C)"
    )

    st.info(
        f"Temperature Range: {temperature_range} °C"
    )


# ==========================================
# DATA PAGE
# ==========================================

elif page == "📋 Data":

    st.title("📋 Temperature Data")

    st.write(
        "Monthly temperature data used for analysis."
    )

    st.dataframe(
        df,
        width="stretch"
    )


# ==========================================
# MATHEMATICS PAGE
# ==========================================

elif page == "🧮 Mathematics":

    st.title("🧮 Mathematical Analysis")

    st.write(
        "Basic statistical calculations performed "
        "on the temperature data."
    )

    st.divider()

    st.subheader("Central Tendency")

    st.write(
        f"**Mean:** {mean_temperature:.2f} °C"
    )

    st.write(
        f"**Median:** {median_temperature:.2f} °C"
    )

    st.divider()

    st.subheader("Measures of Variation")

    st.write(
        f"**Maximum:** {maximum_temperature} °C"
    )

    st.write(
        f"**Minimum:** {minimum_temperature} °C"
    )

    st.write(
        f"**Range:** {temperature_range} °C"
    )

    st.write(
        f"**Standard Deviation:** "
        f"{standard_deviation:.2f} °C"
    )
    st.divider()

    st.subheader("📈 Trend Analysis")

    st.write(
        f"**Overall Change:** "
        f"{overall_change:+.0f} °C"
    )

    st.write(
        f"**Average Monthly Change:** "
        f"{average_change:+.2f} °C"
    )

    st.write(
        "The temperature generally increases during "
        "the early months, reaches its highest value "
        "in May, and then decreases later in the year."
    )

    st.subheader("Month-to-Month Change")

    change_df = pd.DataFrame({
        "Month": df["month"],
        "Temperature (°C)": df["Temperature"],
        "Change (°C)": temperature_change
    })

    change_df["Change (°C)"] = change_df["Change (°C)"].fillna(0)

    st.dataframe(
        change_df,
        width="stretch"
    )


# ==========================================
# GRAPHS PAGE
# ==========================================

elif page == "📈 Graphs":

    st.title("📈 Temperature Graphs")

    st.subheader("Monthly Temperature Trend")

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.plot(
        df["month"],
        df["Temperature"],
        marker="o",
        color="blue",
        linewidth=2
    )

    ax.set_xlabel("Month")

    ax.set_ylabel(
        "Temperature (°C)"
    )

    ax.set_title(
        "Monthly Temperature Trend"
    )

    ax.grid(True)

    plt.xticks(rotation=45)

    plt.tight_layout()

    st.pyplot(fig)

    st.divider()

    st.subheader("Monthly Temperature Comparison")

    fig2, ax2 = plt.subplots(figsize=(10, 5))

    ax2.bar(
        df["month"],
        df["Temperature"]
    )

    ax2.set_xlabel("Month")
    ax2.set_ylabel("Temperature (°C)")
    ax2.set_title("Monthly Temperature Comparison")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig2)


# ==========================================
# ABOUT PAGE
# ==========================================

elif page == "ℹ️ About":

    st.title("ℹ️ About the Project")

    st.write(
        "### Monthly Temperature Analysis"
    )

    st.write(
        "This project analyses monthly temperature data "
        "using basic statistical and mathematical methods."
    )

    st.divider()

    st.subheader("🎯 Project Objectives")

    st.write(
        "• Calculate mean and median temperature."
    )

    st.write(
        "• Determine maximum and minimum temperature."
    )

    st.write(
        "• Calculate temperature range and standard deviation."
    )

    st.write(
        "• Analyse the monthly temperature trend."
    )

    st.write(
        "• Represent the data using graphs."
    )

    st.divider()

    st.subheader("🐍 Python Libraries")

    st.write(
        "🐼 Pandas — Data handling and analysis"
    )

    st.write(
        "🔢 NumPy — Numerical calculations"
    )

    st.write(
        "📊 Matplotlib — Graphs and visualization"
    )

    st.write(
        "🌐 Streamlit — Interactive dashboard"
    )
