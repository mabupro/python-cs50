from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"


# $ pytest test
# ==================================== test session starts ====================================
# platform win32 -- Python 3.12.1, pytest-8.1.1, pluggy-1.4.0
# rootdir: C:\Users\Bilde\Documents\GitHub\python-cs50\lecture5
# collected 2 items

# test\test_hello.py ..                                                                  [100%]

# ===================================== 2 passed in 0.02s =====================================