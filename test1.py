def arithmetic_arranger(problems, answers=None):

  # Check problem limit
  if len(problems) > 5:
    return "Error: Too many problems."

  # Parse individual pieces from problems
  temp = []

  for row in problems:
    row = row.split()
    temp.append(row)

  # Iterate over split operations into new list
  canvas = ["", "", "", ""]

  for i in temp:

    # Check if valid operation
    if i[1] != "+" and i[1] != "-":
      return "Error: Operator must be '+' or '-'."

    # Check if numbers are digits
    if not i[0].isdigit() or not i[2].isdigit():
      return "Error: Numbers must only contain digits."

    # Store length of numbers for each problem
    len_top_num = len(i[0])
    len_bot_num = len(i[2])

    # Find longest number for each problem
    longer_num = max(len_top_num, len_bot_num)

    # Check if numbers are more than 4 digits
    if longer_num > 4:
      return "Error: Numbers cannot be more than four digits."

    # Design layers of string
    canvas[
      0] += f"  {''.join(' ' for x in range(longer_num - len_top_num) if len_bot_num == longer_num)}{i[0]}    "
    canvas[
      1] += f"{i[1]} {''.join(' ' for x in range(longer_num - len_bot_num) if len_top_num == longer_num)}{i[2]}    "
    canvas[2] += f"--{''.join('-' for x in range(longer_num))}    "

    # Design answer layer
    if answers == True:
      if i[1] == '+':
        i.append(str((int(i[0]) + int(i[2]))))
      if i[1] == '-':
        i.append(str((int(i[0]) - int(i[2]))))

      len_result_num = len(i[3])

      canvas[
        3] += f"{''.join(' ' for x in range(longer_num + 2 - len_result_num))}{i[3]}    "

  # Combine all layers into final string
  arranged_problems = ""

  for i in canvas:
    arranged_problems += f"{i.rstrip()}\n"



  # Return completed string
  return arranged_problems.rstrip()

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

