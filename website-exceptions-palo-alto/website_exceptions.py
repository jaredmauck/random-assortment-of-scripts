def fetch_line_items():
    with open('websites.txt', 'r') as sites:
        web_sites = sites.read().splitlines()
        return web_sites
nl = '\n'
line_items = fetch_line_items()
for items in line_items:
    with open('input.txt', 'a') as f:
        f.write(f'{nl}{items}/*{nl}*.{items}{nl}*.{items}/*')
