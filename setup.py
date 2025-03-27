from setuptools import setup, find_packages

setup(
    name="docs_extractor",
    version="0.1.0",
    package_dir={"docs_extractor": "src/docs_extractor"},
    packages=["docs_extractor"],
    install_requires=[
        "gitpython",
        "argparse",
        "urllib3",
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "docs-extractor=docs_extractor.cli:main",
        ],
    },
    description="A tool to extract documentation files from GitHub repositories and local folders.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/docs_extractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)