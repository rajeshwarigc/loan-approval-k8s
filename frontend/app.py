import streamlit as st
import requests

st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦")

st.title("🏦 Loan Approval Prediction System")
st.write("Enter applicant details to check loan eligibility.")

age = st.number_input("Age", min_value=18, max_value=70, value=30)
income = st.number_input("Annual Income", min_value=0, value=80000)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=750)

if st.button("Predict Loan Approval"):
    payload = {
        "age": age,
        "income": income,
        "credit_score": credit_score
    }

    try:
        response = requests.post(
            "http://backend-service:8080/loan",
            json=payload,
            timeout=5
        )

        result = response.json()

        if result.get("loan_approved") is True:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

    except Exception as e:
        st.error("⚠️ Backend service not reachable")
