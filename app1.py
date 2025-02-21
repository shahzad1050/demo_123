import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Setup aur App
st.set_page_config(page_title="Data Sweeper", layout='wide')
st.title("Data Sweeper")
st.write("Transform your file between CSV and Excel format with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload your file (csv or excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Initialize df after checking the file type
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file {file_ext}")
            continue

        # Display info about the file
        st.write(f"**Filename:** {file.name}")
        st.write(f"**Filesize:** {file.size / 1024:.2f} KB")

        # Show 5 rows of df
        st.subheader("Preview the head of DataFrame")
        st.dataframe(df.head(5))

        # Option for data cleaning
        st.subheader("Data cleaning options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates removed!")

            with col2:
                if st.button(f"Fill the missing values"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("Missing values have been filled!")

        st.subheader("Select columns to convert")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Visualization
        st.subheader("Data visualization")
        if st.checkbox(f"Show visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # Convert the file CSV to Excel
        st.subheader("Conversion options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["csv", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "csv":
                df.to_csv(buffer, index=False)
                file.name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"

            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file.name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file.name,
                mime=mime_type
            )

st.success("Process completed!")
