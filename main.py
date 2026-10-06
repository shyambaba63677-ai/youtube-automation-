import os
import requests
import asyncio
import edge_tts

# 1. AI Script Generation using Gemini API
def generate_script():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing in GitHub Secrets!")
        
    prompt = "Write a 30-second viral YouTube Shorts script about an interesting space fact in Hindi."
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    response = requests.post(url, json=payload)
    result = response.json()
    
    if 'candidates' not in result:
        print("API Response Error:", result)
        raise KeyError(f"Gemini API Error: {result.get('error', {}).get('message', 'Unknown error')}")

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
