# testing json comparison
# NEW reading in multiple JSON files from a sourceFolder
# AND reading in after making changes all JSON files from a targerFolder

#read in two json files and compare to see if any changes made
#print out any changes in files

import json

sourcefolder = '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/'
targetfolder = '/Users/arnoldas/Desktop/Fall 2016/hackRPI/targetfolder/'
targetfile = '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/'
outputfilenameprefix = 'test1'


import os
import glob

contentSource = []
contentTarget = []
#json_dir_name = "/path/to/json/dir"

json_pattern = os.path.join(sourcefolder,'*.json')
file_list = glob.glob(json_pattern)
for file in file_list:
  contentSource.append(read(file))

json_pattern = os.path.join(sourcefolder,'*.json')
file_list = glob.glob(json_pattern)
for file in file_list:
  contentTarget.append(read(file))


'''
#reading all files into memory for source files
rawDataSource = sourcefolder.read()
changedDataSource = rawDataSource.replace('][', ']<SPLIT>[')

#splitting the string into an array of strings for source files
splitDataSource = changedDataSource.split('<SPLIT>')

#load each string individually for source files
parsedDataSource = [json.loads(bit_of_data) for bit_of_data in splitDataSource]


#reading all files into memory for target files
rawDataTarget = targetfolder.read()
changedDataTarget = rawDataTarget.replace('][', ']<SPLIT>[')

#splitting the string into an array of strings for target files
splitDataTarget = changedDataTarget.split('<SPLIT>')

#load each string individually for target files
parsedDataTarget = [json.loads(bit_of_data) for bit_of_data in splitDataTarget]
'''

'''
#test data
sample_json1=[{"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 0, "contentChanged": "true"},
              {"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 3, "contentChanged": "false"}]

sample_json2=[{"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 3, "contentChanged": "false"},
              {"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 3, "contentChanged": "false"}, # duplicity
              {"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 1, "contentChanged": "true"}]
'''

# dictionaries are unhashable, let's convert to strings for sorting
sorted_1 = sorted([repr(x) for x in contentSource])
sorted_2 = sorted([repr(x) for x in contentSource])
print(sorted_1 == sorted_2)

# in case the dictionaries are all unique or you don't care about duplicities,
# sets should be faster than sorting
set_1 = set(repr(x) for x in contentTarget)
set_2 = set(repr(x) for x in contentTarget)
if set_1 == set_2:
    print "\neverything is safe and no changes found\n"

else:
    print "\nchanges found here: \n"

print(set_1 == set_2)

