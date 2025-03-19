import os
import shutil
import pytest
from docs_extractor.core import extract_repo_name_from_url, clone_repo, filter_documentation_files, copy_files, delete_repo

def test_extract_repo_name_from_url():
    url = "https://github.com/user/repo.git"
    assert extract_repo_name_from_url(url) == "repo"

def test_clone_repo(tmpdir):
    repo_url = "https://github.com/user/repo.git"
    destination_folder = os.path.join(tmpdir, "repo")
    clone_repo(repo_url, destination_folder)
    assert os.path.exists(destination_folder)
    shutil.rmtree(destination_folder)

def test_filter_documentation_files(tmpdir):
    # Create a temporary directory with some files
    test_files = [
        "README.md",
        "docs/index.md",
        "src/main.py",
        "LICENSE.txt",
    ]
    for file in test_files:
        file_path = os.path.join(tmpdir, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write("test content")
    
    filtered_files = filter_documentation_files(tmpdir)
    assert len(filtered_files) == 3  # README.md, docs/index.md, LICENSE.txt

def test_copy_files(tmpdir):
    source_dir = os.path.join(tmpdir, "source")
    dest_dir = os.path.join(tmpdir, "dest")
    os.makedirs(source_dir)
    os.makedirs(dest_dir)
    
    test_files = ["file1.md", "file2.txt"]
    for file in test_files:
        with open(os.path.join(source_dir, file), "w") as f:
            f.write("test content")
    
    copy_files([os.path.join(source_dir, file) for file in test_files], dest_dir, source_dir)
    for file in test_files:
        assert os.path.exists(os.path.join(dest_dir, file))

def test_delete_repo(tmpdir):
    repo_dir = os.path.join(tmpdir, "repo")
    os.makedirs(repo_dir)
    delete_repo(repo_dir)
    assert not os.path.exists(repo_dir)