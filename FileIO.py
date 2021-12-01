import easygui as eg
import pandas as pd
import os
import csv
import time
from datetime import datetime
from stat import S_IREAD, S_IWUSR

####################### FILE IO ###########################


def get_directory(title = "Choose Directory"):
	return eg.diropenbox(title)


def write_line(filepath, data_dict):

	with open(filepath, 'a') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = data_dict.keys.tolist())
		writer.writerow(data_dict)
		
	#read into pandas dataframe - works, quick to code
	#and is likely easy to extend - but one line doesn't really need it - likely quicker ways to do it
	#df = pd.DataFrame(data_dict).T
	
	#save to csv - append, no index, no header
	#df.to_csv(filepath, header=False, mode='a', index=False)

def start_file(directory, name, headers_list):
	dt = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	filename = '{test_name} {date}.csv'.format(\
				test_name = name, date = dt)
	
	filepath = os.path.join(directory, filename)
	
	return filepath

def get_filepath():
	return eg.fileopenbox(title = "Select the Log to Graph", filetypes = [['*.csv', 'CSV Files']], multiple = False)

def get_multiple_filepaths():
	return eg.fileopenbox(title = "Select the Log(s) to Graph", filetypes = [['*.csv', 'CSV Files']], multiple = True)

def ensure_subdir_exists_dir(filedir, subdir_name):
	candidate_dir = os.path.join(filedir, subdir_name)
	if not os.path.exists(candidate_dir):
		os.makedirs(candidate_dir)
	return candidate_dir
			
def ensure_subdir_exists_file(filepath, subdir_name):
	return ensure_subdir_exists(os.path.dirname(filepath), subdir_name)

def write_data(filepath, data, printout=False):
	data["Log_Timestamp"] = time.time()
	
	if(printout):
		print(data)
	
	write_line(filepath, data)
	
def set_read_only(filepath):
	#make the file read-only so we don't lose decimal places if the CSV is opened in excel
	os.chmod(filepath, S_IREAD)

def allow_write(filepath):
	#make the file writable 
	#https://stackoverflow.com/questions/28492685/change-file-to-read-only-mode-in-python
	os.chmod(filepath, S_IWUSR|S_IREAD)
