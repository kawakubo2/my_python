numbers1 = { 2, 4, 6, 8, 10, 12, 14, 16 }
numbers2 = { 1, 2, 4, 8, 16, 32, 64 }
"""
2つの集合の、和集合(|)、積集合(&)、差集合(-)
と同等の関数を作成する。
"""
class MySet():
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2
    def union(self): # 和集合
        result = set();
        for elem in self.set1:
            result.add(elem)
        for elem in self.set2:
            result.add(elem)
        return result
    
    def intersect(self): # 積集合
        result = set();
        for elem in self.set1:
            if elem in self.set2:
                result.add(elem)
        return result
        
    def minus(self): # 差集合
        result = set();
        for elem in self.set1:
            if elem not in self.set2:
                result.add(elem)
        return result

myset = MySet(numbers1, numbers2)
print(myset.union())
print(myset.intersect())
print(myset.minus())