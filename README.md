# Basic Access Controls API
# by Daniel Pattathil (dp865) and Rafay Safi (rzs7)

This project just lets you set up users, objects, and groups for the users/objects

It follows the basic assignment provided by PK's CS 419 Computer Security Class.

# Design

This project follows the basic concept of storing information related to access in local text files and using those files to validate access checks.

# Usage

python3 access.py [API call flag] [values]

[API call flag] can be any of the operations supported:
-au is to AddUser ex) -au username password
-a is to Authenticate ex) -a username password
-autg is to AddUserToGroup ex) -autg username groupname
-aotg is to AddObjectToGroup ex) -aotg objectname groupname
-aa is to AddAccess ex) -aa operation user-groupname <object-groupname>
-ca is to CanAccess ex) -cu operation  username <objectname>

# Testing 

Used a good bit of manual testing to make sure errors were provided in incorrec$

# Example workflow 

$ python3 access.py -au daniel 1234
$ python3 access.py -au rafay 1234
$ python3 access.py -a rafay 1234
Success
$ python3 access.py -a daniel 1234
Success
$ python3 access.py -autg project daniel
Traceback (most recent call last):
  File "access.py", line 113, in <module>
    raise LookupError
LookupError
$ python3 access.py -autg daniel project
daniel
$ python3 access.py -autg rafay project
['daniel', 'rafay']
$ python3 access.py -aotg laptop backpack
laptop
$ python3 access.py -aotg pen backpack
['laptop', 'pen']
$ python3 access.py -aa use project backpack
['project']
['backpack']
$ python3 access.py -ca use rafay laptop
Can Access
$ python3 access.py -ca use rafay tv
Traceback (most recent call last):
  File "access.py", line 212, in <module>
    raise LookupError
LookupError
$ python3 access.py -ca use daniel pen
Can Access
