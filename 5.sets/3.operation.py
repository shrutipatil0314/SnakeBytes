#|| operation on set ||

subject1 = { "dbms" ,"python" , "dsa" , "c++"}
subject2 = {"dsa", "python" ,"cyber","java"}
days = {"monday","tuesday","wednesday","thursday","friday","saturday","sunday"}
weekend ={"saturday","sunday" }
#intersection
common = subject1.intersection(subject2)
print(common)

#union
all = subject1.union(subject2)
print(all)

#difference
print("days in week",days.difference(weekend))

#symmetric difference
print("weekend" ,days.symmetric_difference(weekend))



