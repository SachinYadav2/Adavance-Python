# 1 method Call krna module ko
# import cal

# print(cal.var)


# print(cal.name)

# print(cal.add(12 ,32)) # 44


# 2 metthod to call module


# import cal as c

# print(c.var)


# print(c.name)

# print(c.add(12 ,32)) # 44


# 3 Method direct Module ke fun var etc ko import krna

# from cal import  var , add

# # accesed hota h ese

# print(add(1212 ,12312))

# print(var)



# 4 Method to import 

# from cal import add as sum

# print(sum(3213,343))

# 5 Method for all ko access

# from cal import *
# print(a)
# print(add(32323,2323))



# New Working

# Yha meri dono mudule me same name ke var fun h

# import first
# import second

# print(first.a)
# print(second.a)

# 6 Method

# from first import name ,a 
# from second import name , a


# # yha ab jo niche import hua hoga uski prioty high hoti h


# print(a)


# Another Method

# import first


# c = first.Myclass()

# c.name()

# d = first.Myschool()

# (d.show())


# 9 Method

# from first import Myclass , Myschool

# a = Myclass()
# a.name()

# b = Myschool()
# b.show()


# Seocnd Module ka use krke use krna basically


# import second
# import first


# c = first.Myclass()
# c.name()

# d = second.Myclass()
# d.name()




# Note hm from ke throw bhi kr skte h basically



# Same With both module inside basically

import first
import second
# first Wala acessed kr liya h 
c = first.Myclass()
c.name()


cl = second.Myclass()
cl.name()

