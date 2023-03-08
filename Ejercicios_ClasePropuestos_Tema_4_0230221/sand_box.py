
numeros = [1000,9000,500,400,100,90,50,40,10,9,5,4,1]
romanos = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
zipped = zip(numeros, romanos)
dicc = {zipped}

print(dicc[5])

# for i in dicc:
#     print(i)