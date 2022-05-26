import random

def quicksort(lst):
   if len(lst) <= 1:
       return lst
   else:
       rnd = random.choice(lst)
       l_nums = []
       m_nums = []
       r_nums = []
       for n in lst:
           if n < rnd:
               l_nums.append(n)
           elif n > rnd:
               r_nums.append(n)
           else:
               m_nums.append(n)
       return quicksort(l_nums) + m_nums + quicksort(r_nums)
