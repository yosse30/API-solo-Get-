from typing import Dict

def user_schema(user) -> Dict[str, str]:
    return {
        "id": str(user.get("_id", "")),
        "marca": user.get("marca", ""),
        "genero": user.get("genero", ""),
        "año": user.get("año", ""),
         "titulo": user.get("tiutlo", "")
        
    }