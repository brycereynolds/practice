def mergesort(arr):
    """Mergesort is a fast, comparison sorting algorithm that is asymptotically
    optimal: any comparison algorithm is at best Omega nlogn. 

    Uses a divide-and-conquer recursive paradigm to partition an input list into
    1 element sublists. This is very quick. Then merges the sublists together with the
    merge subroutine. 

    Mergesort has the following time and space complexities:

        Best Case Time Complexity:      O(nlog(n))
        Avg Case Time Complexity:       O(nlog(n))
        Worst Case Time Complexity:     O(nlog(n))
        Worst Case Space Complexity:    O(n)

    Pros:
        - Most implementations are stable
            Stable sorts maintain the original order of equal elements
            This is useful in the case that satalite data is stored with these elem.
        - Faster than quicksort and heapsort for linked lists

    Cons:
        - High space Complexity
        - Does not sort in-space
        - Slower on average than Quicksort
        - More space than Heapsort
    """
    if len(arr) < 2: return arr

    middle = int(len(arr) / 2)
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:] + right[j:])
    return result

arr = [434, 23, 3, 3,2, 1, 4, 5, 6, 4, 3, 2, 1, 85]

print(mergesort(arr))

