class CountInversions:
    def __init__(self):
        self.swaps = 0

    def mergesort(self, arr):
        self._mergesort(arr, 0, len(arr) - 1)

    def _mergesort(self, arr, start, end):
        mid = int((start + end) / 2)
        if start < end:
            self._mergesort(arr, start, mid)
            self._mergesort(arr, mid + 1, end)

        # Break this up...
        a, f, l = 0, start, mid + 1
        tmp = [None] * (end - start + 1)

        while f <= mid and l <= end:
            if arr[f] < arr[l]:
                tmp[a] = arr[f]
                f += 1
            else:
                self.swaps += 1 if mid - f is 0 else mid - f
                tmp[a] = arr[l]
                l += 1
            a += 1

        if f <= mid:
            tmp[a:] = arr[f:mid + 1]

        if l <= end:
            tmp[a:] = arr[l:end + 1]

        a = 0
        while start <= end:
            arr[start] = tmp[a]
            start += 1
            a += 1

sort = CountInversions()
# arr = [23,4,34,12,43,453,3,44,5,3,4,34,4,5]
# arr = [2,1,3,1,2]

mergesort(arr, 0, len(arr) -)
print(sort.swaps)
# print(arr)
