# QR Code Generator

Ce projet Python génère un QR code à partir d'une URL fournie par l'utilisateur. <br>
Le QR code est sauvegardé en tant qu'image PNG avec un nom de fichier basé sur l'URL.

## Prérequis

Avant de pouvoir utiliser ce script, assurez-vous d'avoir installé les éléments suivants :

- **Python 3.x** : [Téléchargez Python](https://www.python.org/downloads/)
- **pip** : Le gestionnaire de paquets Python (souvent installé avec Python)

## Installation

1. **Clonez ce dépôt** :

   ```bash
      git clone https://github.com/votre-utilisateur/qr-code-generator.git
      cd qr-code-generator
   ```

2. **Créez un environnement virtuel** :

   ```bash
      python3 -m venv venv
      # Sur Mac ou Linux utilisez
      source venv/bin/activate
      # Sur Windows utilisez
      venv\Scripts\activate
   ```
3. **Installez les dépendances** :

   ```bash
      pip install 'qrcode[pil]'
   ```
## Utilisation
1. **Exécuter le script** :

   ```bash
      python create_qr_code.py
   ```
2. Saisissez l'URL lorsque vous y êtes invité.<br> Le script générera un QR code et l'enregistrera dans un fichier PNG avec un nom basé sur l'URL fournie.
3. Vérifiez le fichier généré en utilisant la commande `ls` dans le terminal pour voir le fichier PNG :

## Exemple
Entrer l'URL à encoder en QR code : `https://faceaucode.com`<br>
QR code généré avec succès : `qr_code_https_faceaucode_com.png`<br>
Le fichier PNG sera nommé `qr_code_https_faceaucode_com.png`

## Terminal
<img src="./qrcode_terminal.png" width="700"/>

## Résultat
Lien QRCode vers mon site web `faceaucode.com`<br>
<img src="./qr_code_faceaucode.com.png" width="150"/>