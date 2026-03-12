# solicitar nombre del producto
string = input("ingrese el nombre del producto: ")
# Pedir precio con validación
precio_valido = False
while precio_valido == False:
     try:
         Precio = float(input("Ingrese el precio del producto: "))
         precio_valido = True
     except ValueError:
         print("Valor inválido. Por favor ingrese un número para el precio.  ")
# Pedir Cantidad con validación
cantidad_valido = False
while cantidad_valido == False:
     try:
         Cantidad = int(input("Ingrese la cantidad del producto: "))  
         cantidad_valido = True
     except ValueError:
      print("valor invalido. Por favor ingrese un número entero para la cantidad")
# Mostrar resultado
print("Producto:", string)
print("Precio:", Precio)
print("Cantidad:", Cantidad)
# Calcular valor total
Costo_total = Precio * Cantidad
print("Costo total calculado:", Costo_total)