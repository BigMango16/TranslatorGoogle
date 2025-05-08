import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os

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
    
    # Функция за озвучаване
    def text_to_speech(text, lang):
        tts = gTTS(text=text, lang=lang)
        filename = "translation.mp3"
        tts.save(filename)
        return filename

    # Добавяне на бутон за озвучаване
    if st.button("Озвучаване на превода"):
        audio_file = text_to_speech(translation.text, language_code)
        st.audio(audio_file, format="audio/mp3")
