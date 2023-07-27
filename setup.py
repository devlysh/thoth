from setuptools import setup, find_packages
from thoth.utils import get_version

setup(
    name="thoth",
    version=get_version(),
    packages=find_packages(),
    install_requires=[
        # Your dependencies, like 'lzma', 'cryptography', etc.
    ],
    entry_points={
        'console_scripts': [
            'thoth = thoth.cli:main',   # This allows you to use $ thoth
        ],
    },
)
