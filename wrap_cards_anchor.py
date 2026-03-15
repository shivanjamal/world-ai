import re
import os

files = ["mobile.html", "desktop.html"]

for f in files:
    if os.path.exists(f):
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
        
        # 1. First we need to extract the custom exact href that belonged to that card.
        # We can find the old `<!-- Chatbot -->` comments and `<div class="card-container"...>`
        # This regex will match the card container
        pattern = r'(<div class="card-container" onclick="window\.open\(this\.querySelector\(\'a\'\)\.href, \'_blank\'\)"[^>]+>.*?(<a href="([^"]+)"\s*target="_blank"\s*class="tour-button">.*?</a>).*?</div>\s*</div>)'
        
        def wrap_with_a(match):
            whole_card = match.group(0)
            href = match.group(3)
            # Remove the onclick from the div
            whole_card = re.sub(r'\s*onclick="window\.open\(this\.querySelector\(\'a\'\)\.href, \'_blank\'\)"', '', whole_card)
            # Remove the inner a tag, turn it into a div so it doesn't nest a tags
            whole_card = whole_card.replace(match.group(2), match.group(2).replace('<a href', '<div data-href').replace('</a>', '</div>'))
            
            return f'<a href="{href}" target="_blank" style="text-decoration: none; color: inherit; display: block;">\n{whole_card}\n</a>'

        content_updated = re.sub(pattern, wrap_with_a, content, flags=re.DOTALL)
        
        with open(f, "w", encoding="utf-8") as file:
            file.write(content_updated)

print("done")
