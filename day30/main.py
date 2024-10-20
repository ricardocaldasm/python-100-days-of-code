# Error: Try; Except; Else; Finally

# # File Not Found
# with open(r"day30\a_file.txt") as file:
#     file.read()

try:
    file = open(r"day30\a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:  # if try does not work, runs except
    file = open(r"day30\a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:  # if try works, runs else
    content = file.read()
    print(content)
finally:  # run no matter what happens
    file.close()
    print("File was closed.")
    # raise KeyError ("This is an error I made up.") #no matter what happens, raises an erro

height = float(input("height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)