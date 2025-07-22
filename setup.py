from setuptools import setup, find_packages
import re

requirements = []
for line in open('reduced_requirements.txt'):
  req = line.split('#', 1)[0].strip()  # strip comments and whitespace
  if req:  # only add non-empty requirements
    requirements.append(req)

# follow https://stackoverflow.com/a/7071358/419116
VERSIONFILE = "_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
  verstr = mo.group(1)
else:
  raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name="yolov9",
    version=verstr,
    description="YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information",
    author="Carbon Robotics",
    install_requires=requirements,
    python_requires=">=3.8",
    include_package_data=True,
    package_data={
        "yolov9": ["*.yaml", "*.yml", "*.txt", "*.md", "*.jpg", "*.png", "*.py"],
        "yolov9.data": ["*.yaml", "*.yml"],
        "yolov9.models": ["**/*.yaml", "**/*.yml"],
    },
)