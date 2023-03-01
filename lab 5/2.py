import re

text = "abshds abbbsjhds sjhfsba  ashdahg abbbb"

txt = re.findall("ab{2,3}",text)
print(txt)
