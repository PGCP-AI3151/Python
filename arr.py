
# def longest(arr):
#     if len(arr) == 0:
#         return 0
#
#     long = -1
#     lookup = set(arr)
#     for n in lookup:
#         count = 0
#         if n-1 not in lookup:
#             count += 1
#             while n+1 in lookup:
#                 count += 1
#                 n += 1
#         if count > long:
#             long = count
#
#     return long
#
# if __name__=="__main__":
#     arr = [1,2,3,4,0,8,5,6,7,10]
#     print(longest(arr))

def product(arr):
    if len(arr) == 0:
        return 0
    result = []
    ls = 1
    for i in range(len(arr)):
        rs = 1

        if 0 in arr[i+1:]:
            rs = 0
        else:
            j = len(arr) - 1
            while j > i:
                rs *= arr[j]
                j -= 1

        result.append(ls*rs)
        ls *= arr[i]

    return result

if __name__=="__main__":
    arr = [10,2,20,0]
    print(product(arr))
