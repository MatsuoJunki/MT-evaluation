# coding: utf-8
'''
python system_score.py "scored_file" 
'''
import sys

def main():
	count = 0
	total_score = 0
	scored_file = open(sys.argv[1],"r")
	for line in scored_file:
		count += 1
		score = float(line)
		total_score += score
		if count == 200:
			score_ave = float(total_score)/200
			print score_ave
			total_score = 0
			score_ave = 0
			count = 0

if __name__ == "__main__":
    main()