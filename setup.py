from setuptools import setup, find_packages

setup(
    name="GNews",
    version="0.1.0",
    description="A Python package for GNews integration.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "requests",  # Add dependencies here
        "beautifulsoup4",
    ],
)
