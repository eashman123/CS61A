# Tree definition

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('loki')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        loki
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    if is_leaf(t):
        if label(t)==old:
            return tree(new)
        return tree(label(t))
    else:
        return tree(label(t), [replace_leaf(b, old, new) for b in branches(t)])

def print_move(origin, destination):
    """Print instructions to move a disk."""
    #print("Move the top disk from rod", origin, "to rod", destination)
    return [origin, destination]

memoized_ops={}
def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    >>> move_stack(4, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 1
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 3 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    sub_moves=[]
    if n==1:
        sub_moves.append(print_move(start, end))
    else:
        other=[1, 2, 3]
        other.remove(start)
        other.remove(end)
        other = other[0]
        sub_moves.extend(call_mem(n-1, start, other))
        sub_moves.extend(call_mem(1, start, end))
        sub_moves.extend(call_mem(n-1, other, end))
    memoized_ops[(n, start, end)] = sub_moves
    return sub_moves

def call_mem(n, start, end):
    if (n, start, end) in memoized_ops.keys():
        if len(memoized_ops[(n, start, end)])==1:
            return memoized_ops[(n, start, end)][0]
        else:
            return memoized_ops[(n, start, end)]
    else:
        return move_stack(n, start, end)

def hanoi(n, start, end):
    instructions = call_mem(n, start, end)
    # print(call_mem(n, start, end))
    for index in range(len(instructions)):
        if type(instructions[index])==list:
            origin, destination = instructions[index]
            print("Move the top disk from rod", origin, "to rod", destination)
            continue
        try:
            if type(instructions[index])!=list and type(instructions[index+1])!=list:
                origin, destination = instructions[index], instructions[index+1]
                print("Move the top disk from rod", origin, "to rod", destination)
        except IndexError:
            pass


def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    return min(x)

def upper_bound(x):
    """Return the upper bound of interval x."""
    return max(x)

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    lower = lower_bound(x)-upper_bound(y)
    upper = upper_bound(x)-lower_bound(y)
    return interval(lower, upper)
def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    assert 0 not in range(int(lower_bound(y)), int(upper_bound(y))+1)
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1, 1.000001) # Replace this line!
    r2 = interval(1, 1.000001) # Replace this line!
    return r1, r2

def multiple_references_explanation():
    return """Each time you compute an interval betweek two intervals, the code essentially returns the widest possible 
    interval, at least for the case of mul_interval. This is relevant to par1 and par2 as they both use mul_interval in
    their computations. This means that for par1, which calls mul_interval more times, the resulting interval is greater,
    and this means that the interval returned by par1 and par2 are different"""

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    def find_val(t):
        return (a)*(t**2) + b*t + c
    lower = 0
    upper = 0
    extreme = -b/(2*a)
    if lower_bound(x)<= extreme <= upper_bound(x):
        if a>0:
            upper = max(find_val(lower_bound(x)), find_val(upper_bound(x)))
            lower= find_val(extreme)
            return interval(lower, upper)
        else:
            lower = min(find_val(lower_bound(x)), find_val(upper_bound(x)))
            upper=find_val(extreme)
            return interval(lower, upper)
    upper = max(find_val(lower_bound(x)), find_val(upper_bound(x)))
    lower = min(find_val(lower_bound(x)), find_val(upper_bound(x)))
    return interval(lower, upper)

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"

