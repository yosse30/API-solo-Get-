from typing import Dict

def user_schema(user) -> Dict[str, str]:
    return {
        "id": str(user.get("_id", "")),
        "Name": user.get("Name", ""),
        "Pclass": user.get("Pclass", ""),
        "Survived": user.get("Survived", ""),
        "Sex": user.get("Sex", ""),
        "Age": user.get("Age", ""),
        "SibSp": user.get("SibSp", ""),
        "Parch": user.get("Parch", ""),
        "Ticket": user.get("Ticket", "")
    }
