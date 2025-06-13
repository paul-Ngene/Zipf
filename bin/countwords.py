import sys
import argparse
import string
import csv
from collections import Counter
import utilities as util
def count_words(reader):
	"""Count the occurrence of each word in a string."""
	text = reader.read()
	chunks = text.split()
	npunc = [word.strip(string.punctuation) for word in chunks]
	word_list = [word.lower() for word in npunc if word]
	word_counts = Counter(word_list)
	return word_counts
	
with open('data/dracula.txt', 'r') as reader:
	word_counts = count_words(reader)
#print(word_counts)

#def collection_to_csv(collection, num=None):
#	"""Write collection of items and counts in csv format."""
#	collection = collection.most_common()
#	if num is None:
#		num = len(collection)
#	writer = csv.writer(sys.stdout)
#	writer.writerows(collection[0:num])
	
	
util.collection_to_csv(word_counts, num = 10)

def main(args):
	"""Run the command line program."""
	#with open(args.infile, 'r') as reader:
	#	word_counts = count_words(reader)
	word_counts = count_words(args.infile)
	util.collection_to_csv(word_counts, num=args.num)
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=__doc__)
	#parser.add_argument('infile', type=str,
	#help='Input file name')
	parser.add_argument('infile', type=argparse.FileType('r'),
	nargs='?', default='-',
	help='Input file name')
	parser.add_argument('-n', '--num',
	type=int, default=None,
	help='Output n most frequent words')
	args = parser.parse_args()
	main(args)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
