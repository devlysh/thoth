from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from thoth.constants import CHUNK_SIZE
from tqdm import tqdm
import os
import pyzipper
import tempfile


def encrypt_chacha20_poly1305(input_path, output_path, key):
    chacha = ChaCha20Poly1305(key)
    nonce = os.urandom(12)
    total_size = os.path.getsize(input_path)
    with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        f_out.write(nonce)  # Write the nonce first to the output file
        for chunk in tqdm(iter(lambda: f_in.read(CHUNK_SIZE), b''), total=(total_size//CHUNK_SIZE), unit="chunk"):
            ciphertext = chacha.encrypt(nonce, chunk, None)
            f_out.write(ciphertext)


def decrypt_chacha20_poly1305(input_path, output_path, key):
    chacha = ChaCha20Poly1305(key)
    total_size = os.path.getsize(input_path) - 12  # 12 bytes less due to nonce
    with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        nonce = f_in.read(12)
        for chunk in tqdm(iter(lambda: f_in.read(CHUNK_SIZE), b''), total=(total_size//CHUNK_SIZE), unit="chunk"):
            decrypted_chunk = chacha.decrypt(nonce, chunk, None)
            f_out.write(decrypted_chunk)


def encrypt_zip_aes256(input_path, password):
    total_size = os.path.getsize(input_path)
    with tempfile.NamedTemporaryFile(delete=True) as temp:
        with pyzipper.AESZipFile(temp.name, 'w', compression=pyzipper.ZIP_DEFLATED) as zf, open(input_path, 'rb') as f_in:
            zf.setpassword(password.encode())
            zf.setencryption(pyzipper.WZ_AES, nbits=256)

            # Read data in chunks and write to ZIP, updating the progress bar
            for chunk in tqdm(iter(lambda: f_in.read(CHUNK_SIZE), b''), total=(total_size // CHUNK_SIZE), unit="chunk"):
                zf.writestr("content", chunk)

        # Read encrypted data from the ZIP file
        temp.seek(0)
        encrypted_data = temp.read()

    return encrypted_data


def decrypt_zip_aes256(encrypted_data, password, output_path, filename="content"):
    total_size = len(encrypted_data)

    with tempfile.NamedTemporaryFile(delete=True) as temp:
        temp.write(encrypted_data)
        temp.seek(0)

        with pyzipper.AESZipFile(temp.name, 'r') as zf, open(output_path, 'wb') as f_out:
            zf.setpassword(password.encode())

            # Read data from ZIP in chunks, updating the progress bar
            for chunk in tqdm(iter(lambda: zf.read(filename, CHUNK_SIZE), b''), total=(total_size // CHUNK_SIZE), unit="chunk"):
                f_out.write(chunk)
