equation = input("Equation: ")

terms = [[], []]
x = 0
a = 0
co = 0
par_signs = []
# 2x(3+3)/10+9
# [[2, "x"], [[3], [3]], [10], "*/"], [9]

while a < len(equation):
  # Skip =
  if equation[a]=="=":
    a += 1
  # ()
  if len(terms)>2:
    x = -1
  # Before =
  elif equation.find("=")>a:
    x = 1
  # After =
  else:
    x = 0

  if equation[a] in "+-":
    if equation[a-1] not in "+-*/(":
      terms[x].append([0])
    if equation[a]=="-":
      if isinstance(terms[x][-1][-1], str):
        terms[x][-1][-2][0] *= -1
      else:
        terms[x][-1][-1][0] *= -1
  
  elif equation[a] in "*/":
    if isinstance(terms[x][-1][-1], list):
      terms[x][-1].append("")
    terms[x][-1][-1] += equation[a]

  elif equation[a]=="(":
    # 3-(1+1)
    if equation[a-1]=="-":
      term[x].append([[-1], "*"])
    # 2(2+1)
    elif equation[a-1] not in "+*/":
      if isinstance(terms[x][-1][-1], list):
        terms[x][-1].append("")
      terms[x][-1][-1] += equation[a]
    # New partition
    terms.append([])
    # Save Sign
    par_signs.append(equation[a-1])
  
  elif equation[a]==")":
    
    if par_signs[-1] in "-*/":
      terms
  a += 1