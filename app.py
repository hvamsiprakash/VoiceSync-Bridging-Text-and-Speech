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



import streamlit as st
import os
import time
import glob

from gtts import gTTS
from googletrans import Translator

try:
    os.mkdir("temp")
except:
    pass

# Unique title and description in the sidebar
st.sidebar.title("VoiceSync: Bridging Text and Speech")
st.sidebar.write(
    """
    VoiceSync is a powerful tool that seamlessly converts text to speech in multiple languages. 
    Simply enter your text, select input and output languages, and even customize speech parameters. 
    Experience the convenience of converting your written content into spoken words with VoiceSync!
    """
)

translator = Translator()

# Supported languages (input and output)
languages = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Korean": "ko",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    # Add more languages here
}

# Language selection interface
st.sidebar.subheader("Input Language:")
input_language = st.sidebar.selectbox("Select your input language", list(languages.keys()))

st.sidebar.subheader("Output Language:")
output_language = st.sidebar.selectbox("Select your output language", list(languages.keys()))

# Speech parameters
st.sidebar.subheader("Speech Parameters:")
speed = st.sidebar.slider("Speed", min_value=0.5, max_value=2.0, value=1.0, step=0.1, format="%.1f")
volume = st.sidebar.slider("Volume", min_value=0.0, max_value=1.0, value=1.0, step=0.1, format="%.1f")
pitch = st.sidebar.slider("Pitch", min_value=0.5, max_value=2.0, value=1.0, step=0.1, format="%.1f")

text = st.text_area("Enter text", height=200)

def text_to_speech(input_language, output_language, text, tld):
    # Language mapping for gTTS compatibility
    language_mapping = {
        "en": "en",
        "hi": "hi",
        "bn": "bn",
        "ko": "ko",
        "zh-cn": "zh",
        "ja": "ja",
    }
    
    # Translate text
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    
    # Determine gTTS-compatible language code
    gtts_output_language = language_mapping.get(output_language)
    if gtts_output_language is None:
        raise ValueError("Language not supported by gTTS: %s" % output_language)
    
    # Generate speech
    tts = gTTS(trans_text, lang=gtts_output_language, slow=False)
    tts.save("temp/audio.mp3")
    
    return trans_text

if st.button("Convert"):
    try:
        output_text = text_to_speech(input_language, output_language, text, tld="")
        audio_file = open("temp/audio.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown("### Your audio:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        st.markdown("### Output text:")
        st.write(output_text)
    except ValueError as e:
        st.error(str(e))

# Function to remove old audio files
def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)

remove_files(7)
