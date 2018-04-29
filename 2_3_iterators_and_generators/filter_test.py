#!/usr/bin/python3.6


def judge_all(pos, neg):
    # допускает элемент, если его допускают все функции (neg == 0)
    if pos == 0:
        return False
    return True if neg == 0 else False

print(judge_all(3,4))
print(judge_all(3,0))
