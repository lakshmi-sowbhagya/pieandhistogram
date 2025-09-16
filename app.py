import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 CSV-based Data Visualization")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 Preview of Data")
    st.write(df.head())

    # Select chart type
    chart_type = st.selectbox("Choose a chart type:", ["Pie Chart", "Histogram"])

    if chart_type == "Pie Chart":
        st.subheader("🍕 Pie Chart")

        # Select category and values
        category_col = st.selectbox("Select Category Column:", df.columns)
        value_col = st.selectbox("Select Value Column:", df.columns)

        if st.button("Generate Pie Chart"):
            fig, ax = plt.subplots()
            ax.pie(df[value_col], labels=df[category_col], autopct='%1.1f%%', startangle=90)
            ax.axis("equal")
            st.pyplot(fig)

    elif chart_type == "Histogram":
        st.subheader("📉 Histogram")

        # Select numeric column
        num_col = st.selectbox("Select Numeric Column:", df.select_dtypes(include=["int64", "float64"]).columns)

        bins = st.slider("Number of bins:", 5, 50, 10)

        if st.button("Generate Histogram"):
            fig, ax = plt.subplots()
            ax.hist(df[num_col], bins=bins, color="skyblue", edgecolor="black")
            ax.set_title(f"Histogram of {num_col}")
            ax.set_xlabel("Value")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
