import streamlit as st
import requests

st.title('sstudent performance prediction')

api_url = 'http://127.0.0.1:8000/predict'

gender = st.selectbox('Пол', ['male', 'female'])

race_ethnicity = st.selectbox(
    'Группа',
    ['group A', 'group B', 'group C', 'group D', 'group E']
)

parent_education = st.selectbox(
    'Образование родителей',
    [
        "bachelor's degree",
        'high school',
        "master's degree",
        'some college',
        'some high school'
    ]
)

test_preparation = st.selectbox(
    'Подготовка к тесту',
    ['none', 'completed']
)

lunch = st.selectbox(
    'Питание',
    ['standard', 'free/reduced']
)
math_score = st.number_input('Math score', min_value=0, max_value=100, value=50)
reading_score = st.number_input('Reading score', min_value=0, max_value=100, value=50)

student_data = {
    "gender": gender,
    "race_ethnicity": race_ethnicity,
    "parent_education": parent_education,
    "test_preparation": test_preparation,
    "lunch": lunch,
    "math_score": math_score,
    "reading_score": reading_score
}

if st.button('Предсказать'):
    try:
        response = requests.post(api_url, json=student_data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
        else:
            st.error(f"Ошибка API: {response.status_code}")
    except requests.exceptions.RequestException:
        st.error('Не удалось подключиться к API')