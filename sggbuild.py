# Python script to generate all three static pages using functions.
# Felicia Becerra
# 2020-10-02

print("This is my attempt to build a SGG Python script!")
# Here is the list with all the pages. To add a page, just add it to the list! (You will have to build out that page's content though!)
# [0=index, 1=about, 2=portfolio]

pages = [
	{
		"filename": "content/index.html",
		"output": "docs/index.html",
		"title": "F.A. Becerra - Main Page",
		"active_link_replacement": "active-link"   
	},
	{
		"filename": "content/about.html",
		"output": "docs/about.html",
		"title": "About Me",
		"active_link_replacement": "active-link"   
	},
	{
		"filename": "content/portfolio.html",
		"output": "docs/portfolio.html",
		"title": "My Portfolio",
		"active_link_replacement": "active-link"   
	}
]

# page_title = pages['title']
# page_filename = pages['filename']
# page_output = pages['output']


# Here's where the base (HTML template) is opened.
def main():
	base_html = open("./templates/base.html").read()
	for page in pages:
		apply_template(base_html, page)

# Here is a funtion to replace the replacement links with "active-link", but I couldn't figure out how to get this working.
# def apply_active_link(page):
# 	if page["filename"] == "content/index.html":
# 		page.replace("__replace_index_link__", "active-link")
# 	# elif page["filename"] == "content/about.html":
# 	# 	page.replace("__replace_port_link__", "active-link")
# 	# elif page["filename"] == "content/portfolio.html":
# 	# 	page.replace("__replace_about_link__", "active-link")
	
# Here's what builds all the pages, replacing the contents and title.
def apply_template(template, page):
	final_html = template.replace("__replace_content_here__", get_content(page)).replace("__replace_title__", page["title"])
	publish_page(final_html, page)


# Read in the content of each page file.
def get_content(page):
	return open(page["filename"]).read()

# Publish the actual final HTML file for each page.
def publish_page(text, page):
	open(page["output"], "w+").write(text)


main()


	
