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

### Setting the table title.

To set the table title all we have to do is to specify the `title` attribute during table creation. Example:

```py
def tabulate(column_names, data):
  table = PrettyTable(column_names)
  table.title= "VISUALIZING SETS EXAMPLES"
  for row in data:
    table.add_row(row)
  print(table)
```

### Columns alignment.

Columns can be either aligned to center `c`, left `l` or right `r` by setting the alignment property. Default is `center`. Example:

```py
def tabulate(column_names, data):
  table = PrettyTable(column_names)
  table.title= "VISUALIZING SETS EXAMPLES"
  table.align[column_names[0]] = 'l'
  table.align[column_names[1]] = 'r'
  for row in data:
    table.add_row(row)
  print(table)

column_names = ["SUBSET", "EXAMPLE(s)"]
row_data = [
        ["training", len(train_data)],
        ['validation', len(valid_data)],
        ['test', len(test_data)]
]
tabulate(column_names, row_data)
```

Output:

```
+-----------------------------+
|  VISUALIZING SETS EXAMPLES  |
+--------------+--------------+
| SUBSET       |   EXAMPLE(s) |
+--------------+--------------+
| training     |        29000 |
| validation   |         1014 |
| test         |         1000 |
+--------------+--------------+
```

### Setting the maximum characters per row in each sentence.

We can do this by setting `_max_width` during table creation. This will ensure that the sentence that has more than `_max_width` will be wraped to a new line. Setting `_max_width` property to the table:

```py
 table._max_width = {"column_name" :max_characters, "column_name" :max_characters, "column_name" :max_characters}
```
