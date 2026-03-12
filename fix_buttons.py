import os
import re

DIR = r'c:/Users/tulik/OneDrive/Desktop/HTML/Project1'

# Match exactly: 
# Group 1: <h2...>...</h2> or <h3...>...</h3>
# Group 2: Any content in between that does *not* contain another h2/h3 or button
# Group 3: <button ... class="explore-btn" ...>...</button>

pattern = re.compile(
    r'(<h[23][^>]*>.*?</h[23]>)'             # The heading
    r'((?:(?!<h[23]|<button|</section>).)*?)' # The middle stuff (usually <ul>...</ul>), making sure not to cross borders
    r'(<button[^>]*class="?explore-btn"?[^>]*>.*?</button>)', # The button
    re.IGNORECASE | re.DOTALL
)

def replace_func(match):
    heading = match.group(1).strip()
    middle = match.group(2)
    button = match.group(3).strip()
    
    # Construct new layout wrapper
    new_html = f'<div class="heading-row">\n        {heading}\n        {button}\n      </div>\n{middle}'
    return new_html

count_files = 0
for filename in os.listdir(DIR):
    if filename.endswith('.html'):
        filepath = os.path.join(DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'explore-btn' in content and 'heading-row' not in content:
            new_content, num_subs = pattern.subn(replace_func, content)
            if num_subs > 0:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated {num_subs} buttons in {filename}')
                count_files += 1

print(f"Done modifying HTML structure in {count_files} files.")
