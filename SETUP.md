# Setup Guide

## Prerequisites

Before running the Nano-Banana Autonomous Image Creation Bot, ensure you have:

- Python 3.8 or higher
- A Google account for API access
- Basic familiarity with command-line interfaces

## Step 1: Obtain Your Gemini API Key

Following the official Google Gemini API setup guide:

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Navigate to "Get API Key" section
4. Create a new API key
5. Copy the key (keep it secure!)

For detailed instructions, see: https://github.com/google-gemini/nano-banana-hackathon-kit/blob/main/guides/01-getting-your-api-key.ipynb

**Security Note**: Never commit API keys to version control. Use environment variables.

## Step 2: Clone the Repository

```bash
git clone https://github.com/your-repo/nano-banana-autonomous-img-bot.git
cd nano-banana-autonomous-img-bot
```

## Step 3: Install Dependencies

Install required Python packages:

```bash
pip install python-dotenv google-genai pillow
```

Or create a requirements.txt:
```
python-dotenv==1.0.0
google-genai==0.1.0
pillow==10.0.0
```

Then:
```bash
pip install -r requirements.txt
```

## Step 4: Configure Environment

1. Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=["your-api-key-here"]
   ```

   For multiple keys (recommended for rate limit handling):
   ```
   GEMINI_API_KEY=["key1","key2","key3"]
   ```

2. Ensure `.env` is in your `.gitignore` file.

## Step 5: Prepare Image Directories

Create the following directory structure:

```
nano-banana-autonomous-img-bot/
├── person_images/     # Place person/model images here
├── product_images/    # Place product images here
├── outputs/           # Generated images will be saved here
└── logs/              # Logs will be stored here
```

- Supported formats: JPG, PNG, WebP
- Recommended resolution: 1024x1024 or higher for best results
- File naming: Use descriptive names (e.g., `model_casual.png`, `shoes_running.png`)

## Step 6: Verify Setup

Test your setup:

```bash
python scripts/new_edit_image.py --help
```

If you see the help text, setup is complete!

## Troubleshooting

### API Key Issues
- Ensure the key is valid and has image generation permissions
- Check your API quota in Google AI Studio
- Verify the JSON format in `.env`

### Dependency Errors
- Update pip: `pip install --upgrade pip`
- Use virtual environment: `python -m venv venv && venv\Scripts\activate`

### Path Errors
- Run from project root directory
- Use absolute paths if relative paths fail

For more help, check the logs in `logs/image_generation.log` after running the script.

## Next Steps

Once setup is complete, proceed to USAGE.md for running the bot!
