from setuptools import setup, find_packages

setup(
    name="docs_extractor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gitpython",
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "docs-extractor=src.cli:main",
        ],
    },
    description="A tool to extract documentation files from GitHub repositories.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/docs_extractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)