
def snake(n,m):
    k = 1
    for y in range(m):
        if k % 2 == 0:
            for x in range(-n+1, 1, 1):
               print (x,y)
        else:
            for x in range(0, -n, -1):
                print (x,y)
        k+=1 

def around(n,m):
        start = 0
        for y in range(start,m):
            print(start,y)
        for x in range(start-1,-n,-1):
            print(x,m-1)
        for y in range(m-2,start,-1):
            print(-n+1,y)
        for x in range (-n+1,start+1):
            print(x,start)

    
# snake(5,3)
around(2,2)
