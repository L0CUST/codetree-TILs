h, w = map(int, input().split())
b = int((10000 * w) / (h * h))
if (b >= 25):
    print(b)
    print("Obesity")
else:
    print(b)