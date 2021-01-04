import sqlite3 as sql

#Python API to insertdata into database tabel and retrive reference number
def writing_data(Cname,Ino,Idate,Pname,complaint):
    con = sql.connect('test.db')
    cur=con.cursor()
    print('connection established')
    cur.execute('insert into complaint_process(customer_name,Invoice_no,Invoice_date,Product_name,Naration_of_complaint) values(?,?,?,?,?)',(Cname,Ino,Idate,Pname,complaint))
    print('inserted sucessfully')
    con.commit()
    ref_no=cur.lastrowid
    print( ref_no)
    print('done')
    return ref_no

#Python API to retrive the status of customer complaint
def complaint_status(ref_no):
    con = sql.connect('test.db')
    cur=con.cursor()
    print('connection established')
    status = cur.execute('select status from complaint_process where Reference_no = ?',ref_no)
    print(status)
    status = cur.fetchone()
    return status