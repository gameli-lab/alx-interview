#!/usr/bin/python3
'''
Lockboxes project module
'''


def canUnlockAll(boxes):
    '''
    canUnlockAll method takes boxes as argument
    returns true if box can be unlocked else false
    '''
    n = len(boxes)
    unlocked = set()
    keys = set([0])

    while keys:
        new_keys = set()
        for key in keys:
            if key not in unlocked:
                unlocked.add(key)
                new_keys.update(boxes[key])

        if not new_keys - unlocked:
            break

        keys = new_keys - unlocked

    return len(unlocked) == n
