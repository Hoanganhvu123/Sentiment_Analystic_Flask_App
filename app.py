from flask import Flask, render_template, request
import pickle
import numpy as np
from keras.utils.data_utils import pad_sequences
from keras.models import load_model

app = Flask(__name__)

# # Load the tokenizer
with open('static/models/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# # Load the model
# model = load_model('static/models/model.h5')

# Set max length
max_length = 2000

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/result', methods=['POST'])
# def result():
#     # Get input text
#     text = request.form['text']
#     # Tokenize and pad the text
#     text_seq = tokenizer.texts_to_sequences([text])
#     text_pad = pad_sequences(text_seq, maxlen=max_length, padding='post')
#     # Make prediction
#     prediction = model.predict(text_pad)[0][0]
#     # Round to 2 decimal places
#     prediction = np.round(prediction, 2)
#     # Set sentiment label
#     sentiment = 'Positive' if prediction >= 0.5 else 'Negative'
#     return render_template('result.html', text=text, prediction=prediction, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
