### Plot Images Helper Function.

This function helps us to plot images, very useful function in computer vision task to visualize some images that are in the data set:

```py
import matplotlib.pyplot as plt
def plot_images(images, labels, cols=5):
    rows = 3
    fig = plt.figure()
    fig.set_size_inches(cols * 2, rows * 2)
    labels = np.argmax(labels, axis=1)
    for i, (image, label) in enumerate(zip(images, labels)):
        plt.subplot(rows, cols, i + 1)
        plt.axis('off')
        plt.imshow(image, cmap="gray")
        plt.title(classes[label], color ='g', fontsize=16 )

```

This function is very easy to use all you have to do is to all it and pass the required parameters for example:

```py
plot_images(images[:24], true_labels[:24], cols=8)

```
