#print sum
a = 20
b = 35
sum = a + b
print(sum)

#print Difference
A = 500
B = 100
diff = A - B
print(diff)

#Expression Execution

#Rule 1(string and Numeric value can operate together with *)
A , B = 2 , 3
Txt = "@"
print(A * Txt * B)

#Rule 2(string and string can operate together with +)
A , B = "2", 3
Txt = "@"
print((A + Txt) * B)

#Rule 3(Numeric values can operate with all arithmetic operators)
A , B = 2 , 3
C = 4
print(A+B*C) 

#Rule 4(Arithmetic expression with Integer and float will result in float)
A , B = 20 , 5.0
C = A*B
print(C)

#Rule 5(Result of division operator with two integers will be float)
A , B = 1 , 2
C = A/B
print(C)

#Rule 6(integer divison with float and int will give int displayed at float)
A , B = 1.5 , 3
C = A // B
print(C , A / B)

A , B = 12 , 5
C = A // B
print(C)

#Negative Denominator means -ve answer
A , B = -5 , 2
C = A % B
print(C)

A , B = 5 , -2
C = A % B
print(C)


