#!/usr/bin/python3

"""
You have n number of locked boxes in
front of you. Each box is numbered sequentially
from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    We use list and contditions to obtain the results
    """
    opened = [0]  # Empezamos con la caja 0 abierta
    keys = boxes[0].copy()  # Copiamos las llaves de la caja 0

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in opened:
            opened.append(key)
            for new_key in boxes[key]:
                if new_key not in keys:
                    keys.append(new_key)

    if len(opened) == len(boxes):
        return True
    return False
