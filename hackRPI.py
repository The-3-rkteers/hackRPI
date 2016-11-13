# testing json comparison

#read in two json files and compare to see if any changes made
#print out any changes in files

sourcefolder = '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/'
targetfolder = '/Users/arnoldas/Desktop/Fall 2016/hackRPI/targetfolder/'
targetfile = '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/'
outputfilenameprefix = 'test1'


sample_json1=[{"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 0, "contentChanged": "true"},
              {"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 3, "contentChanged": "false"}]

sample_json2=[{"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 3, "contentChanged": "false"},
              {"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 3, "contentChanged": "false"}, # duplicity
              {"filePath": '/Users/arnoldas/Desktop/Fall 2016/hackRPI/sourcefolder/', "permission": 1, "contentChanged": "true"}]

# dictionaries are unhashable, let's convert to strings for sorting
sorted_1 = sorted([repr(x) for x in sample_json1])
sorted_2 = sorted([repr(x) for x in sample_json2])
print(sorted_1 == sorted_2)

# in case the dictionaries are all unique or you don't care about duplicities,
# sets should be faster than sorting
set_1 = set(repr(x) for x in sample_json1)
set_2 = set(repr(x) for x in sample_json2)
if set_1 == set_2:
    print "everything is safe and no changes found"

else:
    return chanages

print(set_1 == set_2)

