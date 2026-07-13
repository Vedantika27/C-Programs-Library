def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    target_value = 22
    
    result = linear_search(sample_list, target_value)
    print("Element found at index:", result)
