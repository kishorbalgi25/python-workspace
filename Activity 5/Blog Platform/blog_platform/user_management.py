# User Management (users):
# i.      create_user(username, email): Accepts a username and email, creates a new user, and returns a user object.
# ii.      delete_user(user_id): Accepts a user ID, deletes the user, and returns a success message.

# User class:

class User:
    id = 1
    
    def __init__(self,username,email):
        self.id = __class__.id
        self.username = username
        self.email = email
        __class__.id+=1
        
# Users DB:
users = {}

# Create User:
def create_user(username, email):
    newuser = User(username,email)
    
    users.update({str(newuser.id) : newuser})
    
    print(users)
    
    return newuser

# Delete User:
def delete_user(user_id):
    if user_id not in users: 
        print(f"User not found with id {user_id}")
        return 
    userObj = users.pop(user_id)
    del userObj 
    
    print(f"User with id {user_id} deleted successfully")