### Tabulate translation Helper function.

This is a simple helper function for `seq2seq` machine translation that tabulates translation nicely. We can always change the parameters to fit our case. The following is the basic usage of the function.

```py
def tabulate_translations(column_names, data, title, max_characters=25):
  table = PrettyTable(column_names)
  table.title= title
  table.align[column_names[0]] = 'l'
  table.align[column_names[1]] = 'l'
  table.align[column_names[2]] = 'l'
  table._max_width = {column_names[0] :max_characters, column_names[1] :max_characters, column_names[2]:max_characters}
  for row in data:
    table.add_row(row)
  print(table)
columns_names = [
    "German", "English", "Translated"
]
title = "GERMAN to ENGLISH TRANSLATOR"

def translation_table(src, SRC, TRG, model, device,columns_names, title,  max_characters=25,total_translations=10):
  rows_data = []
  for idx in range(total_translations):
    src = vars(test_data.examples[idx])['src']
    trg = vars(test_data.examples[idx])['trg']
    trasl, _ = translate_sentence(src, SRC, TRG, model, device)
    rows_data.append(
        [
        " ".join(src),
        " ".join(trg),
        " ".join(trasl).replace('<eos>', '')
        ],
    )
    if idx+1 != total_translations:
      rows_data.append(["-" * max_characters, "-" * max_characters, "-" * max_characters ])

  tabulate_translations(columns_names, rows_data, title, max_characters)
translation_table(src, SRC, TRG, model, device,columns_names, title, max_characters=30)
```

This was extracted from my pytorch series on `seq2seq` series on notebook number `4`.
