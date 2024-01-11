import streamlit as st

def calculate_mortgage(principal, down_payment, interest_rate, years):
    # Mortgage calculation logic here
    # Return monthly and annual payments
    return monthly_payment, annual_payment

if st.button("Calculate"):
    monthly_payment, annual_payment = calculate_mortgage(
        purchase_price, down_payment, interest_rate, loan_years
    )
    st.write(f"Monthly Payment: ${monthly_payment:.2f}")
    st.write(f"Annual Payment: ${annual_payment:.2f}")