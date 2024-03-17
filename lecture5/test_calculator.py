# from calculator import square

# def main():
#     test_square()

# def test_square():
#     # if square(2) != 4:
#     #     print("2 squared was not 4")
#     # if square(3) != 9:
#     #     print("3 squared was not 9")

#     # assert square(2) == 4
#     # assert square(3) == 9

#     # $ python test_calculator.py
#     # AssertionError

#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")         


# if __name__ == "__main__":
#     main()

# $ pip install pytest
# Successfully installed colorama-0.4.6 iniconfig-2.0.0 packaging-24.0 pluggy-1.4.0 pytest-8.1.1

from calculator import square

# def test_square():
#         assert square(2) == 4
#         assert square(3) == 9
#         assert square(-2) == 4
#         assert square(-3) == 9
#         assert square(0) == 0

# $ pytest test_calculator.py
# ======================== test session starts ========================
# platform win32 -- Python 3.12.1, pytest-8.1.1, pluggy-1.4.0
# rootdir: C:\Users\Bilde\Documents\GitHub\python-cs50\lecture5        
# collected 1 item

# test_calculator.py F                                           [100%]

# ============================= FAILURES ==============================
# ____________________________ test_square ____________________________

#     def test_square():
#             assert square(2) == 4
# >           assert square(3) == 9
# E           assert 6 == 9
# E            +  where 6 = square(3)

# test_calculator.py:50: AssertionError
# ====================== short test summary info ====================== 
# FAILED test_calculator.py::test_square - assert 6 == 9
# ========================= 1 failed in 0.08s ========================= 



# $ pytest test_calculator.py
# ==================================== test session starts ====================================
# platform win32 -- Python 3.12.1, pytest-8.1.1, pluggy-1.4.0
# rootdir: C:\Users\Bilde\Documents\GitHub\python-cs50\lecture5
# collected 1 item

# test_calculator.py .                                                                   [100%]

# ===================================== 1 passed in 0.01s =====================================]


def test_positive():
        assert square(2) == 4
        assert square(3) == 9

def test_negative():
        assert square(-2) == 4
        assert square(-3) == 9

def test_zero():
        assert square(0) == 0