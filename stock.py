import os
fp=open("test.txt","r+")
items=[]
itr=1000
for i in fp.readlines():
	li=i.split('\t');
	dicts={}
	dicts["code"]=li[0]
	dicts["name"]=li[1]
	dicts["price"]=li[2]
	dicts["quan"]=li[3]
	dicts["manuf"]=li[4]
	dicts["expiry"]=li[5]
	items.append(dicts)
fp.close()
def viewdetails(stock):
	print('*'*75)
	print('CODE|\tNAME|\tPRICE|\t\tQUAN|\t\tMANUF|\t\tEXP.DATE|')
	print('*'*75)
	for each in stock:
		print(str(each['code'])+'\t'+each['name']+'\tRS.'+str(each['price'])+'\t '+str(each['quan'])+'\t\t'+each['manuf']+'\t\t'+each['expiry'])
		print('*'*75)
def insertitems(stock):
	items={}
	global itr
	items['code']=int(itr)
	itr+=10
	items['name']=input('ENTER THE PRODUCT NAME:')
	items['price']=float(input('ENTER THE COST:'))
	items['quan']=int(input('ENTER THE QUANTITY:'))
	items['manuf']=input('ENTER THE MANUFACTURER:')
	items['expiry']=input('ENTER THE EXPIRY DATE:')
	stock.append(items)
	os.remove('test.txt')
	fp=open("test.txt","w+")
	fp.write((str(items['code']))+'\t'+items['name']+'\tRS.'+str((items['price']))+'\t '+str(items['quan'])+'\t'+items['manuf']+'\t'+items['expiry']+'\n')
	fp.close()
def delete(stock):
	ch=input('ENTER THE PRODUCT NAME YOU WANT TO DELETE:')
	loop=0
	for each in stock:
		if ch == each['name']:
			stock.pop(loop)
		else:
			os.remove('test.txt')
			fp=open("test.txt","w+")
			fp.write((each['code'])+'\t'+each['name']+'\tRS.'+(each['price'])+'\t '+(each['quan'])+'\t'+each['manuf']+'\t'+each['expiry']+'\n')
			fp.close()
			loop+=1
def update(stock):
	ch=input('ENTER THE PRODUCT NAME YOU WANT TO UPDATE:')
	for each in stock:
		if ch == each['name']:
			print('1.NAME 2.PRICE 3.QUAN 4.MANUF 5.EXP.DATE')
			choice=int(input('ENTER THE COLUMN YOU WANT TO UPDATE:'))
			if choice == 1:
				each['name']=input('ENTER THE NAME:')
			elif choice == 2:
				each['price']=input('ENTER THE PRICE:')
			elif choice == 3:
				each['quan']=input('ENTER THE QUANTITY:')
			elif choice == 4:
				each['manuf']=input('ENTER THE MANUFACTURER:')
			elif choice == 5:
				each['expiry']=input('ENTER THE EXPIRY DATE:')
			os.remove('test.txt')
			fp=open("test.txt","w+")
			fp.write((each['code'])+'\t'+each['name']+'\tRS.'+(each['price'])+'\t '+(each['quan'])+'\t'+each['manuf']+'\t'+each['expiry']+'\n')
			fp.close()
		else:
			os.remove('test.txt')
			fp=open("test.txt","w+")
			fp.write((each['code'])+'\t'+each['name']+'\tRS.'+(each['price'])+'\t '+(each['quan'])+'\t'+each['manuf']+'\t'+each['expiry']+'\n')
			fp.close()
print('*'*75)
num=1
while num>0:
	print('1.VIEW  2.DELETE 3.UPDATE 4.INSERT')
	num=int(input('enter the choice:'))
	if num == 1:
		viewdetails(items)
	elif num == 2:
		delete(items)
	elif num == 3:
		update(items)
	elif num == 4:
		insertitems(items)
print('*'*75)