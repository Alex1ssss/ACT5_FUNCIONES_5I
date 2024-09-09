print("Manejo de funciones V1")
def hola_mundo():
    print("Hola aqui estoy dentro de la funcion")
def mensa(msg):
    print(msg)
def escribeNC(nombre,apellido):
    print(nombre,apellido)
    print(f"tu nombre completo es: {nombre} {apellido}")
def suma2numeros(n1, n2):
    s=n1+n2
    return f"la suma de {n1} y {n2} es de: {s} "
# llamando a la funcion
hola_mundo()
mensa("hola whatsapp")# llama a mensa con un parametro
mensa("el profe me sorprendio enviando mensajes")#vuelve a llamar 
escribeNC("ALEXIS","ESPINO")
print("funciones que regresan valores")
print (suma2numeros(7,3))
print (suma2numeros(15,45))
