# """
# YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information
# """

# __version__ = "0.0.1"

# # Import key modules for easy access
# try:
#     from . import utils
#     from . import models
#     from . import detect
#     from . import train
#     from . import val
#     from . import export
# except ImportError:
#     # Handle cases where modules might not be available
#     pass

# # Make commonly used functions easily accessible
# def load_model(weights_path, device='cpu'):
#     """Load a YOLOv9 model from weights file"""
#     from . import hubconf
#     return hubconf.custom(weights_path, device=device)

# def detect_image(model, image_path, save_dir='runs/detect'):
#     """Run detection on an image"""
#     from . import detect
#     return detect.run(weights=model, source=image_path, project=save_dir)