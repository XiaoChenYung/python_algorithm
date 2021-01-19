import math, time

def binary_search(arr, val):
    """
    binary search
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = math.floor((low + high)/2)
        print(mid)
        time.sleep(1)
        mid_val = arr[mid]
        if mid_val == val:
            return mid
        if mid_val > val:
            high = mid - 1
        if mid_val < val:
            low = mid + 1
    return None

if __name__ == "__main__":
    arr = [1, 3, 6, 7, 8, 9]
    index = binary_search(arr, 3)
    print(index)
    