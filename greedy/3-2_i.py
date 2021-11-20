n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
big_1 = data[n-1]
big_2 = data[n-2]
 
result = 0
i = 0
while i < m:
    for j in range(k):
        result += big_1
        i += 1 
        #print(i, "big_1-",j, result)
        if i == m:
            break;
        else:
            result += big_2
            i += 1
            #print(">>>>>>>", i, "big_2", result)
    
print(result)