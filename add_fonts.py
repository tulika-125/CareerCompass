import os

DIR = r'c:/Users/tulik/OneDrive/Desktop/HTML/Project1'
pages = ['science.html', 'arts.html', 'commerce.html', 'medical.html']

font_tag = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">\n"""

for page in pages:
    filepath = os.path.join(DIR, page)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'fonts.googleapis.com' not in content:
            content = content.replace('</head>', font_tag + '</head>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Added fonts to {page}')
