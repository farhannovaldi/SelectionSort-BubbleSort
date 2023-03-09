def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [60, 2, 11, 32, 5]
print("Array sebelum diurutkan:", arr)
bubble_sort(arr)
print("Array setelah diurutkan:", arr)
