# Reto número 10 repo
### Fecha:  12-10-2023
* Mirar archivo Reto10.ipynb
  
**1.** Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
* Lo primero que hice fue crear una función, la cual tendrá en cuenta todos los elementos ingresados por el usuario. Esteblecí las variables de suma y promedio como cero para empezar en limpio las cuentas. Allí hay un for que irá sumando todos los elementos de la lista. Luego, el resultado de la suma de este for se dividirá entre la longitud de elementos de la lista que se sumaron para encontrar el promedio.

En la función main creé una lista vacía, y la variable elementos que serán los elementos de la lista que ingrese el usuario. Le solicitó al usuario ingresar el número de elementos que quiere que contenga su lista, y, creé un for el cuál funcionara ese número de elementos e irá añadiendo los elementos a la lista. Llamo la función de promedio y, se imprimirá el resultado de este junto con el arreglo al que se le calculó.
* Mirar archivo Punto_1.py
```pseudocode
def Promedio(*args) -> float:
  suma=0
  promedio=0
  for i in lista:
    suma += i
  promedio = suma/len(lista)
  return promedio

if __name__ == "__main__":
  elemento=0
  lista=[]
  j = int(input("Ingrese la cantidad de elementos que desea que tenga la lista:"))
  for elemento in range (j):
    elemento = float(input("Ingrese un valor real:"))
    lista.append(elemento)
  rta = Promedio(elemento)
  print("----------------------------------------------------------------")
  print(lista)
  print("El promedio de los valores es " + str(rta))
```
**2.** Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
* Lo primero que hice fue crear una función, la cual tendrá en cuenta los dos vectores en forma de lista. Esteblecí las variables de productoPunto e i como cero para empezar en limpio las cuentas. Allí hay un for que irá realizando la multiplicación de la posición i del primer vector con la del segundo vector y se sumará el resultado a la variable productoPunto. Se realizará esta operación con todos los elementos de los vectores. La función mostrará el resultado del productoPunto.

En la función main creé dos listas vacias que son mis dos vectores, y la variable elemento1 y elemento2 que serán los elementos de las listas que ingrese el usuario. Le solicitó al usuario ingresar el número de elementos que quiere que contengan los vectores, y, creé dos for (uno para cada lista/vector) el cuál funcionara ese número de elementos e irá añadiendo los elementos a los vectores. Llamo la función de ProductoPunto y, se imprimirá el resultado de este junto con los dos vectores que se evaluaron.
* Mirar archivo Punto_2.py
```pseudocode
def ProductoPunto(vector1, vector2) -> float:
  productoPunto=0
  i=0
  for i in range (j):
    productoPunto += (vector1[i]*vector2[i])
  return productoPunto

if __name__ == "__main__":
  elemento1=0
  elemento2=0
  vector1=[]
  vector2=[]
  j = int(input("Ingrese la cantidad de elementos que desea que tenga los vectores:"))
  for elemento1 in range (j):
    elemento1 = int(input("Ingrese un valor real para el primer vector:"))
    vector1.append(elemento1)
  for elemento2 in range (j):
    elemento2 = int(input("Ingrese un valor real para el segundo vector:"))
    vector2.append(elemento2)
  rta = ProductoPunto(vector1, vector2)
  print("----------------------------------------------------------------")
  print(vector1)
  print(vector2)
  print("El punto medio es: " + str(rta))
```
**3.** Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
* En la función main creé una lista vacia, y la variable elemento que serán los elementos del arreglo. Le solicitó al usuario ingresar el número de elementos que quiere que contengan el arreglo, y, creé un for el cuál funcionara ese número de elementos ingresado e irá añadiendo los elementos que ingrese el usuario al arreglo. Uso la función o el método .count para que me muestre la cantidad de elementos que son iguales a "0". Se imprime la cantidad de 0 que hay en el arreglo y también el arreglo resultante.
* Mirar archivo Punto_3.py
```pseudocode
if __name__ == "__main__":
  lista=[]
  elemento=0
  j = int(input("Ingrese la cantidad de elementos que desea que tenga el arreglo:"))
  for elemento in range (j):
    elemento = int(input("Ingrese un valor real:"))
    lista.append(elemento)
  print("---------------------------------------------------------------")
  print(lista)
  print("El número de 0 que aparecen en el arreglo son: " + str(lista.count(0)))
```
**4.** Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).
* **Algoritmos de sorting:** Son algoritmos diseñados para organizar una lista o arreglo de datos en un orden específico. Existen varios algoritmos de ordenamiento como: Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, Merge Sort, Heap Sort, Radix Sort.
* **Bubble-sort:** Este algoritmo compara (según el tipo de orden que se quiera) pares de elementos y los intercambia si están en el orden incorrecto. Continúa haciendo esto hasta que toda la lista esté ordenada. Es de los algoritmos más sencillos para ordenar pero no es eficiente si se implementa en listas grandes.

![bubble_sort](https://github.com/MariaAleja05/Reto10/assets/141857519/42987ea5-75e8-4208-be95-2e128c2ef6c1)

