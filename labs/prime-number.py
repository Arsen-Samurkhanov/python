# primeArr = [
#     True,
#     True,
#     True,
#     True,
#     True,
#     True,
#     True,
#     True,
#     True,
#     True,
# ]

x = 10

primeArr = [True] * (x + 1)
primeArr[0] = primeArr[1] = False
print(primeArr)
primeNum = 2
while primeNum * primeNum <= x:
    if primeArr[primeNum]:
        innerLoop = primeNum*primeNum
        while innerLoop <= x:
            primeArr[innerLoop] = False
            innerLoop += primeNum
            
    
    primeNum += primeNum
print(primeArr)

