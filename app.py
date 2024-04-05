# import streamlit as st
# import os
# import time
# import glob
# import os


# from gtts import gTTS
# from googletrans import Translator

# try:
#     os.mkdir("temp")
# except:
#     pass
# st.title("Text to speech")
# translator = Translator()

# text = st.text_input("Enter text")
# in_lang = st.selectbox(
#     "Select your input language",
#     ("English", "Hindi", "Bengali", "korean", "Chinese", "Japanese"),
# )
# if in_lang == "English":
#     input_language = "en"
# elif in_lang == "Hindi":
#     input_language = "hi"
# elif in_lang == "Bengali":
#     input_language = "bn"
# elif in_lang == "korean":
#     input_language = "ko"
# elif in_lang == "Chinese":
#     input_language = "zh-cn"
# elif in_lang == "Japanese":
#     input_language = "ja"

# out_lang = st.selectbox(
#     "Select your output language",
#     ("English", "Hindi", "Bengali", "korean", "Chinese", "Japanese"),
# )
# if out_lang == "English":
#     output_language = "en"
# elif out_lang == "Hindi":
#     output_language = "hi"
# elif out_lang == "Bengali":
#     output_language = "bn"
# elif out_lang == "korean":
#     output_language = "ko"
# elif out_lang == "Chinese":
#     output_language = "zh-cn"
# elif out_lang == "Japanese":
#     output_language = "ja"

# english_accent = st.selectbox(
#     "Select your english accent",
#     (
#         "Default",
#         "India",
#         "United Kingdom",
#         "United States",
#         "Canada",
#         "Australia",
#         "Ireland",
#         "South Africa",
#     ),
# )

# if english_accent == "Default":
#     tld = "com"
# elif english_accent == "India":
#     tld = "co.in"

# elif english_accent == "United Kingdom":
#     tld = "co.uk"
# elif english_accent == "United States":
#     tld = "com"
# elif english_accent == "Canada":
#     tld = "ca"
# elif english_accent == "Australia":
#     tld = "com.au"
# elif english_accent == "Ireland":
#     tld = "ie"
# elif english_accent == "South Africa":
#     tld = "co.za"


# def text_to_speech(input_language, output_language, text, tld):
#     translation = translator.translate(text, src=input_language, dest=output_language)
#     trans_text = translation.text
#     tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
#     try:
#         my_file_name = text[0:20]
#     except:
#         my_file_name = "audio"
#     tts.save(f"temp/{my_file_name}.mp3")
#     return my_file_name, trans_text


# display_output_text = st.checkbox("Display output text")

# if st.button("convert"):
#     result, output_text = text_to_speech(input_language, output_language, text, tld)
#     audio_file = open(f"temp/{result}.mp3", "rb")
#     audio_bytes = audio_file.read()
#     st.markdown(f"## Your audio:")
#     st.audio(audio_bytes, format="audio/mp3", start_time=0)

#     if display_output_text:
#         st.markdown(f"## Output text:")
#         st.write(f" {output_text}")


# def remove_files(n):
#     mp3_files = glob.glob("temp/*mp3")
#     if len(mp3_files) != 0:
#         now = time.time()
#         n_days = n * 86400
#         for f in mp3_files:
#             if os.stat(f).st_mtime < now - n_days:
#                 os.remove(f)
#                 print("Deleted ", f)


# remove_files(7)


# import streamlit as st
# import os
# import time
# import glob
# import os
# import speech_recognition as sr
# from gtts import gTTS
# from googletrans import Translator

# try:
#     os.mkdir("temp_audio")
#     os.mkdir("temp_text")
# except:
#     pass

# st.set_page_config(
#     page_title="VoiceSync - Bridging Text and Speech",
#     page_icon=":microphone:",
#     layout="wide"
# )

# st.title("VoiceSync - Bridging Text and Speech")

# st.write("""
# ## Text to Speech
# """)
# translator = Translator()

# text = st.text_input("Enter text")
# in_lang = st.selectbox(
#     "Select input language",
#     ("English", "Hindi", "Bengali", "Korean", "Chinese", "Japanese"),
# )
# input_languages = {"English": "en", "Hindi": "hi", "Bengali": "bn", "Korean": "ko", "Chinese": "zh-cn", "Japanese": "ja"}
# input_language = input_languages[in_lang]

# out_lang = st.selectbox(
#     "Select output language",
#     ("English", "Hindi", "Bengali", "Korean", "Chinese", "Japanese"),
# )
# output_languages = {"English": "en", "Hindi": "hi", "Bengali": "bn", "Korean": "ko", "Chinese": "zh-cn", "Japanese": "ja"}
# output_language = output_languages[out_lang]

# english_accent = st.selectbox(
#     "Select English accent",
#     (
#         "Default",
#         "India",
#         "United Kingdom",
#         "United States",
#         "Canada",
#         "Australia",
#         "Ireland",
#         "South Africa",
#     ),
# )

# english_accents = {"Default": "com", "India": "co.in", "United Kingdom": "co.uk", "United States": "com", 
#                    "Canada": "ca", "Australia": "com.au", "Ireland": "ie", "South Africa": "co.za"}
# tld = english_accents[english_accent]

