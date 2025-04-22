import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# عنوان وشعار
st.image("logo.png", width=200)
st.markdown("<h2 style='text-align: center;'>Loan Risk Classifier</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>By Areeb, Farah, Awrad, Alhanouf, Lolwa</h4>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("Enter Customer Information")

# مدخلات المستخدم
income = st.number_input("Monthly Income (KWD)", min_value=0)
loan_amount = st.number_input("Loan Amount (KWD)", min_value=0)
loan_duration = st.slider("Loan Duration (Years)", 1, 30)
loan_type = st.selectbox("Loan Type", ["Personal", "Car", "Education", "Business", "Housing"])
has_other_loans = st.radio("Do you have other monthly loans?", ["Yes", "No"])

# تحويل نوع القرض إلى رقم
loan_type_map = {
    "Personal": 0,
    "Car": 1,
    "Education": 2,
    "Business": 3,
    "Housing": 4
}
loan_type_val = loan_type_map[loan_type]
other_loans_val = 1 if has_other_loans == "Yes" else 0

# نموذج تدريب مبسط وهمي (AI)
X_train = np.array([
    [1000, 3000, 5, 0, 1],
    [2500, 1500, 2, 1, 0],
    [400, 5000, 3, 2, 1],
    [3000, 2000, 6, 0, 0],
    [1200, 3500, 1, 4, 1],
    [2000, 1000, 4, 3, 0]
])
y_train = ["High", "Low", "High", "Low", "Moderate", "Moderate"]

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# مدخلات المستخدم كصف بيانات
X_input = np.array([[loan_amount, income, loan_duration, loan_type_val, other_loans_val]])

if st.button("Check Loan Risk"):
    prediction = model.predict(X_input)[0]

    st.subheader("Prediction:")
    if prediction == "High":
        st.error("High Risk Loan")
    elif prediction == "Moderate":
        st.warning("Moderate Risk Loan")
    else:
        st.success("Low Risk Loan")