nums = [15, 3, 24, 8, 42, 10]

def find_min_max(num):
    min = num[0]
    max = num[0]

    for n in num:
        if min > n:
            min = n
        if max < n:
            max = n
    
    return (max,min)

maxNum, minNum = find_min_max(nums)

print(f"최대값: {maxNum}, 최소값: {minNum}")
