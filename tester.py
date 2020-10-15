# Here's my Jinja build for website.
# Felicia Becerra
# 2020-10-09

import glob
import os


# glob creates a list of all content files in the variable 'all_html_files'.
all_html_files = glob.glob("content/*.html")
print(all_html_files)
print(all_html_files[0])
print("--------------")

# all_html_files = list
# so all_html_files[0] = blog, [1] = index, [2] = content, [3] = portfolio

pages = [ ]
x = 0

for page in all_html_files:
	file_path = all_html_files[x]
	print(file_path)
	file_name = os.path.basename(file_path) 
	print(file_name)
	name_only, extension = os.path.splitext(file_name) 
	print(name_only)
	print(x)
	pages.append({
		"filename": file_path,
		"title": "__replace_me__",
		"output": "docs/" + file_name})
	x += 1
		


print("Final pages:")
print(pages)

print(pages[0])
print(pages[1])

