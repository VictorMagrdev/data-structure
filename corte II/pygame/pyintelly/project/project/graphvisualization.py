import os
from PIL import Image
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import networkx as nx
import matplotlib.pyplot as plt
import json
import pygame

from facebook_visualization import UserExtractor

json_file = r'C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\project\\facebook_data.json'

def extract_user_names_from_json(file_path):
    
    with open(file_path, "r") as file:
        data = json.load(file)
    users = data["users"]
    user_names = [user["name"] for user in users]

    return user_names

def drawnodefriends(name):
    # Cargar los datos del archivo JSON
    user_extractor = UserExtractor(json_file)

    # Obtener el usuario y sus amigos
    user = user_extractor.get_user_by_name(name)
    friends = user_extractor.get_user_friends(user)

    # Crear el grafo
    G = nx.Graph()

    # Agregar el usuario y sus amigos al grafo
    G.add_node(name)
    for friend in friends:
        friend_name = user_extractor.get_user_name(friend)
        G.add_edge(name, friend_name)

    # Obtener las imágenes de los nodos
    image_folder = r'C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\project\\images'
    images = []
    for node in G.nodes:
        if node == name:
            image_path = user_extractor.get_user_profile_image_url(user)
        else:
            friend = user_extractor.get_user_by_name(node)
            image_path = user_extractor.get_user_profile_image_url(friend)

        image_file = os.path.join(image_folder, image_path)
        image = Image.open(image_file)
        images.append(image)

    # Dibujar el grafo con las imágenes de los nodos y los nombres debajo de ellos
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color='skyblue', node_size=500, font_size=10, with_labels=False)
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes, node_color='red', node_size=500, node_shape='s')

    # Agregar las imágenes a los nodos
    ax = plt.gca()
    for image, node in zip(images, G.nodes):
        x, y = pos[node]
        imagebox = OffsetImage(image, zoom=0.15)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)
        ax.annotate(node, (x, y-0.05), ha='center', fontsize=8)

    # Guardar el grafo en una imagen
    image_path = "grafo_con_imagenes_y_nombres.png"
    plt.savefig(image_path, format="png")

    # Cargar la imagen guardada
    image = Image.open(image_path)

    return image

def draw_image(image_path, surface):
        # Cargar la imagen generada por el grafo
        image = Image.open(image_path)
        image = image.convert("RGBA")  # Convertir a modo RGBA para admitir transparencia

        # Redimensionar la imagen al tamaño de la superficie
        image = image.resize(surface.get_size())

        # Obtener los datos de píxeles de la imagen
        image_data = image.tobytes()

        # Crear una imagen de Pygame a partir de los datos de píxeles
        pygame_image = pygame.image.fromstring(image_data, image.size, "RGBA")

        # Dibujar la imagen en la superficie
        surface.blit(pygame_image, (0, 0))
