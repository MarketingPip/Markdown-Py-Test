#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
import re
import requests
import json

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




var = {}
with open(input_file) as conf:
        for line in conf:
                if ":" in line:
                        name, value = line.split(":")
                        var[name] = str(value).rstrip()
globals().update(var)

    
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

    
data = json.load(f)    

BlogTitle = data['psnr_y']
# Write the file out that we have created
try:
    with codecs.open(output_file, 'w', encoding='utf-8') as f:
        f.write(BlogTitle)
except IOError:
    sys.exit(u'Unable to write to file: {0}'.format(output_file))
