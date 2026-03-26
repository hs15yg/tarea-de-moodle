diccionario = {}

def buscar_coder(diccionario, cedula):
    coderf = None
    for id , coder in diccionario.items():
        if coder["cedula"] == cedula:
            coderf = cedula
            break
    return coderf





diccionario = {
    
        1:{"nombre": "hillary",
             "apellido": "yepes",
             "cedula": 16349809},
        2: {"nombre": "carlos",
               "apellido": "aponte",
               "cedula": 17496076},
        3:{"nombre": "johan",
             "apellido": "mantilla",
             "cedula": 1089898},
        4: { "nombre" : "sofia",
               "edad": "19",
               "cedula": 7690029},
         
        5:{ "nombre": "angela",
               "apellido": "sanchez",
                "cedula": 89076890}
         }




cc = int(input("Dig el numero de cedula: "))


print("Imprimiendo busqueda\n")
print(buscar_coder(diccionario, cc))

print(diccionario)


    
     