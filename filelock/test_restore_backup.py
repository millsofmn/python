import file_lock
import shutil
import os

# setup
test_dir = 'temp'
test_data_file = 'test_data.tsv'

# setup enviroment
if os.path.exists(test_dir):
    shutil.rmtree(test_dir)
os.makedirs(test_dir)

temp_data_file = os.path.join(test_dir, test_data_file)
shutil.copy2(test_data_file, temp_data_file)

# create a file lock
lock = file_lock.FileLock(temp_data_file)

lock_acquired = lock.acquire()
if lock_acquired:
    print "TEST: Lock Acquired Passed"
else:
    exit(1, "TEST: Lock Acquired Failed")

# append backup file with a key
key = 'f25ad001-504b-481c-a945-a4c9b70ffbae'
backup_file = open(lock.backup.backup_file, 'a')
backup_file.write('\n' + key)
backup_file.close()

# create a new lock that will restore backup
additional_lock = file_lock.FileLock(temp_data_file)
additional_lock.acquire_with_prejudice()
additional_lock_acquired = additional_lock.acquire()

if additional_lock_acquired:
    print "TEST: Additional Lock Acquired Passed"
else:
    exit(1, "TEST: Additional Lock Acquired Failed")

additional_lock.release()

file_in = open(temp_data_file, 'rt')
line = file_in.readlines()
file_in.close()

if key in line:
    "TEST Pass: Backup file restored"
else:
    exit(1, "TEST Failed: unable to manipulate backup file")

shutil.rmtree(test_dir)