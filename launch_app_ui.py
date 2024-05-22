import gradio as gr
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
import matplotlib.pyplot as plt
import keras
import numpy as np
import pickle
import tempfile

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Intialize files globaly.
model = None
tokenizer = None
        
def load_model_and_tokenizer(model_path, tokenizer_path):
    """
    Loads the model and tokenizer using the provided names.
    """
    try:
        # Load model
        model = tf.keras.models.load_model(model_path)
        # Load tokenizer
        with open(tokenizer_path, 'rb') as f:
            tokenizer = pickle.load(f)
        return model, tokenizer, None
    except Exception as e:
        return None, None, f"Помилка при завантаженні моделі та токенайзера: {e}"

def predict_text(text, model_file, tokenizer_file, mode, language, model=None, tokenizer=None):
    """
    Makes predictions on the given text using the provided model, mode, and language.
    """
    # Load model and tokenizer from the uploaded files
    #model, tokenizer, error = load_model_and_tokenizer(model_file.name, tokenizer_file.name)
    #if error:
        #return error
    # Завантаж модель і токенайзер лише один раз
    if model is None or tokenizer is None:
        model, tokenizer, error = load_model_and_tokenizer(model_file.name, tokenizer_file.name)
        if error:
            return error, None

    if mode == "emotion_analysis":
        # Tokenize text using the loaded tokenizer
        if isinstance(tokenizer, keras.preprocessing.text.Tokenizer):
            # Keras Tokenizer
            text_sequences = tokenizer.texts_to_sequences([text])  # Convert text to a list for tokenization
            inputs = pad_sequences(text_sequences, maxlen=80, padding='post')  # Pad sequences
        else:
            # Assuming Transformer tokenizer
            inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

        # Make predictions
        outputs = model.predict(inputs)

        # Get predicted emotions
        emotions = {0: 'joy', 1: 'anger', 2: 'love', 3: 'sadness', 4: 'fear', 5: 'surprise'}
        predicted_emotions = [emotions[i] for i in range(len(emotions))]
        predicted_probabilities = outputs.tolist()[0]

        # Find the most probable emotion
        most_probable_idx = np.argmax(predicted_probabilities)
        most_probable_emotion = predicted_emotions[most_probable_idx]
        most_probable_probability = predicted_probabilities[most_probable_idx]

        # Plot the result
        plt.figure(figsize=(8, 6))
        plt.barh(predicted_emotions, predicted_probabilities)
        plt.xlabel('Шанс', fontsize=15)
        plt.ylabel('Емоція', fontsize=15)
        plt.title('Аналіз Емоції Настрою', fontsize=18)
        plt.axhline(y=most_probable_idx, color='red', linestyle='--', label=f'Most Probable: {most_probable_emotion} ({most_probable_probability:.2f})')
        plt.legend()
        
        # Save the plot to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        plt.savefig(temp_file.name)
        plt.close()

        # Highlight the predicted emotion
        result = f"**Передбачена емоція:** {most_probable_emotion} ({most_probable_probability:.2f})\n"
        result += "Список емоцій: " + str(predicted_emotions) + "\n"
        result += "Шанс кожної емоції: " + str(predicted_probabilities)
        return result, temp_file.name

    elif mode == "sentiment_analysis":
        if isinstance(tokenizer, keras.preprocessing.text.Tokenizer):
            # Keras Tokenizer
            sequence = tokenizer.texts_to_sequences([text])  # Convert text to a sequence
            padded = pad_sequences(sequence, maxlen=80, padding='post')  # Pad the sequence
            inputs = tf.convert_to_tensor(padded, dtype=tf.int32)  # Convert to tensor
        else:
            # Assuming Transformer tokenizer
            inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

        # Make predictions
        outputs = model.predict(inputs)

        # Get sentiment prediction
        sentiment = outputs.item()

        # Plot the result
        plt.figure(figsize=(6, 4))
        plt.barh(['Негативний', 'Позитивний'], [1-sentiment, sentiment])
        plt.xlabel('Шанс', fontsize=15)
        plt.ylabel('Настрій', fontsize=15)
        plt.title('Аналіз Настрою', fontsize=18)
        
        # Save the plot to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        plt.savefig(temp_file.name)
        plt.close()

        # Highlight the predicted sentiment
        sentiment_label = "Позитивний" if sentiment > 0.5 else "Негативний"
        result = f"**Передбачений настрій:** {sentiment_label} ({sentiment:.2f})"
        return result, temp_file.name

    elif mode == "none":
        return text

    else:
        return "Режим не підтримується."

# Interface with mode selection
iface = gr.Interface(
    fn=predict_text,
    inputs=[
     gr.Textbox(label="Текстове повідомлення", lines=5),
     gr.File(type="file", label="Upload Model (.h5)"),
     gr.File(type="file", label="Upload Tokenizer (.pickle)"),
     gr.Dropdown(["emotion_analysis", "sentiment_analysis", "none"], label="Режим"),
     gr.Dropdown(["ukrainian", "english"], label="Мова")
    ],
    outputs=["text", "image"],
    title="Emotion Analyzer",
    description="Upload a text and model/tokenizer files (.h5 and .pickle) to predict the emotion.",
    allow_flagging="never"
)

# Run the interface
iface.launch()




