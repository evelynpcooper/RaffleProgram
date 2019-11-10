# Evelyn Cooper
# Project started on Nov 7, 2019
# Hours:
# 11/9 8:30p

import pickle
# import test

#manual 'settings' switch
global export, verbose
export=False
verbose=True

#import names from file
def importFile(filename: str):
  with open(filename) as file:
    users=file.read().splitlines()
  return users

#attach email domain 
def makeEmail(user):
  email=user+'@zagmail.gonzaga.edu'
  return email

#export emails to text file
def exportFile(users):
  global verbose
  export=open('export','a+') 
  for user in users:
    email=user+'@zagmail.gonzaga.edu'
    export.write(email)
    export.write('\n')
  export.close()
  if verbose: print('emails exported to file\n')

#can store account info in file using this
def save(info):
  global verbose 
  with open('saveFile','wb') as f:
    pickle.dump(info, f, pickle.HIGHEST_PROTOCOL)
  if verbose: print('saved info to saveFile\n')

def load():
  global verbose  
  if verbose: print('loaded info from saveFile')
  with open('saveFile','rb') as f:
    things=pickle.load(f)
    return things

#create accounts
class Student:
  def __init__(self, user, email):
    self.user=user
    self.email=email
    self.tickets=1

# def trackAttendance:
users=importFile(filename='attendance')
if verbose: print('usernames loaded\n')
userAccountInfo=[Student(user,makeEmail(user)) for user in users]
#can lookup info by username
s=dict(zip(users, userAccountInfo))
if verbose: print('accounts created\n')
save(s)
s=load()
print(s['ecooper'].tickets)

#add 1 ticket to each account if attended