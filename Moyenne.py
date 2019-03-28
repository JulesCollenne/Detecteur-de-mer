def Votes(Vector) :
    result=[0]*len(Vector[0])
    for i in range(len(Vector)):
        #print(Vector[i])
        for j in range(len(Vector[i])-1):
            #print(i,j,"=",Vector[i][j])
            result[j]+=Vector[i][j]
            
    for i in range(len(result)):
        if(result[i]<0):
            result[i]=-1
        else:
            result[i]=1
    return result