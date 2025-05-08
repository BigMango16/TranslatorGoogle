import streamlit as st
from googletrans import Translator

# Заглавие
st.title('Приложение за превод на текст')

# Входен текст
text = st.text_input("Въведете текст за превод:")

# Списък с налични езици
languages = {
    "Английски": "en",
    "Френски": "fr",
    "Немски": "de",
    "Италиански": "it",
    "Испански": "es",
    "Руски": "ru",
    "Китайски (опростен)": "zh-cn",
    "Японски": "ja",
    "Корейски": "ko",
    "Арабски": "ar"
}

# Избор на език
language_name = st.selectbox("Изберете език за превод", list(languages.keys()))
language_code = languages[language_name]

# Превод
if text:
    translator = Translator()
    translation = translator.translate(text, dest=language_code)
    st.write(f'Преведеният текст на {language_name}: {translation.text}')
