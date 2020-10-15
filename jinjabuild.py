# Here's my Jinja build for the SGG website.
# Felicia Becerra
# 2020-10-09

print("Hello, Jinja!")

# This imports glob and then creates a list of content files 
# in the variable 'all_html_files'
import glob
all_html_files = glob.glob("content/*.html")
return(all_html_files)
print("--------------")

import os
file_path = "content/index.html"
file_name = os.path.basename(file_path) 
print(file_name)
name_only, extension = os.path.splitext(file_name) 
print(name_only)


from jinja2 import Template
index_html = open("./content/index.html").read()
template_html = open("./templates/base.html").read() 
template = Template(template_html) 
template.render(
    title="Homepage",
content=index_html, )

# all_html_files = list
# so all_html_files[0] = index, [1] = content, [2] = portfolio

pages = [ ]

def build_pages_dict():
	x = 0
	for page in pages.append({
		file_path = all_html_files(x)
		x = x + 1
		file_name = os.path.basename(file_path) 
		print(file_name)
		name_only, extension = os.path.splitext(file_name) 
		print(name_only)
	})

build_pages_dict()
print(pages)
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