from dotenv import load_dotenv
load_dotenv()


import os
from google import genai
from PIL import Image
from io import BytesIO

# Load API key from environment variable
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your .env file.")

# Configure the client with your API key
client = genai.Client(api_key=API_KEY)

# The text prompt for image generation
prompt = "Create a photorealistic image modern and sleek also professional image that can bid world number 1 graphics designer. append image refference. as i am developing intereactive 3D simulation books for 11 and 12 grade science student in Bangladesh. Please make it more modern and futuristic. Image should Relevant to HSC science subject any popular topics"

print("Generating image...")

# Call the API to generate the image
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=prompt,
)

# Extract image parts
image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    # Save the first image
    image = Image.open(BytesIO(image_parts[0]))
    output_path = "../outputs/112.png"
    image.save(output_path)
    print(f"Image saved to {output_path}")
else:
    print("No image generated.")
