import os
import inspect
import re

__all__ = [
	'run_here',
	'converter'
]

class run_here():
	def __init__(self):
		self.orig_path = None
	
	def start(self):
		self.orig_path = os.getcwd()
		caller_path = os.path.split(inspect.stack()[1].filename)[0]
		os.chdir(caller_path)
	
	def end(self):
		os.chdir(self.orig_path)
		self.orig_path = None
	
	def path(self, path):
		self.orig_path = os.getcwd()
		os.chdir(path)

def converter(path):
	with open(path, 'r', encoding = 'UTF-8') as game_file:
		data = re.sub(r', *//.*', ',', game_file.read()) #Remove comment
		data = re.sub(r': *\.', ': 0.', data) #Remove float-like(.1, .2, ...)
		data = data.strip() #Remove space at start and end
		list_data = data.split('\n') #Prepare for get first line and last line
		while '"' not in list_data[1]:
			data = data[len(list_data[0]):-len(list_data[-1])].strip() #Remove first line and last line
			list_data = data.split('\n') #Overwrite list_data with new data
		
		data = data.replace(list_data[0], '{') #Let first line turn into "{"
		data = data.replace(list_data[len(list_data)-1], '}') #Let last line turn into "}"
	
	return data