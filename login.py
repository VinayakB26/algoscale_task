# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:24:05 2019

@author: Vinayak
"""

import os 
import getpass
import streaming_tweets

tweets_list=[]
if ('Users' not in os.listdir(os.getcwd())):
    os.mkdir('Users')
choice=input('1. Login \n2. Sign Up\n')

def signup():
    user=input('Username:')
    os.mkdir('Users/'+user)
    password=getpass.getpass('Password:')
    f=open('Users/'+user+'/Password','w+')
    f.write(password)
    f.close()
    return 1,user
    

if(choice=='1'):
    user=input('Username:')
    user_dir=os.listdir('Users')
    if (user in user_dir):
        while(1):
            password=getpass.getpass('Password:')
            f=open('Users/'+user+'/Password','r')
            check_pass=f.read()
            if (password==check_pass):
                f.close()
                streaming_tweets.main(user)
                break
            else:
                print('incorrect password, enter again :(')
        
    else:
        if (len(os.listdir('Users'))==10):
            print('User limit exceeded')
        else:
            print('User not present, please sign up')
            sign_up,user=signup()
            if (sign_up==1):
                print('sign up sucessful, Enjoy!')
                streaming_tweets.main(user))
if (choice=='2'):
        if (len(os.listdir('Users'))==10):
            print('User limit exceeded')
        else:
            print('User not present, please sign up')
            sign_up,user=signup()
            if (sign_up==1):
                print('sign up sucessful, Enjoy!')
                streaming_tweets.main(user)