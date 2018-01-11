import arxiv
OLD_BIB = "bibliography.bib.old"
BIB = "bibliography.bib"
ARXIV = 'arxiv.txt'
bibtex = """@article{{{},
    title  = {{{}}},
    author = {{{}}},
    link   = {{{}}},
    field  = {{{}}},
    prog = {{{}}}
}}

"""

with open(OLD_BIB, 'r') as filehandler:
    text = filehandler.read()
new_bib = text
with open(ARXIV, 'r') as filehandler:
    for arxiv_link in filehandler:
        doi, field, status = arxiv_link.strip().split(' ')
        print("Retrieving {}!".format(doi))
        if status == '.':
            status = ""
        query = arxiv.query(doi)
        link = query[0]['links'][-1]['href']
        authors = query[0]['authors']
        title = query[0]['title'].replace("\n ", "")
        new_bib += "\n"
        description = str(arxiv.query(doi)[0]['published_parsed'].tm_year) + '_' + str(arxiv.query(doi)[0]['published_parsed'].tm_mon) + '_' +  authors[0].replace(' ', '')
        new_bib += bibtex.format(description, title, " & ".join(authors), link, field, status)

with open(BIB, 'w') as filehandler:
     filehandler.write(new_bib)
