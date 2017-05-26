import os
import sys
def help():
	print("create database database_name-->TO CREATE A DATABASE")
	print("use database_name-->TO USE THE DATABASE")
	print("select *from table_name-->TO VIEW THE CONTENTS OF TABLE")
	print("insert into table_name--->TO INSERT VALUES INTO TABLE")
	print("delete table table_name--->TO DELETE THE TABLE")
	print("delete database database_name--->TO DELETE THE DATABASE")
	print("show tables---->TO SHOW THE TABLES");
	print("show databases---->TO SHOW THE DATABASES");
	print("rename oldname as newname--->TO CHANGE THE FILENAME")
	print("quit----------->TO EXIT FROM MYSQL")
def insert():
	f_name=li[2]
	path=path_d+"/"+f_name+".txt"
	fr=open(path,"w+")
	str=input()
	fr.write(str)
	fr.close()	
	
def create():
	try:
		os.mkdir(li[2])
	except Exception:
		print("database already exists")
def create1():
	f_name=li[2]
	path=path_d+"/"+f_name+".txt"
	fr=open(path,"w+")
	fr.close()
def view():
	try:
		f_name=li[2]
		path=path_d+"/"+f_name+".txt"
		fr=open(path,"r+")
		str=fr.read(100000000000)
		print(str)
		fr.close()
	except Exception:
		print("FILE EMPTY")
def delete_table():
	try:
		f_name=li[2]
		os.remove(path_d+"/"+f_name+".txt")
	except Exception:
		print("file not exist")	
def delete_database():
	try:
	   	os.system("rm -rf "+(li[2]))
	except:
		print("Database does not exist")
def show_tables():
	tables=os.listdir(path_d)
	for i in range(len(tables)):
		print(tables[i].replace(".txt",""))
def show_databases():
	database=os.listdir()
	for i in database:
		print(i)
def rename():
	try:
		os.rename(path_d+"/"+li[1]+".txt",path_d+"/"+li[3]+".txt")
	except Exception:
		print("file not exist")	
os.chdir("DB/")
print("TYPE HELP TO KNOW THE FUNCTIONS")
while True:
	print("mysql>>",end="")
	li=list(map(str,input().lower().strip().split(" ")))
	if li[0]=="create" and li[1]=="database":
		if(len(li)==3):
			create()
		else:
			print("INVALID QUERY")
	elif li[0]=="help":
		if(len(li)==1):
			help()
		else:
			print("INVALID QUERY")
	elif li[0]=="quit":
		if(len(li)==1):
			exit(0)
		else:
			print("INVALID QUERY")
	elif li[0]=="use":
		if(len(li)==2):
			path_d=li[1]
		else:
			print("INVALID QUERY")
	elif li[0]=="create" and li[1]=="table":
		if(len(li)==3):
			create1()
		else:
			print("INVALID QUERY")
	elif li[0]=="select" and li[1]=="*from":
		if(len(li)==3):
			view()
		else:
			print("INVALID QUERY")
	elif li[0]=="insert" and li[1]=="into":
		if(len(li)==3):
			insert()
		else:
			print("INVALID QUERY")
	elif li[0]=="delete" and li[1]=="table":
		if(len(li)==3):
			delete_table()
		else:
			print("INVALID QUERY")
	elif li[0]=="delete" and li[1]=="database":
		if(len(li)==3):
			delete_database()
		else:
			print("INVALID QUERY")
	elif li[0]=="show" and li[1]=="tables":
		if(len(li)==2):
			show_tables()
		else:
			print("INVALID QUERY")
	elif li[0]=="show" and li[1]=="databases":
		if(len(li)==2):
			show_databases()
		else:
			print("INVALID QUERY")
	elif li[0]=="rename"and li[2]=="as":
		if(len(li)==4):
			rename()
		else:
			print("INVALID QUERY")

