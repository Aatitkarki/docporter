import os
import shutil
from git import Repo
from pathlib import Path

def extract_repo_name_from_url(repo_url):
    """Extract the repository name from the GitHub URL."""
    return repo_url.split("/")[-1].replace(".git", "")

def clone_repo(repo_url, destination_folder):
    """Clone the GitHub repository to the specified destination folder."""
    try:
        Repo.clone_from(repo_url, destination_folder, depth=1)
        print(f"Cloned repository: {repo_url}")
    except Exception as e:
        print(f"Error during clone: {e}")
        exit(1)

def filter_documentation_files(repo_path):
    """Filter documentation files in the repository."""
    doc_extensions = {".md", ".mdx", ".rst", ".txt"}
    doc_files = []
    
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.lower().startswith("readme") or Path(file).suffix.lower() in doc_extensions:
                doc_files.append(os.path.join(root, file))
    return doc_files

def copy_files(files, output_folder, repo_root):
    """Copy filtered documentation files to the output folder, preserving directory structure."""
    for file in files:
        relative_path = os.path.relpath(file, repo_root)
        dest_file_path = os.path.join(output_folder, relative_path)
        dest_dir = os.path.dirname(dest_file_path)
        
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        try:
            shutil.copy(file, dest_file_path)
            print(f"Copied file: {relative_path}")
        except Exception as e:
            print(f"Error copying file {file}: {e}")

def delete_repo(repo_folder):
    """Delete the cloned repository folder."""
    try:
        shutil.rmtree(repo_folder)
        print(f"Deleted repository folder: {repo_folder}")
    except Exception as e:
        print(f"Error deleting repository folder: {e}")

def main(repo_url, output_folder=None):
    """Main function to extract documentation files from a GitHub repository."""
    repo_name = extract_repo_name_from_url(repo_url)
    destination_folder = repo_name
    output_folder = output_folder or f"{repo_name}-docs"
    
    # Clone the repository
    clone_repo(repo_url, destination_folder)
    
    # Filter documentation files
    doc_files = filter_documentation_files(destination_folder)
    
    # Copy documentation files to the output folder
    copy_files(doc_files, output_folder, destination_folder)
    
    # Clean up the cloned repository
    delete_repo(destination_folder)
    print(f"Documentation extraction completed. Files saved to: {output_folder}")