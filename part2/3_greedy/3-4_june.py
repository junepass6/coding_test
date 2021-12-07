n, k = map(int, input().split())
count = 0

while n > k:
    b = n % k
    if b != 0:
        n -= b
        count += b
    else: 
        count += 1
        n = n // k
        
print(count)