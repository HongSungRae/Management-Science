from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
import math

window=Tk()
window.title('Dijkstra\'s Algorithm by 15113369 홍성래')
window.resizable(width=False, height=False)

### Variables ###

global N
N=[]
unsearchedNode=[]
entList=[]
infButtons=[]
chkList=[]
cbList=[]
D_v=0
D_w=0
p_v=0
c_w_v=0
i=0
inf=math.inf


### Functions ###
def infinite(v):
    '''
    value=infButtons.get(v)
    entList[value].insert(0,'∞')
    value=0
    pass
    '''
    #GUI에서 ent에 리트 속 button을 반환하는 방법을 모르겠습니다 ㅜㅜ
    #그래서 직접 입력으로 바꿨습니다.
    #소스코드에서 지워버리면 그만이지만 언젠가 해결하고싶어서 조금 남겨둡니다.
    

def func_chk():
    pass

def dij_algorithm():

    ##이하 입력숫자의 유효성 검사
    for i in range(len(entList)):
        if (entList[i].get()).isdigit()==True:
            pass
        elif (entList[i].get())=='∞' or (entList[i].get())=='inf' :
            pass
        else:
            messagebox.showinfo('ERROR','Only digits and ∞ are available')
        
    ##이하 starting node의 유효성 검사
    global count
    count=0
    for i in range(len(chkList)):
        count+=chkList[i].get()
        if chkList[i].get()==1:
            #N=[]
            global whatisStartingNode
            whatisStartingNode=0
            N.append(unsearchedNode[i])
            whatisStartingNode=i#반환하는 i값이 sort된 노드에서의 스타팅노드의 순서값
        else:
            pass
        
    if count!=1:
        messagebox.showinfo('Caution','You have to check only one node : Try again!')
        #N=[]
    else:
        pass
        #messagebox.showinfo('Dijkstra\'s Algorithm','Calculating...')
    
    
    ##이하 노드-노드사이거리를 2차원 리스트로 array를 사용않고 행렬로 표현함
    ##이 과정을 거치면 사용자가 입력한 노드와 거리가 행렬로 저장된다.
    global disMatrix
    disMatrix=[]
    global dijMatrix
    dijMatrix=[]
    global count_right
    count_right=-1
    for i in range(len(unsearchedNode)):
        a=[[]]
        disMatrix.extend(a)
        dijMatrix.extend(a)
        row_right=[]
        temp=[]
        for k in range(i+1):
            row_right.append(None)#(n,n)의 거리를 알 필요는 없다.
        for j in range(len(unsearchedNode)-i-1):
            count_right+=1
            if (entList[count_right].get()=='∞') or (entList[count_right].get()=='inf'):
                row_right.append(inf)
            else:
                row_right.append(int(entList[count_right].get()))
            disMatrix[i]=row_right
        for h in range(len(unsearchedNode)):
            temp.append(0)
        dijMatrix[i]=temp
        
    for l in range(len(unsearchedNode)):
        disMatrix[len(unsearchedNode)-1].append(None)

    for m in range(len(unsearchedNode)):
        for n in range(m):
            disMatrix[m][n]=disMatrix[n][m]

    
    ##이하 완성된 노드사이 거리행렬로 디엑스트라의 로직을 실행한다.
    if (count==1):
        label4.grid(row=len(unsearchedNode)+10,column=0,columnspan=2*len(unsearchedNode))
        label8=Label(window,text="<<<  Dijkstra\'s Algorithm  >>>")
        label8.grid(row=len(unsearchedNode)+11,column=0,columnspan=2*len(unsearchedNode))
        label10=Label(window,text="N")
        label10.grid(row=len(unsearchedNode)+12,column=0)
        global D_v
        global D_w

        for i in range(len(unsearchedNode)):
            label_colname=Label(window,text='D(%s)p(%s)'%(unsearchedNode[i],unsearchedNode[i]))
            label_colname.grid(row=len(unsearchedNode)+12,column=2*i+1)
            
            
            

        for j in range(len(unsearchedNode)):
            label_N=Label(window,text=N)
            label_N.grid(row=len(unsearchedNode)+13+j,column=0)
            if len(N)==1:
                for k in range(len(unsearchedNode)):
                    if disMatrix[whatisStartingNode][k]==None:
                        dijMatrix[j][k]=None
                    else:
                        dijMatrix[j][k]=disMatrix[whatisStartingNode][k]
                D_w=min(i for i in dijMatrix[j] if i is not None)
                whatisStartingNode=dijMatrix[j].index(D_w)
                N.append(unsearchedNode[whatisStartingNode])
                dijMatrix[j+1][whatisStartingNode]=None
                
            elif len(N)>1 and len(N)<len(unsearchedNode):
                for k in range(len(unsearchedNode)):
                    if dijMatrix[j-1][k]==None:
                        dijMatrix[j][k]=None
                    elif dijMatrix[j][k]==None:
                        pass
                    elif disMatrix[whatisStartingNode][k]==None:#넌 None일수가 있다.
                        pass
                    else:
                        D_v=min(dijMatrix[j-1][k],D_w+disMatrix[whatisStartingNode][k])
                        dijMatrix[j][k]=D_v
                D_w=min(i for i in dijMatrix[j] if i is not None)
                whatisStartingNode=dijMatrix[j].index(D_w)
                N.append(unsearchedNode[whatisStartingNode])
                dijMatrix[j+1][whatisStartingNode]=None
                        
                    
                    
            elif len(N)==len(unsearchedNode):
                for k in range(len(unsearchedNode)):
                    dijMatrix[j][k]=None
                
                
      

        
                
        ##이하 완성한 dijMatrix를 grid한다.    
        for i in range(len(unsearchedNode)):
            for j in range(len(unsearchedNode)):
                label=Label(window,text=dijMatrix[i][j])
                label.grid(row=len(unsearchedNode)+13+i,column=2*j+1)
                
            
            
            
        
    

