### Machine Learning Utils

This repository contain various machine learning utils that will be very usefull through out the journey. These utils include some helper functions, and some cool features that will help us to create Nueral Network Faster.

### What are Nueral Networks?

Neural networks are one of the earliest examples of a machine learning model. Neural networks were initially introduced in the 1940s and have risen and fallen several times from popularity. The current generation of deep learning begain in 2006 with an improved training algorithm by Geoffrey Hinton. This technique finally allowed neural networks with many layers (deep neural networks) to be efficiently trained. Four researchers have contributed significantly to the development of neural networks. They have consistently pushed neural network research, both through the ups and downs.

<p align="center">
<img src="https://camo.githubusercontent.com/ba31cda474a75980be12fb8ed3cd217901303f32/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6a656666686561746f6e2f7438315f3535385f646565705f6c6561726e696e672f6d61737465722f696d616765732f636c6173735f315f6c756d696e61726965735f616e6e2e6a7067">
</p>

1. [Yann LeCun](http://yann.lecun.com/)

Facebook and New York University - Optical character recognition and computer vision using convolutional neural networks (CNN). The founding father of convolutional nets.

2. [Geoffrey Hinton](http://www.cs.toronto.edu/~hinton/)

Google and University of Toronto. Extensive work on neural networks. Creator of deep learning and early adapter/creator of backpropagation for neural networks.

3. [Yoshua Bengio](http://www.iro.umontreal.ca/~bengioy/yoshua_en/index.html)

University of Montreal. Extensive research into deep learning, neural networks, and machine learning. He has so far remained entirely in academia.

4. [Andrew Ng](https://www.andrewng.org/)

Badiu and Stanford University. Extensive research into deep learning, neural networks, and application to robotics.

### Introduction to Deep Learning.

Neural networks were one of the first machine learning models. Their popularity has fallen twice and is now on its third rise. Deep learning implies the use of neural networks. The `"deep"` in deep learning refers to a neural network with many hidden layers. Because neural networks have been around for so long, they have quite a bit of baggage.

Neural networks accept input and produce output. The input to a neural network is called the feature vector. The size of this vector is always a fixed length. Changing the size of the feature vector means recreating the entire neural network. Though the feature vector is called a "vector," this is not always the case. A vector implies a 1D array. Historically the input to a neural network was always 1D. However, with modern neural networks, you might see input data, such as:

**1D vector** - Classic input to a neural network, similar to rows in a spreadsheet. Common in predictive modeling.
**2D Matrix** - Grayscale image input to a convolutional neural network (CNN).
**3D Matrix** - Color image input to a convolutional neural network (CNN).
**ND Matrix** - Higher-order input to a CNN.

**Dimensions** The term dimension can be confusing in neural networks. In the sense of a 1D input vector, dimension refers to how many elements are in that 1D array. For example, a neural network with ten input neurons has ten dimensions. However, now that we have CNN's, the input has dimensions too. The input to the neural network will usually have 1, 2, or 3 dimensions. Four or more dimensions are unusual. You might have a 2D input to a neural network that has 64x64 pixels. This configuration would result in 4,096 input neurons. This network is either 2D or 4,096D, depending on which set of dimensions you are referencing.

### Classification or Regression

Like many models, neural networks can function in classification or regression:

1. **Regression** - You expect a number as your neural network's prediction.

2. **Classification** - You expect a class/category as your neural network's prediction.

<p align="center">
<img src="https://camo.githubusercontent.com/a9afdb1af22b3ba06600c7a322f1b483d384c831/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6a656666686561746f6e2f7438315f3535385f646565705f6c6561726e696e672f6d61737465722f696d616765732f636c6173735f325f616e6e5f636c6173735f7265672e706e67"/>
</p>

### Neurons and Layers

Most neural network structures use some type of neuron. Many different kinds of neural networks exist, and programmers introduce experimental neural network structures all the time. Consequently, it is not possible to cover every neural network architecture. However, there are some commonalities among neural network implementations. An algorithm that is called a neural network will typically be composed of individual, interconnected units even though these units may or may not be called neurons. The name for a neural network processing unit varies among the literature sources. It could be called a node, neuron, or unit.

1. An Artificial Neuron

<p align="center">
 <img src="https://camo.githubusercontent.com/68cab574ea15db154bbf8cf154a6eee685a63f9f/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6a656666686561746f6e2f7438315f3535385f646565705f6c6561726e696e672f6d61737465722f696d616765732f636c6173735f325f61627374726163745f6e6e2e706e67"/>
</p>

The artificial neuron receives input from one or more sources that may be other neurons or data fed into the network from a computer program. This input is usually floating-point or binary. Often binary input is encoded to floating-point by representing true or false as 1 or 0. Sometimes the program also depicts the binary input as using a bipolar system with true as one and false as -1.

An artificial neuron multiplies each of these inputs by a weight. Then it adds these multiplications and passes this sum to an activation function. Some neural networks do not use an activation function.

2. Three Neuron Neural Network

<p align="center"><img src="https://camo.githubusercontent.com/7a25d677add6186277320efc1ab43e7e1256201e/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6a656666686561746f6e2f7438315f3535385f646565705f6c6561726e696e672f6d61737465722f696d616765732f616e6e2d73696d706c652e706e67"/></p>
