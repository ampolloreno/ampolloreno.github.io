import feedparser
import re

def wrap_latex_with_mathjax(text):
    text = re.sub(r'\$(.*?)\$', r'\(\1\)', text)            # Wrap inline LaTeX with \( ... \)
    text = re.sub(r'\\begin\{equation\}(.*?)\\end\{equation\}', r'\[\1\]', text, flags=re.DOTALL)  # Wrap equation environment with \[ ... \]
    return text

def generate_html(author_last_name):
    base_url = "http://export.arxiv.org/api/query?search_query=au:"
    url = f"{base_url}{author_last_name}&start=0&max_results=100"
    feed = feedparser.parse(url)

    html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ArXiv Papers</title>
    <script type="text/javascript" id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }}

        .header {{
            text-align: center;
            padding: 20px;
        }}

        .header img {{
            width: 150px;
            height: 150px;
            border-radius: 50%;
        }}

        .header h1 {{
            margin-top: 10px;
            margin-bottom: 0;
        }}

        .header p {{
            margin-top: 0;
        }}

        .nav {{
            text-align: center;
            background-color: #333;
            padding: 10px;
        }}

        .nav a {{
            color: #fff;
            text-decoration: none;
            padding: 0 10px;
        }}

        .nav a:hover {{
            text-decoration: underline;
        }}

        .container {{
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
        }}

        .paper {{
            margin-bottom: 20px;
        }}

        .paper h3 {{
            margin-top: 0;
        }}

        .paper a {{
            text-decoration: none;
            color: #1a0dab;
        }}

        .paper a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="header">
        <img src="headshot.jpg" alt="Your headshot">
        <h1>Your Name</h1>
        <p>A summary of your career trajectory, and what you're interested in.</p>
    </div>

    <div class="nav">
        <a href="https://twitter.com/yourusername" target="_blank">Twitter</a> |
        <a href="https://www.linkedin.com/in/yourusername/" target="_blank">LinkedIn</a> |
        <a href="https://github.com/yourusername" target="_blank">GitHub</a> |
        <a href="your-cv.pdf" target="_blank">CV</a>
    </div>

    <div class="container" id="papersContainer">
        {papers}
    </div>

</body>
</html>
    '''

    papers_html = ""

    for entry in feed.entries:
        title = wrap_latex_with_mathjax(entry.title)
        link = entry.link
        abstract = wrap_latex_with_mathjax(entry.summary)
        authors = ', '.join([author['name'] for author in entry.authors])

        paper_html = f'''
<div class="paper">
    <h3><a href="{link}" target="_blank">{title}</a></h3>
    <p><strong>Authors:</strong> {authors}</p>
    <p>{abstract}</p>
</div>
        '''
        papers_html += paper_html

    final_html = html_template.format(papers=papers_html)

    with open(f"{author_last_name}_papers.html", "w") as f:
        f.write(final_html)

# Replace 'Smith' with the desired last name
generate_html("Polloreno")