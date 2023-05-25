import json

def print_related_users(user_id, json_file):
    # Leer el archivo JSON
    with open(json_file, "r") as file:
        data = json.load(file)

    # Buscar el usuario especificado por su ID
    user = next((user for user in data['users'] if user['id'] == user_id), None)
    if user is None:
        print(f"No se encontró ningún usuario con ID {user_id}")
        return

    # Imprimir el usuario
    print(f"Usuario:")
    print(f"ID: {user['id']}")
    print(f"Nombre: {user['name']}")
    print(f"Email: {user['email']}")
    print()

    # Buscar amigos del usuario
    friends = []
    for relationship in data['relationships']:
        if relationship['user_id'] == user_id:
            friends = relationship['friends']
            break

    # Imprimir usuarios relacionados
    print(f"Usuarios relacionados:")
    for friend_id in friends:
        friend = next((user for user in data['users'] if user['id'] == friend_id), None)
        if friend is not None:
            print(f"ID: {friend['id']}")
            print(f"Nombre: {friend['name']}")
            print(f"Email: {friend['email']}")
            relationship_type = next((relation['relation'] for relation in user['family'] if relation['name'] == friend['name']), None)
            if relationship_type is not None:
                print(f"Relación: {relationship_type}")
            else:
                print("Relación: Amigo")
            print()

    # Buscar familiares del usuario que también son usuarios
    relatives = []
    for relative in user['family']:
        relative_name = relative['name']
        relative_user = next((user for user in data['users'] if user['name'] == relative_name), None)
        if relative_user is not None:
            relatives.append((relative_user, relative['relation']))

    # Imprimir familiares que también son usuarios
    print(f"Familiares que también son usuarios:")
    for relative, relation in relatives:
        print(f"ID: {relative['id']}")
        print(f"Nombre: {relative['name']}")
        print(f"Email: {relative['email']}")
        print(f"Relación: {relation}")
        print()


# Ejemplo de uso
json_file = "C:\\UAM\\TAD 1SEM 2023\\corte III\\project\\facebook_data.json"  # Reemplazar con la ruta real del archivo JSON
user_id = 34  # ID del usuario que deseas imprimir junto con sus relaciones y familiares

print_related_users(user_id, json_file)
