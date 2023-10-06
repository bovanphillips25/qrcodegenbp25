import os.path

from qrcodegenerator import create_qr_code_image
from config import Config


def main():
    full_path = os.getcwd()

    directory_path_and_file_name = os.path.join(full_path, Config.IMAGE_DIRECTORY, Config.FILE_NAME)

    qr_image = create_qr_code_image(Config.URL)
    for i in range(0, 1):
        while True:
            try:
                qr_image.save(directory_path_and_file_name)
            except FileNotFoundError:
                qr_directory = Config.IMAGE_DIRECTORY
                new_path = os.path.join(full_path, qr_directory)
                os.mkdir(new_path)
                continue
            break


if __name__ == "__main__":
    main()