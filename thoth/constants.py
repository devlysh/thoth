import os

# Thoth's local storage directory
THOTH_DIR = os.path.expanduser("~/.thoth")

# Configuration
CONFIG_DIR = THOTH_DIR
CONFIG_PATH = os.path.join(CONFIG_DIR, "config")

# Database
DATABASE_PATH = os.path.join(THOTH_DIR, "thoth.db")

# Fixed chunk size for straightforward archiving.
CHUNK_FIXED_SIZE = 64 * 1024  # 64 KB
