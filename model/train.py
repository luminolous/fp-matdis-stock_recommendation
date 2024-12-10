import json
import numpy as np

import nltk
from nltk.stem.porter import PorterStemmer

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from model.modulo import NeuralNet

with open('model/intent.json', 'r') as f:
    intents = json.load(f)

stemer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemer.stem(word.lower())

def bag_of_words(tokenize_sentence, all_words):
    tokenize_sentence = [stem(word) for word in tokenize_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenize_sentence:
            bag[idx] = 1.0
    return bag

all_words = []
tags = []
xy = []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    x_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train
    
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples
    
# Hyperparameter
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate  = 0.001
num_epochs = 1000

if __name__ == '__main__':
    dataset = ChatDataset()
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=2)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = NeuralNet(input_size, hidden_size, output_size).to(device)

    # loss and optimizer
    criterian = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        for (words, labels) in train_loader:
            words = words.to(device)
            labels = labels.to(device)

            # forward
            outputs = model(words)
            loss = criterian(outputs, labels)

            # backward and optimizer step
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch+1) % 100 == 0:
            print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item():.4f}')

    print(f'Final loss, Loss: {loss.item():.4f}')

    data = {
        "model_state" : model.state_dict(),
        "input_size" : input_size,
        "output_size" : output_size,
        "hidden_size" : hidden_size,
        "all_words" : all_words,
        "tags" : tags
    }

    FILE = "data.pth"
    torch.save(data, FILE)

    print(f'training complete, file save to {FILE}')