### Simple `plot_confusion_matrix` function

This is a simple function that plots a beautiful confusion matrix.

Args:

```
    labels:         List of real labels
    pred_labels:    list of predicted labels
    classes:        List of class names default [] -> If classnames are not passed then real labels will be used
```

### Packages

You need to make sure that you imported the following packages first:

```py
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
```

### Function

```py
def plot_confusion_matrix(labels:[], pred_labels:[], classes:list=[]):
  fig = plt.figure(figsize = (10, 10))
  ax = fig.add_subplot(1, 1, 1)
  cm = confusion_matrix(labels, pred_labels)

  if len(classes) == 0:
    classes = labels.numpy()

  cm = ConfusionMatrixDisplay(cm, display_labels= classes)
  cm.plot(values_format = 'd', cmap = 'Blues', ax = ax)
  plt.xticks(rotation = 20, color="black", fontsize=15)
  plt.yticks(rotation = 20, color="black", fontsize=15)

```

### Usage Example

```py
plot_confusion_matrix(labels, pred_labels, classes)
```
