from timeit import timeit
from random import randint

# 生成1000个测试用例
L = [' '.join(''.join(chr(randint(97, 122))
                      for _ in range(randint(3, 13)))
              for _ in range(randint(1, 100)))
     for _ in range(1000)]



funcs = """
from re import compile, split, search
from operator import itemgetter, methodcaller


def first_word1(text):
    index = text.find(' ')
    return text[:index] if index != -1 else text

def first_word2(text):
    try:
        return text[:text.index(' ')]
    except ValueError:
        return text

first_word3 = lambda text: text.split(maxsplit=1)[0]

first_word4 = lambda text: text[:text.find(' ') % (len(text)+1)]

first_word5 = lambda text: text[:(text+' ').index(' ')]

compose = lambda g, f: lambda x: g(f(x))
first_word6 = compose(itemgetter(0), methodcaller('split', ' ', 1))

matcher = compile('(\\S+)\\s?').match
def first_word7(text):
    return matcher(text)[1]

def first_word8(text: str) -> str:
    return search(r"[a-zA-Z]+", text).group(0)

first_word9 = lambda text: text.split()[0]

expr10 = compile('\\W+')
first_word10 = lambda t: split(expr10, t)[0]
"""

stmt = """
for s in L:
    first_word{}(s)
""".format

setup = funcs + f"L = {L}"

for k in range(1, 11):
    res = timeit(stmt(k), setup, number=10000)
    print(f"first_word{k: <2}  {round(res, 2): >6} seconds.")