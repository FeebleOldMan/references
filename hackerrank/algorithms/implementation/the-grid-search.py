#!/usr/bin/env python

def main():
    for _ in range(int(raw_input().strip())):
        rows, cols = map(int, raw_input().strip().split())
        grid = []
        search = []
        for _row in range(rows):
            grid.append(raw_input().strip())
        srows, scols = map(int, raw_input().strip().split())
        for _srow in range(srows):
            search.append(raw_input().strip())
        print find(grid, search)

def find(grid, search):
    for i, row in enumerate(grid[:-len(search)+1]):
        if search[0] in row:
            # put all instances of number combi in array
            cols = []
            pos = 0
            while True:
                try:
                    pos = row.index(search[0], pos)
                    cols.append(pos)
                    pos += 1
                except ValueError:
                    break
            for col in cols:
                isFound = True
                for x, srow in enumerate(search):
                    try:
                        grid[i+x].index(search[x], col, col+len(srow))
                    except ValueError:
                        isFound = False
                    if x == len(search)-1 and isFound:
                        return "YES"
    return "NO"

def test():
#    grid = [
#        '7283455864',
#        '6731158619',
#        '8988242643',
#        '3830589324',
#        '2229505813',
#        '5633845374',
#        '6473530293',
#        '7053106601',
#        '0834282956',
#        '4607924137'
#    ]
#    search = [
#        '9505',
#        '3845',
#        '3530'
#    ]
##    print 'TEST1:', 'pass' if find(grid, search) == 'YES' else '**FAIL**'
#    grid = [
#        '400453592126560',
#        '114213133098692',
#        '474386082879648',
#        '522356951189169',
#        '887109450487496',
#        '252802633388782',
#        '502771484966748',
#        '075975207693780',
#        '511799789562806',
#        '404007454272504',
#        '549043809916080',
#        '962410809534811',
#        '445893523733475',
#        '768705303214174',
#        '650629270887160'
#    ]
#    search = [
#        '99',
#        '99'
#    ]
##    print 'TEST2:', 'pass' if find(grid, search) == 'NO' else '**FAIL**'
#    grid = [
#        '123412',
#        '561212',
#        '123634',
#        '781288'
#    ]
#    search = [
#        '12',
#        '34'
#    ]
#    print 'TEST3:', 'pass' if find(grid, search) == 'YES' else '**FAIL**'
    grid = [
        '111111111111111',
        '111111111111111',
        '111111011111111',
        '111111111111111',
        '111111111111111'
    ]
    search = [
        '11111',
        '11111',
        '11110'
    ]
    print 'TEST9:', 'pass' if find(grid, search) == 'YES' else '**FAIL**'
    return

main()
#test()
