# -*- coding: utf-8 -*-
"""Punto_3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

##**Punto 3**
"""

if __name__ == "__main__":
  lista=[]
  elemento=0
  j = int(input("Ingrese la cantidad de elementos que desea que tenga el arreglo:"))
  for elemento in range (j):
    elemento = int(input("Ingrese un valor real:"))
    lista.append(elemento)
  print("----------------------------------------------------------------")
  print(lista)
  print("El número de 0 que aparecen en el arreglo son: " + str(lista.count(0)))