import os
from gtts import gTTS

# ---- CONFIG ----
USE_OPENAI = False   # Change to True if you want OpenAI TTS (more natural voices)
INPUT_FILE = "book.txt"   # Your book or text file
OUTPUT_FILE = "audiobook.mp3"

# ---- MAIN ----
def generate_audiobook():
    # Read text file
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    if USE_OPENAI:
        # --- OpenAI TTS (requires API key) ---
        import openai
        openai.api_key = "your_api_key_here"

        response = openai.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",   # alloy, verse, sage
            input=text
        )
        with open(OUTPUT_FILE, "wb") as f:
            f.write(response.data)

    else:
        # --- Free gTTS version ---
        tts = gTTS(text=text, lang='en')
        tts.save(OUTPUT_FILE)

    print(f"\n✅ Audiobook saved as {OUTPUT_FILE}")

    # Try to play audio (Windows/Mac/Linux)
    try:
        if os.name == "nt":  # Windows
            os.system(f"start {OUTPUT_FILE}")
        elif os.uname().sysname == "Darwin":  # Mac
            os.system(f"afplay {OUTPUT_FILE}")
        else:  # Linux
            os.system(f"mpg321 {OUTPUT_FILE}")
    except Exception:
        print("🎧 Audiobook generated. Please play it manually.")

if __name__ == "__main__":
    generate_audiobook()
