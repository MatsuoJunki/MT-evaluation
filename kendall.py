# coding: utf-8

import sys
import scipy.stats


def get_human_judgements():
    human_judgements = list()
    #dname = "/home/matsujun/20160904/ASPEC-JE/"
    #for fname in ["0061-0655_aspec-ja-en.txt", "0063-0829_aspec-ja-en.txt", "0071-0529_aspec-ja-en.txt"]:
    fin_hu = open(sys.argv[2], "r")
    for line in fin_hu:
        #src, ref, sys, human_score_1, human_score_2 = line.strip().split("\t")
        #    human_score = (float(human_score_1) + float(human_score_2)) / 2.0
        human_judgements.append(float(line.strip()))
    fin_hu.close()
    return human_judgements


def get_system_outputs():
    system_outputs = list()
    fin = open(sys.argv[1], "r")
    for line in fin:
        line =  line.strip()
        #print type(line)
        line = float(line)
        #print line
        system_outputs.append(line)
    fin.close()
    return system_outputs


def tau(data1, data2):
    return str(scipy.stats.kendalltau(data1, data2)[0])


def main():
    human = get_human_judgements()
    system = get_system_outputs()
    print tau(human, system)


if __name__ == "__main__":
    main()