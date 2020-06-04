def binarySearch(alist, target):
    start = 0
    end = len(alist) - 1

    while start <= end:
        middle = (start + end)// 2
        midpoint = alist[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint, middle