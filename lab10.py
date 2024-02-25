print("------------------TASK 1------------------")
r = int(input("Enter num of rows:")) 
c = int(input("Enter num of column:")) 
print(r,c)
matrix = []

for i in range(r):
    row = []
    for j in range(c):
        column = []
        user1 = int(input(f"Enter elements :"))
        row.append(user1)
    matrix.append(row)
        
print(matrix)


print("------------------TASK 2------------------")


r = int(input("Enter num of rows:")) 
c = int(input("Enter num of column:")) 
print(r,c)
matrix1 = []
print("Matrix 1")
for i in range(r):
    row1 = []
    for j in range(c):
        column1 = []
        user1 = int(input("Enter elements :"))
        row1.append(user1)
    matrix1.append(row1)


print("Matrix 2")
matrix2 = []
for i in range(r):
    row2 = []
    for j in range(c):
        column2 = []
        user2 = int(input("Enter elements :"))
        row2.append(user2)
    matrix2.append(row2)
        
print("Matrix 1:",matrix1)
print("Matrix 2:",matrix2)


print("-------------------------TASK 3-------------------")


if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]) :
    matrix3 = []
    for n in range(0, len(matrix1)):
        sum_matrix = []
        for i in range(0, len(matrix1[0])):
            matrx1 = matrix1[n][i] + matrix2[n][i]
            sum_matrix.append(matrx1)
        matrix3.append(sum_matrix)

    matrix4 = []
    for n in range(0, len(matrix1)):
        sub_matrix = []
        for i in range(0, len(matrix1[0])):
            matrx2 = matrix1[n][i] - matrix2[n][i]
            sub_matrix.append(matrx2)
        matrix4.append(sub_matrix)
    print("Matrix:",matrix3, matrix4)
else:
    print("The number of rows & columns must be equal")