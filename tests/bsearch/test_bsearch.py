from bsearch.bsearch import bsearch, bisect_left, bisect_right
import operator


def test_bsearch():
  a = [0,1,2,4,8]
  assert(bsearch(a, -1) == 0)
  assert(bsearch(a, 0) == 0)
  assert(bsearch(a, 1) == 1)
  assert(bsearch(a, 2) == 2)
  assert(bsearch(a, 4) == 3)
  assert(bsearch(a, 8) == 4)
  assert(bsearch(a, 10) == 5)

def test_bisects():
  a = [0,0,1,1,1,1,2,2,2,3]
  assert(bisect_left(a, 0) == 0)
  assert(bisect_left(a, 1) == 2)
  assert(bisect_left(a, 2) == 6)
  assert(bisect_left(a, 3) == 9)
  assert(bisect_left(a, 4) == 10)

  assert(bisect_right(a, -1) == 0)
  assert(bisect_right(a, 0) == 2)
  assert(bisect_right(a, 1) == 6)
  assert(bisect_right(a, 2) == 9)
  assert(bisect_right(a, 3) == 10)

def test_operator():
  a = [5,4,3,2,1]
  assert(bsearch(a, 5, op=operator.gt) == 0)
  assert(bsearch(a, 4, op=operator.gt) == 1)
  assert(bsearch(a, 3, op=operator.gt) == 2)
  assert(bsearch(a, 2, op=operator.gt) == 3)
  assert(bsearch(a, 1, op=operator.gt) == 4)

def test_key():
  a = [(1,5), (2,8), (2,9), (3,5)]
  fn = lambda x:x[0]
  assert(bisect_left(a, 1, key=fn) == 0)
  assert(bisect_left(a, 2, key=fn) == 1)
  assert(bisect_left(a, 3, key=fn) == 3)