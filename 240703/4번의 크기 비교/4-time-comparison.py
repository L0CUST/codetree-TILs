a = int(input())
b, c, d, e = map(int, input().split())
nums = [b, c, d, e]

for num in nums:
    if (a > num):
        print(1)
    else:
        print(0)