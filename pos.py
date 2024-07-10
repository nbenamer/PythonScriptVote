import pyautogui
import time

print("Placez la souris à l'endroit souhaité et appuyez sur Ctrl+C pour arrêter le script.")

try:
    while True:
        # Récupère la position actuelle de la souris
        x, y = pyautogui.position()
        # Affiche les coordonnées
        print(f"Position de la souris: (x={x}, y={y})", end="\r")
        # Attendre un peu avant de rafraîchir (pour éviter de surcharger la console)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nScript arrêté.")