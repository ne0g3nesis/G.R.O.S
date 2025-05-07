import subprocess

def search_youtube_yt_dlp(query):
    try:
        result = subprocess.run(
            ["yt-dlp", f"ytsearch1:{query}", "--get-id"],
            capture_output=True, text=True, check=True
        )
        video_id = result.stdout.strip()
        return f"https://www.youtube.com/watch?v={video_id}"
    except subprocess.CalledProcessError as e:
        print(f"Erreur pour '{query}': {e}")
        return None

def generate_youtube_links(input_file, output_file):
    with open(input_file, 'r') as f:
        queries = [line.strip() for line in f if line.strip()]

    with open(output_file, 'w') as f_out:
        for query in queries:
            link = search_youtube_yt_dlp(query)
            if link:
                f_out.write(f"{query} => {link}\n")
            else:
                f_out.write(f"{query} => Not found\n")

if __name__ == "__main__":
    generate_youtube_links("tracks.txt", "youtube_links.txt")

