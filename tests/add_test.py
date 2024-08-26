from deneme_for_code_cov.add import add
import pytest

def new_test(x,y):
  assert add(x,y)==x+y
