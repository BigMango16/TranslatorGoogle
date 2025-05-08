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




from gtts import gTTS
import os
import streamlit as st

# Функция за озвучаване
def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("translation.mp3")
    return "translation.mp3"

# Примерна интеграция в Streamlit
translated_text = "Тук е вашият превод."  # Заменете с реалния преведен текст
st.write(translated_text)

if st.button("Озвучаване на превода"):
    audio_file = text_to_speech(translated_text, lang='bg')  # Пример за български
    st.audio(audio_file, format="audio/mp3")
