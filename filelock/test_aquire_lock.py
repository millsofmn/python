import file_lock

file_name = __file__
lock = file_lock.FileLock(file_name)

lock_acquired = lock.acquire()
if lock_acquired:
    print "TEST: Lock Acquired Passed"
else:
    exit(1, "TEST: Lock Acquired Failed")

additional_lock = file_lock.FileLock(file_name)
additional_lock_acquired = additional_lock.acquire()

if not additional_lock_acquired:
    print "TEST: Additional Lock Not Acquired Passed"
else:
    exit(1, "TEST: Additional Lock Not Acquired Failed")

additional_lock.acquire_with_prejudice()
additional_lock_acquired = additional_lock.acquire()

if additional_lock_acquired:
    print "TEST: Additional Lock Acquired Passed"
else:
    exit(1, "TEST: Additional Lock Acquired Failed")

if not lock.valid_lock():
    print "TEST: Lock Validation Passed"
else:
    exit(1, "TEST: Lock Validation Failed")

additional_lock.release()


