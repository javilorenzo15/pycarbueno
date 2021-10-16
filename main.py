# Import a ibrary of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
size = [1300, 600] # Define size of windows
ancho = int(input("ancho de la ventana:"))
alto = int(input("alto de la ventana:"))
size = (ancho,alto)
titulo = input("nombre simulador:")
rojo = int(input("cantidad de rojo:"))
verde = int(input("cantidad de verde:"))
azul = int(input("cantidad de azul:"))
color = (rojo,verde,azul)
main2(size,titulo,color)