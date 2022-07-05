# BestQuestion
#brute force approach worst case 0(n^2)
def findPairs(arr,k):
  if len(arr)&1:
    return 0
  visited = [0]*len(arr)
  for i in range(len(arr)-1):
    if visited[i]:
      continue
    j=i+1
    while(j<len(arr)):
      if not visited[i] and (arr[j]+arr[i])%k==0:
        visited[j]=1
        break
      j=j+1
    if(j==len(arr)):
      return 0
  return 1

if __name__=="__main__":
  #arr=[2,9,4,1,3,5]
  arr=[3,1,2,6,9,4]
  k=5
  if findPairs(arr,k):
    print("Pair are formed")
  else:
    print("Pair are not formed")
