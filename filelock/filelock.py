import os
import time
import random
import socket
import uuid


class FileLock(object):
    def __init__(self, file_to_lock, timeout=5):
        basename = os.path.basename(file_to_lock)
        dirname = os.path.dirname(file_to_lock)
        file_name = os.path.splitext(basename)[0]
        name = '.' + file_name + '.lck'
        self.lock_file = os.path.join(dirname, name)
        self.timeout = timeout
        self._acquire_with_prejudice = False
        self.lock_id = ''
        self.uuid = ''

    def acquire_with_prejudice(self, value=True):
        self._acquire_with_prejudice = value
        return None

    def acquire(self, timeout=None):
        attempts = 1
        if timeout is None:
            timeout = self.timeout

        locked_acquired = False

        start_time = time.time()
        while True:
            if not self.is_locked():
                self._acquire()
                locked_acquired = True
                break
            elif timeout >= 0 and time.time() - start_time > timeout:
                if self._acquire_with_prejudice and attempts <= 1:
                    self.release()
                elif self._acquire_with_prejudice and attempts >= 1:
                    attempts -= 1
                else:
                    break
            else:
                self._sleep()

        return locked_acquired

    def release(self):
        os.remove(self.lock_file)
        self.uuid = ''

    def _sleep(self):
        time.sleep(random.random())

    def is_locked(self):
        if os.path.exists(self.lock_file):
            return True
        else:
            return False

    def valid_lock(self):
        file_locked = self.is_locked()

        if file_locked:
            with open(self.lock_file, 'rt') as file_in:
                line = file_in.readlines()

            if self.uuid in line:
                return True
        return False

    def _acquire(self):
        self.uuid = uuid.uuid4()
        line_out = "File was locked by '{}' at {} {}".format(socket.gethostname(), time.ctime(), self.uuid)

        with open(self.lock_file, 'wt') as file_out:
            file_out.write(line_out)
