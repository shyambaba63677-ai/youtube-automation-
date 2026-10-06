import os
import requests
import asyncio
import edge_tts

# 1. AI Script Generation using Gemini API
def generate_script():
    api_key = os.getenv("GEMINI_API_KEY")
    prompt = "Write a 30-second viral YouTube Shorts script about an interesting space fact in Hindi."
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    response = requests.post(url, json=payload)
    result = response.json()
    script = result['candidates'][0]['content']['parts'][0]['text']
    return script

# 2. Free Text-To-Speech (Microsoft Edge TTS)
async def generate_audio(text, output_file="voiceover.mp3"):
    communicate = edge_tts.Communicate(text, "hi-IN-SwaraNeural")
    await communicate.save(output_file)
    print(f"Audio saved as {output_file}")

# Main Execution Flow
async def main():
    print("Generating Script...")
    script = generate_script()
    print("Generated Script:\n", script)
    
    print("\nGenerating Voiceover Audio...")
    await generate_audio(script)

if __name__ == "__main__":
    asyncio.run(main())
