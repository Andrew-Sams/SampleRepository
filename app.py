import streamlit as st

def calculate_mortgage(principal, down_payment, interest_rate, years):
    loan_amount = principal - down_payment
    monthly_interest_rate = interest_rate / 100 / 12
    number_of_payments = years * 12

    # Monthly mortgage payment calculation
    monthly_payment = None
    if monthly_interest_rate > 0:
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    else:
        monthly_payment = loan_amount / number_of_payments

    annual_payment = monthly_payment * 12
    return monthly_payment, annual_payment

st.title("Mortgage Calculator")

with st.form(key='mortgage_form'):
    purchase_price = st.slider("Purchase Price", 100000, 1000000, 300000)
    down_payment = st.slider("Down Payment", 0, purchase_price, 50000)
    interest_rate = st.slider("Interest Rate (%)", 0.1, 10.0, 3.5)
    loan_years = st.slider("Loan Duration (Years)", 5, 30, 20)
    submit_button = st.form_submit_button(label='Calculate')

if submit_button:
    monthly_payment, annual_payment = calculate_mortgage(purchase_price, down_payment, interest_rate, loan_years)
    st.write(f"Monthly Payment: ${monthly_payment:.2f}")
    st.write(f"Annual Payment: ${annual_payment:.2f}")
