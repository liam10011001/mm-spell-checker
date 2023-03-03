def have_same_characters(a, b): return sorted(a) == sorted(b)

def swap(s, i, j):
    if i > j : 
        tmp = i
        i = j
        j = tmp
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

def drop(s, i):
    return s[:i] + s[i+1:]

def remove(s, ch):
    return "".join([c for c in s if c != ch])

def replace_once(s, a, b):
    new_s = ''
    for ch in s:
        if ch == a: new_s += b
        else: new_s += ch
    return new_s

def lev(a, b):
    ''' Levenshtein Distance '''
    if a == '' or b == '': return len(b) or len(a)
    elif a[0] == b[0]: return lev(a[1:], b[1:])
    else:
        return 1 + min(lev(a[1:], b), lev(a, b[1:]), lev(a[1:], b[1:]))


def minimum_edit_distance(source, target):
    n = len(source)
    m = len(target)
    del_cost = 1
    ins_cost = 1
    
    # create Distance Matrix D with dimension of n+1 x m+1
    # initialize D with 0
    D = [[0 for j in range(m+1)] for i in range(n+1)]
    
    # initialization the 0th row and column
    for r in range(1, n+1):
        D[r][0] = D[r-1][0] + del_cost

    for c in range(1, m+1):
        D[0][c] = D[0][c-1] + ins_cost

    for r in range(1, n+1):        
        for c in range(1, m+1):
            D[r][c] = min(
                D[r-1][c] + del_cost,
                D[r-1][c-1] + (0 if source[r-1] == target[c-1] else 2),
                D[r][c-1] + ins_cost)
    
    """for i in range(n+1):
        for j in range(m+1):
            print(D[i][j], end="\t")
        print(end="\n")"""
    
    return D[n][m]
