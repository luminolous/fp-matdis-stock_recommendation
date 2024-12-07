def PBV_BVPS(market_price, bvps):
  return round((market_price / bvps), 2)

def PE_Ratio(market_price, EPS):
    return round((market_price / EPS), 2)

def divident_yield(divident, market_price):
    return round((divident / market_price), 2)

# def 
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