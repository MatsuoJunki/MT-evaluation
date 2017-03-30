'''
python extraction_Asia.py
'''
import sys

if __name__ == '__main__':

	file1 = open("BLEU_value600.txt", "r")
	file2 = open("NIST_value600.txt", "r")
	file3 = open("PER_value600.txt", "r")
	file4 = open("WER_value600.txt", "r")
	file5 = open("METEOR-ex_value600.txt", "r")
	file6 = open("TERbase_value600.txt", "r")
	file7 = open("Ol_value600.txt", "r")
	file8 = open("GTM-3_value600.txt", "r")
	file9 = open("ROUGE-L_value600.txt", "r")

	for i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_9 in zip(file1,file2,file3,file4,file5,file6,file7,file8,file9):
		i_1 = float(i_1)
		i_2 = float(i_2)
		i_3 = float(i_3)
		i_4 = float(i_4)
		i_5 = float(i_5)
		i_6 = float(i_6)
		i_7 = float(i_7)
		i_8 = float(i_8)
		i_9 = float(i_9)
		print (i_1+i_2+i_3+i_4+i_5+i_6+i_7+i_8+i_9)