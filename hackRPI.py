# testing json comparison

#read in two json files and compare to see if any changes made
#print out any changes in files

sourcefolder = '/Users/arnoldas/Desktop/Fall 2016/ASRC/sourcefolder/'
targetfolder = '/Users/arnoldas/Desktop/Fall 2016/ASRC/targetfolder/'
targetfile = '/Users/arnoldas/Desktop/Fall 2016/ASRC/sourcefolder/20161002_reconstruction_wind_data.csv'
outputfilenameprefix = 'test1'


sample_json1=[{"filePath": 72, "permission": 0, "contentChanged": "true"},
              {"filePath": 77, "permission": 3, "contentChanged": "false"}]

sample_json2=[{"filePath": 77, "permission": 3, "contentChanged": "false"},
              {"filePath": 77, "permission": 3, "contentChanged": "false"}, # duplicity
              {"filePath": 72, "permission": 0, "contentChanged": "true"}]

# dictionaries are unhashable, let's convert to strings for sorting
sorted_1 = sorted([repr(x) for x in sample_json1])
sorted_2 = sorted([repr(x) for x in sample_json2])
print(sorted_1 == sorted_2)

# in case the dictionaries are all unique or you don't care about duplicities,
# sets should be faster than sorting
set_1 = set(repr(x) for x in sample_json1)
set_2 = set(repr(x) for x in sample_json2)
print(set_1 == set_2)
