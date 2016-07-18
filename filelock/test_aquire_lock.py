import file_lock

file_name = 'test_data.tsv'
lock = file_lock.FileLock(file_name)

lock_acquired = lock.acquire()
if lock_acquired:
    print "TEST: Lock Acquired Passed"
else:
    exit(1, "TEST: Lock Acquired Failed")

additional_lock = file_lock.FileLock(file_name)

try:
    additional_lock_acquired = additional_lock.acquire()
    exit(1, "TEST: Additional Lock Not Acquired Failed")
except file_lock.FileLockException as e:
    print "TEST: Additional Lock Not Acquired Passed"

additional_lock.acquire_with_prejudice()
additional_lock_acquired = additional_lock.acquire()

if additional_lock_acquired:
    print "TEST: Additional Lock Acquired Passed"
else:
    exit(1, "TEST: Additional Lock Acquired Failed")

try:
    if lock.valid_lock():
        print "TEST: Lock Validation Passed"
    else:
        exit(1, "TEST: Lock Validation Failed")
except file_lock.FileLockException as e:
    print "TEST: Lock Validation Passed"

additional_lock.release()


