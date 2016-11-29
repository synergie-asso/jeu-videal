def fusion(carre1, carre2):
    '''
    return carre1 * 2
    '''
    # FIXME
    return 2


def isFusion(carre1, carre2):
    '''
    return carre1 == carre2
    '''
    # FIXME
    return False

    
def scoreFusion(carre, score):
    '''
    if (score < 100) :
        score += 10
    if (score % 10 == 0) :
        return score + carre * 10
    return score + carre * 2
    '''
    return score + 1


def win(tab):
    '''
    for i in range(len(tab)):
        if tab[i] == 64:
            return True
    return False
    '''
    # FIXME
    return False


def check(grid, x, y, i, j):
    '''
    if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid) - 1:
        return False
    return grid[i][j] == grid[x][y]
    '''
    # FIXME
    return True


def lose(grid):
    '''
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return False
            else:
                if check(grid, i, j, i - 1, j) or check(grid, i, j, i + 1, j) or check(grid, i, j, i, j - 1) or check(
                        grid, i, j, i, j + 1):
                    return False
    return True
    '''
    # FIXME
    return False
