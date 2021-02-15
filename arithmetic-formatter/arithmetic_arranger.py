def arithmetic_arranger(problems, solve=False):

  arranged_problems = []
  first_num_line = ''
  ops_second_num_line = ''
  dashes = ''
  answers = ''

  if len(problems) > 5:
    return('Error: Too many problems.')

  for problem in problems:
    parts = problem.split()
    if parts[1] != '+' and parts[1] != '-':
      return "Error: Operator must be '+' or '-'."

    if len(parts[0]) > 4 or len(parts[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    if parts[0].isdigit() and parts[2].isdigit():
      length = max([len(parts[0]),len(parts[2])]) + 2
      first_num_line += f'{parts[0]:>{length}}    '
      ops_second_num_line += f'{parts[1]}{parts[2]:>{length-1}}    '
      dashes += '-' * length + '    '

      if solve:
        if parts[1] == '+':
          answer = eval(parts[0]) + eval(parts[2])
        else:
          answer = eval(parts[0]) - eval(parts[2])

        answers += f'{answer:>{length}}    '
    else:
      return "Error: Numbers must only contain digits."

  first_num_line = first_num_line.rstrip(' ')
  ops_second_num_line = ops_second_num_line.rstrip()
  dashes = dashes.rstrip()

  arranged_problems = first_num_line + '\n' + ops_second_num_line + '\n' + dashes

  if solve:
    answers = answers.rstrip()
    arranged_problems += '\n' + answers

  return arranged_problems