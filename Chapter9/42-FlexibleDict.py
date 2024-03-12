# Flexible Dict
#  - Create a new class FlexibleDict()
#    - Should be subclass of python's dict
#    - Should be able to try converting keys to str and int for search
#      - Effectively, be able to use str("1") to find int(1) as a key

class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass
        
        return dict.__getitem__(self, key)

# Optional Exercise: StringKeyDict
#  - Create a new class StringKeyDict()
#    - Should be a subclass of dict
#    - Should convert keys to string by default (e.g., for reading from file as strings)
class StringKeyDict(dict):
    def __setitem__(self, key, val):
        return dict.__setitem__(self, str(key), val)

# Optional Exercise: RecentDict
#  - Create a new class RecentDict()
#    - Should be a subclass of dict
#    - Should only store the N most recent entries. Remove the oldest
class RecentDict(dict):
    item_count = 0
    MAX_ITEMS = 3
    def __setitem__(self, key, val):
        if self.item_count == self.MAX_ITEMS:
            del self[(next(iter(self)))]
        else:
            self.item_count += 1
        
        return dict.__setitem__(self, key, val)
        

if __name__ == '__main__':
    fd = FlexibleDict()

    fd['a'] = 100
    print(fd['a'])

    fd[1] = 500
    print(fd[1])
    print(fd["1"])
    fd["2"] = 1000
    print(fd["2"])
    print(fd[2])
    print("#####\n")

    skd = StringKeyDict()

    skd[1] = 100
    print(skd["1"])
    print("#####\n")

    rd = RecentDict()

    rd[1] = 100
    rd[2] = 200
    rd[3] = 300
    print(rd)
    rd[4] = 400
    print(rd)