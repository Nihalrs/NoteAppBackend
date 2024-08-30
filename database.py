import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='nihal',
    password='temppass',
    database='noteapp'
)

mydb.autocommit=True
pool=mydb.cursor(dictionary=True)

#adding a new note to the "notes" table
def addnote(email,title,category,content,date):
    pool.execute('insert into notes(email,title,category,content,date) values(%s,%s,%s,%s,%s)',(email,title,category,content,date))
    return True

#deleting a note from "notes" table and putting it in the "deletednotes" table    
def delnote(noteid):
    pool.execute('select * from notes where noteid=%s',(noteid,))
    note=pool.fetchone()
    pool.execute('insert into deletednotes(noteid,email,title,category,content,date) values(%s,%s,%s,%s,%s,%s)',(note[0],note[1],note[2],note[3],note[4],note[5]))
    pool.execute('delete from notes where noteid=%s',(noteid,))
    return True

#restoring a note from "deletednotes" table and putting it again in "notes" table
def recovernote(noteid):
    pool.execute('select * from deletednotes where noteid=%s',(noteid,))
    note=pool.fetchone()
    pool.execute('insert into notes(noteid,email,title,category,content,date) values(%s,%s,%s,%s,%s,%s)',(note[0],note[1],note[2],note[3],note[4],note[5]))
    pool.execute('delete from deletednotes where noteid=%s',(noteid,))
    return True

#deleting a note permanently
def permenantdelnote(noteid):
    pool.execute('delete from deletednotes where noteid=%s',(noteid,))
    return True

#displaying a note in the homescreen    
def displayNote(email):
    #category = 0 is taken for all notes and category = 1,2,3... is taken for different category of notes
    pool.execute('select * from notes where email=%s',(email))
    return pool.fetchall()

#displaying deleted notes
def displayDelNote(email):
    #category = 0 is taken for all notes and category = 1,2,3... is taken for different category of notes
    pool.execute('select * from deletednotes where email=%s',(email))
    return pool.fetchall()