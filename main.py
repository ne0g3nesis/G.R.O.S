import subprocess
import sys

def run_script(script_name):
    print(f"\nLancement de {script_name}...\n")
    result = subprocess.run([sys.executable, script_name])
    if result.returncode != 0:
        print(f"Une erreur est survenue dans {script_name}")
        sys.exit(1)

def main():
    
    run_script("Get_Track.py")
    
    run_script("Get_URL.py")

    run_script("Get_Audio.py")

    print("\nTout est terminé. Les fichiers audio sont dans le dossier 'downloads/'")

if __name__ == "__main__":
    main()

