import re

for filename in ["mobile.html", "desktop.html"]:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    def replacer(match):
        inner = match.group(1)
        return f'<button class="tour-button">{inner}</button>'
        
    content = re.sub(r'<a href="[^"]*" target="_blank" class="tour-button">(.*?)</a>', replacer, content, flags=re.DOTALL)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
