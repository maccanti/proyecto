import pygame
from pygame.locals import *
import random
import pickle

tamaño = Ancho, Alto = (800, 800)
camino_A = int(Ancho / 1.6)
linea = int(Ancho / 80)
velocidad = 1

derecha = Ancho / 2 + camino_A / 4
izquierda = Ancho / 2 - camino_A / 4

pygame.init()
correr = True
# CONFIGURACIÓN DE LA PANTALLA ANCHO Y ALTO
pantalla = pygame.display.set_mode((tamaño))
pygame.display.set_caption("juego brahian")
pantalla.fill((60, 220, 0))

pygame.display.update()
# carro 1
carro_1 = pygame.image.load("car.png")
car_loc = carro_1.get_rect()
car_loc.center = derecha, Alto * 0.8

# carro 2
carro_2 = pygame.image.load("otherCar.png")
car2_loc = carro_2.get_rect()
car2_loc.center = izquierda, Alto * 0.2

# Solicitar el nombre del jugador
jugador = input("Ingresa tu nombre: ")

# Contadores
puntos = 0
contador = 1
nivel = 0


# Validar nombre de jugador
while True:
    jugador = input("Ingresa tu nombre (mínimo 6 caracteres alfanuméricos): ")
    if len(jugador) >= 6 and jugador.isalnum():
        break
    print("Nombre inválido. Debe tener al menos 6 caracteres alfanuméricos.")


while correr:
    contador += 1
    puntos += 1
    if contador == 1000:
        velocidad += 2.0
        contador = 0
        puntos = 0
        nivel += 1
        print("Ganaste", velocidad)
        print("Monedas ganadas:", nivel)

    # Animación del carro
    car2_loc[1] += velocidad
    if car2_loc[1] > Alto:
        car2_loc[1] = -200
        if random.randint(0, 1) == 0:
            car2_loc.center = derecha, -200
        else:
            car2_loc.center = izquierda, -200

    # Fin del juego
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("Perdiste =)!")
        reiniciar = input("¿Deseas reiniciar el juego? (s/n): ")
        if reiniciar.lower() == 's':
            correr = True 
            nivel = 0
            contador = 0
            puntos = 0 
            velocidad = 1.0
            puntos = 0
        else:
            break 
    

    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            correr = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(camino_A / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(camino_A / 2), 0])

    # Configuración gráfica de la pantalla
    pygame.draw.rect(pantalla, (50, 50, 50), (Ancho / 2 - camino_A / 2, 0, camino_A, Alto))

    pygame.draw.rect(pantalla, (225, 240, 60), (Ancho / 2 - linea / 2, 0, linea, Alto))
    pygame.draw.rect(pantalla, (255, 255, 255), (Ancho / 2 - camino_A / 2 + linea * 2, 0, linea, Alto))
    pygame.draw.rect(pantalla, (255, 255, 255), (Ancho / 2 + camino_A / 2 - linea * 3, 0, linea, Alto))

    pantalla.blit(carro_1, car_loc)
    pantalla.blit(carro_2, car2_loc)

    # Mostrar nombre del jugador, puntuación y monedas en pantalla
    font = pygame.font.Font(None, 36)
    nombre_surface = font.render(f"Jugador: {jugador}", True, (255, 255, 255))
    puntuacion_surface = font.render(f"Puntuación: {puntos}", True, (255, 255, 255))
    monedas_surface = font.render(f"nivel: {nivel}", True, (255, 255, 255))
  

    pantalla.blit(nombre_surface, (10, 10))
    pantalla.blit(puntuacion_surface, (10, 50))
    pantalla.blit(monedas_surface, (10, 90))
    

    pygame.display.update()