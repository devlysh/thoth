import os

# Constants
CONFIG_DIR = os.path.expanduser("~/.thoth")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config")

DEFAULT_CONFIG = {
    "archive": "lz4",
    "encryption": "chachapoly"
}

ARCHIVE_MAPPING = {
    "1": "lz4",
    "2": "lzma",
    "3": "zip",
    "4": "none"
}

ENCRYPTION_MAPPING = {
    "1": "chachapoly",
    "2": "aes",
    "3": "none"
}


def save_config(data):
    """Save the configuration to file."""
    with open(CONFIG_PATH, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

def read_config():
    """Reads the saved configuration and returns it as a dictionary."""
    with open(CONFIG_PATH, 'r') as file:
        lines = file.readlines()
    config = {}
    for line in lines:
        key, value = line.strip().split(': ')
        config[key] = value
    return config



def ensure_config_exists():
    """Ensure the configuration directory and file exists."""
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)


def get_interactive_choices():
    """Get the user choices in interactive mode."""
    print("Choose archiving method:")
    print("1) LZ4           - .lz4 (Default)")
    print("2) LZMA (7-Zip)  - .7z")
    print("3) DEFLATE (ZIP) - .zip")
    print("4) None          - No compression")
    archive_choice = input("Your choice: ")

    selected_archive = ARCHIVE_MAPPING.get(archive_choice, "lz4")

    print("\nChoose encryption method:")
    print("1) ChaCha20-Poly1305 (Default)")
    print("2) AES")
    print("3) None - No encryption")
    encryption_choice = input("Your choice: ")

    selected_encryption = ENCRYPTION_MAPPING.get(encryption_choice, "chachapoly")
    
    return selected_archive, selected_encryption


def handle_args(args):
    """Handle the user provided arguments."""
    # Set defaults if necessary
    if not args.archive and not args.encryption:
        args.archive, args.encryption = get_interactive_choices()
    
    # Set defaults based on single provided argument
    if args.archive and not args.encryption:
        if args.archive in ["lz4", "lzma", "zip"]:
            args.encryption = "chachapoly"
        else:
            args.encryption = "none"

    if args.encryption and not args.archive:
        if args.encryption in ["chachapoly", "aes"]:
            args.archive = "lz4"
        else:
            args.archive = "none"
    
    # Compatibility check
    if args.encryption == "none" and args.archive == "none":
        print("Error: You must select either compression or encryption or both.")
        return

    # Save choices to config
    config_data = {
        "archive": args.archive,
        "encryption": args.encryption
    }
    save_config(config_data)
