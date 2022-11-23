"""# Self is always required as the first argument
class check:
    def __init__(self):
        print("This is Constructor")
 
object = check()
print("Worked fine")"""


# Write Python3 code here
 
class this_is_class:
    def __init__(in_place_of_self):
        print("we have used another "
        "parameter name in place of self")
         
object = this_is_class()