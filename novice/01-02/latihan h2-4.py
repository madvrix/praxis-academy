matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
matrix2=[
    [9,8,7,6],
    [5,4,3,2]
]
matrix

[[row[i] for row in matrix] for i in range(4)]

for row in matrix:
    for i in range(4):
        row[i]
'cek'
matrix3=[]
matrix3=matrix2
list(zip(*matrix))