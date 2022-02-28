'''#creat class
class User:
#to leave the class empty we can use "pass"
    pass
#PascalCase - camelCase - snake_case
user_1 = User()
#how create an attribute for that class 1.
user_1.id = "001"
user_1.username = "angela"

print(user_1.username)'''
#instagram
class User:
#initialize an object
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        #it doesn't make sense put it inside the definition
        self.followers = 0
        self.following = 0
#we want we follow each other , follower counter goes up, user decides to follow
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
