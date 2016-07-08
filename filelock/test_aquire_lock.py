import filelock

lock = filelock.FileLock('test.txt')

lock_acquired = lock.acquire_lock()

if lock_acquired:
    print "TEST: Lock Acquired Successfully"
else:
    exit(1, "TEST: Lock Acquired Failed")

additional_lock = filelock.FileLock('test.txt')
additional_lock_acquired = additional_lock.acquire_lock()

if not additional_lock_acquired:
    print "TEST: Additional Lock Not Acquired Successfully"
else:
    exit(1, "TEST: Additional Lock Not Acquired Failed")

lock.release_lock()

additional_lock_acquired = additional_lock.acquire_lock()

if additional_lock_acquired:
    print "TEST: Additional Lock Acquired Successfully"
else:
    exit(1, "TEST: Additional Lock Acquired Failed")

