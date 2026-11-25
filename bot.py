
# Belle Ébène Assistante

def saluer():
    return "Bonjour et bienvenue chez Belle Ébène ! ❤️"

def repondre(message):
    message = message.lower()

    if "bonjour" in message or "salut" in message:
        return saluer()

    if "qui es-tu" in message:
        return "Je suis Belle Ébène, votre assistante virtuelle."

    if "merci" in message:
        return "Avec plaisir ! ❤️"

    return "Je suis là pour vous aider. Pouvez-vous préciser votre demande ?"

if __name__ == "__main__":
    print(saluer())
