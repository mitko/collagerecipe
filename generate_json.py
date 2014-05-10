import sys

recipe = sys.argv[1]
rows = []

with open(recipe, 'r') as files:
  curr_row = []
  def save_row():
    global curr_row
    if curr_row:
      rows.append(curr_row)
      curr_row = []
            
  for fname in files:
    fname = fname.replace('\n', '')
    if not fname:
      save_row()
    else:
      curr_row.append({'path': fname})
  save_row()

with open('images.json', 'w') as output:
  ## Really ghetto JSON serialization 
  jsout = str(rows).replace("'", '"')
  print >>output, jsout
        
            
