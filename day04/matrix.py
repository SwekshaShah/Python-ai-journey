#Nested lists: build a 3×3 matrix. Write functions to print it as a formatted grid, calculate the transpose, and add two matrices element by element. No NumPy — do it manually. This bridges directly to Week 2.
matrix1=[[11,12,13],[14,15,16],[17,18,19]]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
def matrix_3x3(matix):  #Formatteed grid
    for row in matrix:
        for items in row:
            print(items,end=' ')
        print()
matrix_3x3()


def transpose():
  for col in range(3):
    for row in matrix:
      print(row[col],end=" ")
    print()
transpose()

def add_matrices():
   new=[]
   for row in range(3):
      for col in range(3):
        new.append(matrix[row][col]+matrix1[row][col])
      print(new)  
add_matrices()