#SENTENCE COUNT
#python sentence_count.py input.txt
from mrjob.job import MRJob
import re

class MRSentenceCount(MRJob):
    
    # Mapper function to emit each sentence with count 1
    def mapper(self, _, line):
        # Regular expression pattern to split sentences
        sentences = re.split(r'[.!?]', line)
        
        for sentence in sentences:
            # Strip whitespace from the sentence
            sentence = sentence.strip()
            
            # Emit the sentence with count 1
            yield sentence, 1

    # Reducer function to sum up the counts for each sentence
    def reducer(self, sentence, counts):
        # Emit the sentence with its total count
        yield sentence, sum(counts)

if __name__ == '__main__':
    MRSentenceCount.run()
