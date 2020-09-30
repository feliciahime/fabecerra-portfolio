# Python script to generate all three static pages using functions.
# Felicia Becerra
# 2020-09-29

print("This is my attempt to build a SGG Python script!")
# Here is the list with all the pages. To add a page, just add it to the list!
# [0=index, 1=about, 2=portfolio]
pages = [
	{
		"filename": "content/index.html",
		"output": "docs/index.html",
		"title": "F.A. Becerra - Main Page"   
	},
	{
		"filename": "content/about.html",
		"output": "docs/about.html",
		"title": "About Me"
	},
	{
		"filename": "content/portfolio.html",
		"output": "docs/portfolio.html",
		"title": "My Portfolio"
	}
]

# page_title = pages['title']
# page_filename = pages['filename']
# page_output = pages['output']


print("Here's the main function.")
def main():
	base_html = open('./templates/base.html').read()
	index_contents = open('./content/index.html').read()
	about_contents = open('./content/about.html').read()
	port_contents = open('./content/portfolio.html').read()

	
	for page in pages:	
		final_index_page = base_html.replace("__replace_content_here__", index_contents) 
		open("docs/index.html", "w+").write(final_index_page)
		open(page['output'], 'w+').replace("__replace_title__", pages['title'])

		final_portfolio_page = base_html.replace("__replace_content_here__", port_contents) 
		open("docs/portfolio.html", "w+").write(final_portfolio_page)

		final_about_page = base_html.replace("__replace_content_here__", about_contents) 
		open("docs/index.html", "w+").write(final_about_page)

		open(page['output'], 'w+').replace("__replace_title__", pages['title'])




main()





# content placement suggestion: __replace_content_here__

# content = open(filename, 'r').read() -- need to open and read the file before you can replace
# template.replace("__replace_content_here", open("./locationg-of,replacement", 'r').read())
# open(outputfile name, 'w').write(page)


# def replace_title():
#	for output in pages
#		final_index_html = replace("__replace_title__", pages['title'] 
#		open("docs/index.html", "w+").write(final_index_page)
#
#		final_portfolio_html = base_html.replace("__replace_title__", port_contents) 
#		open("docs/portfolio.html", "w+").write(final_portfolio_page)
#
#		final_about_html = base_html.replace("__replace_title__", ) 
#		open("docs/index.html", "w+").write(final_about_page)
	
