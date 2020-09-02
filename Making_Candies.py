#!/usr/bin/env python3

import math
import os
import random
import re
import sys

def minimumPasses(m, w, p, n):
    candi = 0
    days = 0
    while candi < n:
        days += 1

        curCandi = m * w
        tempDays = days + math.ceil((n - candi) / curCandi)
        if candi + curCandi >= p:
            minTempDaysWBuy = 1000000000000000000
            canPurcase = (candi + curCandi) // p
            m2 = m
            w2 = w
            for purchase in range(1, canPurcase + 1):
                if m > w:
                    w2 += 1
                else:
                    m2 += 1
                curCandiNext = m2 * w2
                tempDaysWBuy = days + math.ceil(((n - ((candi + curCandi) - (purchase * p))) / curCandiNext))
                if tempDaysWBuy < minTempDaysWBuy:
                    minTempDaysWBuy = tempDaysWBuy
                    bestPurchase = purchase
            if minTempDaysWBuy < tempDays:
                m, w = makePurchase(m, w, bestPurchase)
                curCandi -= bestPurchase * p
        candi += curCandi
    return days

def makePurchase(m, w, bestPurchase):
    if m > w:
        w += bestPurchase
    else:
        m += bestPurchase
    return m, w


if __name__ == '__main__':

    mwpn = input().split()
    m = int(mwpn[0])
    w = int(mwpn[1])
    p = int(mwpn[2])
    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    print(result)
