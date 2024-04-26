#WORD_COUNT
#python word_count.py input.txt
from mrjob.job import MRJob
import re

# Regular expression pattern to match words
WORD_REGEXP = re.compile(r"\w+")

class MRWordCount(MRJob):
    
    # Mapper function to emit each word with count 1
    def mapper(self, _, line):
        for word in WORD_REGEXP.findall(line):
            yield word.lower(), 1

    # Reducer function to sum up the counts for each word
    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()
