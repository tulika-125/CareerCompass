import os

DIR = r'c:/Users/tulik/OneDrive/Desktop/HTML/Project1'

old_font_tag1 = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">'
old_font_tag2 = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">'

new_font_tag = '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=VT323&display=swap" rel="stylesheet">'

for filename in os.listdir(DIR):
    if filename.endswith('.html'):
        filepath = os.path.join(DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        updated = False
        if old_font_tag1 in content:
            content = content.replace(old_font_tag1, new_font_tag)
            updated = True
        elif old_font_tag2 in content:
            content = content.replace(old_font_tag2, new_font_tag)
            updated = True
            
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated fonts in {filename}')
        else:
            # Maybe it wasn't exact match, or already updated. Let's just do a manual check if Poppins is there.
            if "family=Poppins" in content:
                # Find the line and replace
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if "family=Poppins" in line:
                        lines[i] = f'    {new_font_tag}'
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))
                print(f'Updated fonts (fallback method) in {filename}')

print("Done updating HTML fonts.")
