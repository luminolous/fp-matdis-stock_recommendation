import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


def PBV_BVPS(market_price, bvps):
  return round((market_price / bvps), 2)

def PE_Ratio(market_price, netto, stocks):
    return round((market_price / EPS(netto, stocks)), 2)

def divident_yield(divident, market_price):
    return round((divident / market_price), 2)

def EPS(netto, stocks):
    return round((netto / stocks), 2)


def quick_sort_reverse(arr):
  if len(arr) <= 1:
      return arr

  pivot = arr[-1]

  left = [x for x in arr[:-1] if x <= pivot]
  right = [x for x in arr[:-1] if x > pivot]

  return quick_sort_reverse(left) + [pivot] + quick_sort_reverse(right)

def quick_sort(arr):
  if len(arr) <= 1:
      return arr

  pivot = arr[-1]

  left = [x for x in arr[:-1] if x <= pivot]
  right = [x for x in arr[:-1] if x > pivot]

  return quick_sort(right) + [pivot] + quick_sort(left)
  

def pbv(uploadedFile):
  data = pd.read_csv(uploadedFile)

  data['PBV'] = PBV_BVPS(data['MARKET_PRICE'], data['BOOK_VALUE_PER_SHARE'])
  columnSort = data['PBV'].tolist()
  sortedColumn = quick_sort(columnSort)

  sorted_index = [columnSort.index(val) for val in sortedColumn]
  dataSorted = data.iloc[sorted_index].reset_index(drop=True)

  st.write("### Data Tabel")
  return AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)

def pbv_reverse(uploadedFile):
  data = pd.read_csv(uploadedFile)

  data['PBV'] = PBV_BVPS(data['MARKET_PRICE'], data['BOOK_VALUE_PER_SHARE'])
  columnSort = data['PBV'].tolist()
  sortedColumn = quick_sort_reverse(columnSort)

  sorted_index = [columnSort.index(val) for val in sortedColumn]
  dataSorted = data.iloc[sorted_index].reset_index(drop=True)

  st.write("### Data Tabel")
  return AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)

def pe_ratio(uploadedFile):
  data = pd.read_csv(uploadedFile)

  data['PE_RATIO'] = PE_Ratio(data['MARKET_PRICE'], data['NETTO'], data['STOCKS'])
  columnSort = data['PE_RATIO'].tolist()
  sortedColumn = quick_sort(columnSort)

  sorted_index = [columnSort.index(val) for val in sortedColumn]
  dataSorted = data.iloc[sorted_index].reset_index(drop=True)
                
  st.write("### Data Tabel")
  return AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)

def pe_ratio_reverse(uploadedFile):
  data = pd.read_csv(uploadedFile)

  data['PE_RATIO'] = PE_Ratio(data['MARKET_PRICE'], data['NETTO'], data['STOCKS'])
  columnSort = data['PE_RATIO'].tolist()
  sortedColumn = quick_sort_reverse(columnSort)

  sorted_index = [columnSort.index(val) for val in sortedColumn]
  dataSorted = data.iloc[sorted_index].reset_index(drop=True)
                
  st.write("### Data Tabel")
  return AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)

def divident_yield(uploadedFile):
  data = pd.read_csv(uploadedFile)

  data['DIVIDENT_YIELD'] = divident_yield(data['DIVIDENT'], data['MARKET_PRICE'])
  columnSort = data['DIVIDENT_YIELD'].tolist()
  sortedColumn = quick_sort(columnSort)

  sorted_index = [columnSort.index(val) for val in sortedColumn]
  dataSorted = data.iloc[sorted_index].reset_index(drop=True)
                
  st.write("### Data Tabel")
  return AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)

def divident_yield_reverse(uploadedFile):
  data = pd.read_csv(uploadedFile)

  data['DIVIDENT_YIELD'] = divident_yield(data['DIVIDENT'], data['MARKET_PRICE'])
  columnSort = data['DIVIDENT_YIELD'].tolist()
  sortedColumn = quick_sort_reverse(columnSort)

  sorted_index = [columnSort.index(val) for val in sortedColumn]
  dataSorted = data.iloc[sorted_index].reset_index(drop=True)
                
  st.write("### Data Tabel")
  return AgGrid(dataSorted, editable=False, height=400, fit_columns_on_grid_load=True)