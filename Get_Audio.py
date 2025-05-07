import subprocess
import os

def download_youtube_audio(url, output_path="downloads"):
    try:
        cmd = [
            "yt-dlp",
            "-x",
            "--audio-format", "mp3",
            "-o", f"{output_path}/%(title)s.%(ext)s",
            url
        ]
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Échec du téléchargement : {url}\nErreur : {e}")

def download_from_file(input_file, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with open(input_file, "r") as f:
        for line in f:
            if "=>" in line:
                try:
                    url = line.split("=>")[1].strip()
                    if url.startswith("https://www.youtube.com"):
                        download_youtube_audio(url, output_path)
                except Exception as e:
                    print(f"⚠️ Ligne mal formatée : {line}\nErreur : {e}")

if __name__ == "__main__":
    input_file = "youtube_links.txt"
    download_from_file(input_file)

