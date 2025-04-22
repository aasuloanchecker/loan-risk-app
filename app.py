import streamlit as st

# شاشة ترحيب
st.image("logo.png", width=200)
st.markdown("<h2 style='text-align:center;'>Welcome to our project from AASU</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: gray;'>This loan risk assessment app was developed as part of our INF120 course.</p>", unsafe_allow_html=True)
st.markdown("---")

# عنوان التطبيق
st.markdown("<h1 style='text-align: center; color: navy;'>Loan Risk Assessment System</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)

# بيانات العميل
st.subheader("Customer Information")

with st.container():
    name = st.text_input("Customer Name")
    age = st.number_input("Age:", min_value=18, max_value=100)
    income = st.number_input("Monthly Income (KWD):", min_value=0)
    loan_amount = st.number_input("Loan Amount (KWD):", min_value=0)
    loan_type = st.selectbox("Loan Type:", ["Personal", "Car", "Housing", "Education", "Business"])
    loan_duration = st.slider("Loan Duration (in years):", 1, 30)
    has_other_loans = st.radio("Do you have other monthly obligations?", ["Yes", "No"])

st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)

# التقييم
if st.button("Check Loan Risk"):
    if income == 0:
        st.warning("Income can't be zero!")
    else:
        ratio = loan_amount / income
        if has_other_loans == "Yes":
            ratio *= 1.2

        st.subheader(f"Customer Summary: {name}")
        st.write(f"- Age: {age}")
        st.write(f"- Loan Type: {loan_type}")
        st.write(f"- Duration: {loan_duration} years")
        st.write(f"- Other Obligations: {has_other_loans}")

        if ratio > 5:
            st.error("High Risk Loan")
        elif ratio > 3:
            st.warning("Moderate Risk Loan")
        else:
            st.success("Low Risk Loan")

# التذييل بأسماء الفريق
st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>By Areeb, Farah, Awrad, Alhanouf, Lolwa</p>", unsafe_allow_html=True)