import torch
import streamlit as st

# Memuat model
model = torch.load('model/data.pth', map_location=torch.device('cpu'), weights_only=True)

# Gunakan model untuk prediksi atau tugas lainnya
# Menampilkan hasil di Streamlit
print(dir(torch.classes))
import torch

# Misalkan kita memiliki kelas kustom yang digunakan dalam model
class MyCustomClass:
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print(self.data)

# Sekarang Anda dapat memuat model yang bergantung pada kelas ini
model = torch.load('model/data.pth', map_location=torch.device('cpu'), weights_only=True)
