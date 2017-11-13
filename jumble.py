#imports mr job
from mrjob.job import MRJob
from mrjob.step import MRStep

#develops class for anagram unjumbler
class MR_program(MRJob):	
	
	def mapper (self, _,line):
		#parses out anagrams to be unjumbled 	
		if "?" in line:
			true = line	
			line = line[0:-2]	
		
		#parses out words that will be evaluated to see if they are a match
		else:
			true = line
			
		#turns words into themselves 
		line = ''.join(sorted(list(line)))
		
		#yields the word, and its original self( contains ? for analgrams )
		yield line, true
	
	def reducer (self, key, values):
		#evaluates all values based on key
		values = [x for x in values]
		
		#if there is a key with values longer than one (ie match for jumble) yields anagram and match
		if len(values) > 1:
			c1 = values
			if "?" in c1[0]:
				yield c1[0], values[1:]
		
		#else, iterates to the next key
		else: 
			pass	
	
if __name__ == '__main__':
	#executes mrjob
	MR_program.run()
	
#execute with % python jumble.py  jumble.txt  sowpods.txt –q
