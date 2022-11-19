import shutil
import os
from pathlib import Path
import config


class Initializer:
    @staticmethod
    def run():
        Initializer.remove_old_data()
        Initializer.unpack_data()
        
    @staticmethod
    def remove_old_data():
        shutil.rmtree(os.path.join('..', config.DATA_DIR), ignore_errors=True)

    @staticmethod
    def unpack_data():
        shutil.unpack_archive(os.path.join('..', config.INITIAL_RAW_DATA_COMPRESSED_FILE), '..')

        for root, _, files in os.walk(os.path.join('..', config.INTERMEDIATE_DATA_DIR)):
            for file in files:
                source = os.path.join(root, file)
                dest = os.path.join('..', config.DATA_DIR, Path(file).stem)
                shutil.unpack_archive(source, dest)

    @staticmethod
    def remove_intermediate_data():
        shutil.rmtree(os.path.join('..', config.INTERMEDIATE_DATA_DIR), ignore_errors=True)
