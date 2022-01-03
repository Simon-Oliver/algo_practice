board = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

board1 = [
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1]
]


print(board[0][2])

# 2,2     4,4
# 1,1     3,3
# 0,0     2,2
#         1,1
#         0,0

def diagonal(b,start):
    s = 0
    count = 0
    
    for row in b:
        try:
            if row.index(1) != -1:
                s = row.index(1)
                break
        except:
            pass

    for row in b[s:]:
        print("-----",s)
        n = row
        if n[s] == 1:
            count+=1
        s +=1
    print(count)

diagonal(board1, (4,4))