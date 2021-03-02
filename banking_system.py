import mysql.connector 

mydb=mysql.connector.connect(host='localhost',user='root',passwd='tarun9199',auth_plugin='mysql_native_password',database ='BankDB')

mycursor=mydb.cursor()
#mycursor.execute('create database BankDB')

def Menu():
    print('*'*165)
    print('*'*165,'\n')
    print('Main Menu'.center(165),'\n')
    print('1. Insert Record(s)'.center(165))
    print('2. Display Records as per Account Number'.center(165))
    print('   a. Sorted as per Account Number'.center(165))
    print('   b. Sorted as per Name'.center(165))
    print('   c. Sorted as per Customer Balance'.center(165))
    print('3. Search Records as per Account Number'.center(165))
    print('4. Update Record'.center(165))
    print('5. Delete Record'.center(165))
    print('6. Transaction'.center(165))
    print('   a. Credit into Account'.center(165))
    print('   b. Debit/Withdrawl from Account'.center(165))
    print('7. Exit'.center(165),'\n')
    print('*'*165)
    print('*'*165)

def Menu_Sort():
    print('a. Sorted as per Account Number'.center(165))
    print('b. Sorted as per Name'.center(165))
    print('c. Sorted as per Customer Balance'.center(165))
    print('d. Back'.center(165))

def Menu_Transaction():
    print('a. Credit into Account'.center(165))
    print('b. Debit/Withdrawl from Account'.center(165))
    print('c. Back'.center(165)) 

def Create():
    try:
        mycursor.execute('create table Bank(Acc_No bigint, Name varchar(15), Mobile bigint, Email varchar(50), Address varchar(30), City varchar(15), Country varchar(15), Balance float')
        print('Table created.')
        Insert()
    except:
        print('Table already exists.')
        Insert()

def Insert():
    while True:
        acc=int(input('Enter Account Number:'))
        name=input('Enter Name:')
        mobile=int(input('Enter Mobile Number:'))
        email=input('Enter Email:')
        address=input('Enter Address:')
        city=input('Enter City:')
        country=input('Enter Country:')
        balance=float(input('Enter Balance:'))
        cmd = 'insert into Bank values(%s,%s,%s,%s,%s,%s,%s,%s)'
        rec = [acc, name.upper(), mobile, email.lower(), address.upper(), city.upper(), country.upper(), balance]
        mycursor.execute(cmd,rec)
        mydb.commit()
        ans=input('Do you want to enter another record (Y/N):')
        if ans=='N' or ans=='n':
            break

def Display_Sort_Acc():
    try:
        mycursor.execute('select * from Bank order by Acc_No')
        A=mycursor.fetchall()
        print('='*165)
        space='%14s %15s %18s %18s %19s %18s %22s %20s'
        print(space % ('Acc_No', 'Name', 'Mobile', 'Email', 'Address', 'City', 'Country', 'Balance'))
        print('='*165)
        for i in A:
            for j in i:
                print('%15s' % j, end='    ')
            print()
        print('='*165)
    except:
        print("Table doesn't exist.")

def Display_Sort_Name():
    try:
        mycursor.execute('select * from Bank order by Customer_Name')
        A=mycursor.fetchall()
        print('='*165)
        space='%18s %18s %18s %18s %18s %18s %18s %18s'
        print(space % ('Acc_No', 'Name', 'Mobile', 'Email', 'Address', 'City', 'Country', 'Balance'))
        print('='*165)
        for i in A:
            for j in i:
                print('%19s' % j, end=' ')
            print()
        print('='*165)
    except:
        print("Table doesn't exist.")

def Display_Sort_Balance():
    try:
        mycursor.execute('select * from Bank order by Balance')
        A=mycursor.fetchall()
        print('='*165)
        space='%18s %18s %18s %18s %18s %18s %18s %18s'
        print(space % ('Acc_No', 'Name', 'Mobile', 'Email', 'Address', 'City', 'Country', 'Balance'))
        print('='*165)
        for i in A:
            for j in i:
                print('%17s' % j, end=' ')
            print()
        print('='*165)
    except:
        print("Table doesn't exist.")

def Search():
    try:
        mycursor.execute('select * from Bank')
        A=mycursor.fetchall()
        ans=int(input('Enter the Account Number to be searched:'))
        for i in A:
            i=list(i)
            if i[0]==ans:
                print('='*165)
                space='%18s %18s %18s %18s %18s %18s %18s %18s'
                print(space % ('Acc_No', 'Name', 'Mobile', 'Email', 'Address', 'City', 'Country', 'Balance'))
                print('='*165)       
                for j in i:
                    print('%17s' % j, end=' ')
                print()
                break
        else:
            print('Record not found.')
    except:
        print("Table doesn't exist.")
    
