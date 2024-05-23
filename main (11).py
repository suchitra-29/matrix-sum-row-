r,c=int(input()),int(input())
l,max=[0]*r,0
for i in range(r):
  l[i]=list(map(int,input().split()))
for i in l:
  print(i)
  print(f"sum of {l.index(i)+1} row: {sum(i)}")
  for j in range(1,len(i)):
    if i[j-1]+i[j]>max:
      max=i[j-1]+i[j]
print("max:",max)    





