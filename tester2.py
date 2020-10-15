# Here's my Jinja build for website.
# Felicia Becerra
# 2020-10-09

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

# os creates the file path and file name.
def create_pages_dict(all_html_files):
	x = 0
	for page in all_html_files:
		file_path = all_html_files[x]
		print(file_path)
		file_name = os.path.basename(file_path) 
		print(file_name)
		name_only, extension = os.path.splitext(file_name) 
		print(name_only)
		append_pages_dict(file_path)
		x += 1
		print(x)


def append_pages_dict(page):
	x = 0
	for page in pages:
		file_path = all_html_files[x]
		pages.append({
			"filename": file_path,
			"title": "__replace_me__",
			"output": "docs/" + file_name})
		x += 1
		

print("Before the function: " + str(pages))
create_pages_dict(all_html_files)

print("After the function:")
print(pages)





# Here's where the base (HTML template) is opened.
def main():
	base_html = open("./templates/base.html").read()
	for page in pages:
		apply_template(base_html, page)

# Here is a funtion to replace the replacement links with "active-link", but I couldn't figure out how to get this working.
def apply_active_link(html, page):
	if page["filename"] == "content/index.html":
		return html.replace("__replace_index_link__", "active-link")
	elif page["filename"] == "content/about.html":
		return html.replace("__replace_about_link__", "active-link")
	elif page["filename"] == "content/portfolio.html":
		return html.replace("__replace_port_link__", "active-link")

	
# Here's what builds all the pages, replacing the contents and title.
def apply_template(template, page):
	final_html = template.replace("__replace_content_here__", get_content(page)).replace("__replace_title__", page["title"])
	final_html = apply_active_link(final_html, page)
	publish_page(final_html, page)


# Read in the content of each page file.
def get_content(page):
	return open(page["filename"]).read()

# Publish the actual final HTML file for each page.
def publish_page(text, page):
	open(page["output"], "w+").write(text)


main()





# --------- The above version is the last manage.py save before converting to tester.
import glob
import os


# glob creates a list of all content files in the variable 'all_html_files'.
all_html_files = glob.glob("content/*.html")
print(all_html_files)
print(all_html_files[0])
print("--------------")

# all_html_files = list
# so all_html_files[0] = blog, [1] = index, [2] = content, [3] = portfolio

# os creates the file path and file name.
def create_pages_dict(all_html_files):
	x = 0
	for item in all_html_files:
		file_path = all_html_files[x]
		print(file_path)
		file_name = os.path.basename(file_path) 
		print(file_name)
		name_only, extension = os.path.splitext(file_name) 
		print(name_only)
		append_pages_dict(file_path)
		x += 1
		print(x)

pages = [ ]


def append_pages_dict(page):
	x = 0
	for page in pages:
		file_path = all_html_files[x]
		pages.append({
			"filename": file_path,
			"title": "__replace_me__",
			"output": "docs/" + file_name})
		x += 1
		print(pages)
		

print("Before the function: " + str(pages))
create_pages_dict(all_html_files)

print("After the function:")
print(pages)


# print(pages)
# 	"filename": "content/index.html",
# 	"title": "F.A. Becerra - Main Page",
# 	"output": "docs/index.html"},
# 	# {"filename": "content/about.html",
# 	# "output": "docs/about.html",
# 	# "title": "About Me"},
# 	# { "filename": "content/portfolio.html",
# 	# "output": "docs/portfolio.html",
# 	# "title": "My Portfolio"}
# 	)
# print(pages)



from jinja2 import Template
index_html = open("./content/index.html").read()
template_html = open("./templates/base.html").read() 
template = Template(template_html) 
template.render(
    title="Homepage",
content=index_html, )











































# The above works
--------------------
# Here's my Jinja build for website.
# Felicia Becerra
# 2020-10-09

import glob
import os


# glob creates a list of all content files in the variable 'all_html_files'.
all_html_files = glob.glob("content/*.html")
print(all_html_files)
print("--------------")

# all_html_files = list
# so all_html_files[0] = blog, [1] = index, [2] = content, [3] = portfolio

# os creates the file path and file name.
# file_path = "content/index.html"

def split_text():
	for page in pages:
		x = 0
		file_path = all_html_files[x]
		x = x + 1
		file_name = os.path.basename(file_path) 
		return print(file_name)
		name_only, extension = os.path.splitext(file_name) 
		return print(name_only)

def build_pages_variables(all_html_files):
	for page in pages:
		# x = 0
		# file_path = all_html_files[x]
		# x = x + 1
		split_text()
		file_name = os.path.basename(file_path) 
		print(file_name)
		name_only, extension = os.path.splitext(file_name) 
		print(name_only)
		return file_path
		return file_name

pages = [ ]


def build_pages_dict(all_html_files):
	pages.append({
		"filename": file_path,
		"title": "__replace_me__",
		"output": "docs/" + file_name})
	return pages

build_pages_variables(all_html_files)
build_pages_dict(all_html_files)
print(pages)



-------



# Here's my Jinja build for website.
# Felicia Becerra
# 2020-10-09

import glob
import os


# glob creates a list of all content files in the variable 'all_html_files'.
all_html_files = glob.glob("content/*.html")
print(all_html_files)
print("--------------")

# all_html_files = list
# so all_html_files[0] = blog, [1] = index, [2] = content, [3] = portfolio

# os creates the file path and file name.
def create_pages_dict(all_html_files):
	for page in pages:
		x = 0
		file_path = all_html_files[x]
		x += 1	
		
file_path = "content/index.html"
file_name = os.path.basename(file_path) 
print(file_name)
name_only, extension = os.path.splitext(file_name) 
print(name_only)

def build_pages_variables(all_html_files):
	for page in pages:
		# x = 0
		# file_path = all_html_files[x]
		# x = x + 1
		file_name = os.path.basename(file_path) 
		print(file_name)
		name_only, extension = os.path.splitext(file_name) 
		print(name_only)
		return file_path
		return file_name

pages = [ ]


def append_pages_dict(all):
	pages.append({
		"filename": file_path,
		"title": "__replace_me__",
		"output": "docs/" + file_name})
	return pages

build_pages_variables(all_html_files)
build_pages_dict(all_html_files)
print(pages)



-------



# os creates the file path and file name.
def create_pages_dict(all_html_files):
	for page in all_html_files:
		x = 0
		file_path = all_html_files[x]
		return file_path
		file_name = os.path.basename(file_path) 
		return file_name
		name_only, extension = os.path.splitext(file_name) 
		return name_only
		append_pages_dict()
		print(all_html_files)
		print(pages)
		x += 1

pages = [ ]


def append_pages_dict():
	pages.append({
		"filename": file_path,
		"title": "__replace_me__",
		"output": "docs/" + file_name})

print("Before the function: " + str(pages))
create_pages_dict(all_html_files)

print("After the function:")
print(pages)






------

def render_templates(all_html_files):
	for page in pages:
		file_path = open(file_path).read()
		template_html = open("./templates/base.html").read()
		template = Template(template_html)
		template.render(
			title = {{ pages.title }},
			content = pages.file_name,)