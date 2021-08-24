
def swap_case(s):
    arr = []
    swaped = ''
    for i in s:
        if i != i.lower():
            arr.append(i.lower())
        else:
            arr.append(i.upper())
    for i in range(len(arr)):
        swaped += arr[i]
    return swaped


print(swap_case(input()))
