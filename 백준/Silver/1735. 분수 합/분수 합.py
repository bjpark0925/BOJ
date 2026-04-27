import math
a_son, a_mom = map(int, input().split())
b_son, b_mom = map(int, input().split())
gcdVal = math.gcd(a_mom, b_mom)
mom = a_mom//gcdVal * b_mom
son = (mom//a_mom*a_son) + (mom//b_mom*b_son)
answer_gcd = math.gcd(mom, son)
print(son//answer_gcd, mom//answer_gcd)