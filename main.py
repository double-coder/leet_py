from binarysearch import finditem
from twopointers import arraychan
from arrayops import comparearr, minele
from stringops import flipbit, containcontones
from linkedlist import createalinkedlist
from bfsdfs import rottenoranges

def main():
    # binary search
    sample = [-4,-1,0,3,10]
    sol = finditem.Solution
    x = sol.search(sol, [-1,0,3,5,9,12], 9)
    print(x)
    
    # easy two pointers question
    sortarr = arraychan.sortedSquares
    print(sortarr(sortarr, sample))
    
    """
    medium question from leet code
    Q. when you see # hit backspace and compare if both strings are same?
    """
    com = comparearr.Solution
    com.backspaceCompare(com, 'ab##', 'c#d#')

    # mine = minele.Solution
    # mine.minElements(mine, [1,-10,9,1], 100, 0)

    """
    medium level question from leat code
    Q. how man bits we need to flip to get to target?
       target = 7
       source = 10
    """
    bitops = flipbit.Solution
    bitops.minBitFlips(bitops, 10, 7)
    cones = containcontones.Solution
    cones.checkOnesSegment(cones, '10')
    # linked list implementation
    ll = createalinkedlist.LinkedList()
    Node = createalinkedlist.Node
    ll.head = Node(1)
    ll.append(Node(2))
    ll.printlist()

    """
    
    """
    ro = rottenoranges.Solution
    ro.orangesRotting(ro, [[2,1,1],[1,1,0],[0,1,1]])
if __name__ == '__main__':
    main()