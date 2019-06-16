#Building Itertools permutations

from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

from itertools import combinations_with_replacement
s,n = input().split()
print(*[''.join(i) for i in combinations_with_replacement(sorted(s),int(n))],sep='\n')

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

# Enter your code here. Read input from STDIN. Print output to STDOUT
#You are given a function . You are also given  lists. The  list consists of  elements.
#You have to pick one element from each list so that the value from the equation below is maximized: 
# denotes the element picked from the  list . Find the maximized value  obtained.
# denotes the modulo operator.
#Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
