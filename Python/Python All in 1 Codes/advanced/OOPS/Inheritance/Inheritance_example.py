class twenty:
    def __init__(self, name, age,month_salary):
        self.name = name
        self.age = age
        self.month_salary = month_salary

    def annual_salary_twenty(self):
        total_amount_twenty = self.month_salary * 12
        return f" Name:{self.name} and age {self.age} and his salary in 2020 is: {total_amount_twenty} PA"

class twenty_one(twenty):
    def annual_salary_twenty_one(self, percentage):
        increament = (self.month_salary * percentage ) // 100
        new_salary = self.month_salary + increament
        total_amount_twenty_one = new_salary * 12
        return f" Name:{self.name} and age {self.age} and his new salary in 2021 after revision is: {total_amount_twenty_one} PA"

obj = twenty('Surendra Kumar A',26, 38000)
obj2 = twenty_one('Surendra Kumar A',27, 38000)

print(obj.annual_salary_twenty())
print(obj2.annual_salary_twenty_one(15))



