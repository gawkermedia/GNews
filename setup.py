from setuptools import setup, find_packages

setup(
    name="GNews",
    version="0.1.0",
    description="A Python package for GNews integration.",
    author="Someone",
    url="https://github.com/gawkermedia/GNews",
    packages=find_packages(),  # Automatically discover packages in `gnews/`
    install_requires=[
        "requests",  # Add your package dependencies here
        "beautifulsoup4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires
)
