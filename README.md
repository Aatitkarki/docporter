# Docs Extractor

A Python package to extract documentation files from GitHub repositories.

## Features

- **GitHub Repository Cloning**: Clones a specified GitHub repository using a shallow clone.
- **Documentation File Filtering**: Identifies and filters documentation files (e.g., `.md`, `.rst`, `README.md`).
- **Directory Structure Preservation**: Copies filtered files to a new directory while preserving the original structure.
- **Repository Cleanup**: Removes the cloned repository after extraction.
- **Command-Line Interface**: Accepts a GitHub repository URL as input.

## Installation

```bash
pip install .
```

## Usage

```bash
docs-extractor https://github.com/user/repo.git
```

## Options

- `-o`, `--output`: Specify the output directory for documentation files.

## Example

```bash
docs-extractor https://github.com/user/repo.git -o ./docs
```

## License

MIT
