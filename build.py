# Python script to generate all three static pages:
# Felicia Becerra
# 2020-09-24

# This is my Python script for re-generating all three website pages.
print("First I'm going to create the main function.")




# First step: create a variable with the top.html:
open('./templates/top.html').read()
top_html = open('./templates/top.html').read()

# Second step: create a variable with the bottom.html:
open('./templates/bottom.html').read()
bottom_html = open('./templates/bottom.html').read()

# Third step: create a variable with the index contents:
open('./content/index.html').read()
index_contents = open('./content/index.html').read()

# Fourth step: create a variable with the about contents:
open('./content/about.html').read()
about_contents = open('./content/about.html').read() 

# Fifth step: create a variable with the portfolio contents:
open('./content/portfolio.html').read()
port_contents = open('./content/portfolio.html').read()
 
print('Next build each page.')

# Build the index.html:
index_html = top_html + index_contents + bottom_html
open('./docs/index.html', '+w').write(index_html)

# Build the portfolio.html:
portfolio_html = top_html + port_contents + bottom_html
open('./docs/portfolio.html', '+w').write(portfolio_html)

# Build the about.html:
about_html = top_html + about_contents + bottom_html
open('./docs/about.html', '+w').write(about_html)


