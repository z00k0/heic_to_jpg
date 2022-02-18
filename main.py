from PIL import Image
from pillow_heif import register_heif_opener
import os
import glob


register_heif_opener()


def convert_heic_to_jpg(infile):
    f, e = os.path.splitext(infile)
    outfile = f + '.jpg'
    if infile != outfile:
        try:
            with Image.open(infile) as img:
                img.save(outfile)
        except OSError:
            print('Cannot convert', infile)


def get_list_of_heic():
    filelist = glob.glob('*.HEIC')
    return filelist


if __name__ == '__main__':
    list_of_heic = get_list_of_heic()
    counter = 0
    for file in list_of_heic:
        convert_heic_to_jpg(file)
        print(f'Convert: {file}')
        counter += 1
    print(f'Converted {counter} file(s)')
