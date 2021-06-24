### Tabulating the data.

This helper function will helps us to tabulate data (printing the data in a beautiful table format). This function is very simple to use and it is generic, we can change the parameters to fit our data:

```py
from prettytable import PrettyTable
def tabulate(column_names, data):
  table = PrettyTable(column_names)
  for row in data:
    table.add_row(row)
  print(table)
```

### Usage

This is how you can use it:

- You just have to pass column names as a list or a tuple
- You then data which is a 2D list of list or tuple of tuples.

**Note:** The length of columns must be equal to the length of each row, meaning:

```py
len(column_names) == len(data[0])
```

```py
column_names = ["SUBSET", "EXAMPLE(s)"]
data = [
        ["training", len(train_data)],
        ['validation', len(validation_data)],
        ['test', len(test_data)]
]
tabulate(column_names, data)
```

### Output

```
+------------+---------+
|   SUBSET   | EXAMPLE |
+------------+---------+
|  training  |  29000  |
| validation |   1014  |
|    test    |   1000  |
+------------+---------+
```
