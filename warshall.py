import time
def get_information():
    n = input("Enter your set :").split(",")
    matris1 = []
    
    for j in n:
        for i in range(len(n)):
            matris1.append(j + n[i])
        
    helper_matris = matris1 + []
    m = int(input("Enter the size of Relation : "))
    R = set({})
    help_list1 = []
    for i in range(m):
        zoj = tuple(input(f"Enter relation {i+1}: "))
        help_list1.append(zoj)
        R |= set(help_list1)
    for i in R:
        z = i[0]+i[1]
        for j in range(len(matris1)):
            if matris1[j] == z:
                matris1[j] = matris1[j].replace(z,"1")

    for i in range(len(matris1)):
        if matris1[i] != "1":
            matris1[i] = matris1[i].replace(matris1[i], "0")
        matris1[i] = int(matris1[i]) 

    matris2 = []
    def matris(n,b, matris1, matris2, a=0):
        matris2.append(matris1[a:b])
        if len(matris2) < n:
            matris(n,b+n, matris1, matris2, b)
        return matris2
    return matris(len(n),len(n), matris1, matris2), helper_matris, R


def varshal(matris:list, n:list):
    W = matris + []
    print("w0:")
    for y in W:
        print(y)
    print()

    for i in range(len(W)):
        I = []
        J = []
        for j in range(len(W)):
            if W[j][i] == 1:
                I.append(j)
            if W[i][j] == 1:
                J.append(j)
        for k in I:
            for h in J:
                W[k][h] = 1       
        help_list2 = []
        help_list3 = []     
        for z in W:
            for s in z:
                help_list2.append(s)

        for t in range(len(help_list2)):
            if help_list2[t] == 1:
                help_list3.append(tuple(n[t]))
        
        print(f"w{i+1}:") 
        for e in W:
            print(e)
        print()
        print(f"w{i+1} = {set(help_list3)}")
        print()


matris, n, R= get_information()
print("w0 = ",R,"\n")
varshal(matris, n)

time.sleep(30)
