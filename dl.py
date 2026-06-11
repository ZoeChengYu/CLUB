def main():
    n=int(input())
    date=[[0 for _ in range(n)]for _ in range(n)]
    ans=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        date[i]=input().split()
        for j in range(n):
            date[i][j]=(int)(date[i][j])
    for i in range(n):
        for j in range(n):
            if date[i][j]==1:
                ans=called1(i,j,ans,n,date)
            if date[i][j]==2:
                ans=called2(i,j,ans,n,date)
    printf(ans)
def called1(i,j,ans,n,data):
    for m in range(3):
        if(i-1>=0 and 0<=j+m-1<n and data[i-1][j+m-1]==0):ans[i-1][j+m-1]+=1
        if(i+1<n and 0<=j+m-1<n and data[i+1][j+m-1]==0):ans[i+1][j+m-1]+=1
    if(j-1>=0 and data[i][j-1]==0):ans[i][j-1]+=1
    if(j+1<n and data[i][j+1]==0):ans[i][j+1]+=1
    ans[i][j]="*"
    return ans
def called2(i,j,ans,n,data):
    for m in range(3):
        for k in range(2):
            if(i+2*(m-1)>=0 and i+2*(m-1)<n and j+2*k-1>=0 and j+2*k-1<n and data[i+2*(m-1)][j+2*k-1]==0):
                ans[i+2*(m-1)][j+2*k-1]+=1
            if(i+2*k-1>=0 and i+2*k-1<n and j+2*(m-1)>=0 and j+2*(m-1)<n and data[i+2*k-1][j+2*(m-1)]==0):
                ans[i+2*k-1][j+2*(m-1)]+=1
    ans[i][j]="#"
    return ans
def printf(ans):
    for i in range(len(ans)):
        for j in range(len(ans)):
            print(ans[i][j],end=" ")
        print()
main()