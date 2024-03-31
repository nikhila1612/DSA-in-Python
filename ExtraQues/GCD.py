def findHCF(n1,n2):
    hcf=1
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf

print(findHCF(36,60))