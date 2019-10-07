import argparse


######################################################################
#SETUP CODE
parser = argparse.ArgumentParser(description = "Deal with User Access Controls")
parser.add_argument('-au', help='To add users', action = "store_true")
parser.add_argument('-a', help='To authenticate a user', action = "store_true")
parser.add_argument('-autg', help='To add a user to a group', action = "store_true")
parser.add_argument('-aotg', help='To add an object to a group', action = "store_true")
parser.add_argument('-aa', help='To add access', action = "store_true")
parser.add_argument('-ca', help='To check for valid access', action = "store_true")
parser.add_argument('values', nargs = '*', help = 'Values to pass in with API access', type = str)
args = parser.parse_args()


#this code tries to read if there are stored users currently
try:
    f = open("users.txt")
    users = {}
    for line in f:
        line = line.strip()
        line = line.split(" ")
        users[line[0]] = line[1]
except FileNotFoundError:
    users = {}
    pass

#this code tries to read if there are stored user groups currently
try:
    f = open("groups.txt")
    groups = {}
    for line in f:
        line = line.strip()
        line = line.split(" ")
        groups[line[0]] = line[1:]
except FileNotFoundError:
    groups = {}
    pass

#this code tries to read if there are stored object groups currently
try:
    f = open("objects.txt")
    objs = {}
    for line in f:
        line = line.strip()
        line = line.split(" ")
        objs[line[0]] = line[1:]
except FileNotFoundError:
    objs = {}
    pass

#this code tries to read if there are stored operations currently
try:
    f = open("user_operations.txt")
    user_ops = {}
    for line in f:
        line = line.strip()
        line = line.split(" ")
        user_ops[line[0]] = line[1:]
except FileNotFoundError:
    user_ops = {}
    pass

#this code tries to read if there are stored operations currently
try:
    f = open("object_operations.txt")
    object_ops = {}
    for line in f:
        line = line.strip()
        line = line.split(" ")
        object_ops[line[0]] = line[1:]
except FileNotFoundError:
    object_ops = {}
    pass


######################################################################
#FUNCTIONAL CODE

#this code is to add users
if args.au:
    user = args.values
    if len(user) != 2:
        raise SyntaxError
    if user[0] in users:
        raise LookupError
    users[user[0]] = user[1]
    f = open("users.txt", "w")
    for user in users:
        f.write(user + " " + users[user] + "\n")

#this code is to authenticate users 
elif args.a:
    user = args.values
    if len(user) != 2:
        raise SyntaxError
    if user[0] not in users:
        raise LookupError
    elif user[1] != users[user[0]]:
        raise ValueError
    else:
        print("Success")

#this code is to add users to groups
elif args.autg:
    user_group = args.values
    if len(user_group) != 2:
        raise SyntaxError
    user = user_group[0]
    group = user_group[1]
    if user not in users:
        raise LookupError
    if group in groups:
        stored_users = groups[group]
        if user in stored_users:
            print(stored_users)
        else:
            stored_users.append(user)
            groups[group] = stored_users
            print(stored_users)
    else:
        groups[group] = [user]
        print(user)
    f = open("groups.txt", "w")
    for group in groups:
        f.write(group + " " + " ".join(groups[group]) + "\n")

#this code is to add objects to groups
elif args.aotg:
    object_group = args.values
    if len(object_group) != 2:
        raise SyntaxError
    obj = object_group[0]
    group = object_group[1]
    if group in objs:
        stored_objs = objs[group]
        if obj in stored_objs:
            print(stored_objs)
        else:
            stored_objs.append(obj)
            objs[group] = stored_objs
            print(stored_objs)
    else:
        objs[group] = [obj]
        print(obj)
    f = open("objects.txt", "w")
    for group in objs:
        f.write(group + " " + " ".join(objs[group]) + "\n")

#this code is to add access operations for users on certain objects
elif args.aa:
    operation = args.values
    if (len(operation) < 2) or (len(operation) > 3):
        raise SyntaxError
    op = operation[0]
    user_group = operation[1]
    if len(operation) > 2:
        object_group = operation[2]
    else:
        object_group = None
    if op in user_ops:
        stored_values = user_ops[op]
        if user_group not in stored_values:
            stored_values.append(user_group)
    else:
        stored_values = [user_group]
    print(stored_values)
    user_ops[op] = stored_values
    #if there is an object group parameter
    if object_group:
        if op in object_ops:
            stored_values = object_ops[op]
            if object_group not in stored_values:
                stored_values.append(object_group)
        else:
            stored_values = [object_group]
        print(stored_values)
        object_ops[op] = stored_values
    f = open("user_operations.txt", "w")
    for op in user_ops:
        f.write(op + " " + " ".join(user_ops[op]) + "\n")
    f = open("object_operations.txt", "w")
    for op in object_ops:
        f.write(op + " " + " ".join(object_ops[op]) + "\n")
    
#this code is to check if this access is allowable
elif args.ca:
    operation = args.values
    if (len(operation) < 2) or (len(operation) > 3):
        raise SyntaxError
    op = operation[0]
    user = operation[1]
    if len(operation) > 2:
        obj = operation[2]
    else:
        obj = None
    if op in user_ops:
        user_groups = user_ops[op]
        for group in user_groups:
            if user in groups[group]:
                if obj and op in object_ops:
                    object_groups = object_ops[op]
                    for ogroup in object_groups:
                        if obj in objs[ogroup]:
                            print("Can Access")
                            exit()
                elif not obj:
                    print("Can Access")
                    exit()
    #this error occurs if invalid operation, user, or object
    raise LookupError


