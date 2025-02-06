import streamlit as st
import pandas as pd
import os

# File to store expenses
CSV_FILE = "expenses.csv"

# Load or create CSV file
def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

# Streamlit UI
st.title("💰 Expense Tracker")

# Load expenses
df = load_data()

# Form to add new expenses
with st.form("expense_form"):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Others"])
    amount = st.number_input("Amount", min_value=0.01, format="%.2f")
    description = st.text_input("Description")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        new_expense = pd.DataFrame([[date, category, amount, description]], columns=df.columns)
        df = pd.concat([df, new_expense], ignore_index=True)
        save_data(df)
        st.success("Expense added!")
        st.experimental_rerun()

# Display expenses
st.subheader("Expenses List")
st.dataframe(df)

# Total Expenses Summary
st.subheader("Total Expenses")
st.write(f"**Total Spent:** ${df['Amount'].sum():.2f}")
