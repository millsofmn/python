import os
import time
import random
import socket
import uuid

"""
    FileLock creates a lock file to indicate that a process is working
    with the resource.

    Variables that can be set:
    timeout - how long a lock will be attempted until it fails
    acquire_with_prejudice - after so many attempts the current lock will
        be terminated and acquired for current process
    attempts - total attempts until acquire_with_prejudice, if negative
        then only one attempt will be made

"""


class FileLock(object):
    """
    FileLock input is file that will be locked and default timeout period
    in seconds.
    """
    def __init__(self, file_to_lock, timeout=5):
        basename = os.path.basename(file_to_lock)
        dirname = os.path.dirname(file_to_lock)
        file_name = os.path.splitext(basename)[0]
        name = '.' + file_name + '.lck'
        self.lock_file = os.path.join(dirname, name)
        self.timeout = timeout
        self._acquire_with_prejudice = False
        self.attempts = 1
        self.lock_id = ''
        self.uuid = ''

    def acquire_with_prejudice(self, value=True):
        """
        If this is set then a lock from a previous operation will be
        terminated and after a period of time. It is assumed that the previous
        resource that was using the file died.

        :param value:
        :return:
        """
        self._acquire_with_prejudice = value
        return None

    def total_attempts(self, attempts):
        """
        Set total attempts before acquire with prejudice if value is negative
        then only one attempt will be made before the lock is terminated.
        Default attempts is 2

        :param attempts:
        :return:
        """
        self.attempts = attempts
        return None

    def acquire(self, timeout=None):
        """
        Acquire will attempt to get the lock on a the file and once that has
        happened then it will return true. If unable to get the lock it will
        continually try until the timeout period (defined in seconds). After
        that period has passed it will return false or if
        acquire_with_prejudice is true then another attempt will be made and
        if that fails the lock will be grabbed anyway assuming that the
        process was hung or terminated prematurely. This happens by
        terminating the lock from the previous resource.

        :param timeout: seconds
        :return:
        """

        # setup defaults
        if timeout is None:
            timeout = self.timeout
        locked_acquired = False
        start_time = time.time()

        while True:
            # if file is not locked go ahead and lock file
            if not self.is_locked():
                self._acquire()
                locked_acquired = True
                break

            # Unable to lock file and timeout has passed
            elif timeout >= 0 and time.time() - start_time > timeout:

                # after timeout period and enough attempts has been completed
                # go ahead and remove the previous lock and attempt to
                # obtain the lock again
                if self._acquire_with_prejudice and self.attempts <= 1:
                    self.release()

                # if additional attempts need to be made go ahead and od that
                elif self._acquire_with_prejudice and self.attempts >= 1:
                    self.attempts -= 1

                # exit loop because lock couldn't be attained
                else:
                    break

            # Unable to lock file so sleep and try again
            else:
                self._sleep()

        return locked_acquired

    def release(self):
        """
        Remove lock file
        :return:
        """
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
        """
        Check if file locked and if it is verify that the lock was created
        by the same resource that is checking for a valid lock.
        :return:
        """
        file_locked = self.is_locked()
        if file_locked:
            file_in = open(self.lock_file, 'rt')
            line = file_in.readlines()
            file_in.close()

            if self.uuid in line:
                return True
        return False

    def _acquire(self):
        """
        Create lock file
        :return:
        """
        self.uuid = uuid.uuid4()
        line_out = "File was locked by '{}' at {} {} {}".format(socket.gethostname(), time.ctime(), os.getpid(), self.uuid)

        file_out = open(self.lock_file, 'wt')
        file_out.write(line_out)
        file_out.close()
