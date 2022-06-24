import requests

with open("test.md", "r") as markdown, open("index.html", "w") as html:
    payload = {"text": markdown.read(), "mode": "markdown"}
    html.write(requests.post("https://api.github.com/markdown", json=payload).text)
