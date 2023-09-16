a = int(input())
l = int(input())
p = int(input())
h = int(input())
m1 = (a + l + (abs(a - l))) / 2
m2 = (m1 + p + (abs(m1 - p))) / 2
m = m2*h
print(int(m))