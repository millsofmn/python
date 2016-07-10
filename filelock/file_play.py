import os

filename = __file__
print "Script Executing", filename
path = os.path.abspath(filename)

print "ABS Path", path
print "Basename", os.path.basename(path)
print "Dirname", os.path.dirname(path)
print "Exists", os.path.exists(path)
print "Last Access", os.path.getatime(path)
print "Last Modify", os.path.getmtime(path)
print "Size", os.path.getsize(path)
print "Is Abs", os.path.isabs(path)
print "Is File", os.path.isfile(path)
print "Is Dir", os.path.isdir(path)

print "===================================="
#print "Join", os.path.join(path, *paths)

print "Split", os.path.split(path)
print "Split Drive", os.path.splitdrive(path)
print "Split Text", os.path.splitext(path)

name = os.path.split(path)[-1]
print "File: ", os.path.split(path)[-1]
print "File and Path without ext: ", os.path.splitext(path)[0]

print "====================================="
base = os.path.basename(path)
fname = os.path.splitext(base)[0]
print "File Name", fname

dirname = os.path.dirname(path)
name = '.' + fname + '.lck'
print name
lock_file = os.path.join(dirname, name)
print "Lock File", lock_file