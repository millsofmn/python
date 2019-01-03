import argparse
import hashlib
import os
import zipfile


def zip_directory(path, name):
    zfile = zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED)

    zip_path = os.path.basename(path)

    print(zip_path)

    dir_path = len(path)

    for base, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(base, file)
            zfile.write(file_path, file_path[dir_path :])

    for f in zfile.namelist():
        print('Added %s' % f)

    zfile.close()

    h = hashlib.sha256()
    b = bytearray(128*1024)
    mv = memoryview(b)
    with open(name, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])

    print('Hash: %s' % h.hexdigest())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Zip Directory')
    parser.add_argument('--path', action="store", dest="path")
    parser.add_argument('--name', action="store", dest="name")
    given_args = parser.parse_args()

    zip_directory(given_args.path, given_args.name)
