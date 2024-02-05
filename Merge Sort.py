import matplotlib.pyplot as plt
import numpy as np

def merge_sort(arr, ax):
    if len (arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, ax)
        merge_sort(R, ax)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i +=1
            else:
                arr[k] = R[j]
                j += 1
            k +=1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        ax.cla()
        ax.bar(np.arange(len(arr)), arr, color='#C3EEFA')
        plt.pause(1)
def visualize_merge_sort(arr):
    fig, ax = plt.subplots()
    ax.bar(np.arange(len(arr)), arr, color='#C3EEFA', label='Original Array')
    plt.pause(1)
    merge_sort(arr, ax)

    plt.bar(np.arange(len(arr)), arr, color='#C3EEFA', label='Sorted Array')
    plt.show

arr = [40, 25, 43, 5, 11, 89, 12]
visualize_merge_sort(arr)