def Update():
    try:
        mycursor.execute('select * from Bank')
        A=mycursor.fetchall()
        ans=int(input('Enter the Account Number whose details to be changed:'))
        for i in A:
            i=list(i)
            if i[0]==ans:
                
                ans1=input('Change Name?(Y/N):')
                if ans1=='Y' or ans1=='y':
                    i[1]=input('Enter Name:')
                    i[1]=i[1].upper()

                ans1=input('Change Mobile?(Y/N):')
                if ans1=='Y' or ans1=='y':
                    i[2]=int(input('Enter Mobile:'))

                ans1=input('Change Email?(Y/N):')
                if ans1=='Y' or ans1=='y':
                    i[3]=input('Enter Email:')
                    i[3]=i[3].lower()

                ans1=input('Change Address?(Y/N):')
                if ans1=='Y' or ans1=='y':
                    i[4]=input('Enter Address:')
                    i[4]=i[4].upper()

                ans1=input('Change City?(Y/N):')
                if ans1=='Y' or ans1=='y':
                    i[5]=input('Enter City:')
                    i[5]=i[5].upper()

                ans1=input('Change Country?(Y/N):')
                if ans1=='Y' or ans1=='y':
                    i[6]=input('Enter Country:')
                    i[6]=i[6].upper()

                ans1=input('Change Balance?(Y/N):')
                if ans1=='Y' or ans1=='y':
                    i[7]=float(input('Enter Balance:'))

                cmd='update Bank set Name=%s, Mobile=%s, Email=%s, Address=%s, City=%s, Country=%s, Balance=%s where Acc_No=%s'
                val=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print('Account updated.')
                break
        else:
            print('Record not found.')
    except:
        print("Table doesn't exist.")
        
def Delete():
    try:
        mycursor.execute('select * from Bank')
        A=mycursor.fetchall()
        ans=int(input('Enter the Account Number to be deleted:'))
        for i in A:
            i=list(i)
            if i[0]==ans:
                cmd='delete from Bank where Acc_No=%s'
                val=(i[0],)
                mycursor.execute(cmd, val)
                mydb.commit()
                print('Account deleted.')
                break
        else:
            print('Record not found.')
    except:
        print("Table doesn't exist.")

def Credit():
    try:
        mycursor.execute('select * from Bank')
        A=mycursor.fetchall()
        ans=int(input('Enter the Account Number in which the amount is to be credited:'))
        for i in A:
            i=list(i)
            if i[0]==ans:
                ans1=float(input('Enter the amount to be credited:'))
                i[7]+=ans1
                cmd='update Bank set Balance=%s where Acc_No=%s'
                val=(i[7],i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print('Amount is credited.')
                break
        else:
            print('Record not found.')
    except:
        print("Table doesn't exist.")

def Debit():
    try:
        mycursor.execute('select * from Bank')
        A=mycursor.fetchall()
        print('Note: Amount can only be debited if minimum balance of Rs 1000 exists after transaction.')
        ans=int(input('Enter the Account Number from which the amount is to be debited:'))
        for i in A:
            i=list(i)
            if i[0]==ans:
                ans1=float(input('Enter the amount to be debited:'))
                if i[7]-ans1>=1000:
                    i[7]-=ans1
                    cmd='update Bank set Balance=%s where Acc_No=%s'
                    val=(i[7],i[0])
                    mycursor.execute(cmd, val)
                    mydb.commit()
                    print('Amount is debited.')
                    break
                else:
                    print("Amount can't be debited due to minimum balance.")
                    break
        else:
            print('Record not found.')
    except:
        print("Table doesn't exist.")

while True:
    Menu()
    ans=input('Enter your choice:')
    if ans=='1':
        Create()
    elif ans=='2':
        while True:
            Menu_Sort()
            ans1=input('Enter your choice (a/b/c/d):')
            if ans1=='A' or ans1=='a':
                Display_Sort_Acc()
            elif ans1=='B' or ans1=='b':
                Display_Sort_Name()
            elif ans1=='C' or ans1=='c':
                Display_Sort_Balance()
            elif ans1=='D' or ans1=='d':
                print('Back to the Main Menu')
                break
            else:
                print('Invalid choice')
    elif ans=='3':
        Search()
    elif ans=='4':
        Update()
    elif ans=='5':
        Delete()
    elif ans=='6':
        while True:
            Menu_Transaction()
            ans1=input('Enter your choice (a/b/c):')
            if ans1=='A' or ans1=='a':
                Credit()
            elif ans1=='B' or ans1=='b':
                Debit()
            elif ans1=='C' or ans1=='c':
                print('Back to the Main Menu')
                break
            else:
                print('Invalid choice')
    elif ans=='7':
        print('Exiting...')
        break
    else:
        print('Invalid choice')