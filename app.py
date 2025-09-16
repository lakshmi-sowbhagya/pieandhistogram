import streamlit as st
import pandas as pd
import io

st.title("📊 Pie and Histogram Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Check if a file was uploaded
if uploaded_file is not None:
    try:
        # Try decoding and reading the CSV
        content = uploaded_file.getvalue().decode("utf-8")
        df = pd.read_csv(io.StringIO(content))

        st.subheader("📋 Preview of Data")
        st.write(df.head())

        # You can add your pie chart and histogram logic here

    except Exception as e:
        st.error(f"❌ Failed to read CSV file: {e}")
else:
    st.info("Please upload a CSV file to begin.")

