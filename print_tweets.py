# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:40:00 2019

@author: Vinayak
"""

import json
import psycopg2
import sys


connection = psycopg2.connect(user = "postgres",
                              password = "Thegraywiz",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "postgres")

cursor = connection.cursor()
cursor.execute('CREATE TABLE tweets(ID AUTOINCREMENT INT,Username VARCHAR, Date DATE, tweets VARCHAR);')
connection.commit()

def print_tweets(tweets_list,user):
    for items in tweets_list:
        items=json.loads(items)
        print(items['created_at'],end=' ')
        print(items['text'], end='\n')
    
    select_tweet=int(input('enter the number of the tweet to mark it fav'))

    items=json.loads(tweets_list[select_tweet])
    postgres_insert_query = """ INSERT INTO tweets (Username, Date, tweets) VALUES (%s,%s,%s)"""
    record_to_insert = ('user', items['created_at'],items['text'])
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    
    print( 'Records in the table for User')
    sql_select_query = """select * from tweets where  Username= %s"""
    cursor.execute(sql_select_query, (user, ))
    record = cursor.fetchone()
    print(record)
    
    user_id=int(input('Enter the id needs to be deleted'))
    
    sql_delete_query = """Delete from mobile where id = %s AND Username=%s"""
    cursor.execute(sql_delete_query, (user_id,user, ))
    connection.commit()
    
    print('Thanks')
    sys.exit(0)
    
       
    
