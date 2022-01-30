test = [1,3,5,7,9]

def minMaxSum(arr):
    arr.sort()
    max = arr[1:]
    min = arr[:4]

    print(sum(min), sum(max))

minMaxSum(test)