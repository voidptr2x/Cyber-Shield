<div align="center"> 
Cyber Shield
<p>The Official Cyber Shield Application Repo.</p>
<p>Helping the community protect their networks!</p>
</div>

# Config Use Example
Call the ``Config`` class to retrieve all information from JSON file then use class properities to get the values
```
cfg = Config()

if len(cfg.term.size) == 0: return
term_row_sz = cfg.term.size[0] # Row
term_col_sz = cfg.term.size[1] # Column
```

# Config File
Special field addition value '_c' added to them represents '_color' and '_p' short for '_position'

See ``vars.py (/cores/utilities/config/vars.py)`` for a list of properities to use!