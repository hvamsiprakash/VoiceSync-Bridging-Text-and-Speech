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


import streamlit as st
import os
import librosa
import torch
import soundfile as sf
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from expertai.nlapi.cloud.client import ExpertAiClient

# Set up directories
audio_folder = "uploaded_audio"
Path(audio_folder).mkdir(parents=True, exist_ok=True)

# Function to process uploaded audio file
def process_audio(file_path):
    # Load uploaded audio file using Librosa
    audio, sr = librosa.load(file_path, sr=16000)
    
    # Perform speech recognition using PyTorch with Transformers
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    input_values = processor(audio, return_tensors="pt").input_values
    logits = model(input_values).logits
    transcription = processor.decode(torch.argmax(logits, dim=-1)[0])
    
    # Analyze transcribed text using Expert.ai NLU API
    client = ExpertAiClient()
    analysis = client.specific_resource_analysis(text=transcription, language="en", resource="relevants")
    
    # Extract relevant information from the analysis
    entities = [entity.value for entity in analysis.entities]
    
    # Print or process the extracted information as needed
    print("Transcription:", transcription)
    print("Entities:", entities)
    
    return transcription, entities

# Streamlit app
st.title("Speech to Text Analysis")

# File upload section
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

if uploaded_file is not None:
    # Save the uploaded file
    file_path = os.path.join(audio_folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process the uploaded audio file
    st.write("Processing audio file...")
    transcription, entities = process_audio(file_path)
    
    # Display results
    st.write("Transcription:", transcription)
    st.write("Entities:", entities)


# remove_files(7)






