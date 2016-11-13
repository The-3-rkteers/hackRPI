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


import os, json
import pandas as pd

#for filesystem before downloading anything or possibility of damage
json_filesSource = [pos_json for pos_json in os.listdir(sourcefolder) if pos_json.endswith('.json')]
print json_filesSource

for js in json_filesSource:
    with open(os.path.join(sourcefolder, js)) as json_file:
        contentSource.append(json.load(json_file))
        #print json.load(json_file)
        print contentSource

#for filesystem after changes are made
json_filesTarget = [pos_json for pos_json in os.listdir(targetfolder) if pos_json.endswith('.json')]
print json_filesTarget

for js in json_filesTarget:
    with open(os.path.join(targetfolder, js)) as json_file:
        contentTarget.append(json.load(json_file))
        #print json.load(json_file)
        print contentTarget

'''
json_pattern = os.path.join(sourcefolder,'*.json')
file_list = glob.glob(json_pattern)
print file_list
for file in file_list:
  contentSource.append(file.read())
  print contentSource

json_pattern = os.path.join(sourcefolder,'*.json')
file_list = glob.glob(json_pattern)
for file in file_list:
  contentTarget.append(file.read())
'''

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

print "printing sorted_1 : from contentsource: ", sorted_1
print "printing sorted_2 : from contenttarget: ", sorted_2

# in case the dictionaries are all unique or you don't care about duplicities,
# sets should be faster than sorting
set_1 = set(repr(x) for x in contentTarget)
set_2 = set(repr(x) for x in contentTarget)
if set_1 == set_2:
    print "\neverything is safe and no changes found\n"

else:
    #add code for when cahnges are found
    print "\nchanges found here: \n"

print "Prints true if filesystem doesnt have changes and youre safe\n" \
      "False printed if changes found:\n" \
      "Result: "
print(set_1 == set_2)

