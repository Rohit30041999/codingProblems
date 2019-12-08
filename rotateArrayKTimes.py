#ROTATE ARRAY K TIMES:>>>>>

def rotateArray(arr: list, k: int) -> list:
  if len(arr) <= 0 : return arr
  if k % len(arr) == 0: return arr
  k = k % len(arr)
  arr = arr[k:] + arr[:k]
  return arr

array = [1, 2, 3, 4, 5]
array1 = []
array2 = [1]
print(rotateArray(array, 212345566))
print(rotateArray(array1, 45))
print(rotateArray(array2, 21234556))
