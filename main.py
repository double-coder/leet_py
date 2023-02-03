from binarysearch import finditem
from twopointers import arraychan
from arrayops import comparearr
from stringops import flipbit
from linkedlist import createalinkedlist

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
    """
    medium level question from leat code
    Q. how man bits we need to flip to get to target?
       target = 7
       source = 10
    """
    bitops = flipbit.Solution
    bitops.minBitFlips(bitops, 10, 7)

    # linked list implementation
    ll = createalinkedlist.LinkedList()
    Node = createalinkedlist.Node
    ll.head = Node(1)
    ll.append(Node(2))
    ll.printlist()
if __name__ == '__main__':
    main()