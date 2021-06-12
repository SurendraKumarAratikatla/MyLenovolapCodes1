# s = {1,2,3,4,5}
# print(s)
# Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
# Months={"Jan","Feb","Mar"}
# Dates={21,22,17}
# print(Days)
# print(Months)
# print(Dates)

# adding an element

Days={"Mon","Tue","Wed","Thu","Fri","Sat"}

Days.add("Sun")
print(Days)

# removing an element

Days.discard('Sun')
print(Days)

Days.remove('Tue')
print(Days)

# Union of sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)

#Intersection of sets

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)

#Diffrence of sets

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays)


#Compare of sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)