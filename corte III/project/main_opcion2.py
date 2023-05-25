import json
import random
import os
from PIL import Image
import urllib.parse
from io import BytesIO
from faker import Faker
fake = Faker()

# Obtener la lista de archivos de imagen en la carpeta
image_folder = r"C:\\UAM\\TAD 1SEM 2023\\corte III\\project\\images"
image_files = [file for file in os.listdir(image_folder) if file.endswith(".png")]

# Generar una imagen de perfil aleatoria de la carpeta de imágenes
def generate_profile_image():
    image_file = random.choice(image_files)
    image_path = os.path.join(image_folder, image_file)
    image = Image.open(image_path)
    return image

# Generar un diccionario de datos falsos
users = []
relationships = []

# Generar usuarios
for i in range(50):
    try:
        name = fake.name()
        profile_image = generate_profile_image()
        profile_image_url = f"image_{i+1}.png"  # Nombre de archivo de imagen personalizado
        profile_image.save(os.path.join(image_folder, profile_image_url))

        user = {
            "id": i + 1,
            "name": name,
            "email": f"{name}@example.com",
            "birthdate": "1990-01-01",
            "profile_image_url": profile_image_url,
            "liked_photos": [],
            "family": [],
            "groups": [],
            "communities": []
        }
        users.append(user)

        num_family_members = 3
        num_family_members = min(num_family_members, len(users))
        family_members = random.sample(users, num_family_members)
        for family_member in family_members:
            if family_member["name"] != user["name"]:
                member = {
                    "name": family_member["name"],
                    "relation": random.choice(["Father", "Mother", "Sibling"]),
                }
            else:
                member = None
            if member is not None:
                user["family"].append(member)
                
        group_names = ["barrio gal", "Cuchilla", "UAM", "DnD", "Asados"]
        community_names = ["PintaAPIS", "MoureDev", "Cosmere", "Genshin", "Malaz"]
        for user in users:
            # Generar grupos
            num_groups = random.randint(0, 3)  # Número aleatorio de grupos (puede ser de 0 a 3)
            groups = random.sample(group_names, num_groups)  # Seleccionar nombres aleatorios de grupos
            user["groups"] = groups

            # Generar comunidades
            num_communities = random.randint(0, 3)  # Número aleatorio de comunidades (puede ser de 0 a 3)
            communities = random.sample(community_names, num_communities)  # Seleccionar nombres aleatorios de comunidades
            user["communities"] = communities

        
    except Exception as e:
        print(f"Error al generar el usuario {i + 1}: {e}")

# Generar relaciones de amistad
for user in users:
    num_friends = random.randint(1, 5)
    friends = random.sample(users, num_friends)
    user_relationships = {
        "user_id": user["id"],
        "friends": [friend["id"] for friend in friends]
    }
    relationships.append(user_relationships)

# Crear diccionario final con usuarios y relaciones
data = {
    "users": users,
    "relationships": relationships
}

# Exportar el JSON
with open("facebook_data.json", "w") as file:
    json.dump(data, file, indent=2)

print("El archivo facebook_data.json ha sido creado exitosamente.")
