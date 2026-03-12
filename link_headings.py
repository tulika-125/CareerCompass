import os
import re

DIR = r'c:/Users/tulik/OneDrive/Desktop/HTML/Project1'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    # First, handle the cases where they are wrapped in heading-row
    while '<div class="heading-row">' in content:
        start_idx = content.find('<div class="heading-row">')
        end_idx = content.find('</div>', start_idx) + 6
        if start_idx == -1 or end_idx < 6:
            break
            
        block = content[start_idx:end_idx]
        
        btn_match = re.search(r'<button[^>]*data-page="([^"]+)"[^>]*>.*?</button>', block, re.IGNORECASE | re.DOTALL)
        if not btn_match:
            # Maybe the button isn't here, just remove the div wrapper
            new_block = block.replace('<div class="heading-row">', '').replace('</div>', '')
            content = content[:start_idx] + new_block + content[end_idx:]
            modified = True
            continue
            
        data_page = btn_match.group(1)
        new_block = block[:btn_match.start()] + block[btn_match.end():]
        
        h_matchers = list(re.finditer(r'<h([23])([^>]*)>(.*?)</h\1>', new_block, re.IGNORECASE | re.DOTALL))
        if h_matchers:
            last_h = h_matchers[-1]
            h_tag = last_h.group(1)
            h_attrs = last_h.group(2)
            h_content = last_h.group(3).strip()
            
            # If it already has an 'a' tag (unlikely, but safe), don't wrap
            if '<a href' not in h_content:
                new_h = f'<h{h_tag}{h_attrs}><a href="{data_page}" class="heading-link">{h_content}</a></h{h_tag}>'
                new_block = new_block[:last_h.start()] + new_h + new_block[last_h.end():]
        
        # Remove <div class="heading-row"> and trailing </div>
        new_block = re.sub(r'^\s*<div class="heading-row">\s*', '', new_block, count=1)
        new_block = re.sub(r'\s*</div>\s*$', '\n', new_block)
        
        content = content[:start_idx] + new_block + content[end_idx:]
        modified = True

    # Next, handle any leftover explore buttons not in heading-row
    while True:
        btn_match = re.search(r'<button[^>]*class="?explore-btn"?[^>]*data-page="([^"]+)"[^>]*>.*?</button>', content, re.IGNORECASE | re.DOTALL)
        if not btn_match:
            break
            
        data_page = btn_match.group(1)
        # Find the closes h2/h3 before the button
        before_btn = content[:btn_match.start()]
        
        h_matchers = list(re.finditer(r'<h([23])([^>]*)>(.*?)</h\1>', before_btn, re.IGNORECASE | re.DOTALL))
        if h_matchers:
            last_h = h_matchers[-1]
            h_tag = last_h.group(1)
            h_attrs = last_h.group(2)
            h_content = last_h.group(3).strip()
            
            if '<a href' not in h_content:
                new_h = f'<h{h_tag}{h_attrs}><a href="{data_page}" class="heading-link">{h_content}</a></h{h_tag}>'
                before_btn = before_btn[:last_h.start()] + new_h + before_btn[last_h.end():]
        
        content = before_btn + content[btn_match.end():]
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated", filepath)

for filename in os.listdir(DIR):
    if filename.endswith('.html'):
        process_file(os.path.join(DIR, filename))

print("Done.")
