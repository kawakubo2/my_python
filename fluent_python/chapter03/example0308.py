import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

if __name__ == '__main__':
    my_dict = StrKeyDict()
    my_dict['a'] = 13
    my_dict['x'] = 53
    my_dict[100] = 1000
    my_dict[(1, 2, 3)] = 50
    for key, value in my_dict.items():
        print('{}:{}'.format(key, value))
