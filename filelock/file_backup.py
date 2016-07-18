import os
import shutil


class FileBackup(object):

    def __init__(self, file_to_backup):
        self.file_to_backup = file_to_backup
        basename = os.path.basename(file_to_backup)
        dirname = os.path.dirname(file_to_backup)
        file_name = os.path.splitext(basename)[0]
        name = '.'.join(['.' + file_name, 'bck'])
        self.backup_file = os.path.join(dirname, name)

    def create_backup(self):
        if os.path.exists(self.file_to_backup):
            shutil.copy2(self.file_to_backup, self.backup_file)
            return True
        else:
            return False

    def restore_backup(self):
        if os.path.exists(self.backup_file):
            shutil.copy2(self.backup_file, self.file_to_backup)
            return True
        else:
            return False

    def delete_backup(self):
        if os.path.exists(self.backup_file):
            os.remove(self.backup_file)
            return True
        else:
            return False
