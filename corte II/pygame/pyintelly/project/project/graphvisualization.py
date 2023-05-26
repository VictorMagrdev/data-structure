# facebook_visualization_module.py

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

def friendlessness(name):
    user_extractor = UserExtractor(json_file)

    user = user_extractor.get_user_by_name(name)
    friends = user_extractor.get_user_friends(user)

    G = nx.Graph()

    G.add_node(name)
    for friend in friends:
        friend_name = user_extractor.get_user_name(friend)
        G.add_edge(name, friend_name)

    # Conexiones entre amigos
    common_friends = set()
    for friend1 in friends:
        friend1_name = user_extractor.get_user_name(friend1)
        friend1_friends = user_extractor.get_user_friends(friend1)
        for friend2 in friend1_friends:
            friend2_name = user_extractor.get_user_name(friend2)
            if friend2_name != name and friend2_name in G.nodes:
                G.add_edge(friend1_name, friend2_name)
                common_friends.add(friend1_name)
                common_friends.add(friend2_name)

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

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color='skyblue', node_size=500, font_size=10, with_labels=False)
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes, node_color='red', node_size=500, node_shape='s')

    # Resaltar conexiones entre amigos
    for edge in G.edges:
        if edge[0] in common_friends and edge[1] in common_friends:
            nx.draw_networkx_edges(G, pos, edgelist=[edge], width=2.0)

    ax = plt.gca()
    for image, node in zip(images, G.nodes):
        x, y = pos[node]
        imagebox = OffsetImage(image, zoom=0.15)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)
        ax.annotate(node, (x, y - 0.05), ha='center', fontsize=8)

    plt.show()

    image_path = "grafo_con_imagenes_y_nombres.png"
    plt.savefig(image_path, format="png")

    image = Image.open(image_path)

    return image

friendlessness('Lisa Kim')


def drawnodefamily(name):
    user_extractor = UserExtractor(json_file)

    user = user_extractor.get_user_by_name(name)
    family_members = user_extractor.get_user_family_members(user)

    G = nx.Graph()

    G.add_node(name)
    for family_member in family_members:
        family_member_name = user_extractor.get_user_name(family_member)
        family_member_relationship = family_member['relation']
        G.add_edge(name, family_member_name, relationship=family_member_relationship)

    image_folder = r'C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\project\\images'
    images = []
    labels = {}
    label_positions = {}
    for node in G.nodes:
        if node == name:
            image_path = user_extractor.get_user_profile_image_url(user)
            labels[node] = f"{name}\n(User)"
        else:
            family_member = user_extractor.get_user_by_name(node)
            image_path = user_extractor.get_user_profile_image_url(family_member)
            relationship = G.edges[(name, node)]['relationship']
            labels[node] = f"{node}\n({relationship})"

        image_file = os.path.join(image_folder, image_path)
        image = Image.open(image_file)
        images.append(image)

        x, y = nx.spring_layout(G)[node]
        label_positions[node] = (x, y - 0.1)  
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color='skyblue', node_size=500, font_size=10, with_labels=False)
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes, node_color='red', node_size=500, node_shape='s')

    ax = plt.gca()
    for image, node in zip(images, G.nodes):
        x, y = pos[node]
        imagebox = OffsetImage(image, zoom=0.15)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)
        ax.text(x, y - 0.15, labels[node], ha='center', va='top', fontsize=8, wrap=True)  # Ajuste del texto

    plt.show()

    image_path = "grafo_con_imagenes_y_nombres.png"
    plt.savefig(image_path, format="png")

    image = Image.open(image_path)

    return image


def drawnodecommunities(name):
    user_extractor = UserExtractor(json_file)

    user = user_extractor.get_user_by_name(name)
    communities = user_extractor.get_user_communities(user)

    G = nx.Graph()

    G.add_node(name)
    for community in communities:
        G.add_edge(name, community)

    image_folder_user = r'C:\\UAM\\TAD 1SEM 2023\\corte III\\project\\images'
    image_folder_community = r'C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\project\\community_images'

    images = []
    labels = {}
    for node in G.nodes:
        if node == name:
            image_path = user_extractor.get_user_profile_image_url(user)
            labels[node] = name  # Usuario principal
            image_folder = image_folder_user
        else:
            community = user_extractor.get_community_by_name(node)
            if community is not None:
                image_path = community['image']
                labels[node] = node  # Nombre de la comunidad
                image_folder = image_folder_community

        image_file = os.path.join(image_folder, image_path)
        image = Image.open(image_file)
        images.append(image)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color='skyblue', node_size=500, font_size=10, with_labels=False)
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes, node_color='red', node_size=500, node_shape='s')

    ax = plt.gca()
    for image, node in zip(images, G.nodes):
        x, y = pos[node]
        imagebox = OffsetImage(image, zoom=0.15)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)
        ax.text(x, y - 0.15, labels[node], ha='center', va='top', fontsize=8, wrap=True)  # Ajuste del texto

    plt.show()

    image_path = "grafo_comunidades_con_imagenes_y_nombres.png"
    plt.savefig(image_path, format="png")

    image = Image.open(image_path)

    return image


def drawuserandfriend(name, friend_name):
    user_extractor = UserExtractor(json_file)

    user = user_extractor.get_user_by_name(name)
    user_communities = user_extractor.get_user_communities(user)

    friend = user_extractor.get_user_by_name(friend_name)
    friend_communities = user_extractor.get_user_communities(friend)

    G = nx.Graph()

    G.add_node(name)
    G.add_node(friend_name)

    common_communities = set(user_communities) & set(friend_communities)
    for community in common_communities:
        G.add_node(community)

    G.add_edge(name, friend_name)  
    for community in common_communities:
        G.add_edge(name, community)  
        G.add_edge(friend_name, community)

    image_folder_user = r'C:\\UAM\\TAD 1SEM 2023\\corte III\\project\\images'
    image_folder_community = r'C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\project\\community_images'

    images = []
    labels = {}
    for node in G.nodes:
        if node == name:
            image_path = user_extractor.get_user_profile_image_url(user)
            labels[node] = f"{name}\n(User)"
            image_folder = image_folder_user
        elif node == friend_name:
            image_path = user_extractor.get_user_profile_image_url(friend)
            labels[node] = f"{friend_name}\n(User)"
            image_folder = image_folder_user
        else:
            community = user_extractor.get_community_by_name(node)
            image_path = community['image']
            labels[node] = f"{node}\n(Community)"
            image_folder = image_folder_community

        image_file = os.path.join(image_folder, image_path)
        image = Image.open(image_file)
        images.append(image)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color='skyblue', node_size=500, font_size=10, with_labels=False)
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes, node_color='red', node_size=500, node_shape='s')
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, verticalalignment='bottom')

    ax = plt.gca()
    for image, node in zip(images, G.nodes):
        x, y = pos[node]
        imagebox = OffsetImage(image, zoom=0.15)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)

    plt.show()

    image_path = "grafo_usuario_y_amigo.png"
    plt.savefig(image_path, format="png")

    image = Image.open(image_path)

    return image


def draw_image(image_path, surface):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    image = image.resize(surface.get_size())

    image_data = image.tobytes()

    pygame_image = pygame.image.fromstring(image_data, image.size, "RGBA")

    surface.blit(pygame_image, (0, 0))


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
