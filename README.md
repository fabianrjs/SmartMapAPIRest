# SmartMap API Rest con DJango Rest Framework y MongoDB

API Rest desarrollado para el Proyecto SmartMap Javeriana, el cual ofrece la busqueda de rutas en un grafo que representa el campus de la Pontifica Universidad Javeriana - Bogotá

Para la busqueda de en el grafo se hizo uso del siguiente algoritmo:
## Dijkstra's Algorithm Unity

Shortest path finding using Dijkstra's Algorithm in Unity 3D, coded with C#.

[![Demo CountPages alpha](https://share.gifyoutube.com/jqLgol.gif)](https://youtu.be/U0Ra8RoUgX8)

### Download: [Algorithm for WindowOS](https://www.n3evin.com/unity/DijkstraUnity.zip)

### Features:
- Finding the shortest path from A to B.
- Avoiding paths that are block.
- RTS Units style selection system (drag mouse to select multiple nodes).

### Requisitos Para Ejecutar el proyecto:

1. Python 3
2. pip
3. Crear un Python Virtual Enviroment: `python3 -m venv <nombre enviroment>`
4. Instalar todos los paquetes que se encuentran en _**requirements.txt**_
5. Crear archivo local _**properties.py**_ con las credenciales de la base de datos a usar

### Ejecutar Proyecto:

1. Activar virtual enviroment: `<nombre enviroment>\Scripts\activate`
2. Ejecutar: `python manage.py runserver`

### Otros comandos importantes:
- Crear requirements: pip freeze > requirements.txt
- Preparar migraciones: python manage.py makemigrations
- Hacer migraciones: python manage.py migrate