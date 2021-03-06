def crude_match(str1,str2):
    m=0
    for n in range(len(str1)):
        while m <= len(str2):
            if str1[n]==str1[m]:
                n += 1
                m += 1
                if m==len(str2):
                    return n-m
            else:
                break

def kmp(str1,str2):
    i=0
    j=0
    n=len(str1)
    m=len(str2)
    pnext=my_bullshit_get_next(str2)
    while j<n and i<m:
        if i==-1 or str1[j]==str2[i]:
            j=j+1
            i=i+1
        else:
            i=pnext[i]
        if i==m:
            return j-i
    return False



def my_bullshit_get_next(strs):
    total_length=len(strs)
    next_list=[]
    temp=[]
    for i in range(1,total_length+1):
        for j in range(i):
            temp.append(strs[j])
        next_list.append(my_bullshit_get_mutual_value(temp))
        temp=[]
    i=len(next_list)-1
    while i>0:
        next_list[i]=next_list[i-1]
        i=i-1
    next_list[0]=-1
    return next_list





def my_bullshit_get_mutual_value(list_strs):
    prevs=set()
    rears=set()
    maxs=0
    for i in range(1,len(list_strs)+1):
        rears.add(''.join(list_strs[i:]))
    for i in range(1,len(list_strs)):
        prevs.add(''.join(list_strs[:i]))
    alu=list(prevs & rears)
    for elem in alu:
        if maxs<len(elem):
            maxs=len(elem)
    return maxs

def get_next(p):
    i,k,m=0,-1,len(p)
    pnext=[-1]*m
    while i<m-1:
        if k==-1 or p[i]==p[k]:
            i,k=i+1,k+1
            if p[i]==p[k]:
                pnext[i]=pnext[k]
            else:
                pnext[i]=k
        else:
            k=pnext[k]
    return pnext



strs2="ABCDABD"
strs1="BBC ABCDAB ABCDABCDABDE"

print(kmp(strs1,strs2))
