"""
YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information
"""

__version__ = "0.0.1"

# Import submodules to make them accessible as yolov9.utils, yolov9.models, etc.
from . import utils
from . import models

# Import main scripts as submodules
from . import detect
from . import train
from . import val
from . import export
from . import hubconf

# Also import other main modules
try:
    from . import detect_dual
    from . import train_dual
    from . import train_triple
    from . import val_dual
    from . import val_triple
    from . import benchmarks
except ImportError:
    pass

# Import subpackages
try:
    from . import classify
    from . import segment
    from . import panoptic
except ImportError:
    pass