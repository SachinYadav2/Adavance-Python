
# Hm accses kr pa rhe h Admin ke python file ke throw admin ke sub module ko
# uske function ko accesed kr pa rhe  



# import Admin.service
# Admin.service.admin_service()


# import Admin.product
# Admin.product.admin_product()    

# import Admin.Common.header

# Admin.Common.header.admin_service_header()


# 3

# import Tech.work
# Tech.work.tech_work()


# Abhi tak hm Module ko access kr rhe

# from Admin import service

# service.admin_service()

# from Admin import product

# product.admin_product()


# 4

# Sub Package ko use kr rhe and module ko

# from Admin.Common import header
# header.admin_service_header()


# 5
# ab ham module ke inside ke bat krenge ke varibale and method ko kaise accese kiya ja skta


# from Admin.service import admin_service
# admin_service()

# from User.request import  user_request
# user_request()


# 6 
# ab hm _all_ ka use krenge


# from Admin import service , product
# service.admin_service()
# product.admin_product()


# Ese hm package me use nhi kr skte h basically
# Solu h __ALL__  variable
# Ab hmara error nhi aega because hmne __init__ file ke under code dal diay h
from Admin import *
product.admin_product()


# 7 Sibling Concept
# Teck ke work Module me jo h



