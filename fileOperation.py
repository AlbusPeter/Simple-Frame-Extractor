import os
import numpy as np
import glob
from tqdm import tqdm

def main():
    source_dir = "interpolation_comb1/942_867/"
    target_dir = "images/"
    for filename in tqdm(glob.glob(source_dir + '*.png')):
        base_name = os.path.basename(filename)
        file_idx, file_ext = os.path.splitext(base_name)
        new_idx = - int(file_idx) + 149
        newName = target_dir + str(new_idx) + file_ext
        os.rename(filename, newName)

if __name__ == "__main__":
    main()