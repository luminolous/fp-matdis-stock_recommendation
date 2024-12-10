import streamlit as st
from function import *
import json
import torch
from model.modulo import NeuralNet   
from model.train import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

with open('model/intent.json', 'r') as f:
    intents = json.load(f)

data = torch.load("data.pth",map_location=torch.device('cpu'))

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

st.title("Stocks Recommendation")
st.write("## Input :")
uploadedFile = st.file_uploader("Masukkan file csv yang berisikan kolom (MARKET_PRICE,BOOK_VALUE_PER_SHARE)", type=["csv"])
sentence = st.text_input("Masukkan prompt:")

sentence = tokenize(sentence)
x = bag_of_words(sentence, all_words)
x = x.reshape(1, x.shape[0])
x = torch.from_numpy(x)

output = model(x)
_, predicted = torch.max(output, dim=1)
tag = tags[predicted.item()]

probs = torch.softmax(output, dim=1)
prob = probs[0][predicted.item()]
print(f"Probabilitas : {prob.item()}")
button = st.button("Run")
st.write("## Result :")

if button:
    if prob.item() > 0.7:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                print(intent['responses'])
                if intent['responses'] == ['PBV']:
                    pbv(uploadedFile)

                elif intent['responses'] == ['PBV REVERSE']:
                    pbv_reverse(uploadedFile)

                elif intent['responses'] == ['PE RATIO']:
                    pe_ratio(uploadedFile)

                elif intent['responses'] == ['PE RATIO REVERSE']:
                    pe_ratio_reverse(uploadedFile)

                elif intent['responses'] == ['DIVIDENT YIELD']:
                    divident_yield(uploadedFile)

                elif intent['responses'] == ['DIVIDENT YIELD REVERSE']:
                    divident_yield_reverse(uploadedFile)
    else:
        st.write("Saya tidak mengerti maksud anda...")