import os
import hashlib
from .constants import THOTH_DIR

CHUNK_DIR = os.path.join(THOTH_DIR, 'chunks')

def ensure_chunk_dir_exists():
    """Ensure chunk directory exists."""
    if not os.path.exists(CHUNK_DIR):
        os.makedirs(CHUNK_DIR)

def get_chunk_hash(chunk_data):
    """Return the SHA-256 hash of the given data."""
    sha256 = hashlib.sha256()
    sha256.update(chunk_data)
    return sha256.hexdigest()

def save_chunk_to_fs(chunk_data):
    """Save chunk to filesystem and return the path."""
    chunk_hash = get_chunk_hash(chunk_data)
    chunk_path = os.path.join(CHUNK_DIR, chunk_hash)
    with open(chunk_path, 'wb') as chunk_file:
        chunk_file.write(chunk_data)
    return chunk_path

ensure_chunk_dir_exists()
