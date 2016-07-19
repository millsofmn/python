import os


class Properties(object):
    def __init__(self):
        self._properties = {}

    def load(self, properties_file):
        if os.path.exists(properties_file):
            with open(properties_file, 'rt') as fin:
                for line in fin:
                    (key, val) = line.split('=')

                    if '#' not in key:
                        key = key.strip().replace(' ', '_').replace('.', '_')
                        val = val.strip()

                        if '#' in val:
                            val = val.split('#')[0]

                        print "key={} value={}".format(key, val)
                        self._properties[key] = val

    def __len__(self):
        return len(self._properties)

    def __getitem__(self, item):
        if item not in self._properties:
            return None
        else:
            return self._properties[item]

    def __str__(self):
        for key, val in self._properties.items():
            print "key={} value={}".format(key, val)


def find_properties_file(cur_dir, name):

    print os.path.abspath(cur_dir)

    while True:
        file_list = os.listdir(cur_dir)
        parent_dir = os.path.dirname(cur_dir)

        if name in file_list:
            return os.path.join(cur_dir, name)
        elif cur_dir in parent_dir:
            print "At", cur_dir
            raise IOError(name + " File Not Found")
        else:
            cur_dir = parent_dir

if __name__ == '__main__':

    prop = Properties()
    prop_file = find_properties_file(os.path.dirname(os.path.realpath(__file__)), 'my.properties')

    print "Using file ", prop_file

    prop.load(prop_file)

    print prop['need.cool']
    print prop['KEEP_COOL']
    print prop['not_found']
    print prop['COMMENT']
