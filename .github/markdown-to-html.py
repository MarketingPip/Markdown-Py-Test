#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

import requests

PUBLIC_GITHUB_MARKDOWN_URL = 'https://api.github.com/markdown'

input_file = "README.md"
input_file_contents = None

output_file = "test.html"

blog_post_template = ".github/static-gen/html_templates/blog_post.html"


try:
    with open(blog_post_template, 'r') as f:
        blog_post_template_contents = f.read()
except IOError:
    sys.exit('Input file does not exist, or has no content.  Exiting')


# Open our file and
try:
    with open(input_file, 'r') as f:
        input_file_contents = f.read()
except IOError:
    sys.exit('Input file does not exist, or has no content.  Exiting')

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
        f.write(f"""<style>* {
	 box-sizing: border-box;
}
 body {
	 display: flex;
	 justify-content: center;
	 width: 100%;
	 height: calc(max(100vh, 400px));
	 padding: 100px;
	 color: #222;
	 font-family: "Plus Jakarta Sans", sans-serif;
}
 body article {
	 width: 100%;
	 max-width: 1000px;
}
 body article header {
	 display: flex;
	 flex-direction: column;
	 justify-content: space-between;
	 width: 100%;
	 min-height: 400px;
	 padding: 50px;
	 border-radius: 16px;
	 color: #fff;
	 background-position: center;
	 background-repeat: no-repeat;
	 background-size: cover;
}
 body article header .upper-header {
	 display: flex;
	 justify-content: space-between;
	 padding-bottom: 20px;
}
 body article header .upper-header .mini-title {
	 font-size: 1.125rem;
	 font-weight: bold;
	 letter-spacing: 0.4rem;
	 text-transform: uppercase;
	 opacity: 0.9;
}
 body article header .upper-header .date-since {
	 display: flex;
	 align-items: center;
	 opacity: 0.5;
	 font-size: 0.875rem;
}
 body article header .upper-header .date-since .date-value {
	 display: inline-block;
	 padding-bottom: 2px;
}
 body article header .upper-header .date-since svg {
	 width: 20px;
	 margin-left: 10px;
}
 body article header .lower-header {
	 padding-top: 50px;
}
 body article header .lower-header .tags-container {
	 display: flex;
	 align-items: center;
	 opacity: 0.75;
	 margin-bottom: 12px;
}
 body article header .lower-header .tags-container > span:not(:nth-child(2))::before {
	 content: ", ";
}
 body article header .lower-header .tags-container svg {
	 width: 20px;
	 margin-right: 10px;
}
 body article header .lower-header .tags-container span {
	 font-size: 0.875rem;
}
 body article header .lower-header .title {
	 margin: 20px 0;
	 font-size: 3rem;
	 font-weight: bold;
	 opacity: 0.9;
}
 body article header .lower-header .subtitle {
	 width: 50%;
	 margin-top: 10px;
	 opacity: 0.75;
	 line-height: 1.75;
}
 body .summary {
	 width: 100%;
	 display: flex;
	 justify-content: space-between;
	 margin-top: 50px;
	 padding: 30px 50px;
	 border-radius: 16px;
	 box-shadow: 0 0 0 1px #f2f2f2;
}
 body .summary .summary-item {
	 width: 100%;
	 padding-right: 20px;
}
 body .summary .summary-item .item-title {
	 color: #999;
}
 body .summary .summary-item .item-text {
	 margin-top: 12px;
	 font-size: 1.5rem;
}
 body .main-article {
	 width: 100%;
	 margin-top: 50px;
	 padding-bottom: 50px;
	 line-height: 1.75;
}
 body .main-article h4 {
	 margin-top: 60px;
	 margin-bottom: 20px;
	 font-size: 1.25em;
}
 body .main-article p {
	 margin-bottom: 20px;
	 color: #777;
	 font-size: 1.125em;
}
 body .main-article blockquote {
	 position: relative;
	 margin: 40px 0;
	 padding: 40px;
	 background-color: #f8f8f8;
	 border-radius: 16px;
}
 body .main-article blockquote::before {
	 content: url("https://icons.craftwork.design/static/media/QuotesFill.f65b03951f44e212816420b00909f4df.svg");
	 position: absolute;
	 top: -10px;
	 left: -10px;
	 transform: scale(2);
	 opacity: 0.1;
}
 body .main-article blockquote::after {
	 content: url("https://icons.craftwork.design/static/media/QuotesFill.f65b03951f44e212816420b00909f4df.svg");
	 position: absolute;
	 bottom: -10px;
	 right: -10px;
	 transform: scale(2) rotate(180deg);
	 opacity: 0.1;
}
 body .main-article .gallery {
	 display: grid;
	 gap: 20px;
	 grid-template-areas: "img1 img1 img2 img3" "img1 img1 img4 img5";
	 min-height: 400px;
	 margin-top: 40px;
}
 body .main-article .gallery .image-item {
	 min-height: 200px;
	 background-color: #eee;
	 background-position: center;
	 background-repeat: no-repeat;
	 background-size: cover;
	 border-radius: 8px;
	 transition: 250ms;
}
 body .main-article .gallery .image-item:hover {
	 opacity: 0.9;
	 cursor: pointer;
}
 body .main-article .gallery .image-1 {
	 grid-area: img1;
}
 body .main-article .gallery .image-2 {
	 grid-area: img2;
}
 body .main-article .gallery .image-3 {
	 grid-area: img3;
}
 body .main-article .gallery .image-4 {
	 grid-area: img4;
}
 body .main-article .gallery .image-5 {
	 grid-area: img5;
}
 body .main-article .gallery .gallery-mask {
	 position: fixed;
	 top: 0;
	 left: 0;
	 z-index: 1;
	 width: 100vw;
	 height: 100vh;
	 padding: 40px;
	 background-color: #222 88;
	 transition: 500ms;
}
 body .main-article .gallery .gallery-mask img {
	 width: 100%;
	 height: 100%;
	 object-fit: contain;
	 transition: 500ms;
}
 body .main-article .gallery .mask-off {
	 visibility: hidden;
	 background-color: #222 0;
}
 body .main-article .gallery .mask-off img {
	 visibility: hidden;
	 opacity: 0;
}
 @media screen and (max-width: 1024px) {
	 body {
		 padding: 50px;
	}
	 body article header .lower-header .subtitle {
		 width: 100%;
	}
}
 @media screen and (max-width: 768px) {
	 body article header .lower-header .title {
		 word-break: break-all;
	}
	 body article .summary {
		 flex-direction: column;
	}
	 body article .summary .summary-item:not(:last-child) {
		 padding-bottom: 30px;
	}
	 body article .main-article .gallery {
		 grid-template-areas: "img1 img1" "img1 img1" "img2 img3" "img4 img5";
	}
}
 @media screen and (max-width: 425px) {
	 body {
		 padding: 25px;
	}
	 body article header .upper-header .date-since {
		 display: none;
	}
}
 </style> <article>
	<header style="background-image: url('https://images.unsplash.com/photo-1520808663317-647b476a81b9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2073&q=80');">
		<div class="upper-header">
			<div class="mini-title">article</div>
			<div class="date-since">
				<p><span class="date-value" id="sinceData"></span></p>
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 30">
					<defs>
						<style>
							.d {
								width: 20px;
								fill: #fff;
								opacity: .5;
							}
						</style>
					</defs>
					<path class="d" d="M15,0C6.75,0,0,6.75,0,15s6.75,15,15,15,15-6.75,15-15S23.25,0,15,0Zm7.35,16.65h-7.35c-.83,0-1.5-.67-1.5-1.5V7.8c0-.9,.6-1.5,1.5-1.5s1.5,.6,1.5,1.5v5.85h5.85c.9,0,1.5,.6,1.5,1.5s-.6,1.5-1.5,1.5Z" />
				</svg>
			</div>
		</div>
		<div class="lower-header">
			<div class="tags-container">
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
					<defs>
						<style>
							.d {
								width: 20px;
								fill: #fff;
								opacity: .75;
							}
						</style>
					</defs>
					<path class="d" d="M19.22,9.66L10.77,1.21c-.74-.74-1.86-1.21-2.97-1.21H1.67C.75,0,0,.75,0,1.67V7.8c0,1.11,.46,2.23,1.3,2.97l8.45,8.46c1,1,2.62,1,3.62,0l5.94-5.95c.93-.93,.93-2.6-.09-3.62ZM6.96,6.35c-.59,.59-1.56,.59-2.15,0-.59-.59-.59-1.56,0-2.15,.59-.59,1.56-.59,2.15,0,.59,.59,.59,1.56,0,2.15Z" />
				</svg>
				<span>Nature</span><span>Animal</span>
			</div>
			<h1 class="title">Birds, Birds, Birds!</h1>
			<p class="subtitle">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet ut quam sit amet vehicula.</p>
		</div>
	</header>
	<section class="summary">
		<div class="summary-item">
			<h5 class="item-title">Reading Time</h5>
			<p class="item-text"><span class="item-data">6</span> Mins</p>
		</div>
		<div class="summary-item">
			<h5 class="item-title">View</h5>
			<p class="item-text"><span class="item-data">1288</span> Views</p>
		</div>
		<div class="summary-item">
			<h5 class="item-title">Publish Date</h5>
			<p class="item-text"><span class="item-data" id="dateData"></span></p>
		</div>
	</section>
	<section class="main-article">
	{html_response.text}
	
	</section>
</article> """)
except IOError:
    sys.exit(u'Unable to write to file: {0}'.format(output_file))
