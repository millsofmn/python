import os
import time
import random


class FileLock(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.lock_file = file_name + '.lck'

    def acquire_lock(self):
        lock_file = os.path.abspath(self.lock_file)
        locked = False
        attempts = 1

        while not locked and attempts < 10:
            if os.path.isfile(lock_file):
                self.go_to_sleep()
                attempts += 1
            else:
                locked = True

        if locked:
            with open(lock_file, 'wt') as file_out:
                file_out.write("Lock File")
        else:
            return False
        return True

    def release_lock(self):
        os.remove(self.lock_file)

    def go_to_sleep(self):
        time.sleep(random.random())
