import os
import hashlib
from rich import print
from chatterbox_api import ChatterboxAPI
from tqdm import tqdm
from pydub import AudioSegment
import concurrent.futures
from dotenv import load_dotenv

load_dotenv()

# Ensure audio directory exists
AUDIO_DIR = "audios"
os.makedirs(AUDIO_DIR, exist_ok=True)

api = ChatterboxAPI(os.getenv("CHATTERBOX_API_URL"))

# Load script
with open("script.txt", "r") as file:
    script = file.readlines()

audio_segments = []

def get_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def process_line(line):
    speaker, line = line.split(':', 1)
    speaker, line = speaker.strip().lower(), line.strip().strip('"').strip("'")
    print(f"[bold green]{speaker}[/bold green]: {line}")

    # Generate MD5 hash
    audio_hash = get_md5(speaker + line)
    audio_path = os.path.join(AUDIO_DIR, f"{audio_hash}.wav")

    if os.path.exists(audio_path):
        print(f"[yellow]Using cached audio for:[/yellow] {speaker}: {line}")
        segment = AudioSegment.from_mp3(audio_path)
    else:
        response = api.synthesize(
            text=line,
            audio_prompt=speaker + ".mp3",
            exaggeration=0.75,
            temperature=0.8,
            cfg_weight=0.5
        )
        
        with open(audio_path, "wb") as f:
            f.write(response.content)

        segment = AudioSegment.from_mp3(audio_path)

    return segment

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = list(tqdm(executor.map(process_line, script), total=len(script), desc="Generating audio"))

audio_segments = results

# Combine audio segments
combined_audio = AudioSegment.empty()
for segment in audio_segments:
    combined_audio += segment

combined_audio.export("combined_audio.mp3", format="mp3")
