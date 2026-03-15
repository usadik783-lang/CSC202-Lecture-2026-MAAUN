import random

# 1. Generate Data
scores = [random.randint(1, 100) for _ in range(10)]
print("Original Scores:", scores)

# 2. Recursive Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Sort the scores
sorted_scores = merge_sort(scores)
print("Sorted Scores:", sorted_scores)


# 3. Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# 4. Ask user for score
x = int(input("Enter the score you want to find: "))

# Execute search
rank = binary_search(sorted_scores, x)

if rank != -1:
    print(f"Candidate with score {x} found at rank {rank}.")
else:
    print("Score not found.")
