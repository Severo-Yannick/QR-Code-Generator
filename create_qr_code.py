import qrcode
import re

# Demander à l'utilisateur de saisir une URL
url = input("Veuillez entrer l'URL à encoder en QR code : ")

# Nettoyer l'URL pour obtenir un nom de fichier valide
# Remplacer les caractères non valides par des underscores
file_name = re.sub(r'[\/:*?"<>|]', '_', url)
file_name = file_name[:50]  # Limiter la longueur du nom de fichier pour éviter les problèmes
file_name = f"qr_code_{file_name}.png"

# Générer le QR code
qr_code = qrcode.QRCode(
    version=1,  # Taille du QR code (1 à 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
    box_size=10,  # Taille des boîtes (pixels par boîte)
    border=4,  # Taille de la bordure (boîtes)
)
qr_code.add_data(url)
qr_code.make(fit=True)

# Créer l'image
qr_image = qr_code.make_image(fill_color="black", back_color="white")

# Sauvegarder l'image avec un nom de fichier basé sur l'URL
qr_image.save(file_name)

# Afficher un message de confirmation
print(f"QR code généré avec succès : {file_name}")

