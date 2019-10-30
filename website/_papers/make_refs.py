import os
import re

blocks = []
d = '.'
dirs = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d, o))]
for dir in dirs:
    category = os.path.basename(dir)
    for paper in os.listdir(os.path.join(dir, 'todo')):
        paper = '.'.join(paper.split('.')[:-1]) #remove the file extension
        author = paper.split('-')[0]
        title_doiorarxiv = "-".join(paper.split('-')[1:])
        doiorarxiv = title_doiorarxiv.split('_')[-1]
        doi = True if '|' in doiorarxiv else False

        if re.match('\d{4}.', doiorarxiv):
            arxiv = True
        else:
            arxiv = False

        doiorarxiv = doiorarxiv.replace('|', '/')
        if doi:
            ref = f'doi: {doiorarxiv}'
        elif arxiv:
            ref = f'arxiv: {doiorarxiv}'
        else:
            ref = ''
        lines = [f'{paper}:', f'tags: {category}', ref]
        blocks.append("\n  ".join(lines))

with open('../_gitbib/example/refs.yaml', 'w') as handler:
    handler.write(('\n'.join(blocks)))