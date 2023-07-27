from tqdm import tqdm
import lz4.frame as lz4f
import os
from thoth.constants import CHUNK_SIZE


def compress_with_lz4(input_path, output_path):
    file_size = os.path.getsize(input_path)

    with open(input_path, 'rb') as f_in, lz4f.open(output_path, 'wb') as f_out:
        for _ in tqdm(range(0, file_size, CHUNK_SIZE), unit="B", unit_scale=True, desc="Compressing"):
            data = f_in.read(CHUNK_SIZE)
            f_out.write(data)


def decompress_with_lz4(input_path, output_path):
    file_size = os.path.getsize(input_path)

    with lz4f.open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        for _ in tqdm(range(0, file_size, CHUNK_SIZE), unit="B", unit_scale=True, desc="Decompressing"):
            data = f_in.read(CHUNK_SIZE)
            f_out.write(data)
