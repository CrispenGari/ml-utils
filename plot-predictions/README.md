### Plot Predictions

This function is very handy especially when working with image classification because it allows us to plot images with their respective labels. If the prediction is correct then the label text will be shown in `green` else `red`.

```py
from matplotlib import pyplot as plt
def plot_predictions_images(images_and_classes, labels_true, labels_pred, cols=5, rows = 3):
    fig = plt.figure()
    fig.set_size_inches(cols * 2, rows * 2)
    for i, (image, label_true, label_pred) in enumerate(zip(images_and_classes, labels_true.astype("int32"), labels_pred)):
        plt.subplot(rows, cols, i + 1)
        plt.axis('off')
        plt.imshow(image, cmap="gray")
        plt.title(classes[label_true], color ='g' if label_true == label_pred else 'r', fontsize=16 )
```

This function is very easy to use all you have to do is call it and pass parameters to it for example:

```py
plot_predictions_images(images[:24], true_labels[:24], prediction_labels[:24], cols=8)
```
