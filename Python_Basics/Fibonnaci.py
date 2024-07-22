def solve(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  
  return solve(n-1) + solve(n-2);


for x in range(1,6):
  ans = solve(x)
  print(ans, " ", end="")
