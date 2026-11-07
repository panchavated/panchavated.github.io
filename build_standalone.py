import re

def build():
    with open('d:/Portfolio/test.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('d:/Portfolio/styles.css', 'r', encoding='utf-8') as f:
        css = f.read()

    with open('d:/Portfolio/script.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # Inline CSS
    html = html.replace('<link rel="stylesheet" href="styles.css">', f'<style>\n{css}\n</style>')
    # Inline JS
    html = html.replace('<script src="script.js"></script>', f'<script>\n{js}\n</script>')

    with open('d:/Portfolio/test-standalone.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Created test-standalone.html")

if __name__ == '__main__':
    build()
