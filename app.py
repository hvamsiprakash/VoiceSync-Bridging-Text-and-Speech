# import streamlit as st
# import os
# import time
# import glob

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
#     ("English", "Hindi", "Bengali", "Korean", "Chinese", "Japanese"),
# )
# if in_lang == "English":
#     input_language = "en"
# elif in_lang == "Hindi":
#     input_language = "hi"
# elif in_lang == "Bengali":
#     input_language = "bn"
# elif in_lang == "Korean":
#     input_language = "ko"
# elif in_lang == "Chinese":
#     input_language = "zh-cn"
# elif in_lang == "Japanese":
#     input_language = "ja"

# out_lang = st.selectbox(
#     "Select your output language",
#     ("English", "Hindi", "Bengali", "Korean", "Chinese", "Japanese"),
# )
# if out_lang == "English":
#     output_language = "en"
# elif out_lang == "Hindi":
#     output_language = "hi"
# elif out_lang == "Bengali":
#     output_language = "bn"
# elif out_lang == "Korean":
#     output_language = "ko"
# elif out_lang == "Chinese":
#     output_language = "zh-cn"
# elif out_lang == "Japanese":
#     output_language = "ja"

# english_accent = st.selectbox(
#     "Select your English accent",
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
#     try:
#         translation = translator.translate(text, src=input_language, dest=output_language)
#         trans_text = translation.text
#         tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
#         try:
#             my_file_name = text[0:20]
#         except:
#             my_file_name = "audio"
#         tts.save(f"temp/{my_file_name}.mp3")
#         return my_file_name, trans_text
#     except ValueError as e:
#         st.error(f"Error: {str(e)}")


# display_output_text = st.checkbox("Display output text")

# if st.button("Convert"):
#     result = text_to_speech(input_language, output_language, text, tld)
#     if result:
#         audio_file = open(f"temp/{result[0]}.mp3", "rb")
#         audio_bytes = audio_file.read()
#         st.markdown(f"## Your audio:")
#         st.audio(audio_bytes, format="audio/mp3", start_time=0)

#         if display_output_text:
#             st.markdown(f"## Output text:")
#             st.write(f" {result[1]}")


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

import streamlit as st
import os
import time
import glob
from gtts import gTTS
from googletrans import Translator
from pydub import AudioSegment
from pydub.playback import play
import numpy as np

try:
    os.mkdir("temp")
except:
    pass

# Setting up Streamlit page title and description
st.title("VoiceSync-Bridging-Text-and-Speech")
st.sidebar.title("How VoiceSync Works")

# Adding description in sidebar markdown
st.sidebar.markdown(
    """
    **VoiceSync** is a tool that converts text into speech with various language options. 
    It uses Google Translate for language translation and the Google Text-to-Speech (gTTS) library for generating speech from text.
    Users can input text, select the desired input and output languages, customize speech parameters, and listen to the generated audio.
    """
)

translator = Translator()

# Larger input text size
text = st.text_area("Enter text", height=150)

# Mapping input and output languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Korean": "ko",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Russian": "ru",
    "Italian": "it",
    "Portuguese": "pt",
}

input_lang = st.selectbox("Select input language", list(languages.keys()))
output_lang = st.selectbox("Select output language", list(languages.keys()))

input_language = languages[input_lang]
output_language = languages[output_lang]

# Selecting English accent
english_accents = {
    "Default": "com",
    "India": "co.in",
    "United Kingdom": "co.uk",
    "United States": "com",
    "Canada": "ca",
    "Australia": "com.au",
    "Ireland": "ie",
    "South Africa": "co.za",
}

english_accent = st.selectbox("Select English accent", list(english_accents.keys()))

tld = english_accents[english_accent]

# Customization options
speech_rate = st.slider("Speech Rate", 0.5, 2.0, 1.0, step=0.1)
speech_pitch = st.slider("Speech Pitch", 0.5, 2.0, 1.0, step=0.1)
speech_volume = st.slider("Speech Volume", 0.0, 1.0, 1.0, step=0.1)


def text_to_speech(input_language, output_language, text, tld, speech_rate, speech_pitch, speech_volume):
    try:
        translation = translator.translate(text, src=input_language, dest=output_language)
        trans_text = translation.text
        tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
        tts.speed = speech_rate
        tts.pitch = speech_pitch
        tts.volume = speech_volume
        try:
            my_file_name = text[0:20]
        except:
            my_file_name = "audio"
        tts.save(f"temp/{my_file_name}.mp3")
        return my_file_name, trans_text
    except ValueError as e:
        st.error(f"Error: {str(e)}")


# Display output text option
display_output_text = st.checkbox("Display output text")

# Convert button
if st.button("Convert"):
    result = text_to_speech(input_language, output_language, text, tld, speech_rate, speech_pitch, speech_volume)
    if result:
        audio_file = open(f"temp/{result[0]}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown("## Your audio:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)

        if display_output_text:
            st.markdown("## Output text:")
            st.write(f" {result[1]}")

        # Highlighting text synchronized with speech output
        audio = AudioSegment.from_mp3(f"temp/{result[0]}.mp3")
        durations = np.cumsum([0] + [len(chunk) for chunk in audio])
        st.markdown("## Highlighted Text:")
        for i in range(len(text)):
            st.markdown(
                f"<span style='background-color: {'yellow' if durations[i] <= len(audio) else 'white'}'>{text[i]}</span>",
                unsafe_allow_html=True,
            )


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)

