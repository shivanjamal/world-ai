import re

for filename in ["mobile.html", "desktop.html"]:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Step 1: Remove data-tilt attributes
    # The pattern matches data-tilt and any attribute starting with data-tilt-
    content = re.sub(r'\s*data-tilt(?:-[a-z]+(?:="[^"]*")?)?', '', content)

    # Step 2: Add onclick to make the whole card clickable
    # We replace class="card-container" with class="card-container" onclick="window.open(this.querySelector('a').href, '_blank')"
    # Only if not already added.
    if 'onclick="window.open' not in content:
        content = content.replace('class="card-container"', 'class="card-container" onclick="window.open(this.querySelector(\'a\').href, \'_blank\')"')

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("done")
