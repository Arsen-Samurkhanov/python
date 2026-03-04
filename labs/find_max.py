arr = [50, 32, 1, 78, 4, 3, 10, 99, 65]

max = arr[0]
v= 0
while v < len(arr):
    if max < arr[v]:
        max = arr[v]
    #print(arr[v])
    v +=1   
print(max)


max = arr[0]
for v in arr:
    if v > max:
            max = v
print(max)        