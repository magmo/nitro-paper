from overlap import overlap
from remove import remove
from restrict import restrict
from transfer import transfer
from claim import claim

def test_overlap():
  assert overlap('a', [['a', 5], ['b', 3]], 10) == 5
  assert overlap('b', [['a', 5], ['b', 3]], 10) == 3
  assert overlap('b', [['a', 5], ['b', 3]], 7) == 2

def test_remove():
  assert remove([['a', 5], ['b', 3]], 'a', 5) == [['a', 0], ['b', 3]]
  assert remove([['a', 5], ['b', 3]], 'b', 2) == [['a', 5], ['b', 1]]

def test_transfer():
  assert transfer('a', [['a', 5]], 10, 5) == (5, [['a', 0]], 5)
  assert transfer('a', [['a', 5]], 10, 2) == (2, [['a', 3]], 8)
  assert transfer('b', [['a', 5]], 10, 2) == (0, [['a', 5]], 10)

def test_restrict():
  assert restrict([['a', 5], ['b', 3]], 'a', 4) == [['a', 4], ['b', 3]]
  assert restrict([['a', 5], ['b', 3]], 'a', 6) == [['a', 5], ['b', 3]]
  assert restrict([['a', 5], ['b', 3]], 'b', 2) == [['a', 5], ['b', 2]]

def test_claim():
  assert claim('a', [['a', 10]], [['a', 5]], 5, 5) == (5, [['a', 0]], [['a', 0]], 0)
