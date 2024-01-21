import pickle as p 
import random

def add():
    f=open("Sub.dat","+ab")

    n=int(input("Enter no.of teachers to be added"))
    for i in range(n):
        l=[]
        name=input("Enter name")
        z=eval(input("Enter TT"))
        l+=[name]
        l+=[z]
        p.dump(l,f) 

    f.close()
    home()
def sub():
    f=open("Sub.dat","rb+")
    x=input("Enter name of the teacher absent")
    try:
        while True:
            d=p.load(f)
            if d[0]==x:
                q=[]
                for i in d[1]:
                    q.append(i)
    except:
        f.close()
    m=dict()
    c=[]
    for i in q:
        if i!=None:
            c+=[q.index(i)]


    f=open("Sub.dat","rb+")
    try:
        while True:
            d=p.load(f)
            for i in range(len(d[1])):
                if d[0]==x:
                    pass
                    
                else:
                    if d[1][i]==None and i in c:
                        m[i]=d[0]
    except:
        f.close()
    for i in range(len(c)):
        g=[]
        r=random.choice(c)
        
        h=m.keys()
        b=m.values()
        
        w=[]
        v=[]
        for i in h:
            v.append(i)
        for k in b:
            w.append(k)

        if r in h:
            s=v.index(r)
            q[r]+=w[s]
            c.remove(r)
    
    print(x,q)
    f.close()
    home()
def display():
    f=open("sub.dat","rb+")
    try:
        while True:
            d=p.load(f)
            print(d)
    except:
        f.close()
        home()
def home():
    e=int(input("1.add\n2.sub\n3.display\n4.Exit"))
    if e==1:
        add()
    elif e==2:
        sub()
    elif e==3:
        display()
    elif e==4:
        exit()
home()
        