# coding=utf-8

#1. Mostrar los nombres de todas las plantas.
#2. Plantas en un rango de precio.
#3. Obtener existencias de una planta introduciendo una subcadena o el nombre completo.
#4. Obtener las plantas según el tipo de luz.
#5. Plantas ordenadas de más baratas a más caras.
#6. Salir

#1
#Muy fácil, obtengo todos los nombres dentro de una lista con una simple ruta de xpath.
def nombres(parser):
  lista_nombres= parser.xpath("//COMMON/text()")
  return lista_nombres

#2
def precio(parser):

##########################################################################
  #Este código lo he copiado de otro ejercicio hecho previamente y es para asegurarme de que el límite inferior es más pequeño que el superior, y que los decimales sólo son 2 como mucho.
  comprobado_inferior=False
  comprobado_superior=False

  print("--------------------------------------------------------------------------")
  inferior=input("¿Cuál es el límite inferior?: ")
  print("--------------------------------------------------------------------------")
  superior=input("¿Cuál es el límite superior?: ")
  print("--------------------------------------------------------------------------")

  cont_inferior=0
  for i in range (len(inferior)):
    if inferior[i]==".":
      for x in range (i+1,len(inferior)):
        cont_inferior=cont_inferior + 1

  while comprobado_inferior==False:
    if cont_inferior<=2:
      try:
        inferior = float(inferior)
        comprobado_inferior=True
      except ValueError:
        print("El límite inferior no es correcto.")
        print("Sólo se admiten números y un punto para separar los decimales.")
        print("Vuelve a introducir el número.")
        inferior=input("¿Cuál es el límite inferior?: ")
        print("--------------------------------------------------------------------------")
        comprobado_inferior=False
    else:
      comprobado_superior=True
      return -2

  while comprobado_superior==False:

    cont_superior=0
    for i in range (len(superior)):
      if superior[i]==".":
        for x in range (i+1,len(superior)):
          cont_superior=cont_superior+1

    if cont_superior<=2:
      try:
        superior = float(superior)
        comprobado_superior=True
      except ValueError:
        print("El límite superior no es correcto.")
        print("Sólo se admiten números y un punto para separar los decimales.")
        print("Vuelve a introducir el número.")
        superior=input("¿Cuál es el límite superior?: ")
        print("--------------------------------------------------------------------------")
        comprobado_superior=False
    else:
      return -3

  resta=superior-inferior
  resta="{0:.2f}".format(resta)
  resta=float(resta)
##########################################################################

#Una vez comprobado todo, para encontrar los libros entre ese intervalo de precios, hay que ir al precio de cada planta. Entramos en //PLANT, que son todas las plantas, y obtenemos el .//PRICE, que es el precio de cada planta. Por último se entra en un bucle dentro de la lista de todos estos precios obtenidos y utilizando un contador, ya que los precios están en la misma posición que los nombres (COMMON) dentro de la lista CATALOG. El contador servirá como posición dentro de esta lista. De este modo se pueden añadir uno por uno los nombres de las planats que cumplan las condiciones que queramos usando un if y lo siguiente:
#(parser.xpath("//PLANT/COMMON/text()")[contador])

  if resta>0:
    lista=[]
    contador=0
    for planta in parser.xpath("//PLANT"):
      precio = parser.xpath(".//PRICE/text()")
      for elemento in precio:
        if float(elemento)>inferior and float(elemento)<superior:
          try:
            lista.append(parser.xpath("//PLANT/COMMON/text()")[contador])
          except:
            break
        contador=contador+1
    inferior = "{0:.2f}".format(inferior)
    superior = "{0:.2f}".format(superior)
    print("Las plantas que valen entre "+str(inferior)+"€ y "+str(superior)+"€ son:")
    print("")
    return lista

  if resta<0:
    return -1
  if resta==0:
    return 0

#3
#He reutilizado código del ejercicio anterior ya que la forma de buscar es similar. En este caso, se pide una cadena y se compara con todas las cadenas dentro del xpath "//PLANT/COMMON/", que contiene todos los nombres de todas las plantas. Para hacerlo mejor, me aseguro de que ambas cadenas (la introducida y el nombre con el que se compara) están en minúsculas. Si coincide, se añade el nombre y las existencias a una lista.

def existencias(parser):
  lista=[]
  cadena=input("Introduce una subcadena: ")
  cadena=cadena.lower()
  contador=0
  for plantas in parser.xpath("//PLANT"):
    nombre=parser.xpath(".//COMMON/text()")
    for elemento in nombre:
      elemento=elemento.lower()
      if elemento.find(cadena) >= 0:
        try:
          lista.append(parser.xpath("//PLANT/COMMON/text()")[contador])
          lista.append(int(parser.xpath("//PLANT/AVAILABILITY/text()")[contador]))
        except:
          break
      contador=contador+1
  print("Plantas que contienen '"+str(cadena)+"':")
  print("")
  return lista

#4
#También he reutilizado código para la búsqueda dentro del xml. En este caso busco los tipos de luces disponibles y las añado a una lista sin repetir. Esta lista se enseña y se da a elegir al usuario (hay que escribir la cadena completa, aunque no distingue entre mayúsculas y minúsculas). Se recorre, como he hecho en el ejercicio anterior, todas las plantas y se compara este tipo de luz con el tipo de luz de cada planta. Si coincide, se añade el nombre de la planta a una lista que será la solución. Si la lista está vacía, eso significa que la cadena es errónea o el tipo de luz especificado no existe y por lo tanto se dará el error pertinente.

def luz(parser):
  luces=[]
  lista=[]
  for luz in parser.xpath("//LIGHT/text()"):
    if luz not in luces:
      luces.append(luz)
  print("--------------------------------------------------------------------------")
  print("Tipos de luces:")
  print("")
  for i in luces:
    print(i)
  print("")
  cadena=input("Introduce un tipo de luz: ")
  cadena=cadena.lower()
  contador=0
  for elemento in parser.xpath("//COMMON/text()"):
    try:
      tipo_luz=parser.xpath("//PLANT/LIGHT/text()")[contador]
      tipo_luz=tipo_luz.lower()
      if cadena==tipo_luz and cadena not in lista:
        lista.append(parser.xpath("//PLANT/COMMON/text()")[contador])
    except:
      break
    contador=contador+1
  return lista

#5
#Para hacer esto he utilizado un diccionario ya que no he visto otra manera de ordenar conjuntamente dos valores a la vez pero dependiendo de uno solo. Para hacer esto he añadido al diccionario dic[precio]=nombre, es decir que el nombre y el precio (buscados con xpath con "//COMMON/text()" y "//PRICE/text()") están relacionados. Es necesario que el precio sea el "objeto" y el nombre sea el "valor" del diccionario ya que a la hora de ordenarlo lo hace según el objeto. Para ordenarlos se usa "dict(sorted(dic.items()))" que los ordena de menor a mayor automáticamente. Si se quiere hacer de mayor a menor se podría poner "dict(sorted(dic.items(), reverse=True))".

def ordenar(parser):
  dic={}
  contador=0
  for elemento in parser.xpath("//PLANT"):
    try:
      nombre=parser.xpath("//COMMON/text()")[contador]
      precio=float(parser.xpath("//PRICE/text()")[contador])
      precio="{0:.2f}".format(precio)
      dic[precio]=nombre
    except:
      break
    contador=contador+1
  ordenado = dict(sorted(dic.items()))
  return ordenado
