immutable_var = 1,2,"a","b",True,False,[1,2]
tuple_= immutable_var
print(tuple_)
#tuple_[3] = "c" - содержимое кортежных скобок не изменно
mutable_list = [1,2,"a","b",True,False,[1,2]]
print(mutable_list)
mutable_list[3] = "c"
print(mutable_list)