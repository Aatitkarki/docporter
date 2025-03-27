import subprocess
import os
import shutil

def test_cli_help():
    """Test that CLI help command works"""
    result = subprocess.run(["docs-extractor", "--help"], capture_output=True, text=True)
    assert "usage: docs-extractor" in result.stdout
    assert result.returncode == 0

def test_local_extraction(tmp_path):
    """Test basic local folder extraction"""
    test_dir = tmp_path / "test_docs"
    test_dir.mkdir()
    (test_dir / "README.md").write_text("# Test Document")
    
    output_dir = tmp_path / "output"
    result = subprocess.run(
        ["docs-extractor", str(test_dir), "-o", str(output_dir)],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert (output_dir / "README.md").exists()
    assert "Copied file: README.md" in result.stdout

if __name__ == "__main__":
    test_cli_help()
    print("Smoke tests passed!")
