"""

"""
import copy
user = {
    "name": "vishwas",
    "age": 22,
    "email": "vp.msdos@gmail.com",
    "password": "tt"
}

sensitive = ["email", "password","tes"]
u1 = copy.copy(user)
for x in sensitive:
    if(x in user):
        user.pop(x)


print(user)
