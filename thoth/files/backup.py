from thoth.compress import compress_with_lz4, compress_with_lzma, compress_with_deflate
from thoth.encrypt import encrypt_chacha20_poly1305, encrypt_zip_aes256

def create_backup(input_path, output_path):
    # Read the saved configuration
    config = read_config()

    # First, we'll archive the file
    if config["archive"] == "lz4":
        temp_archive_path = input_path + ".lz4"
        compress_with_lz4(input_path, temp_archive_path)
    elif config["archive"] == "lzma":
        temp_archive_path = input_path + ".lzma"
        compress_with_lzma(input_path, temp_archive_path)
    elif config["archive"] == "zip":
        temp_archive_path = input_path + ".zip"
        compress_with_deflate(input_path, temp_archive_path)
    elif config["archive"] == "none":
        temp_archive_path = input_path

    # Then, if required, we'll encrypt the archived file
    if config["encryption"] == "chachapoly":
        with open(temp_archive_path, 'rb') as f:
            encrypted_data = encrypt_chacha20_poly1305(f.read(), YOUR_SECURE_KEY)
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)
    elif config["encryption"] == "aes":
        with open(temp_archive_path, 'rb') as f:
            encrypted_data = encrypt_zip_aes256(f.read(), YOUR_PASSWORD)
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)
    elif config["encryption"] == "none":
        if config["archive"] != "none":
            os.rename(temp_archive_path, output_path)
        else:
            raise ValueError("No operation performed as both archive and encryption are set to 'none'")
