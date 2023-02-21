class Member:
    def __init__(self, name, active):
        self.name = name
        self.active = active

class ActiveMemberIterator:
    def __init__(self, member_list):
        self.__member_list = member_list
        self.__index = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.__member_list) == 0:
            raise StopIteration
        while True:
            if self.__index >= len(self.__member_list):
                raise StopIteration
            elif self.__member_list[self.__index].active:
                member = self.__member_list[self.__index]
                self.__index += 1
                return member
            else:
                self.__index += 1

if __name__ == '__main__':
    members = [
        Member("山田太郎", True),
        Member("横山花子", True),
        Member("田中一郎", False),
        Member("山本久美子", True),
        Member("鈴木次郎", False),
    ]

    for m in ActiveMemberIterator(members):
        print(f"名前: {m.name}")