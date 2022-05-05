from bs4 import BeautifulSoup

HEADER = """<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" epub:prefix="z3998: http://www.daisy.org/z3998/2012/vocab/structure/, se: https://standardebooks.org/vocab/1.0" xml:lang="en-US">
	<head>
		<title>{title}</title>
		<link href="../css/core.css" rel="stylesheet" type="text/css"/>
		<link href="../css/se.css" rel="stylesheet" type="text/css"/>
	</head>
    <body epub:type="bodymatter">
"""

FOOTER = """    </body>
</html>
"""

def proc_chap(fn):
    doc = BeautifulSoup(open(fn, 'r'), 'lxml')
    paras = doc.select('p')
    seen_page_num = False
    out_paras = []

    for p in paras:
        if p.get('align') == 'RIGHT' and 'Page' in p.text:
            seen_page_num = True
        elif 'TABLE OF CONTENTS' in p.text:
            # Next chapter link, so skip
            seen_page_num = False
        else:
            if (seen_page_num and out_paras and
                not p.text.split()[0].istitle() and
                not out_paras[-1].text[-1] in '.!?'):
                # This is probably the same paragraph, so copy the contents
                # over to the previous paragraph.
                for c in p.children:
                    out_paras[-1].append(c)
            else:
                out_paras.append(p)
            seen_page_num = False

    with open(fn.replace('otext', 'text').replace('.html', '.xhtml'), 'w') as output:
        output.write(HEADER.format(title=doc.select_one('title').text))
        for p in out_paras:
            output.write(p.prettify())
        output.write(FOOTER)

if __name__ == '__main__':
    import sys
    for fn in sys.argv[1:]:
        print(f'Processing {fn}...')
        proc_chap(fn)

