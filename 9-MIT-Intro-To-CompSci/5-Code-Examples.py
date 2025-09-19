def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)
    
(quot, rem) = quotient_and_remainder(5,3)
print(quot)
print(rem)

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

test = ((1,"a"),(2, "b"),
        (1,"a"),(7,"b"))
(a, b, c) = get_data(test)
print("a:",a,"b:",b,"c:",c)

def sum_elem_method1(L):
  total = 0 
  for i in range(len(L)): 
      total += L[i] 
  return total
  
def sum_elem_method2(L):
    total = 0 
    for i in L: 
        total += i 
    return total
  
print(sum_elem_method1([1,2,3,4]))
print(sum_elem_method2([1,2,3,4]))


L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2
L1.extend([0,6])

L = [2,1,3,6,3,7,0]
L.remove(2)
L.remove(3)
del(L[1])
print(L.pop())

s = "I<3 cs"
print(list(s))
print(s.split('<'))
L = ['a', 'b', 'c']
print(''.join(L))
print('_'.join(L))

L=[9,6,0,3]
print(sorted(L))
L.sort()
L.reverse()

warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink')
print(hot)
print(warm)

cool = ['blue', 'green', 'grey']
chill = cool[:]
chill.append('black')
print(chill)
print(cool)

def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print(L1, L2)