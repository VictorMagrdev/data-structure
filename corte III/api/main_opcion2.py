import json
import random
import requests
from PIL import Image
import urllib.parse
from io import BytesIO
from faker import Faker
fake = Faker()

# Generar una URL de imagen de perfil falsa con un avatar generado
def generate_profile_image_url(name):
    style = random.choice(["female", "male"])
    encoded_name = urllib.parse.quote(name)  # Codificar el nombre para usarlo en la URL
    url = f"https://avatars.dicebear.com/api/{style}/{encoded_name}.png"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error al generar la imagen de perfil: {response.status_code}")
    content_type = response.headers.get("content-type")
    if "image" not in content_type:
        raise Exception("La respuesta no es una imagen válida.")
    return url


# Generar un diccionario de datos falsos
users = []
relationships = []

# Generar usuarios
for i in range(50):
    try:
        name = fake.name()
        profile_image_url = generate_profile_image_url(name)
        user = {
            "id": i + 1,
            "name": name,
            "email": f"{name}@example.com",
            "birthdate": "1990-01-01",
            "profile_image_url": profile_image_url,
            "liked_photos": [],  # Lista vacía para almacenar las fotos que le gusta al usuario
            "family": [],       # Lista vacía para almacenar miembros de la familia
            "groups": [],       # Lista vacía para almacenar grupos que siguen
            "communities": []   # Lista vacía para almacenar comunidades a las que pertenecen
        }
        users.append(user)
        num_family_members = 3
        num_family_members = min(num_family_members, len(users))
        family_members = random.sample(users, num_family_members)
        for family_member in family_members:
            if family_member["name"] != user["name"]:
                member = {
                    "name": family_member["name"],
                    "relation": random.choice(["Father", "Mother", "Sibling"])
                }
            else:
                member = None
            if member is not None:
                user["family"].append(member)
    except Exception as e:
        print(f"Error al generar el usuario {i + 1}: {e}")

# Generar relaciones de amistad
for user in users:
    num_friends = random.randint(1, 5)  # Número aleatorio de amigos por usuario
    friends = random.sample(users, num_friends)  # Muestrear amigos aleatoriamente
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