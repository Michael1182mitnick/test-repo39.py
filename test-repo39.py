# write a Python program to merge two list, remove duplicate an into a single list.

def merge_arrays(arrayA, arrayB):
    #  1: Merge arrayA and arrayB
    #  2: Remove duplicate
    #  3: Sort list in ascending order
    return sorted(set(arrayA + arrayB))

# Example list
a = [1, 2, 3, 3, 4, 5, 6]
b = [4, 4, 5, 6, 7, 8, 9]

c = merge_arrays(a, b)

print(c)
