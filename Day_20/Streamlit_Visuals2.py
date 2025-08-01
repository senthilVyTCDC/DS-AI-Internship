import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title and layout
st.set_page_config(page_title="Adidas Data Visualizations", layout="wide")
st.title("Adidas Dataset Visualizations")

sns.set()

# Load default dataset
dataset = pd.read_excel('Adidas Dataset.xlsx')

# Identify column types
numeric_cols = dataset.select_dtypes(include='number').columns.tolist()
categorical_cols = dataset.select_dtypes(include='object').columns.tolist()

# Sidebar chart selection
chart_option = st.sidebar.radio(
    "Choose a chart to display",
    ("Line Chart", "Bar Chart", "Scatter Plot", "Correlation Heatmap", "Pairplot", "Pie Chart")
)

# Show dataset preview
if st.checkbox("Show Data Preview"):
    st.subheader("Dataset Preview")
    st.dataframe(dataset)

# ------------------------ LINE CHART ------------------------
if chart_option == "Line Chart":
    st.subheader("Line Chart")
    selected_line_cols = st.multiselect("Select numeric columns for Line Chart", numeric_cols, default=numeric_cols[2])
    if selected_line_cols:
        st.line_chart(dataset[selected_line_cols])
    else:
        st.warning("Please select at least one numeric column for Line Chart.")

# ------------------------ BAR CHART ------------------------
elif chart_option == "Bar Chart":
    st.subheader("Bar Chart")
    selected_bar_col = st.selectbox("Select a column to aggregate for Bar Chart", numeric_cols)
    if selected_bar_col:
        bar_data = dataset[selected_bar_col].value_counts().head(10)
        st.bar_chart(bar_data)

# ------------------------ SCATTER PLOT ------------------------
elif chart_option == "Scatter Plot":
    st.subheader("Scatter Plot")
    scatter_x = st.selectbox("X-axis", numeric_cols, index=2, key='scatter_x')
    scatter_y = st.selectbox("Y-axis", numeric_cols, index=4, key='scatter_y')
    fig1, ax1 = plt.subplots()
    sns.scatterplot(data=dataset, x=scatter_x, y=scatter_y, ax=ax1, color='blue')
    st.pyplot(fig1)

# ------------------------ CORRELATION HEATMAP ------------------------
elif chart_option == "Correlation Heatmap":
    st.subheader("Correlation Heatmap")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.heatmap(dataset[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax2)
    st.pyplot(fig2)

# ------------------------ PAIRPLOT ------------------------
elif chart_option == "Pairplot":
        selected_cols = st.multiselect("Select numeric columns for Pairplot", numeric_cols, default=numeric_cols[:2])
        st.subheader("Pairplot")
        fig3 = sns.pairplot(dataset[selected_cols])
        st.pyplot(fig3)

# ------------------------ PIE CHART ------------------------
elif chart_option == "Pie Chart":
    st.subheader("Pie Chart")
    selected_cat_col = st.selectbox("Select a categorical column for Pie Chart", categorical_cols, index=4)
    selected_num_col = st.selectbox("Select a numeric column to aggregate", numeric_cols, key='pie_numeric', index=3)

    if selected_cat_col and selected_num_col:
        pie_data = dataset.groupby(selected_cat_col)[selected_num_col].sum()
        fig4, ax4 = plt.subplots()
        ax4.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
        ax4.axis('equal')
        st.pyplot(fig4)
