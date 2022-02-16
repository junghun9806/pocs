# -*- coding: utf-8 -*-
""" 
Last update: 2022-02-16
Module information
key - key of 2nd level - value
klv : 
{
    key0: {
        l0  : v0,
        l1  : v1,
        ...
        ln  : vn,
    },
    
    key1: {
        l0  : v0,
        l1  : v1,
        ...
        ln  : vn,
    },
    
    ...
    
    key1: {
        l0  : v0,
        l1  : v1,
        ...
        ln  : vn,
    }
}

Required module. 

Code written by Woojoong Kim. 
Contact: henrik@unist.ac.kr 
Annotation by Junghun Chae
contact: Junghun Chae
"""
"""
Develop Note. 
Things to do. 
"""

from ..ADT import nested_dict

def vkeys(klv):
    """
    list of keys for 2nd level dictionary
    """
    return [list(lv.keys()) for lv in klv.values()]


def vvalues(klv):
    """
    list of values for 2nd level dictionary
    """
    return [list(lv.values()) for lv in klv.values()]


def vitems(klv):
    """
    items for 2nd level dictionary
    """
    return [tuple(lv.items()) for lv in klv.values()]


def ikeys(klv):
    """
    list of [key for 1st level dict, [keys for 2nd level dict]]
    """
    return [[k, list(lv.keys())] for k, lv in klv.items()]


def ivalues(klv):
    return [[k, list(lv.values())] for k, lv in klv.items()]


def iitems(klv):
    return [(k, list(lv.items())) for k, lv in klv.items()]


def fkeys(klv):
    return [(k, l) for k, lv in klv.items() for l in lv.keys()]


def fvalues(klv):
    return [v for lv in klv.values() for v in lv.values()]


def fitems(klv):
    return [((k, l), v) for k, lv in klv.items() for l, v in lv.items()]


def tfkeys(klv):
    lk = ((l, k) for k, lv in klv.items() for l in lv.keys())
    return sorted(lk)


def tfvalues(klv):
    lk = tfkeys(klv)
    return [klv[k][l] for l, k in lk]


def tfitems(klv):
    lk = tfkeys(klv)
    return [((l, k), klv[k][l]) for l, k in lk]


def leys(klv):
    # return list(Counter(l for lv in klv.values() for l in lv.keys()))
    return list({l: 0 for lv in klv.values() for l in lv.keys()})


def first_key(klv):
    return next(iter(klv))


def first_lv(klv):
    return next(iter(klv.values()))


def first_ley(klv):
    return next(iter(first_lv(klv)))


def first_value(klv):
    return next(iter(first_lv(klv).values()))


def transpose(klv, dtype=dict):
    """{k: {l: v}} -> {l: {k: v}}"""
    lkv = dtype()
    for k, lv in klv.items():
        for l, v in lv.items():
            lkv.setdefault(l, {})[k] = v
    return lkv


class KLV(dict):
    def KLV
    
    def vkeys(self):
        return vkeys(self)

    def vvalues(self):
        return vvalues(self)

    def vitems(self):
        return vitems(self)

    def ikeys(self):
        return ikeys(self)

    def ivalues(self):
        return ivalues(self)

    def iitems(self):
        return iitems(self)

    def fkeys(self):
        return fkeys(self)

    def fvalues(self):
        return fvalues(self)

    def fitems(self):
        return fitems(self)

    def leys(self):
        return leys(self)

    def first_key(self):
        return first_key(self)

    def first_lv(self):
        return first_lv(self)

    def first_ley(self):
        return first_ley(self)

    def first_value(self):
        return first_value(self)

    def transpose(self):
        return transpose(self, dtype=KLV)

    @staticmethod
    def from_lkv(lkv):
        return transpose(lkv, dtype=KLV)

    @classmethod
    def from_fitems(cls, it):
        new = cls()
        for (k, l), v in it:
            new.setdefault(k, {})[l] = v
        return new

    def zip_fitems(self, *others):
        for (k, l), v in self.fitems():
            yield (k, l), (v,) + tuple(other[k][l] for other in others)
