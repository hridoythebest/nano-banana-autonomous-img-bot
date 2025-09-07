# Usage Guide

## Basic Usage

The Nano-Banana bot supports both single image generation and batch processing.

### Single Image Generation

Generate an advertisement by specifying person and product images:

```bash
python scripts/new_edit_image.py --person person_images/model.png --product product_images/shoes.png
```

**Output**: An image saved to `outputs/ad_model__shoes__<timestamp>.jpg`

### Batch Processing

Process all combinations of person and product images:

```bash
python scripts/new_edit_image.py
```

This will generate images for every person-product pair.

## Command-Line Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--person` | string | None | Path to specific person image |
| `--product` | string | None | Path to specific product image |
| `--person_dir` | string | `person_images/` | Directory containing person images |
| `--product_dir` | string | `product_images/` | Directory containing product images |
| `--outdir` | string | `outputs/` | Output directory |
| `--prompt` | string | Default prompt | Custom prompt (see below) |
| `--model` | string | `gemini-2.5-flash-image-preview` | Gemini model to use |
| `--max_workers` | int | 20 | Number of concurrent threads |
| `--custom_prompt` | string | None | Override default prompt |
| `--theme` | string | `modern` | Theme: modern/luxury/casual/professional |

## Advanced Usage

### Custom Prompts

Create specialized advertisements:

```bash
python scripts/new_edit_image.py --person person_images/model.png --product product_images/watch.png --custom_prompt "Create a luxurious watch advertisement in a high-end store setting with dramatic lighting"
```

### Theme Selection

Apply predefined styles:

```bash
# Luxury theme for premium products
python scripts/new_edit_image.py --theme luxury

# Casual theme for everyday items
python scripts/new_edit_image.py --theme casual
```

### Performance Tuning

Adjust thread count based on your system:

```bash
# For high-end systems
python scripts/new_edit_image.py --max_workers 50

# For limited resources
python scripts/new_edit_image.py --max_workers 5
```

### Directory Customization

Use custom directories:

```bash
python scripts/new_edit_image.py --person_dir /path/to/people --product_dir /path/to/products --outdir /path/to/results
```

## Examples

### Example 1: Fashion E-commerce

```bash
python scripts/new_edit_image.py --person person_images/fashion_model.jpg --product product_images/dress.jpg --theme luxury
```

*Result*: Model in elegant attire showcasing the dress in a sophisticated setting.

### Example 2: Tech Products

```bash
python scripts/new_edit_image.py --person person_images/tech_user.png --product product_images/laptop.png --theme modern --custom_prompt "Create a modern tech advertisement showing the laptop in a sleek workspace"
```

*Result*: Professional user with updated workspace environment.

### Example 3: Sports Equipment

```bash
python scripts/new_edit_image.py --theme casual --max_workers 10
```

*Result*: Casual outfits and outdoor settings for all sports products.

### Example 4: Seasonal Campaign

```bash
python scripts/new_edit_image.py --custom_prompt "Create holiday-themed advertisements with festive decorations and winter clothing"
```

*Result*: Seasonal adaptations for all products.

## Output Management

### File Naming Convention
Generated files follow: `ad_<person_stem>__<product_stem>__<timestamp>.jpg`

Examples:
- `ad_model__shoes__20231201_143022.jpg`
- `ad_executive__watch__20231201_143023.jpg`

### Directory Structure
```
outputs/
├── ad_model1__product1__20231201_143022.jpg
├── ad_model1__product2__20231201_143023.jpg
└── ad_model2__product1__20231201_143024.jpg
```

### Log Files
All operations logged to `logs/image_generation.log`:
```
2023-12-01 14:30:22 - INFO - Starting generation for model.png and shoes.png
2023-12-01 14:30:35 - INFO - Successfully saved outputs/ad_model__shoes__20231201_143022.jpg
```

## Troubleshooting

### Common Issues

#### "File not found" Error
- Ensure paths are correct
- Use absolute paths if relative fail
- Check file permissions

#### API Rate Limits
- The script automatically handles this with key rotation
- Monitor logs for rate limit messages
- Add more API keys to `.env` for better performance

#### Memory Issues
- Reduce `--max_workers` for large batches
- Process in smaller chunks

#### Quality Issues
- Use high-resolution input images
- Experiment with custom prompts
- Try different themes

### Performance Tips

- Use SSD storage for faster I/O
- Increase `--max_workers` on multi-core systems
- Process similar products together for better caching

### Monitoring

Check logs regularly:
```bash
tail -f logs/image_generation.log
```

For detailed debugging, run with verbose output (if implemented).

## Integration Examples

### Cron Job for Daily Generation
```bash
# Add to crontab for daily batch processing
0 9 * * * cd /path/to/nano-banana-bot && python scripts/new_edit_image.py
```

### Script Integration
```python
import subprocess

result = subprocess.run([
    'python', 'scripts/new_edit_image.py',
    '--person', 'person_images/model.png',
    '--product', 'product_images/product.png'
], capture_output=True)

if result.returncode == 0:
    print("Image generated successfully")
```

## Next Steps

- Review FEATURES.md for full capability list
- Check API_USAGE.md for technical details
- See CONTRIBUTING.md for development guidelines
