from tqdm import tqdm
import pyzipper
import os
from thoth.constants import CHUNK_FIXED_SIZE


def compress_with_deflate(input_path, output_path, password=None):
    file_size = os.path.getsize(input_path)

    with pyzipper.AESZipFile(output_path, 'w', compression=pyzipper.ZIP_DEFLATED) as zf:
        if password:
            zf.pwd = password.encode()
            zf.setencryption(pyzipper.WZ_AES, nbits=256)
        for _ in tqdm(range(0, file_size, CHUNK_FIXED_SIZE), unit="B", unit_scale=True, desc="Compressing"):
            with open(input_path, "rb") as f_in:
                f_in.seek(_)
                data = f_in.read(CHUNK_FIXED_SIZE)
                zf.writestr("content", data)


def decompress_with_deflate(input_path, output_path, password=None):
    file_size = os.path.getsize(input_path)

    with pyzipper.AESZipFile(input_path, 'r') as zf:
        if password:
            zf.pwd = password.encode()
        for _ in tqdm(range(0, file_size, CHUNK_FIXED_SIZE), unit="B", unit_scale=True, desc="Decompressing"):
            data = zf.read("content")
            with open(output_path, "wb") as f_out:
                f_out.write(data)
