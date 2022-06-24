#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
import re
import requests

PUBLIC_GITHUB_MARKDOWN_URL = 'https://api.github.com/markdown'

input_file = "README.md"
input_file_contents = None

output_file = "test.html"


# Open the templates
blog_post_template = ".github/static-gen/html_templates/blog_post.html"

try:
    with open(blog_post_template, 'r') as f:
        blog_post_template_contents = f.read()
except IOError:
    sys.exit('Template does not exist, or has no content.  Exiting')



# Open our file and
try:
    with open(input_file, 'r') as f:
        input_file_contents = f.read()
        
        
except IOError:
    sys.exit('Input file does not exist, or has no content.  Exiting')

with open(input_file) as f:
    txt = list(f)
    pattern = r'psnr_y:([\d.]+)'
    for line in txt:
        BlogTitle = re.search(pattern, line)[1]
        BlogPostDate = re.search(pattern, line)[2]

    
# Set github url
github_url = PUBLIC_GITHUB_MARKDOWN_URL

# Make the request to github to create markdown
payload = {"text": input_file_contents, "mode": "markdown"}
html_response = requests.post(github_url, json=payload)

# Determine our output file
if output_file:
    output_file = output_file
else:
    output_file = u'{0}.html'.format(input_file)

# ensure we have a .html suffix on our file
if output_file[-5:] != '.html':
    output_file += '.html'

# Write the file out that we have created
try:
    with codecs.open(output_file, 'w', encoding='utf-8') as f:
        f.write(BlogTitle + BlogPostDate)
except IOError:
    sys.exit(u'Unable to write to file: {0}'.format(output_file))
