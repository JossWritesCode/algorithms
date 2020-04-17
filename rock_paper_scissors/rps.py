#!/usr/bin/python

import sys

# r p s (3)
# rr rp rs pp pr ps ss sp sr (9)
# rrr rrp rrs rpr rsr rpp rss ppp ppr pps prp psp prr pss sss ssp ssr sps srs srr spp (21)


def rock_paper_scissors(n):
    rps = ["rock", "paper", "scissors"]
    result_array = []

    def rock_paper_scissors_helper(n, array=[]):

        if n == 0:
            result_array.append(array)
        else:
            for move in rps:
                rock_paper_scissors_helper(n - 1, array + [move])

    rock_paper_scissors_helper(n)
    return result_array


print(rock_paper_scissors(3))
print(len(rock_paper_scissors(1)), "should be 3")
print(len(rock_paper_scissors(2)), "should be 9")
print(len(rock_paper_scissors(3)), "should be 27")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
