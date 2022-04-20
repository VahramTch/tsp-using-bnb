graph={ "a" : ["b"],
        "b" : ["a","c"],
        "c" : ["b","j", "d"],
        "d" : ["c","e"],
        "e" : ["d","f"],
        "f" : ["e","g"],
        "g" : ["f","h"],
        "h" : ["g","i"],
        "j" : ["c","i"],
        "i" : ["h","k","j"],
        "k" : ["i","l"],
        "l" : ["k"],   
         }
print("graph:",graph)
x=[]
y=[]

for i in graph:
    l=graph[i]
    x.append(i)
    for p in graph[i]:
        if p in x:graph[i].remove(p)

print("The initial graph was simplified to:",graph)    

bestlimit=[]
limit=[]
closed=[]
search=["a"]
counter=1

while True:
    if len(search)==0:
        print("The cost of the shortest path is:",min(bestlimit))
        break
    else:
        x=search[0]
        if x in closed:
            continue
        
        if x == "abcdefghikl" or x=="abcjikl":
            print("FINAL STATE",limit[-1])
            bestlimit.append(limit[-1])
            search.remove(x)
            s=0
            if(len(search)==0):
                continue
            for i in range(len(search[0])):
                s+=1
            limit[-1]=s
            print(limit)
            counter=s
            continue

        closed.append(x)
        limit.append(counter)

        p=search[0]
        k=graph[p[-1]]
        print(counter,"~~~~~~~~~~~~~~~~~")
        print("microscope:",p)
        print("k:",k)
        if len(k)==1:       
            search[0]+=k[0]
        else:
            search.append(search[0])
            search[0]+=k[0]
            search[1]+=k[1]
            
        print("search set:",search)
        print("closed set:",closed)
        counter+=1
    
