# Resources

## Read or watch:

- [Regularization (mathematics)](https://en.wikipedia.org/wiki/Regularization_(mathematics))
- [An Overview of Regularization Techniques in Deep Learning](https://www.analyticsvidhya.com/blog/2018/04/fundamentals-deep-learning-regularization-techniques/) (up to "A case study on MNIST data with keras" excluded)
- [L2 Regularization and Back-Propagation](https://jamesmccaffrey.wordpress.com/2017/02/19/l2-regularization-and-back-propagation/)
- [Intuitions on L1 and L2 Regularisation](https://towardsdatascience.com/intuitions-on-l1-and-l2-regularisation-235f2db4c261)
- [Analysis of Dropout](https://pgaleone.eu/deep-learning/regularization/2017/01/10/anaysis-of-dropout/)
- [Early stopping](https://en.wikipedia.org/wiki/Early_stopping)
- [How to use early stopping properly for training deep neural network?](https://stats.stackexchange.com/questions/231061/how-to-use-early-stopping-properly-for-training-deep-neural-network)
- [Data Augmentation | How to use Deep Learning when you have Limited Data](https://medium.com/nanonets/how-to-use-deep-learning-when-you-have-limited-data-part-2-data-augmentation-c26971dc8ced)
- [deeplearning.ai videos](https://www.deeplearning.ai) (Note: I suggest watching these videos at 1.5x - 2x speed):
  - [Regularization](https://www.youtube.com/watch?v=NyG-7nRpsW8&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=6)
  - [Why Regularization Reduces Overfitting](https://www.youtube.com/watch?v=6g0t3Phly2M&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=5)
  - [Dropout Regularization](https://www.youtube.com/watch?v=D8PJAL-MZv8&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=7)
  - [Understanding Dropout](https://www.youtube.com/watch?v=ARq74QuavAo&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=8)
  - [Other Regularization Methods](https://www.youtube.com/watch?v=BOCLq2gpcGU&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=9)

## References:

- [numpy.linalg.norm](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.linalg.norm.html)
- [numpy.random.binomial](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.binomial.html)
- [tf.contrib.layers.l2_regularizer](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/contrib/layers/l2_regularizer.md)
- [tf.layers.Dense#kernel_regularizer](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/layers/Dense.md#kernel_regularizer)
- [tf.losses.get_regularization_loss](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/losses/get_regularization_losses.md)
- [tf.layers.Dropout](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/layers/Dropout.md)
- [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf)
- [Early Stopping - but when?](http://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)
- [L2 Regularization versus Batch and Weight Normalization](https://arxiv.org/pdf/1706.05350)

# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- What is regularization? What is its purpose?
- What are L1 and L2 regularization? What is the difference between the two methods?
- What is dropout?
- What is early stopping?
- What is data augmentation?
- How do you implement the above regularization methods in Numpy? TensorFlow?
- What are the pros and cons of the above regularization methods?

# Requirements

## General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 16.04 LTS using python3 (version 3.5)
- Your files will be executed with numpy (version 1.15)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.4)
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Unless otherwise noted, you are not allowed to import any module except `import numpy as np` and `import tensorflow as tf`
- You are not allowed to use the `keras` module in TensorFlow
- You should not import any module unless it is being used
- All your files must be executable
- The length of your files will be tested using `wc`
- When initializing layer weights, use `tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")`