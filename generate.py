import random
import os
from hoshino import logger

punclist = ['，']*5+['。']*5+['！']*3+['……']*3+['，，，。。。']+['（）']
l1 = []
l2 = []
l3 = []
l4 = []
re = []
me = '我'
my = '我的'
l33 = ['那么']*3+['又']*3+['意想不到地']

words_path = os.path.join(os.path.dirname(__file__), 'words.txt')


def get_words():
    if os.path.exists(words_path):
        with open(words_path, 'r', encoding='utf-8') as f:
            try:
                txt = []
                for line in f:
                    txt.append(line.strip())
                return txt
            except Exception as ex:
                logger.exception(ex)
                return None
    else:
        logger.error('words.txt文件不存在')
        return None


def punc():
    pun = random.choice(punclist)
    return pun


def be():
    return random.choice(['是', '是', '你是'])


def _l(txt: list):
    global l1, l2, l3, l4
    l1 = txt[0].split(',')
    l2 = txt[1].split(',')
    l3 = txt[2].split(',')
    l4 = txt[3].split(',')


def ch(i):
    global l1, l2, l3, l4
    if i == 1:
        return random.choice(l1)
    elif i == 2:
        return random.choice(l2)
    elif i == 3:
        return random.choice(l33)+random.choice(l3)
    else:
        return random.choice(l4)


def generate_txt(name: str):
    num1 = random.randint(3, 6)
    num2 = random.randint(3, 6)
    num3 = 12-num1-num2

    txt = get_words()
    if not txt:
        return '发生错误：发疯文不存在'

    _l(txt)

    raw = []
    raw.append(ch(1))
    raw.append(my+name)
    raw.append(my+ch(2)+'般的'+name)
    for i in range(num1):
        raw.append(be()+ch(2))
    for i in range(num2):
        raw.append(ch(3))
    for i in range(num3):
        raw.append(me+ch(4))

    for i in range(random.randint(2, 4)):
        raw.insert(random.randint(0, len(raw)), name)

    for i in range(len(raw)):
        re.append(raw[i])
        re.append(punc())

    result = ''.join(re)
    return result
