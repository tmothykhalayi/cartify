import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import speech_recognition as sr
import pyttsx3

# Create the translator object
translator = Translator()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to perform translation
def translate_text():
    source_text = source_text_box.get("1.0", tk.END).strip()
    src_lang = source_lang.get()
    dest_lang = target_lang.get()
    
    if source_text:
        try:
            translated = translator.translate(source_text, src=src_lang, dest=dest_lang)
            target_text_box.delete("1.0", tk.END)
            target_text_box.insert(tk.END, translated.text)
        except Exception as e:
            target_text_box.delete("1.0", tk.END)
            target_text_box.insert(tk.END, f"Error: {e}")

# Function for voice input
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        target_text_box.delete("1.0", tk.END)
        target_text_box.insert(tk.END, "Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            source_text_box.delete("1.0", tk.END)
            source_text_box.insert(tk.END, text)
        except Exception as e:
            target_text_box.delete("1.0", tk.END)
            target_text_box.insert(tk.END, f"Voice recognition error: {e}")

# Function for text-to-speech
def text_to_speech():
    text = target_text_box.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

# Initialize the main application window
app = tk.Tk()
app.title("Real-Time Language Translator with Voice")
app.geometry("600x500")

# Language selection drop-downs
source_lang = ttk.Combobox(app, values=list(LANGUAGES.keys()), width=20)
source_lang.set("en")  # Default source language
source_lang_label = tk.Label(app, text="Source Language:")
source_lang_label.pack(pady=5)
source_lang.pack(pady=5)

target_lang = ttk.Combobox(app, values=list(LANGUAGES.keys()), width=20)
target_lang.set("fr")  # Default target language
target_lang_label = tk.Label(app, text="Target Language:")
target_lang_label.pack(pady=5)
target_lang.pack(pady=5)

# Text boxes for input and output
source_text_box = tk.Text(app, height=10, width=50)
source_text_box.pack(pady=10)

translate_button = tk.Button(app, text="Translate", command=translate_text)
translate_button.pack(pady=5)

target_text_box = tk.Text(app, height=10, width=50)
target_text_box.pack(pady=10)

# Voice input and output buttons
voice_input_button = tk.Button(app, text="Speak (Input)", command=voice_input)
voice_input_button.pack(pady=5)

text_to_speech_button = tk.Button(app, text="Speak (Output)", command=text_to_speech)
text_to_speech_button.pack(pady=5)

# Run the application
app.mainloop()
