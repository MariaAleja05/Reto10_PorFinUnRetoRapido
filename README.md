# Reto número 10 repo
### Fecha:  12-10-2023
* Mirar archivo Reto10.ipynb
**1.** Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
* EXPLICACIÓN
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
* EXPLICACIÓN
* Mirar archivo Punto_2.py
```pseudocode

```
**3.** Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
* EXPLICACIÓN
* Mirar archivo Punto_3.py
```pseudocode

```
**4.** Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).
* EXPLICACIÓN
* Mirar archivo Punto_4.py
```pseudocode

```
