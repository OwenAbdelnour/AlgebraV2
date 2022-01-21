equation = input("Equation: ")

terms = [[[[0]]], [[[0]]]]
x = 0
a = 0
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

  # Modifier Control
  if isinstance(terms[x][-1][-1], list):
    mc = -1
  else:
    mc = -2

  # +-
  if equation[a] in "+-":
    # New term
    if equation[a-1] not in "+-*/(":
      terms[x].append([[0]])
    # Negative sign
    if equation[a]=="-":
      if terms[x][-1][mc][0] != "-":
        terms[x][-1][mc][0] = "-"
      else:
        terms[x][-1][mc][0] = 0
  
  # */
  elif equation[a] in "*/":
    terms[x][-1].append([0])
    if isinstance(terms[x][-1][-1], list):
      terms[x][-1].append("")
    terms[x][-1][-1] += equation[a]

  # (
  elif equation[a]=="(":
    # 3-(1+1)
    if equation[a-1]=="-":
      terms[x].append([[-1], "*"])
      par_signs.append("*")
    # 3*(1+1) | 6/(1+1)
    elif equation[a-1] in "*/":
      del terms[x][-1][-2]
      par_signs.append(equation[a-1])
    # 2(2+1)
    elif equation[a-1] != "+":
      if isinstance(terms[x][-1][-1], list):
        terms[x][-1].append("")
      terms[x][-1][-1] += "*"
      par_signs.append("*")
    # New partition
    terms.append([[[0]]])
  
  # )
  elif equation[a]==")":
    # Find term to add partition
    if len(terms)>3 or equation.find("=")>a:
      y = -2
    else:
      y = 0
    # Add partition based off saved sign
    if par_signs[-1] in "-*/":
      terms[y][-1].insert(-1, terms[-1])
    else:
      terms[y].append(terms[-1])
    # Delete partition and saved sign
    del par_signs[-1]
    del terms[-1]

  # Numbers and Varibles
  else:
    # Numbers
    if equation[a] in ".0123456789":
      terms[x][-1][mc][0] = int(str(terms[x][-1][mc][0])+equation[a])
    # Varibles
    else:
      if len(terms[x][-1][mc])==1:
        terms[x][-1][mc].append("")
      terms[x][-1][mc][1] += equation[a]
  a += 1
  print(terms)

def display():
  eq = []
  def inner(term):
    pass

  # Main Loop
  for term in terms:
    inner(term)

  # Print Loop
  for i in eq:
    print(i, end="")
  print()
display()