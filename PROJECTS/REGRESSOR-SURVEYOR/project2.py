import mysql.connector
import pandas as pd
import tkinter as tk 
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score
from matplotlib import pyplot as plt
        

def create_table():
    global root
    root.destroy()
    con=mysql.connector.connect(host='localhost',user='root',passwd='toor',database='bobmarley',port=8080)
    cur=con.cursor()
    root=tk.Tk()
    root.title('CREATE TABLE')
    root.configure(bg="#121212")
    t_name=tk.StringVar()
    name_label=tk.Label(root,text='Enter Table Name : ',bg='#ffa500',fg='#0000cc')
    name_label.grid(row=0,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=t_name,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=0,column=1)
    bye_button=tk.Button(root,text='Submit',command=root.destroy,bg='#ffa500',fg='#0000cc')#closes application
    bye_button.grid(row=1,column=1,sticky='EW')
    root.mainloop()

    create='CREATE TABLE {} (survey_id INT PRIMARY KEY AUTO_INCREMENT,price INT,company VARCHAR(25),review DECIMAL(2,1), km INT, fueltype int, hp INT, gearbox INT, cc INT,weight INT);'.format(t_name.get())
    cur.execute(create)
    con.commit()

def insert_data():
    global root
    root.destroy()
    con=mysql.connector.connect(host='localhost',user='root',passwd='toor',database='bobmarley',port=8080)
    cur=con.cursor()
    root=tk.Tk()
    root.configure(bg='black')
    root.title('INSERT DATA')
    t_name=tk.StringVar()
    name_label=tk.Label(root,text='Enter Table Name : ',bg='#ffa500',fg='#0000cc')
    name_label.grid(row=0,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=t_name,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=0,column=1)
    bye_button=tk.Button(root,text='Submit',command=root.destroy,bg='#ffa500',fg='#0000cc')#closes application
    bye_button.grid(row=1,column=1,sticky='EW')
    root.mainloop()

    root=tk.Tk()
    root.configure(bg='black')
    root.title('SURVEYOR')
    dfueltype={'diesel':0,'petrol':1}
    dgearbox={'manual':0,'automatic':1}
    price=tk.StringVar()
    company=tk.StringVar()
    review=tk.StringVar()
    km=tk.StringVar()
    fueltype=tk.StringVar()
    hp=tk.StringVar()
    gearbox=tk.StringVar()
    cc=tk.StringVar()
    weight=tk.StringVar()
        
    name_label=tk.Label(root,text='Price : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=0,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=price,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=0,column=1)

    name_label=tk.Label(root,text='Company : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=1,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=company,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=1,column=1)

    name_label=tk.Label(root,text='Review(/5) : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=2,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=review,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=2,column=1)

    name_label=tk.Label(root,text='Mileage : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=3,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=km,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=3,column=1)

    name_label=tk.Label(root,text='Fueltype(Diesel/Petrol) : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=4,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=fueltype,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=4,column=1)

    name_label=tk.Label(root,text='Brake Horsepower : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=5,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=hp,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=5,column=1)

    name_label=tk.Label(root,text='Gearbox(Manual/Automatic) : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=6,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=gearbox,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=6,column=1)

    name_label=tk.Label(root,text='CC of Engine : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=7,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=cc,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=7,column=1)

    name_label=tk.Label(root,text='Weight : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=8,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=weight,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=8,column=1)

    bye_button=tk.Button(root,text='Submit',command=root.destroy,bg='#ffa500',fg='#0000cc',width=10)#closes application
    bye_button.grid(row=8,column=2,sticky='EW')
    root.mainloop()

    fueltype=dfueltype[fueltype.get().lower()]
    gearbox=dgearbox[gearbox.get().lower()]
    add_user = "INSERT INTO {} (price,company,review,km,fueltype,hp,gearbox,cc,weight) VALUES({},'{}',{},{},{},{},{},{},{}) ;".format(t_name.get(),price.get(),company.get(),review.get(),km.get(),fueltype,hp.get(),gearbox,cc.get(),weight.get())
    cur.execute(add_user)
    con.commit()        

def fetch():
    global root
    root.destroy()
    con=mysql.connector.connect(host='localhost',user='root',passwd='toor',database='bobmarley',port=8080)
    cur=con.cursor()
    root=tk.Tk()
    root.title('FETCH')
    root.configure(bg='black')
    t_name=tk.StringVar()
    name_label=tk.Label(root,text='Enter Table Name : ',bg='#ffa500',fg='#0000cc')
    name_label.grid(row=0,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=t_name,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=0,column=1)
    bye_button=tk.Button(root,text='Submit',command=root.destroy,bg='#ffa500',fg='#0000cc')#closes application
    bye_button.grid(row=1,column=1,sticky='EW')
    root.mainloop()

    query='SELECT * FROM {}'.format(t_name.get())
    cur.execute(query)
    data=cur.fetchall()
    root=tk.Tk()
    root.title('FETCH')
    i=1 
    e=tk.Label(root,width=12,text='Survey_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=tk.Label(root,width=12,text='Price',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=tk.Label(root,width=12,text='Company',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=tk.Label(root,width=12,text='Review',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=tk.Label(root,width=12,text='Mileage',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=tk.Label(root,width=12,text='FuelType',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    e=tk.Label(root,width=12,text='Horsepower',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)
    e=tk.Label(root,width=12,text='Gearbox',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    e=tk.Label(root,width=12,text='Cubic Capacity',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=8)
    e=tk.Label(root,width=12,text='Weight',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=9)
    for cars in data: 
        for j in range(len(cars)):
            e = tk.Label(root, width=12, text=cars[j]) 
            e.grid(row=i, column=j) 
        i=i+1
    root.mainloop()
    '''
    cur.execute('SELECT * FROM {}'.format(t_name))
    data = cur.fetchall()
    print(data)
    '''

def predictor():
    global root
    root.destroy()
    con=mysql.connector.connect(host='localhost',user='root',passwd='toor',database='bobmarley',port=8080)
    cur=con.cursor()
    root=tk.Tk()
    root.title('PREDICTOR')
    root.configure(bg='black')
    t_name=tk.StringVar()
    name_label=tk.Label(root,text='Enter Table Name : ',bg='#ffa500',fg='#0000cc')
    name_label.grid(row=0,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=t_name,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=0,column=1)
    bye_button=tk.Button(root,text='Submit',command=root.destroy,bg='#ffa500',fg='#0000cc')#closes application
    bye_button.grid(row=1,column=1,sticky='EW')
    root.mainloop()

    query='Select * from {}'.format(t_name.get())
    data  =pd.read_sql(query,con)

    root=tk.Tk()
    root.title('REGRESSOR')
    root.configure(bg='black')

    X=data.drop(['survey_id','price','company','review'],axis='columns',inplace=False)
    Y=data['price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    model = linear_model.LinearRegression()
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    coeffi=model.coef_
    '''print('Coefficients:', coeffi)      
    print('Coefficient of determination (R^2): %.2f'
        % r2_score(Y_test, Y_pred))'''

    km=tk.IntVar()
    fuel=tk.StringVar()
    hp=tk.IntVar()
    gearbox=tk.StringVar()
    cc=tk.IntVar()
    weight=tk.IntVar()

    name_label=tk.Label(root,text='Mileage : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=0,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=km,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=0,column=1)

    name_label=tk.Label(root,text='Fueltype(Diesel/Petrol) : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=1,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=fuel,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=1,column=1)

    name_label=tk.Label(root,text='Brake Horsepower : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=2,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=hp,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=2,column=1)

    name_label=tk.Label(root,text='Gearbox(Manual/Automatic) : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=3,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=gearbox,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=3,column=1)

    name_label=tk.Label(root,text='CC of Engine : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=4,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=cc,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=4,column=1)

    name_label=tk.Label(root,text='Weight : ',bg='#ffa500',fg='#0000cc',width=30)
    name_label.grid(row=5,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=weight,bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=5,column=1)

    bye_button=tk.Button(root,text='Submit',command=root.destroy,bg='#ffa500',fg='#0000cc')#closes application
    bye_button.grid(row=6,column=1,sticky='EW')

    root.mainloop()
    
    dfueltype={'diesel':0,'petrol':1}
    dgearbox={'manual':0,'automatic':1}
    fuel=dfueltype[fuel.get().lower()]
    gearbox=dgearbox[gearbox.get().lower()]

    list=[km.get(),fuel,hp.get(),gearbox,cc.get(),weight.get()]
    price=0
    for a in range(6):
        price+=(list[a]*coeffi[a])

    root=tk.Tk()
    root.title('PREDICTED PRICE')
    root.configure(bg='black')
    name_label=tk.Label(root,text='PREDICTED PRICE : '+str(price/4),bg='#ffa500',fg='#0000cc')
    name_label.grid(row=0,column=0,padx=(0,100),pady=(0,100))#first row and column of input frame
    root.mainloop()

def stop():
    global running
    global root
    running=False
    root.destroy()


def graph():
    global root
    root.destroy()
    con=mysql.connector.connect(host='localhost',user='root',passwd='toor',database='bobmarley',port=8080)
    cur=con.cursor()
    root=tk.Tk()
    root.title('GRAPH')
    root.configure(bg='black')
    t_name=tk.StringVar()
    name_label=tk.Label(root,text='Enter Table Name :', bg='#ffa500',fg='#0000cc')
    name_label.grid(row=0,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=t_name, bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=0,column=1)
    bye_button=tk.Button(root,text='Submit',command=root.destroy, bg='#ffa500',fg='#0000cc')#closes application
    bye_button.grid(row=1,column=1,sticky='EW')
    root.mainloop()

    query='Select * from {}'.format(t_name.get())
    data  =pd.read_sql(query,con)

    root=tk.Tk()
    root.title('GRAPH')
    root.configure(bg='black')
    c_name=tk.StringVar()
    name_label=tk.Label(root,text='Enter Column Name : ', bg='#ffa500',fg='#0000cc')
    name_label.grid(row=0,column=0,padx=(0,10))#first row and column of input frame
    name_entry=tk.Entry(root,width=15,textvariable=c_name, bg='#ffa500',fg='#0000cc')
    name_entry.grid(row=0,column=1)
    bye_button=tk.Button(root,text='Submit',command=root.destroy, bg='#ffa500',fg='#0000cc')#closes application
    bye_button.grid(row=1,column=1,sticky='EW')
    root.mainloop()
    
    plt.scatter(data[c_name.get()], data['price'], c='red')
    plt.title('{} VS PRICE OF CAR'.format(c_name.get()))
    plt.xlabel(c_name.get())
    plt.ylabel('price')
    plt.show()
    

running=True
while running:
    root=tk.Tk()
    root.title('SURVEYOR')
    root.configure(bg="#121212")
    mybutton=tk.Button(root,text='CREATE TABLE',command=create_table,width=20,bg='#ffa500',fg='#0000cc').grid(column=0,row=0)
    mybutton=tk.Button(root,text='INSERT DATA',command=insert_data,width=20,bg='#ffa500',fg='#0000cc').grid(column=0,row=1)
    mybutton=tk.Button(root,text='FETCH DATA',command=fetch,width=20,bg='#ffa500',fg='#0000cc').grid(column=0,row=2)
    mybutton=tk.Button(root,text='PREDICT PRICE',command=predictor,width=20,bg='#ffa500',fg='#0000cc').grid(column=0,row=3)
    mybutton=tk.Button(root,text='GRAPH VERSUS PRICE',command=graph,width=20,bg='#ffa500',fg='#0000cc').grid(column=0,row=4)
    mybutton=tk.Button(root,text='EXIT',command=stop,width=20,bg='#ffa500',fg='#cc0000').grid(column=0,row=5)
    root.mainloop()
