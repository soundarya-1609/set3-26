sse=int(input())
nal=list(map(int,input().split()[:sse]))
nal.sort()
for i in nal:
  print(i,end=" ")
