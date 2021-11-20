n, m = map(int, input().split())

box = []
for i in range(n):
    data = list(map(int, input().split()))
    box.append(min(data))
print(max(box))