################################################################################
# ReadFolder.py
# Author: Ming-Cee Yee
# Date Created: 2015-09-24
# Reference: http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
################################################################################

from os import walk

# def gallery(request):
# 	path = ""
# 	img_list =os.listdir(path)
# 	return render_to_response('gallery.html', {'images': img_list})



f = []
for (dirpath, dirnames, filenames) in walk(mypath):
	f.extend(filenames)