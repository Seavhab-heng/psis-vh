# psis-vh: Mobile Camera Watermark Application

## Overview

A dual-stack watermarking application with:
- **Web component** (`index.html`): Real-time camera capture with in-browser watermarking (1920×1080 @ 1080p)
- **Python component** (`watermark.py`): Batch image processing with PIL-based watermarking

## Quick Start

### Web Component
- Open `index.html` in a mobile browser (or desktop with camera)
- Requires camera permissions
- Captures 1080p photos with watermark overlay and triggers download

### Python Batch Processing
```bash
# Requires: input/ folder with .png, .jpg, .jpeg files
# Requires: watermark.png in project root
python watermark.py
# Outputs processed images to output/ folder
```

## Architecture

### Web Stack
- **HTML5 Canvas** for drawing and watermarking
- **MediaDevices API** for rear camera access with ideal resolution constraints
- **Responsive design** with fixed 16:9 aspect ratio (mobile-optimized)
- Watermark rendered as white text: "MY WATERMARK" at bottom-left

### Python Stack
- **PIL (Pillow)** for image operations
- Watermark applied at bottom-right with 10px padding
- Converts output to JPEG for web compatibility
- Supports PNG, JPG, JPEG input formats

## Key Files
- `index.html` - Web interface and camera capture logic
- `watermark.py` - Batch processing script
- `watermark.png` - Watermark image asset (required for Python script)
- `output/` - Directory where processed images are saved

## Common Issues & Solutions

### Python Script Exit Code 1
**Problem**: `python watermark.py` fails immediately
- Check that `input/` folder exists in project root
- Check that `watermark.png` exists in project root
- Verify PIL/Pillow is installed: `pip install Pillow`

### Web Component
- Ensure browser has camera permissions enabled
- Test on mobile or use browser camera emulation
- Canvas download may be blocked by CORS or browser policies in some contexts

## Development Patterns

1. **Image Processing**: Uses RGBA intermediate layer to preserve transparency during overlay
2. **Responsive UI**: Video container uses CSS aspect-ratio for consistent mobile experience
3. **File Operations**: Python script auto-creates output folder if missing

## Testing Checklist
- [ ] Web: Camera access works and captures at 1920×1080
- [ ] Web: Downloaded image contains watermark text
- [ ] Python: Process sample images from input/ folder
- [ ] Python: Output files exist in output/ folder with watermarks applied
- [ ] Both: Verify watermark positioning (bottom-right for Python, bottom-left for web)

## Future Improvements
- Configurable watermark text/image in web component
- Watermark positioning options
- Batch processing progress feedback in web UI
- Mobile app wrapper (React Native, Flutter, etc.)
