#% python jumble.py  jumble.txt  sowpods.txt –q

from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy as np

class MR_program(MRJob):	
	
	def mapper (self, _,line):
		#true text and table indicator		
		if "?" in line:
			destination = 1
			true = line	
			line = line[0:-2]					
		else:
			destination = 0
			true = line
			
		#turns words into themselves 
		line = ''.join(sorted(list(line)))
		
		yield line, true
	
	def reducer (self, key, values):	
		values = [x for x in values]
		if len(values) > 1:
			c1 = values
			if "?" in c1[0]:
				yield c1[0], values[1:]
		else: # our join missed
			pass	
	
if __name__ == '__main__':
	#change to match the name of the class
	MR_program.run()
