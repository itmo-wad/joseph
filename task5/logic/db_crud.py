from logic import mongo as m

def userOneInsert(user):
    return m.db.user.insert(user)

def findOneUser(user):
    return m.db.user.find_one(user)

def findByEmail(email):
    return m.db.user.find_one({'mail': email})
