import file_backup
import os

line_out = "File was created to backed up"

backup_file = "my-file.txt"

file_out = open(backup_file, 'wt')
file_out.write(line_out)
file_out.close()

backup = file_backup.FileBackup(backup_file)

backup.create_backup()

backup.restore_backup()

backup.delete_backup()

os.remove(backup_file)
