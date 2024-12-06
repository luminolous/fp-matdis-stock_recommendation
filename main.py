import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


def stock_recommendation(name, market_price, bvps):
  if len(bvps) == 1:
    def PBV(market_price, bvps):
      return market_price / bvps[0]
  else:
    def PBV(market_price, bvps):
      return market_price / (bvps[0] / bvps[1])
    
def PBV_BVPS(market_price, bvps):
  return market_price / bvps
# def PBV_Equity(market_price, equity, stocks):
#   return market_price / (equity / stocks)

def quick_sort(arr):
  if len(arr) <= 1:
      return arr

  pivot = arr[-1]

  left = [x for x in arr[:-1] if x <= pivot]
  right = [x for x in arr[:-1] if x > pivot]

  return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
    st.title("Stocks Recommendation")
    st.write("## Input :")
    st.write("Masukkan file csv yang berisikan kolom (MARKET_PRICE,BOOK_VALUE_PER_SHARE)")
    uploadedFile = st.file_uploader("Unggah file CSV Anda", type=["csv"])
    st.write("## Result :")
    if uploadedFile is not None:
            data = pd.read_csv(uploadedFile)
            data['PBV'] = PBV_BVPS(data['MARKET_PRICE'], data['BOOK_VALUE_PER_SHARE'])
            columnSort = data['PBV'].tolist()
            sortedColumn = quick_sort(columnSort)
            sorted_index = [columnSort.index(val) for val in sortedColumn]
            dataSorted = data.iloc[sorted_index].reset_index(drop=True)
            st.write("### Data Tabel")
            AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)

    else:
       st.info("Silahkan unggah file csv terlebih dahulu!")