#import pywhatkit as kt
#target='Ed Sheeran'
#kt.search(target)
import pymysql as p
conn=p.connect(host='localhost',user='root',password='vishesh14',database='The_Vimsical')
cur=conn.cursor()
'''
cmd=' drop table Night'
cur.execute(cmd)
cmd=' drop table Energize'
cur.execute(cmd)
cmd=' drop table Dance'
cur.execute(cmd)
cmd=' drop table Favourites'
cur.execute(cmd)
'''
cmd=' create table if not exists Night (Serial int primary key, Name varchar(60), Artists varchar(50),file varchar(70))'
cur.execute(cmd)
cmd=' create table if not exists Favourites  (Serial int primary key, Name varchar(60), Artists varchar(50), file varchar(70))'
cur.execute(cmd)
cmd=' create table if not exists Energize (Serial int primary key, Name varchar(60), Artists varchar(50), file varchar(70))'
cur.execute(cmd)
cmd=' create table if not exists Dance (Serial int primary key, Name varchar(60), Artists varchar(50), file varchar(70))'
cur.execute(cmd)

# cmd=' START TRANSACTION'
# cur.execute(cmd)

# cmd=' savepoint a'
# cur.execute(cmd)

# cmd=' Alter table Energize drop file'
# cur.execute(cmd)

import os 
for word in ['Favourites','Night','Dance','Energize']: 
    path = 'C:/Users/aggar/Music/The Vimsical/Musics/{}'.format(word)
    i=1
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                print(song)
                sr=i
                nm=song[0:-4]
                #nm=song[0:-4]
                file=song
                from windows_metadata import WindowsAttributes
                attr = WindowsAttributes('C:/Users/aggar/Music/The Vimsical/Musics/{}/{}'.format(word,file))
                title = attr["Title"]
                title = attr.title 
                author = attr.contributing_artists
                cmd='insert into {} values ({},"{}","{}","{}")'.format(word,sr,nm,author,file)
                # print(title,author)
                # print(cmd)
                cur.execute(cmd)
                conn.commit()
                i+=1
                
