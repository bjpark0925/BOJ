'''
10^11을 12로 나눈다.
= ((10^5)%12 x (10^5)%12 x 10)% 12
= ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
'''
def power(a,b,c):
  if b==0:
    return 1

  half = power(a,b//2,c)
  if b%2==0:
    half = (half*half)%c
  else:
    half = (half*half*a)%c

  return half

a, b, c = map(int, input().split())
print(power(a,b,c))