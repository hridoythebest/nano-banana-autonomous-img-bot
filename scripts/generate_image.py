from dotenv import load_dotenv
load_dotenv()

import os
import json
from google import genai
from PIL import Image
from io import BytesIO
import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import cycle

# Load API keys from environment variable (now a JSON array)
API_KEYS_STR = os.environ.get("GEMINI_API_KEY")
if not API_KEYS_STR:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your .env file.")

try:
    API_KEYS = json.loads(API_KEYS_STR)
    if not isinstance(API_KEYS, list):
        raise ValueError("GEMINI_API_KEY must be a JSON array of keys.")
    if not API_KEYS:
        raise ValueError("No API keys provided in GEMINI_API_KEY.")
except json.JSONDecodeError:
    raise ValueError("GEMINI_API_KEY must be valid JSON.")

key_cycle = cycle(API_KEYS)

# The text prompt for image generation
prompt = "Create a photorealistic image modern and sleek also professional image that can bid world number 1 graphics designer. append image refference. as i am developing intereactive 3D simulation books for 11 and 12 grade science student in Bangladesh. Please make it more modern and futuristic. Image should Relevant to HSC science subject any popular topics"

def generate_single_image(prompt, output_path, api_key):
    client = genai.Client(api_key=api_key)
    max_retries = len(API_KEYS)
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-image-preview",
                contents=prompt,
            )
            break
        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                print(f"[Retry] API quota exhausted with key ending {api_key[-10:]}, switching key (attempt {attempt+1}/{max_retries})")
                api_key = next(key_cycle)
                client = genai.Client(api_key=api_key)
                time.sleep(2)
                continue
            else:
                print(f"[Error] API call failed: {e}")
                return
    else:
        print("[Error] All keys exhausted.")
        return

    # Extract image parts
    image_parts = [
        part.inline_data.data
        for part in response.candidates[0].content.parts
        if part.inline_data
    ]

    if image_parts:
        image = Image.open(BytesIO(image_parts[0]))
        image.save(output_path)
        time.sleep(2.5)  # Rate limit sleep
        print(f"Image saved to {output_path}")
    else:
        print("No image generated.")

def main():
    parser = argparse.ArgumentParser(description="Generate images using Gemini API with API key rotation and multi-threading.")
    parser.add_argument("--num_images", type=int, default=1, help="Number of images to generate.")
    args = parser.parse_args()

    print(f"Generating {args.num_images} image(s)...")

    with ThreadPoolExecutor(max_workers=min(args.num_images, 10)) as executor:
        futures = []
        for i in range(args.num_images):
            api_key = next(key_cycle)
            output_path = f"../outputs/112_{i+1}.png"
            futures.append(executor.submit(generate_single_image, prompt, output_path, api_key))
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
