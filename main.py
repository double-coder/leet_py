from binarysearch import finditem
from twopointers import arraychan
from arrayops import comparearr
from stringops import flipbit

def main():
    sample = [-4,-1,0,3,10]
    sol = finditem.Solution
    x = sol.search(sol, [-1,0,3,5,9,12], 9)
    print(x)
    sortarr = arraychan.sortedSquares
    print(sortarr(sortarr, sample))
    com = comparearr.Solution
    com.backspaceCompare(com, 'ab##', 'c#d#')
    bitops = flipbit.Solution
    bitops.minBitFlips(bitops, 10, 7)

if __name__ == '__main__':
    main()