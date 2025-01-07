
#백준_입출력과 사칙연산
"""
#문제 1
#https://www.acmicpc.net/problem/2557

print("Hello World!")

#문제2
#https://www.acmicpc.net/problem/1000
A, B = map(int, input().split())
print(A+B)
"""
#문제3
#https://www.acmicpc.net/problem/1001
A, B = map(int, input().split())
print(A-B)

#문제4
#https://www.acmicpc.net/problem/10998
A, B = map(int, input().split())
print(A*B)

#문제5
#https://www.acmicpc.net/problem/1008
A, B = map(int, input().split())
print(A/B)

#문제6
#https://www.acmicpc.net/problem/10869
A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print((int)(A / B))
print(A % B)

#문제7
#https://www.acmicpc.net/problem/10926
n = input()
a = n+"??!"
print(a)

#문제8
#https://www.acmicpc.net/problem/18108
n = input()
a = int(n) - 543
print(a)

#문제9
#https://www.acmicpc.net/problem/10430
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#문제10
#https://www.acmicpc.net/problem/2588
A = int(input())
B = input()
C = list(map(int,B))
for i in C[::-1]:
    D = A * i
    print(D)
print(A * int(B))

#문제11
#https://www.acmicpc.net/problem/11382
a, b, c = map(int,input().split())
print(a+b+c)

#문제12
#https://www.acmicpc.net/problem/10171
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

#문제13
#https://www.acmicpc.net/problem/10172
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')  
print('|"^"`    |')
print("||_/=\\\\__|")  

#문제14
#아직 안풀음