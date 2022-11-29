import sympy as sp

idiv = (lambda x,y: (x-x%y)/y)

def _rectE(n,m):
    return sp.MatrixSymbol(' ', n, m)

def _sqE(n):
    return _rectE(n,n)

def _dots(orient:str, rowsize: int, colsize: int):
    if orient == 'h':
        return sp.MatrixSymbol('\dots', rowsize, colsize)
    elif orient == 'v':
        return sp.MatrixSymbol('\\vdots', rowsize, colsize)
    elif orient == 'd' and rowsize == colsize:
        return sp.MatrixSymbol('\ddots', rowsize, colsize)
    elif orient == 'd' and rowsize != colsize:
        return sp.BlockMatrix([
            [sp.MatrixSymbol(' ', 1, 1), sp.MatrixSymbol('\dots', 1, colsize-1)],
            [sp.MatrixSymbol('\\vdots', rowsize-1, 1), sp.MatrixSymbol(' ', rowsize-1, colsize-1)]  
        ])
    else:
        raise ValueError("Invalid orientation")

def matrixSymbolAsColVectors(upperLetter, rowsize, colsize, rule=False):
    # to cancel out the effect of odd number of rowsize
    # we need to add a mod 2 value to the midgapsize
    # see https://www.desmos.com/calculator/pviz78wnx3
    _vecname = upperLetter.lower()
    midgapsize = idiv(colsize-3, 2)
    bgap = midgapsize + (colsize-3)%2 -1
    agap = midgapsize + 1
    if not rule:
        mat = sp.BlockMatrix([
            sp.MatrixSymbol(f"{_vecname}_1", rowsize, 1),
            _dots('h', rowsize, bgap),
            sp.MatrixSymbol(f"{_vecname}_j", rowsize, 1),
            _dots('h', rowsize, agap),
            sp.MatrixSymbol(f"{_vecname}_{colsize}", rowsize, 1)
            ])
    else:
        raise NotImplementedError("Not implemented yet")
    return mat

def matrixSymbolAsRowVectors(upperLetter, rowsize, colsize, rule=False):
    # to cancel out the effect of odd number of rowsize
    # we need to add a mod 2 value to the midgapsize
    # see https://www.desmos.com/calculator/pviz78wnx3
    _vecname = upperLetter.lower()
    midgapsize = idiv(rowsize-3, 2)
    bgap = midgapsize + (rowsize-3)%2 -1
    agap = midgapsize + 1
    if not rule:
        mat = sp.BlockMatrix([
            [sp.MatrixSymbol("\\tilde{" + _vecname + "}_1^T", 1, colsize)],
            [_dots('v', bgap, colsize)],
            [sp.MatrixSymbol("\\tilde{" + _vecname + "}_i^T", 1, colsize)],
            [_dots('v', agap, colsize)],
            [sp.MatrixSymbol("\\tilde{" + _vecname + "}" + f"_{rowsize}^T", 1, colsize)]
            ])
    else:
        raise NotImplementedError("Not implemented yet")
    return mat


def blockMatSymbolAsSqBlocks(
        matLetter,
        subsize,
        nblocksrow=None,
        nblockscols=None,
        rule=False,
        nodiag=False):
    # to cancel out the effect of odd number of rowsize
    # we need to add a mod 2 value to the midgapsize
    # see https://www.desmos.com/calculator/pviz78wnx3
    
    if not rule:
        mat = sp.BlockMatrix([
            [
                sp.MatrixSymbol(f"{matLetter}"+"_{1,1}", subsize, subsize),
                _dots('h', subsize, subsize),
                sp.MatrixSymbol(f"{matLetter}"+"_{1,j}", subsize, subsize),
                _dots('h', subsize, subsize),
                sp.MatrixSymbol(f"{matLetter}"+"_{1,m}", subsize, subsize)
            ],
            [
                _dots('v', subsize, subsize),
                _dots('d', subsize, subsize) if not nodiag else _sqE(subsize),
                _dots('v', subsize, subsize),
                _dots('d', subsize, subsize) if not nodiag else _sqE(subsize),
                _dots('v', subsize, subsize)
            ],
            [
                sp.MatrixSymbol(f"{matLetter}"+"_{i,1}", subsize, subsize),
                _dots('h', subsize, subsize),
                sp.MatrixSymbol(f"{matLetter}"+"_{i,j}", subsize, subsize),
                _dots('h', subsize, subsize),
                sp.MatrixSymbol(f"{matLetter}"+"_{i,m}", subsize, subsize)
            ],
            [
                _dots('v', subsize, subsize),
                _dots('d', subsize, subsize) if not nodiag else _sqE(subsize),
                _dots('v', subsize, subsize),
                _dots('d', subsize, subsize) if not nodiag else _sqE(subsize),
                _dots('v', subsize, subsize)
            ],
            [
                sp.MatrixSymbol(f"{matLetter}"+"_{i,1}", subsize, subsize),
                _dots('h', subsize, subsize),
                sp.MatrixSymbol(f"{matLetter}"+"_{i,j}", subsize, subsize),
                _dots('h', subsize, subsize),
                sp.MatrixSymbol(f"{matLetter}"+"_{i,m}", subsize, subsize)
            ],
            ])
    else:
        raise NotImplementedError("Not implemented yet")
    return mat