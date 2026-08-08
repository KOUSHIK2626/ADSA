import typing
def The_Great_Run(N: int,k:int,arr:typing.List[int]) -> int:
   window_sum = sum(arr[:k])
   max_sum = window_sum

   for i in range(k, N):
      window_sum += arr[i] - arr[i - k]
      max_sum = max(max_sum, window_sum)

   return max_sum
if __name__ == '__main__':
    N,k = map(int,input().split())
    path = list(map(int,input().split()))
    print(The_Great_Run(N,k,path))
