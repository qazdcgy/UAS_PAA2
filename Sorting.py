import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def print_iterations(arr):
    print("5 iterasi pertama:")
    for i in range(5):
        print(arr[i], end=" ")
    print("\n5 iterasi terakhir:")
    for i in range(len(arr)-5, len(arr)):
        print(arr[i], end=" ")
    print()

def print_execution_time(start_time):
    end_time = time.time()
    execution_time = end_time - start_time
    print("Waktu komputasi:", execution_time, "detik")

def print_before_after(before_arr, arr):
    print("Sebelum pengurutan:", before_arr)
    print("Setelah pengurutan:", arr)

arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

print("Pilihan algoritma pengurutan:")
print("1. Bubble Sort")
print("2. Insertion Sort")
choice = input("Masukkan pilihan (1/2): ")

if choice == '1':
    before_arr = arr.copy()
    start_time = time.time()
    bubble_sort(arr)
    print_iterations(arr)
    print_execution_time(start_time)
    print_before_after(before_arr, arr)
elif choice == '2':
    before_arr = arr.copy()
    start_time = time.time()
    insertion_sort(arr)
    print_iterations(arr)
    print_execution_time(start_time)
    print_before_after(before_arr, arr)
else:
    print("Pilihan tidak valid.")
