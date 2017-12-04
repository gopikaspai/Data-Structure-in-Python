'''Due to recent rains (I know it’s very rare here), water has pooled in various
places in the campus, which is represented by a rectangle of N x M (1 <= N
<= 100; 1 <= M <= 100) squares. Each square contains either water ('#') or
dry land ('-'). A pond is a connected set of squares with water in them, where
a square is considered adjacent to all eight of its neighbors. The problem is
to figure out how many ponds have formed in the campus, given a diagram
of the campus. The campus is represented by a grid represented by a list of
N lines of characters separated by “,”. Each line contains M characters per
line representing one row of the grid (campus). Each character is either '#' or
'-'. The characters do not have spaces between them. Write a program to
compute and return the number of ponds in the campus.

Sample Input
["#--------##-",
"-###-----###",
"----##---##-",
"---------##-",
"---------#--",
"--#------#--",
"-#-#-----##-",
"#-#-#-----#-",
"-#-#------#-",
"--#-------#-"]

Sample Output
3

(There are three ponds: one in the upper left, one in the lower left,and one
along the right side)'''

def depth_first_search(i, j, visited, m, n, G):
    row_number = [-1, -1, -1, 0, 0, 1, 1, 1]
    column_number = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited[i][j] = True

    for k in range(8):
        if (not ((not (i + row_number[k] >= 0) or not (i + row_number[k] < m)
                  or not (0 <= j + column_number[k] < n)
                  or visited[i + row_number[k]][j + column_number[k]])
                 or not G[i + row_number[k]][j + column_number[k]] == "#")):
            depth_first_search(i + row_number[k], j + column_number[k],
                               visited, m, n, G)


def count_ponds(G):
    if not G:
        return 0
    m = len(G)
    n = len(G[0])

    visited = [[False for j in range(n)] for i in range(m)]

    count = 0
    for i in range(m):
        for j in range(n):

            if not visited[i][j] and G[i][j] == "#":
                depth_first_search(i, j, visited, m, n, G)
                count += 1

    return count


def test_suite():
    if count_ponds(["#--------##-",
                    "-###-----###",
                    "----##---##-",
                    "---------##-",
                    "---------#--",
                    "--#------#--",
                    "-#-#-----##-",
                    "#-#-#-----#-",
                    "-#-#------#-",
                    "--#-------#-"]) == 3:
        print('passed')
    else:
        print('failed')


if __name__ == '__main__':
    test_suite()
