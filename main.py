frutas=["aguacate",'melon','tomate','berenjenas',"zanahorias"]

print(frutas)

print(len(frutas))

print(frutas[2])

frutas.append('papaya')
print(frutas)

frutas.append("sandia")
print(frutas )

frutas.sort()
print(frutas)

compra=input('ingresa una fruta :')
frutas.append(compra)

print(frutas)