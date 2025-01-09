# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"


# print(format_name(input("What is your first name?"), input("what is your last name?")))


# use of return to break the function

def is_leap_year(year):
    if year %  4 == 0:
        if year % 100 == 0:  
            if year % 400 == 0:
                return True
              
            else:
                return False
        else:
            return True
    else:
        return False   
        
print(is_leap_year(2000) ) 
print(is_leap_year(2400) )      
print(is_leap_year(2100) )   
print(is_leap_year(2020) )     
print(is_leap_year(1989) )   