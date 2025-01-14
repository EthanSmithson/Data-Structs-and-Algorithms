list = [1,2,3,4,5,6,7,8,9,10]
target = 5

def binarySearch(list, target):
    n = len(list)
    l = 0
    r = n - 1

    while l <= r:
        m = (l+r) // 2
        if target == list[m]:
            return m
        elif target < list[m]:
            r = m - 1
        else:
            l = m + 1
    
    return -1



print(binarySearch(list, target))