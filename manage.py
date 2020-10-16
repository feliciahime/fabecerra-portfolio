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
# for all_html_files[0] = blog, [1] = index, [2] = content, [3] = portfolio

pages = [ ]
x = 0

#	Blog [0] = "title": "Coming Soon!"
# 	Index [1] =  "title": "F.A. Becerra - Main Page"
# 	About [2] = "title": "About Me"}
# 	Port [3] = "title": "My Portfolio"

title_list = ["Blog", "Home", "About Me", "Portfolio"]

for page in all_html_files:
	file_path = all_html_files[x]
	print(file_path)
	file_name = os.path.basename(file_path) 
	print(file_name)
	name_only, extension = os.path.splitext(file_name) 
	print(name_only)
	print(x)
	pages.append({
		"filename": str(file_path),
		"title": title_list[x],
		"output": "docs/" + str(file_name)})
	x += 1
		
print("Final pages:")
print(pages)


def main():
	base_html = open("./templates/base.html").read()
	for page in pages:
		apply_template(base_html, page)

def apply_active_link(html, page):
	if page["filename"] == "content/index.html":
		return html.replace("__replace_index_link__", "active-link")
	elif page["filename"] == "content/about.html":
		return html.replace("__replace_about_link__", "active-link")
	elif page["filename"] == "content/portfolio.html":
		return html.replace("__replace_port_link__", "active-link")
	elif page["filename"] == "content/blog.html":
		return html.replace("__replace_blog_link__", "active-link")

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

from jinja2 import Template
index_html = open("./content/index.html").read()

# template_html = open("./templates/base.html").read() 
# template = Template(template_html) 

# for pages in pages:
# 	template.render(
# 	    pages=pages,
# 		content=page.file_path,
# 		title=page.title )
# print(template_html)



