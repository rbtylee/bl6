with open('mini.install','r') as f:
    mini = f.readlines()

with open('now2.installed','r') as f:
    now = f.readlines()

for i in now:
   if i not in mini:
      print(i.strip())
 
