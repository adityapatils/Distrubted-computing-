#CHAR_COUNT
#python char_count.py input.txt
from mrjob.job import MRJob

class MRCharCount(MRJob):
    
    # Mapper function to emit each character with count 1
    def mapper(self, _, line):
        for char in line.strip():
            yield char, 1

    # Reducer function to sum up the counts for each character
    def reducer(self, char, counts):
        yield char, sum(counts)

if __name__ == '__main__':
    MRCharCount.run()
