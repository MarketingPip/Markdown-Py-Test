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
var = {}
with open(input_file) as conf:
        for line in conf:
                if ":" in line:
                        name, value = line.split(":")  # Needs replaced with regex match 
                        var[name] = str(value).rstrip() # needs a value added
                        
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

    
data = var 

BlogTitle = data['BlogTitle']
if not data['BlogDate']:
  BlogDate = ""
else:
  BlogDate = data['BlogDate']

if not data['SEO_Title']:
  SiteTitle = "Site Name"
else:
  SiteTitle = data['SEO_Title'] + "| Site Name"

Facebook_Meta = ""

if not data['OG_Title']:
  pass
else:
  Facebook_Meta += """<meta property="og:title" content="Simply Docs Demo">"""

if not data['OG_Image']:
  pass
else:
  Facebook_Meta += """<meta property="og:image" content="./assets/images/OG_image.png">"""


if not data['OG_URL']:
  pass
else:
  Facebook_Meta += """<meta property="og:url" content="https://marketingpipeline.github.io/Simply-Docs/">"""

if not data['OG_Type']:
  pass
else:
  Facebook_Meta += """<meta property="og:type" content="article">"""

if not data['OG_Description']:
  pass
else:
  Facebook_Meta += """<meta property="og:description" content="A Simply Docs / Blog Template built using Simple.css.">"""



# Write the file out that we have created
try:
    with codecs.open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"""<head><title>{SiteTitle}</title>
            <meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">


<script src="https://cdn.jsdelivr.net/npm/prismjs@1.28.0/prism.min.js">
{Facebook_Meta}         


     </head>""" + """
	<style>
	
	body { 
    margin: 0;   /* Remove body margins */
}
	.banner {
  background-image: linear-gradient(rgba(39, 71, 118, 0.6), rgba(39, 71, 118, 0.6)), url(https://images.unsplash.com/photo-1509136561942-7d8663edaaa2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1055&q=80);
  background-size: cover;
  background-position: center;
  color: white;
  text-shadow: 0 0 10px rgba(0,0,0,0.2);
  padding: 80px 0px;
}
.banner h1 {
  font-size: 40px;
  margin-top: 0;
  opacity: 0.8;
}
.banner p {
  font-size: 25px;
  margin-bottom: 0;
  opacity: 0.9;
  font-weight: lighter;
}
.container {
  width: 900px;
  margin: 0px auto;
}
.blogpost-content h2 {
  margin-top: 50px;
  opacity: 0.4;
  font-weight: bolder;
}
.blogpost-content p {
  font-weigh: lighter;

  
}
@media(max-width: 992px) {
  .container {
    width: 700px;
  }
}
@media(max-width: 768px) {
  .container {
    width: 500px;
  }
}
@media(max-width: 480px) {
  .container {
    width: 350px;
  }
}
</style>
<!-- Image and text -->
<div class="banner">
      <div class="container">""" +
     f"<h1>{BlogTitle}</h1>" + 
        f"<p>{BlogDate}</p>" + """
      </div>
    </div>
    <div class="container blogpost-content"> """ +
   html_response.text + """
    </div>
	
	""")
except IOError:
    sys.exit(u'Unable to write to file: {0}'.format(output_file))
