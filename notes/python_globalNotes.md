<!-- I'm a note! -->

list uses []
tuple uses ()
dictionary uses {}

<!-- Friday Jul 8th -->

To copy a list, do you need [:]? Would setting the variable value to words not accomplish the same thing?
# Making a copy of a list
copy_of_words = words[:]

# useful syntax for ending while loops:

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")

?? Exiting the function: Reaching a return statement always means "EXIT THIS FUNCTION NOW" whether or not there is more code. Any remaining code will not be run. ??

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

