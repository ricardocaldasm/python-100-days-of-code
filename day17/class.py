# atribute is a variable associated with an object
class User:
    def __init__(self, user_id, username) -> None:  # __init__: initialize atributes | None: to allow static type checking (cannot return a int)
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # pass -> pass to the next line (like '...')
    
    def follow(self, user): # method
        user.followers += 1 # the user who we're following, their follower count goes up by one
        self.following += 1 # our own following count goes up by one


user_1 = User("001", "Ricardo")
# user_1.id = "001"
# user_1.username = "Ricardo"
print(user_1)

user_2 = User("002","Gaia")
# user_2.id = "002"
# user_2.username = "Gaia"
print(user_2.id, user_2.username, user_2.followers)

user_1.follow(user_2) #user_1: object | follow(): method
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