##################################
######## Main Source Code ########
##################################


label1=Label(window,text="__Follow the pop-up instructions__"
             ,fg='red',font=('',20))
label4=Label(window,text="---------------------------------------------------------")
label5=Label(window,text="[[ To ]]")
label6=Label(window,text="[[From▼]]")
button1=Button(window,text='Search shortest path with Dijkstra\'s Algorithm',command=dij_algorithm)


label1.grid(row=0,column=0)


value=askinteger('Dijkstra\'s Algorithm','How much nodes are there?'
                 ,minvalue=1)

while (True):
    node=askstring('Dijkstra\'s Algorithm','What is node\'s name?%d/%d'
                   %(i+1,value))
    i+=1
    if (node in unsearchedNode):
        messagebox.showinfo('ERROR','You entered same name : Try again')
        i-=1
    else:
        unsearchedNode.append(node)

    if (len(unsearchedNode)==value):
        unsearchedNode.sort()##필요할까? 아마도 당장은 필요해보임
        break
    else:
        continue

label1.destroy()
label1_1=Label(window,text="Fill distance of each nodes in the blank"
             ,font=('',10))
label2=Label(window,text="If each nodes have no direct arc, write down <<inf>> or click <<∞>> button"
             ,fg='red',font=('',10))
label3=Label(window,text="Reference : distance \'0\' means \'No cost between nodes\'")




label4.grid(row=3,column=0,columnspan=2*len(unsearchedNode))
label5.grid(row=4,column=0,columnspan=2*len(unsearchedNode))

label6.grid(row=5,column=0)
label1_1.grid(row=0,column=0,columnspan=2*len(unsearchedNode)+2)
label2.grid(row=1,column=0,columnspan=2*len(unsearchedNode)+2)
label3.grid(row=2,column=0,columnspan=2*len(unsearchedNode)+2)

for i in range(len(unsearchedNode)):
    label_colname=Label(window,text=unsearchedNode[i])
    label_colname.grid(row=5,column=2*i+1)
    label_rowname=Label(window,text=unsearchedNode[i])
    label_rowname.grid(row=i+6,column=0)


##이하 행렬 입력 GUI

for j in range(len(unsearchedNode)):
    temp1=[]#temp는 순서대로 정렬해서 entList에 넣기위해 도입
    temp2=[]
    for k in range(len(unsearchedNode)-j-1):
        ent=Entry(window,width=5)
        ent.grid(row=j+6,column=2*len(unsearchedNode)-2*k-1)
        temp1.append(ent)
        button=Button(window,text='∞',bg='blue',fg='white',command=infinite)
        temp2.append(button)
        button.grid(row=j+6,column=2*len(unsearchedNode)-2*k)
    temp1.reverse()
    temp2.reverse()
    entList.extend(temp1)
    infButtons.extend(temp2)
    

for i in range(len(unsearchedNode)):
    chk=IntVar()
    cb=Checkbutton(window,text=unsearchedNode[i],variable=chk,command=func_chk)
    chkList.append(chk)
    cbList.append(cb)
    cbList[i].grid(row=len(unsearchedNode)+8,column=2*i+1)


        
label7=Label(window,text="▼Check only one starting node",fg='red')
label7.grid(row=len(unsearchedNode)+7,column=0,columnspan=2*len(unsearchedNode))
button1.grid(row=len(unsearchedNode)+9,column=0,columnspan=2*len(unsearchedNode))
    

window.mainloop()