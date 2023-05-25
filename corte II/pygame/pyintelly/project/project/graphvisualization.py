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
    user_extractor = UserExtractor(json_file)

    user = user_extractor.get_user_by_name(name)
    friends = user_extractor.get_user_friends(user)

    G = nx.Graph()

    G.add_node(name)
    for friend in friends:
        friend_name = user_extractor.get_user_name(friend)
        G.add_edge(name, friend_name)

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

    ax = plt.gca()
    for image, node in zip(images, G.nodes):
        x, y = pos[node]
        imagebox = OffsetImage(image, zoom=0.15)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)
        ax.annotate(node, (x, y-0.05), ha='center', fontsize=8)
        
    plt.show()

    image_path = "grafo_con_imagenes_y_nombres.png"
    plt.savefig(image_path, format="png")

    image = Image.open(image_path)

    return image

drawnodefriends('Deanna Schultz')

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
        label_positions[node] = (x, y - 0.1)  # Ajustar la posición vertical de los nombres

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color='skyblue', node_size=500, font_size=10, with_labels=False)
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes, node_color='red', node_size=500, node_shape='s')
    nx.draw_networkx_labels(G, label_positions, labels=labels, font_size=8, verticalalignment='top')

    ax = plt.gca()
    for image, node in zip(images, G.nodes):
        x, y = pos[node]
        imagebox = OffsetImage(image, zoom=0.15)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)

    # Mostrar el grafo generado
    plt.show()

    image_path = "grafo_con_imagenes_y_nombres.png"
    plt.savefig(image_path, format="png")

    image = Image.open(image_path)

    return image



drawnodefamily('Deanna Schultz')

def draw_image(image_path, surface):
        image = Image.open(image_path)
        image = image.convert("RGBA") 
        image = image.resize(surface.get_size())

        image_data = image.tobytes()

        pygame_image = pygame.image.fromstring(image_data, image.size, "RGBA")

        surface.blit(pygame_image, (0, 0))
