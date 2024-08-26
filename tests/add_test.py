from add import add
import pytest

def new_test(x,y):
  assert add(x,y)==x+y
