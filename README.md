# G.R.O.S
Get Rid Of Spotify

##Spotify to YouTube MP3 Downloader

Ce projet permet de convertir une playlist Spotify en fichiers audio MP3 en téléchargeant automatiquement les morceaux via YouTube. Il fonctionne en trois étapes :

1. Extraction des titres depuis une playlist Spotify
2. Recherche des morceaux sur YouTube
3. Téléchargement des fichiers audio en MP3

## Structure du projet

- `Get_Track.py` : Récupère les titres d’une playlist Spotify et les enregistre dans `tracks.txt`.
- `Get_URL.py` : Recherche chaque titre sur YouTube et crée un fichier `youtube_links.txt` contenant les correspondances.
- `Get_Audio.py` : Télécharge les fichiers MP3 des vidéos YouTube listées.

## Prérequis

- Python 3.x
- yt-dlp (installable via `pip install yt-dlp`)
- spotipy (installable via `pip install spotipy`)
- Compte Spotify avec accès développeur pour obtenir :
  - CLIENT_ID
  - CLIENT_SECRET

## Utilisation

1. Configurer l’accès Spotify :  
   Dans `Get_Track.py`, remplace les valeurs de `CLIENT_ID` et `CLIENT_SECRET` si besoin.

2. Extraire les titres Spotify :

   python main.py

