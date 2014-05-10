import sys

spec = sys.argv[1]
# spec = 'spec.files.italy'
rows = []

with open(spec, 'r') as files:
    curr_row = []
    def save():
        global curr_row
        if curr_row:
            rows.append(curr_row)
            curr_row = []
            
    for fname in files:
        fname = fname.replace('\n', '')
        if not fname:
            save()
        else:
            curr_row.append({'path': fname})
    save()

with open('images.json', 'w') as output:
    jsout = str(rows).replace("'", '"')
    print >>output, jsout
        
            