# def text_to_speech(input_language, output_language, text, tld):
#     translation = translator.translate(text, src=input_language, dest=output_language)
#     trans_text = translation.text
#     tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
#     try:
#         my_file_name = text[0:20]
#     except:
#         my_file_name = "audio"
#     tts.save(f"temp_audio/{my_file_name}.mp3")
#     return my_file_name, trans_text

# display_output_text = st.checkbox("Display output text")

# if st.button("Convert Text to Speech"):
#     result, output_text = text_to_speech(input_language, output_language, text, tld)
#     audio_file = open(f"temp_audio/{result}.mp3", "rb")
#     audio_bytes = audio_file.read()
#     st.markdown(f"## Your audio:")
#     st.audio(audio_bytes, format="audio/mp3", start_time=0)

#     if display_output_text:
#         st.markdown(f"## Output text:")
#         st.write(f" {output_text}")

# def remove_audio_files(n):
#     audio_files = glob.glob("temp_audio/*mp3")
#     if len(audio_files) != 0:
#         now = time.time()
#         n_days = n * 86400
#         for f in audio_files:
#             if os.stat(f).st_mtime < now - n_days:
#                 os.remove(f)

# remove_audio_files(7)

# st.write("""
# ---
# ## Speech to Text
# """)

# uploaded_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])

# if uploaded_file is not None:
#     audio_data = uploaded_file.read()

#     st.audio(audio_data, format="audio/wav", start_time=0)

#     r = sr.Recognizer()
#     with sr.AudioFile(uploaded_file) as source:
#         audio_text = r.listen(source)
#         try:
#             text = r.recognize_google(audio_text)
#             st.write("Transcribed text:")
#             st.write(text)
#         except sr.UnknownValueError:
#             st.write("Google Speech Recognition could not understand the audio")
#         except sr.RequestError as e:
#             st.write("Could not request results from Google Speech Recognition service; {0}".format(e))

# def remove_text_files(n):
#     text_files = glob.glob("temp_text/*")
#     if len(text_files) != 0:
#         now = time.time()
#         n_days = n * 86400
#         for f in text_files:
#             if os.stat(f).st_mtime < now - n_days:
#                 os.remove(f)

# remove_text_files(7)


import streamlit as st
import os
import time
import glob
import os
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator

try:
    os.mkdir("temp_audio")
    os.mkdir("temp_text")
except:
    pass

st.set_page_config(
    page_title="VoiceSync - Bridging Text and Speech",
    page_icon=":microphone:",
    layout="wide"
)

st.title("VoiceSync - Bridging Text and Speech")

# Sidebar for project description
st.sidebar.title("Project Description")
st.sidebar.write("""
This is a Streamlit app that allows you to convert text to speech and speech to text. You can choose the input and output languages along with the English accent for text-to-speech conversion.
""")

translator = Translator()

# Text to Speech Section
st.write("""
## Text to Speech
""")
text = st.text_input("Enter text")
in_lang = st.selectbox(
    "Select input language",
    ("English", "Hindi", "Bengali", "Korean", "Chinese", "Japanese"),
)
input_languages = {"English": "en", "Hindi": "hi", "Bengali": "bn", "Korean": "ko", "Chinese": "zh-cn", "Japanese": "ja"}
input_language = input_languages[in_lang]

out_lang = st.selectbox(
    "Select output language",
    ("English", "Hindi", "Bengali", "Korean", "Chinese", "Japanese"),
)
output_languages = {"English": "en", "Hindi": "hi", "Bengali": "bn", "Korean": "ko", "Chinese": "zh-cn", "Japanese": "ja"}
output_language = output_languages[out_lang]

english_accent = st.selectbox(
    "Select English accent",
    (
        "Default",
        "India",
        "United Kingdom",
        "United States",
        "Canada",
        "Australia",
        "Ireland",
        "South Africa",
    ),
)

english_accents = {"Default": "com", "India": "co.in", "United Kingdom": "co.uk", "United States": "com", 
                   "Canada": "ca", "Australia": "com.au", "Ireland": "ie", "South Africa": "co.za"}
tld = english_accents[english_accent]

def text_to_speech(input_language, output_language, text, tld):
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp_audio/{my_file_name}.mp3")
    return my_file_name, trans_text

display_output_text = st.checkbox("Display output text")

if st.button("Convert Text to Speech"):
    result, output_text = text_to_speech(input_language, output_language, text, tld)
    audio_file = open(f"temp_audio/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Your audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    if display_output_text:
        st.markdown(f"## Output text:")
        st.write(f" {output_text}")

def remove_audio_files(n):
    audio_files = glob.glob("temp_audio/*mp3")
    if len(audio_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in audio_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)

remove_audio_files(7)

st.write("""
---
## Speech to Text
""")

uploaded_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])

if uploaded_file is not None:
    audio_data = uploaded_file.read()

    st.audio(audio_data, format="audio/wav", start_time=0)

    r = sr.Recognizer()
    with sr.AudioFile(uploaded_file) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            st.write("Transcribed text:")
            st.write(text)
        except sr.UnknownValueError:
            st.write("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            st.write("Could not request results from Google Speech Recognition service; {0}".format(e))

def remove_text_files(n):
    text_files = glob.glob("temp_text/*")
    if len(text_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in text_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)

remove_text_files(7)
