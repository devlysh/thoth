import os
import hashlib


def get_version():
    """Retrieve the current version of the Thoth tool from version.txt."""
    with open(os.path.join(os.path.dirname(__file__), '..', 'version'), 'r') as f:
        return f.read().strip()


def generate_file_id(file_path):
    """Generate a SHA-256 ID for the given file."""
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        # Read and update hash in chunks for efficiency
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()
