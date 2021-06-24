from prettytable import PrettyTable
def tabulate(column_names, data):
  table = PrettyTable(column_names)
  for row in data:
    table.add_row(row)
  print(table)

column_names = ["SUBSET", "EXAMPLE(s)"]
data = [
        ["training", len(train_data)],
        ['validation', len(validation_data)],
        ['test', len(test_data)]
]
tabulate(column_names, data)