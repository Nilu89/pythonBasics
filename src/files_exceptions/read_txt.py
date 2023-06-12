# Chapter 10: Read files (txt)

# SYNTAX:
# with open(filepath_txt) as file_object:
#   file_content = file_object.read()
#   print(file_contents)

# OPTION 1
filepath_txt = "../../data/fruits.txt"
with open (filepath_txt) as file_object:
    file_contents = file_object.read()
    print('-----Now printing file contents-----')
    print(file_contents)
    print('----Reading line by line-------')

print('****************************************')
# OPTION 2
filepath_txt = "../../data/fruits.txt"
with open (filepath_txt) as file_object:
    for fruit in file_object:
        print(f"Current loop fruit: {fruit.strip()}")
