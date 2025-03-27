import rawpy
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
from tqdm import tqdm

def apply_pro_enhancements(img):
    """Apply professional image enhancements using PIL"""
    # Your specified adjustments
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.33)  # +33% brightness
    
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.30)  # +30% contrast
    
    # Exposure simulation (+43%)
    img = ImageOps.autocontrast(img, cutoff=2)
    
    # Tone curve adjustments (Highlights +26, Shadows -69)
    img = ImageOps.equalize(img)
    
    # Color adjustments (Saturation +4-5%, Tint -37, Temp -36)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.04)  # +4% saturation
    
    # Alternative to sharpness - Local contrast enhancement
    img = img.filter(ImageFilter.UnsharpMask(
        radius=2,
        percent=150,
        threshold=3
    ))
    
    # Definition enhancement (57)
    img = ImageEnhance.Sharpness(img).enhance(1.2)
    
    return img

def process_cr2_to_hd(input_path, output_path):
    """Convert CR2 to HD JPEG with professional processing"""
    try:
        with rawpy.imread(input_path) as raw:
            # Corrected RAW processing parameters
            rgb = raw.postprocess(
                output_color=rawpy.ColorSpace.sRGB,
                demosaic_algorithm=rawpy.DemosaicAlgorithm.AHD,
                no_auto_bright=True,
                gamma=(1, 1),
                output_bps=8,
                use_camera_wb=True
            )
        
        # Convert to PIL Image and apply enhancements
        enhanced_img = apply_pro_enhancements(Image.fromarray(rgb))
        enhanced_img.save(output_path, 'JPEG', 
                         quality=100, 
                         subsampling=0,
                         dpi=(300, 300))
        return True
    except Exception as e:
        print(f"\nError processing {os.path.basename(input_path)}: {str(e)}")
        return False

def batch_process(input_dir, output_dir):
    """Batch process all CR2 files with robust path handling"""
    # Convert to absolute paths
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)
    
    # Verify input directory exists
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    
    # Create output directory if needed
    os.makedirs(output_dir, exist_ok=True)
    
    # Get CR2 files (case-insensitive)
    cr2_files = [f for f in os.listdir(input_dir) 
                if f.lower().endswith('.cr2')]
    
    if not cr2_files:
        print(f"No CR2 files found in {input_dir}")
        return
    
    # Process files with progress bar
    for filename in tqdm(cr2_files, desc="Processing CR2 files"):
        input_path = os.path.join(input_dir, filename)
        output_filename = f"enhanced_{os.path.splitext(filename)[0]}.jpg"
        output_path = os.path.join(output_dir, output_filename)
        
        if not process_cr2_to_hd(input_path, output_path):
            continue  # Skip if processing failed

if __name__ == "__main__":
    # Configuration - modify these paths as needed
    INPUT_DIR = "Images_CR2"  # Relative to script location
    OUTPUT_DIR = "Enhanced_JPEGs"
    
    # Get script directory for reliable path resolution
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Run batch processing
    batch_process(
        input_dir=os.path.join(SCRIPT_DIR, INPUT_DIR),
        output_dir=os.path.join(SCRIPT_DIR, OUTPUT_DIR)
    )