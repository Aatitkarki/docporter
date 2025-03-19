import argparse
from .core import main as core_main

def main():
    parser = argparse.ArgumentParser(description="Extract documentation files from a GitHub repository.")
    parser.add_argument("repo_url", type=str, help="URL of the GitHub repository to clone.")
    parser.add_argument("-o", "--output", type=str, default=None, help="Output directory for documentation files.")
    
    args = parser.parse_args()
    core_main(args.repo_url, args.output)