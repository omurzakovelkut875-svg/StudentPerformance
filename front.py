import streamlit as st
import requests

st.title("Student Performance Predictor")


hours_study = st.slider("Hours of Study", 0, 12, 5)
attendance = st.slider("Attendance (%)", 0, 100, 75)
sleep_hours = st.slider("Sleep Hours", 0, 12, 7)


if st.button("Predict"):
    data = {
        "hours_study": hours_study,
        "attendance": attendance,
        "sleep_hours": sleep_hours
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"📈 Predicted Score: {result['prediction']}")
        else:
            st.error("Ошибка сервера")

    except:
        st.error("Сервер недоступен")