# Python script to generate all three static pages:
# Felicia Becerra
# 2020-09-24

print('This is my Python script for re-generasting all three website pages.')

python3 open('./templates/top.html').read()

top_html = open('./templates/top.html').read()

python3 open('./templates/bottom.html').read()

bottom_html = open('./templates/top.html').read()

python3 open('./content/index.html').read()

index_contents = open('./content/index.html').read()

python3 open('./content/blog.html').read()

blog_contents = open('./content/blog.html').read()

python3 open('./content/portfolio.html').read()

port_contents = open('./content/portfolio.html').read()

python