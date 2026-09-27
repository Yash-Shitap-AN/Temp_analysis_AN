import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# 1. PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="Temperature Analysis",
    page_icon="🌡️",
    layout="wide"
)


# ==========================================
# 2. PROJECT TITLE
# ==========================================

st.title("🌡️ Monthly Temperature Analysis")

st.write(
    "Diploma First Semester Mathematics Project"
)

st.write(
    "This project uses Pandas, NumPy and Matplotlib "
    "to analyse monthly temperature data."
)


# ==========================================
# 3. DATA
# ==========================================

data = {
    "month": [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ],

    "Temperature": [
        24, 26, 30, 34, 36, 31,
        28, 28, 29, 30, 27, 24
    ]
}


# ==========================================
# 4. CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(data)


# ==========================================
# 5. DISPLAY DATA
# ==========================================

st.header("📋 Weather Data")

st.dataframe(
    df,
    use_container_width=True
)


# ==========================================
# 6. MATHEMATICAL CALCULATIONS
# ==========================================

temperature = df["Temperature"]


# Mean
mean_temperature = temperature.mean()


# Median
median_temperature = temperature.median()


# Maximum
maximum_temperature = temperature.max()


# Minimum
minimum_temperature = temperature.min()


# Range
temperature_range = (
    maximum_temperature - minimum_temperature
)


# Standard deviation using NumPy
temperature_array = np.array(temperature)

standard_deviation = np.std(
    temperature_array
)


# ==========================================
# 7. DISPLAY MATHEMATICAL RESULTS
# ==========================================

st.header("📊 Mathematical Analysis")


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


st.write(
    f"**Temperature Range:** "
    f"{temperature_range} °C"
)


st.write(
    f"**Standard Deviation:** "
    f"{standard_deviation:.2f} °C"
)


# ==========================================
# 8. HOTTEST MONTH
# ==========================================

hottest_index = df["Temperature"].idxmax()

hottest_month = df.loc[
    hottest_index,
    "month"
]


st.success(
    f"🔥 Hottest Month: {hottest_month} "
    f"({maximum_temperature} °C)"
)


# ==========================================
# 9. LINE GRAPH
# ==========================================

st.header("📈 Monthly Temperature Trend")


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


ax.set_title(
    "Monthly Temperature Trend"
)

ax.set_xlabel(
    "Month"
)

ax.set_ylabel(
    "Temperature (°C)"
)

ax.grid(
    True,
    linestyle="--",
    alpha=0.5
)


plt.xticks(
    rotation=45
)

plt.tight_layout()


st.pyplot(fig)


# ==========================================
# 10. BAR GRAPH
# ==========================================

st.header("📊 Monthly Temperature Comparison")


fig2, ax2 = plt.subplots(
    figsize=(10, 5)
)


ax2.bar(
    df["month"],
    df["Temperature"],
    color="orange"
)


ax2.set_title(
    "Temperature by Month"
)

ax2.set_xlabel(
    "Month"
)

ax2.set_ylabel(
    "Temperature (°C)"
)


plt.xticks(
    rotation=45
)

plt.tight_layout()


st.pyplot(fig2)
