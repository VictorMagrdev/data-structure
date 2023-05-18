cartas = ["AsdeTrebol", "DosdeTrebol", "TresdeTrebol", "CuatrodeTrebol", 
        "CincodedeTrebol", "SeisdeTrebol",    
        "SietedeTrebol", "OchodeTrebol", "NuevedeTrebol", "DiezdeTrebol", 
        "JotadeTrebol", "ReinadeTrebol", "ReydeTrebol",    
        "AsdeCorazones", "DosdeCorazones", "TresdeCorazones", 
        "CuatrodeCorazones", "CincodedeCorazones", "SeisdeCorazones",    
        "SietedeCorazones", "OchodeCorazones", "NuevedeCorazones", 
        "DiezdeCorazones", "JotadeCorazones", "ReinadeCorazones", 
        "ReydeCorazones",    "AsdeDiamantes", "DosdeDiamantes", 
        "TresdeDiamantes", "CuatrodeDiamantes", "CincodedeDiamantes", 
        "SeisdeDiamantes",    "SietedeDiamantes", "OchodeDiamantes", 
        "NuevedeDiamantes", "DiezdeDiamantes", "JotadeDiamantes", 
        "ReinadeDiamantes", "ReydeDiamantes",    
        "AsdePicas", "DosdePicas", "TresdePicas", 
        "CuatrodePicas", "CincodedePicas", "SeisdePicas",    
        "SietedePicas", "OchodePicas", "NuevedePicas", "DiezdePicas", 
        "JotadePicas", "ReinadePicas", "ReydePicas"]

with open("cartas.py", "w") as archivo:
    for nombre_clase in cartas:
        contenido = f"""

class {nombre_clase}(Card):
        def __init__(self,image):
            self.image = image
            self.valor = valor"""
        archivo.write(contenido)
