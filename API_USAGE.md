# API Usage Guide

## Overview

This guide explains how the Nano-Banana Autonomous Image Creation Bot integrates with Google's Gemini API, following official guidelines and best practices from the Nano Banana Hackathon Kit.

## Gemini API Integration

### Model Selection
The bot uses `gemini-2.5-flash-image-preview` (Nano Banana) for optimal performance:

```python
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt, person_image, product_image],
)
```

**Why this model?**
- Fast inference times
- High-quality image generation
- Multimodal input support
- Cost-effective for batch processing

### Authentication
Following [Getting Your API Key guide](https://github.com/google-gemini/nano-banana-hackathon-kit/blob/main/guides/01-getting-your-api-key.ipynb):

```python
import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
```

**Security Best Practices**:
- Store keys in environment variables
- Use `.env` files with `.gitignore`
- Rotate keys for rate limit management
- Never commit keys to version control

## Prompt Engineering

### Default Prompt Structure
Following [Image Generation Prompt Guide](https://ai.google.dev/gemini-api/docs/image-generation#prompt-guide):

```
Create a high-quality, commercial advertisement-ready creative by combining the provided model/person image with the provided product image. First, analyze the product image to determine its category, style, theme, and appropriate context. Based on the product analysis, dynamically update the person's clothing, accessories, pose, location, and background to perfectly match the product's theme and style. Place the product naturally in the model's hand or in an appropriate position, ensuring proper perspective, lighting, and shadows for realism. Generate a cohesive scene that reflects a professional advertising style, with the updated elements harmonizing with the product. Maintain a clean, visually appealing composition with a focus on the product, while keeping the overall aesthetic modern, premium, and brand-appropriate.
```

### Prompt Components

1. **Task Definition**: Clear instruction for advertisement creation
2. **Analysis Request**: Explicit product image analysis
3. **Dynamic Adaptation**: Instructions for element updates
4. **Composition Guidelines**: Professional layout requirements
5. **Style Specifications**: Aesthetic and quality standards

### Custom Prompts
Users can override defaults following these guidelines:

```bash
python scripts/new_edit_image.py --custom_prompt "Create a luxurious watch advertisement in a high-end store with dramatic lighting and elegant composition"
```

**Best Practices for Custom Prompts**:
- Start with action verb ("Create", "Generate", "Design")
- Specify composition details
- Include lighting and mood
- Reference specific styles
- Mention brand elements

## Image Input Handling

### Supported Formats
Following Gemini specifications:
- JPG, PNG, WebP
- Maximum size: 20MB per image
- Recommended resolution: 1024x1024+

### Multimodal Input
```python
contents = [
    "Generate advertisement for this product",
    person_image,  # PIL Image object
    product_image  # PIL Image object
]
```

**Image Processing**:
- Automatic format detection
- Quality preservation
- Memory-efficient loading

## Response Processing

### Output Extraction
```python
image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]
```

### Error Handling
Following API error handling patterns:

```python
try:
    response = client.models.generate_content(...)
except Exception as e:
    if "429" in str(e):
        # Rate limit - rotate key
        switch_api_key()
    elif "RESOURCE_EXHAUSTED" in str(e):
        # Quota exceeded - wait and retry
        time.sleep(60)
    else:
        # Other error - log and skip
        logging.error(f"API Error: {e}")
```

## Rate Limit Management

### Key Rotation Strategy
```python
key_cycle = cycle(API_KEYS)
current_key = next(key_cycle)
```

**Benefits**:
- Prevents service interruptions
- Distributes load across keys
- Maintains high success rates

### Retry Logic
- Maximum 3 retries per request
- Exponential backoff: 2s, 4s, 8s
- Key rotation on each retry
- Comprehensive error logging

## Performance Optimization

### Multi-Threading
```python
with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(generate_image, *args) for args in tasks]
```

**Optimization**:
- Concurrent API calls
- Load balancing
- Memory management

### Batch Processing
- Process multiple combinations simultaneously
- Efficient resource utilization
- Progress tracking

## Monitoring and Analytics

### Logging Implementation
```python
logging.basicConfig(
    filename='logs/image_generation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

**Tracked Metrics**:
- API call success/failure
- Response times
- Key usage statistics
- Error patterns

## Cost Optimization

### Efficient API Usage
- Minimal prompt length
- Optimized image sizes
- Batch processing for volume discounts
- Smart retry logic to avoid wasted calls

### Quota Management
- Real-time quota monitoring
- Automatic key switching
- Usage reporting

## Security Considerations

### API Key Protection
- Environment variable storage
- No hardcoded keys
- Secure key rotation
- Access logging

### Data Privacy
- No user data storage
- Local processing only
- Secure file handling

## Integration Examples

### Basic Generation
Based on [JavaScript Getting Started](https://github.com/google-gemini/nano-banana-hackathon-kit/blob/main/examples/javascript-getting-started.md):

```javascript
// Equivalent JS implementation
const { GoogleGenerativeAI } = require('@google/generative-ai');
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
```

### Colab Integration
Following [Image Out Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Image_out.ipynb):

```python
# Colab-compatible code
from google import genai
import PIL.Image

model = genAI.GenerativeModel('gemini-2.5-flash-image-preview')
response = model.generate_content([
    "Create an advertisement",
    person_img,
    product_img
])
```

## Troubleshooting

### Common API Issues

#### Rate Limits
- Solution: Add more API keys
- Monitor: Check logs for 429 errors
- Prevention: Implement proper delays

#### Invalid Requests
- Check image formats and sizes
- Validate prompt structure
- Ensure proper authentication

#### Model Errors
- Update to latest model version
- Check API key permissions
- Verify quota availability

## Best Practices Summary

1. **Secure Key Management**: Use environment variables
2. **Efficient Prompts**: Clear, concise instructions
3. **Error Handling**: Comprehensive retry logic
4. **Performance**: Multi-threaded processing
5. **Monitoring**: Detailed logging and metrics
6. **Cost Control**: Optimized API usage patterns

## Resources

- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Image Generation Guide](https://ai.google.dev/gemini-api/docs/image-generation)
- [Nano Banana Hackathon Kit](https://github.com/google-gemini/nano-banana-hackathon-kit)
- [AI Studio Getting Started](https://aistudio.google.com/apps/bundled/get_started_image_out)

This API integration ensures the bot follows all Google guidelines while maximizing performance and reliability for hackathon evaluation.
