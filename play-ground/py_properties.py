import csv


class Property(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Properties(object):
    def __init__(self):
        self._properties = {}

    def load(self, properties_file):
        with open(properties_file, 'rt') as fin:
            cin = csv.reader(fin, delimiter='=')
            for row in cin:
                print row
            # proper = [row for row in cin]
            # print proper

        # print proper


if __name__ == '__main__':
    prop = Properties()
    prop.load('my.properties')
