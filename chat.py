import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from function import *
import json
import torch
from model import NeuralNet
from train import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intent.json', 'r') as f:
    intents = json.load(f)

data = torch.load("data.pth",map_location=torch.device('cpu'), weights_only=True)

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

if prob.item() > 0.5:
    for intent in intents["intents"]:
        if tag == intent["tag"]:
            button = st.button("Run")
            if button:
                print(intent['responses'])
                if intent['responses'] == ['PBV']:
                    st.write("## Result :")
                    data = pd.read_csv(uploadedFile)

                    data['PBV'] = PBV_BVPS(data['MARKET_PRICE'], data['BOOK_VALUE_PER_SHARE'])
                    columnSort = data['PBV'].tolist()
                    sortedColumn = quick_sort(columnSort)

                    sorted_index = [columnSort.index(val) for val in sortedColumn]
                    dataSorted = data.iloc[sorted_index].reset_index(drop=True)

                    st.write("### Data Tabel")
                    AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)

                elif intent['responses'] == "PE RATIO":
                    data = pd.read_csv(uploadedFile)

                    data['PBV'] = PBV_BVPS(data['MARKET_PRICE'], data['BOOK_VALUE_PER_SHARE'])
                    columnSort = data['PBV'].tolist()
                    sortedColumn = quick_sort(columnSort)

                    sorted_index = [columnSort.index(val) for val in sortedColumn]
                    dataSorted = data.iloc[sorted_index].reset_index(drop=True)
                
                    st.write("### Data Tabel")
                    AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)

                elif intent['responses'] == "DIVIDENT YIELD":
                    data = pd.read_csv(uploadedFile)

                    data['PBV'] = PBV_BVPS(data['MARKET_PRICE'], data['BOOK_VALUE_PER_SHARE'])
                    columnSort = data['PBV'].tolist()
                    sortedColumn = quick_sort(columnSort)

                    sorted_index = [columnSort.index(val) for val in sortedColumn]
                    dataSorted = data.iloc[sorted_index].reset_index(drop=True)
                
                    st.write("### Data Tabel")
                    AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)

else:
    print(f"Saya tidak mengerti maksud anda...")



# st.write("## Result :")
# if uploadedFile is not None:
#     data = pd.read_csv(uploadedFile)
#     data['PBV'] = PBV_BVPS(data['MARKET_PRICE'], data['BOOK_VALUE_PER_SHARE'])
#     columnSort = data['PBV'].tolist()
#     sortedColumn = quick_sort(columnSort)
#     sorted_index = [columnSort.index(val) for val in sortedColumn]
#     dataSorted = data.iloc[sorted_index].reset_index(drop=True)
#     st.write("### Data Tabel")
#     AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)
# else:
#     st.info("Silahkan unggah file csv terlebih dahulu!")