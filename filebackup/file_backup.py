import os
import shutil

class FileBackup(object):

    def __init__(self, file_to_backup):
        self.file_to_backup = file_to_backup
        basename = os.path.basename(file_to_backup)
        dirname = os.path.dirname(file_to_backup)
        file_name = os.path.splitext(basename)[0]
        name = '.'.join(['.' + file_name, str(os.getpid()), 'bck'])
        self.backup_file = os.path.join(dirname, name)

    def create_backup(self):
        shutil.copy2(self.file_to_backup, self.backup_file)

    def restore_backup(self):
        shutil.copy2(self.backup_file, self.file_to_backup)

    def delete_backup(self):
        os.remove(self.backup_file)
