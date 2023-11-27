from typing import Dict

def user_schema(user) -> Dict[str, str]:
    return {
        "id": str(user.get("_id", "")),
        "username": user.get("username", ""),
        "full_name": user.get("full_name", ""),
        "email": user.get("email", ""),
        "phone": user.get("phone", ""),
        "disabled": user.get("disabled", "")
    }
