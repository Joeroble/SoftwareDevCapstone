
# defines the main function
def main():
    complete_class_list = create_class_list()
    print_class_list(complete_class_list)

# creates the class list by asking for the number of classes, which is used to iterate in a while loop for the user to enter the names of each classes
#  and appends it to the list.
def create_class_list ():
    i = 0
    class_number = int(input('How many classes are you taking this semester?  '))
    class_list = []
    while i < class_number:
        class_name = input('Please enter the name of the class: ')
        class_list.append(class_name)
        i += 1
    return class_list
    
# prints the class list
def print_class_list (complete_list):
    for classes in complete_list:
        print(classes)
    
        
main()



        
