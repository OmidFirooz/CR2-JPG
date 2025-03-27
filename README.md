# CR2-JPG
This python script converts the Canon raw files to the JPG format and enhances their quality.

📷 Professional CR2 to JPEG Converter
Automated RAW photo conversion with professional quality enhancements

🌟 Features
Batch convert Canon .CR2 files to high-quality JPEGs

Precise image adjustments without quality loss

Preserve original details while reducing blur

Automatic folder processing with progress tracking

Customizable enhancement parameters

🚀 Quick Start
Requirements
Python 3.6+

Windows/macOS/Linux

Installation
git clone https://github.com/yourusername/cr2-converter.git
cd cr2-converter
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt


🖼️ How to Use
Place your .CR2 files in the Images_CR2 folder

Run the script:
> python converter.py

Find enhanced JPEGs in the Enhanced_JPEGs folder

⚙️ Default Enhancements
Adjustment     	Value	   Description
Brightness	    +33%	   Lightens overall image
Contrast	      +30%	   Improves tonal range
Saturation	    +4%	     Enhances colors
Definition	    +20%	   Sharpness alternative
DPI	            300	     Print-quality output


📂 File Structure
cr2-converter/
├── Images_CR2/          # Input folder (put CR2 files here)
│   └── your_photos.CR2
│
├── Enhanced_JPEGs/      # Output folder (auto-created)
│   └── enhanced_your_photos.jpg
│
├── converter.py         # Main conversion script
├── requirements.txt     # Dependency list
└── README.md           # This document



🛠️ Customization
Edit these values in converter.py:
ENHANCEMENT_PROFILE = {
    'brightness': 1.33,    # 1.0 = original
    'contrast': 1.30,      # 1.0 = original
    'saturation': 1.04,    # 1.0 = original
    'dpi': 300,            # Output resolution
    'jpeg_quality': 100    # 0-100 scale
}

⚠️ Troubleshooting
Problem: Missing dependencies
Solution:
> pip install rawpy pillow tqdm numpy

Problem: File not found errors
Solution:

Verify that files are in the Images_CR2 folder

Use absolute paths if needed

Problem: Permission errors
Solution: Run as administrator/sudo

🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b improve-feature)

Commit your changes (git commit -m 'Add new enhancement')

Push to the branch (git push origin improve-feature)

Open a Pull Request
