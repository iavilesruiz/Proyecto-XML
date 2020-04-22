# coding=utf-8

#Enlace xml:
#https://paloz.marum.de/bitbucket/projects/SWIFACT/repos/pangaeaclient/raw/Vendor/XMLCoder/Tests/XMLCoderTests/PlantCatalog.swift?at=refs%2Ftags%2F0.0.1

#Importo el archivo de funciones:
import funciones

#Importo lxml:
import lxml.etree as leer

#Importo el documento xml y lo defino como "plantas" para usarlo en el archivo "funciones.py".
with open ("plantas.xml", "rb") as plantas:
  parser = leer.parse(plantas)

#He creado un menú que básicamente te da 6 opciones a elegir y después te pregunta qué opción quieres (del 1 al 6).

print("---------------------------------- MENÚ ----------------------------------")
print("1 - Mostrar los nombres de todas las plantas")
print("2 - Plantas en un rango de precio")
print("3 - Obtener existencias de una planta introduciendo una subcadena o el nombre completo")
print("4 - Poblaciones de una provincia")
print("5 - Provincia d'una població")
print("6 - Salir del menú")
print("--------------------------------------------------------------------------")

#Si no escoges ninguna de las opciones te pide que escojas otra vez mediante un bucle que verifica si la opción es 1, 2, 3, 4, 5 o 6.

comprobado=False
while comprobado==False:
  try:
    op=int(input("Elige una opción: "))
    while op not in range (1,7):
      print("--------------------------------------------------------------------------")
      print("Debes elegir una de las seis opciones.")
      print("--------------------------------------------------------------------------")
      op=int(input("Elige una opción: "))
      print("--------------------------------------------------------------------------")
    comprobado=True
  except:
    print("--------------------------------------------------------------------------")
    print("Debes elegir una de las seis opciones.")
    print("--------------------------------------------------------------------------")

#A continuación están las 8 opciones y creo de nuevo un bucle del cual no se puede salir hasta que se pulse la opción 9 y si se introduce algo que no sea uno de los valores especificados volverá a pedirlo. Al final de cada opción vuelve a pedir elegir otra del menú y hasta que no se elija el número 9 no sale del menú.

while op in range (1,6):
  if op==1:
    solucion=funciones.nombres(parser)
    print("--------------------------------------------------------------------------")
    print("Plantas disponibles:")
    print("")
    print("--------------------------------------------------------------------------")
    for i in solucion:
      print(i)

  if op==2:
    solucion = funciones.precio(parser)
    if solucion==0:
      print("")
      print("No hay intervalo de precios.")
      print("")
      print("--------------------------------------------------------------------------")
    elif solucion==-1:
      print("")
      print("El límite superior es insuficiente.")
      print("")
      print("--------------------------------------------------------------------------")
    elif solucion==-2:
      print("")
      print("El límite inferior tiene un valor incorrecto.")
      print("")
      print("--------------------------------------------------------------------------")
    elif solucion==-3:
      print("")
      print("El límite superior tiene un valor incorrecto.")
      print("")
      print("--------------------------------------------------------------------------")
    else:
      for i in solucion:
        print(i)
      print("--------------------------------------------------------------------------")
  
  if op==3:
    solucion = funciones.existencias(parser)
    if solucion==[]:
      print("No hay ninguna coincidencia.")
    else:
      for i in solucion:
        print(i)
    print("--------------------------------------------------------------------------")

  if op==4:
    solucion = funciones.luz(parser)
    if solucion==[]:
      print("--------------------------------------------------------------------------")
      print("Este tipo de luz no está en la lista.")
      print("--------------------------------------------------------------------------")
    else:
      print("--------------------------------------------------------------------------")
      print("Plantas con este tipo de luz:")
      print("")
      for i in solucion:
        print(i)
      print("--------------------------------------------------------------------------")

  if op==5:
    solucion=funciones.ordenar(parser)
    print("--------------------------------------------------------------------------")
    print("Plantas de más baratas a más caras:")
    print("")
    for i,x in solucion.items():
      print ("%s  -  %s €" %(x,i))
    print("--------------------------------------------------------------------------")

  if op==6:
    break

  comprobado=False
  while comprobado==False:
    try:
      op=int(input("Elige una opción: "))
      while op not in range (1,7):
        print("--------------------------------------------------------------------------")
        print("Debes elegir una de las seis opciones.")
        print("--------------------------------------------------------------------------")
        op=int(input("Elige una opción: "))
        print("--------------------------------------------------------------------------")
      comprobado=True
    except:
      print("--------------------------------------------------------------------------")
      print("Debes elegir una de las seis opciones.")
      print("--------------------------------------------------------------------------")

print("--------------------------------------------------------------------------")
print("FIN DEL PROGRAMA")
print("--------------------------------------------------------------------------")
