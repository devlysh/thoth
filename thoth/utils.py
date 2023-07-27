import os

def get_version():
    """Retrieve the current version of the Thoth tool from version.txt."""
    with open(os.path.join(os.path.dirname(__file__), '..', 'version'), 'r') as f:
        return f.read().strip()
