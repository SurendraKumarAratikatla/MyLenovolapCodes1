import monkey_pactching_list_1

class b(monkey_pactching_list_1):
    def func(self):
        re = self.li
        return re

obj = b()
print(obj.func())