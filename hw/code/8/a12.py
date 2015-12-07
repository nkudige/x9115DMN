from __future__ import division
from random import randrange
from random import randint
from random import random
from random import uniform
from math import sqrt

class o():
  "Anonymous container"
  def __init__(i,**fields) :
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i

  def __repr__(i):
    d = i.__dict__
    name = i.__class__.__name__
    return name+'{'+' '.join([':%s %s' % (k,pretty(d[k]))
                     for k in i.show()])+ '}'
  def show(i):
    return [k for k in sorted(i.__dict__.keys())
            if not "_" in k]

def a12(lst1,lst2):
  """how often is lst1 often more than y in lst2?
  assumes lst1 nums are meant to be greater than lst2"""

  def loop(t,t1,t2):
    while t1.m < t1.n and t2.m < t2.n:
      h1 = t1.l[t1.m] #mth element of list 1
      h2 = t2.l[t2.m] #mth element of list 2
      h3 = t2.l[t2.m+1] if t2.m+1 < t2.n else None # next element if it is not end of list else None
      # print "h1:", h1, ""
      if h1 > h2:
        t1.m  += 1; t1.gt += t2.n - t2.m
      elif h1 == h2:
        # if h3 and gt(h1,h3) < 0:
        if h3 and h1 > h3:
            t1.gt += t2.n - t2.m  - 1
        t1.m  += 1; t1.eq += 1; t2.eq += 1
      else:
        t2,t1  = t1,t2
    return t.gt*1.0, t.eq*1.0
  #--------------------------
  lst1 = sorted(lst1,reverse=True)
  lst2 = sorted(lst2,reverse=True)
  n1   = len(lst1)
  n2   = len(lst2)
  t1   = o(l=lst1,m=0,eq=0,gt=0,n=n1)
  t2   = o(l=lst2,m=0,eq=0,gt=0,n=n2)
  # print t1
  gt,eq= loop(t1, t1, t2)
  a12_value=gt/(n1*n2) + eq/2/(n1*n2)
  return a12_value


lst1=[100, 1000, 0, 1000, 1000]
lst2=[9, 9, 10, 9, 9]
  
print a12(lst1, lst2)


