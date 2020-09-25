# Bash script to generate all three static pages:
# Felicia Becerra
# 2020-09-24

cat ./templates/top.html ./content/portfolio.html ./templates/bottom.html > ./docs/portfolio.html

cat ./templates/top.html ./content/about.html ./templates/bottom.html > ./docs/about.html

cat ./templates/top.html ./content/index.html ./templates/bottom.html > ./docs/index.html