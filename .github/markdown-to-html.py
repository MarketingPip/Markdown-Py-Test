import requests

with open("README.md", "r") as markdown, open("index.html", "w") as html:
    payload = {"text": markdown.read(), "mode": "markdown"}
    html.write(requests.post("https://api.github.com/markdown", json=payload).text)
