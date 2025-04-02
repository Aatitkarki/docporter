import subprocess
import os
import shutil
import pytest

def test_cli_help():
    """Test that CLI help command works"""
    result = subprocess.run(["docporter", "--help"], capture_output=True, text=True)
    assert "usage: docporter" in result.stdout
    assert result.returncode == 0

def test_local_extraction(tmp_path):
    """Test basic local folder extraction"""
    test_dir = tmp_path / "test_docs"
    test_dir.mkdir()
    (test_dir / "README.md").write_text("# Test Document")
    
    output_dir = tmp_path / "output"
    result = subprocess.run(
        ["docporter", "extract", str(test_dir), "-o", str(output_dir)],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert (output_dir / "README.md").exists()
    # Just verify file was copied, don't check output message

def test_include_filter(tmp_path):
    """Test include pattern filtering"""
    test_dir = tmp_path / "filter_test"
    test_dir.mkdir()
    (test_dir / "README.md").write_text("# Doc")
    (test_dir / "script.py").write_text("print('test')")
    (test_dir / "notes.txt").write_text("notes")
    
    output_dir = tmp_path / "include_output"
    result = subprocess.run(
        ["docporter", "extract", str(test_dir), "--include", "*.py", "-o", str(output_dir)],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert (output_dir / "script.py").exists()
    # notes.txt is included by default doc types
    assert (output_dir / "notes.txt").exists()
    # Just verify files were copied as expected

def test_exclude_filter(tmp_path):
    """Test exclude pattern filtering"""
    test_dir = tmp_path / "exclude_test" 
    test_dir.mkdir()
    (test_dir / "test.py").write_text("test")
    (test_dir / "main.py").write_text("main")
    
    output_dir = tmp_path / "exclude_output"
    result = subprocess.run(
        ["docporter", "extract", str(test_dir), "--include", "*.py", "--exclude", "*test*", "-o", str(output_dir)],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    # Verify test.py was excluded
    assert not (output_dir / "test.py").exists()
    # main.py should exist
    if not (output_dir / "main.py").exists():
        print(f"Files in output: {list(output_dir.glob('*'))}")
    assert (output_dir / "main.py").exists()
    assert not (output_dir / "test.py").exists()

def test_combined_filters(tmp_path):
    """Test combined include/exclude filters"""
    test_dir = tmp_path / "combined_test"
    test_dir.mkdir()
    (test_dir / "module.py").write_text("module")
    (test_dir / "test_module.py").write_text("test")
    (test_dir / "config.txt").write_text("config")
    
    output_dir = tmp_path / "combined_output"
    result = subprocess.run(
        ["docporter", "extract", str(test_dir), "--include", "*.py", "--exclude", "*test*", "-o", str(output_dir)],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert (output_dir / "module.py").exists()
    assert not (output_dir / "test_module.py").exists()
    # config.txt is included by default doc types
    assert (output_dir / "config.txt").exists()

def test_copy_basic(tmp_path):
    """Test basic copy command"""
    test_dir = tmp_path / "copy_test"
    test_dir.mkdir()
    (test_dir / "README.md").write_text("# Test Doc")
    
    result = subprocess.run(
        ["docporter", "copy", str(test_dir)],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert "Copied LLM format" in result.stdout

def test_copy_include_filter(tmp_path):
    """Test copy with include filter"""
    test_dir = tmp_path / "copy_include_test"
    test_dir.mkdir()
    (test_dir / "module.py").write_text("code")
    (test_dir / "config.txt").write_text("config")
    
    result = subprocess.run(
        ["docporter", "copy", str(test_dir), "--include", "*.py"],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert "module.py" in result.stdout
    assert "config.txt" not in result.stdout

def test_copy_exclude_filter(tmp_path):
    """Test copy with exclude filter"""
    test_dir = tmp_path / "copy_exclude_test"
    test_dir.mkdir()
    (test_dir / "main.py").write_text("main")
    (test_dir / "test.py").write_text("test")
    
    result = subprocess.run(
        ["docporter", "copy", str(test_dir), "--exclude", "*test*"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    # Since no --include is given and main.py is not a default doc type,
    # it should not be included. test.py is explicitly excluded.
    assert "No files matched" in result.stdout
    assert "main.py" not in result.stdout # Ensure main.py is not included
    assert "test.py" not in result.stdout # Ensure test.py is not included

def test_copy_combined_filters(tmp_path):
    """Test copy with combined filters"""
    test_dir = tmp_path / "copy_combined_test"
    test_dir.mkdir()
    (test_dir / "app.py").write_text("app")
    (test_dir / "test_app.py").write_text("test")
    (test_dir / "notes.txt").write_text("notes")
    
    result = subprocess.run(
        ["docporter", "copy", str(test_dir), "--include", "*.py", "--exclude", "*test*"],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert "app.py" in result.stdout
    assert "test_app.py" not in result.stdout
    assert "notes.txt" not in result.stdout

if __name__ == "__main__":
    test_cli_help()
    print("Smoke tests passed!")
