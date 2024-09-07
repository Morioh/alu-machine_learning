# Neural Style Transfer: Creating Art with Deep Learning

This project explores Neural Style Transfer (NST) using TensorFlow's `tf.keras` and Eager Execution. It focuses on applying deep convolutional networks (CNNs) to create artistic images by merging the content of one image with the style of another.

## Resources

### Read or Watch:
- [Neural Style Transfer: Creating Art with Deep Learning using tf.keras and Eager Execution](https://medium.com/tensorflow/neural-style-transfer-creating-art-with-deep-learning-using-tf-keras-and-eager-execution-7d541ac31398) 
- [deeplearning.ai](https://www.deeplearning.ai)
- [What is Neural Style Transfer?](https://www.youtube.com/watch?v=R39tWYYKNcI&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=38)
- [What are deep CNNs learning?](https://www.youtube.com/watch?v=ChoV5h7tw5A&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=39)
- [Cost Function](https://www.youtube.com/watch?v=xY-DMAJpIP4&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=39)  
  - [Content Cost Function](https://www.youtube.com/watch?v=b1I5X3UfEYI&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=40)  
  - [Style Cost Function](https://www.youtube.com/watch?v=QgkLfjfGul8&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=42)
- [Eager Execution](https://www.tensorflow.org/guide/basics)
- [A Neural Algorithm of Artistic Style](https://arxiv.org/pdf/1508.06576)

### Advanced Readings:
- [Total Variation Denoising](https://en.wikipedia.org/wiki/Total_variation_denoising)
- [tf.image.total_variation](https://www.tensorflow.org/api_docs/python/tf/image/total_variation)
- [Nonlinear Total Variation Based Noise Removal Algorithms](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.117.1675&rep=rep1&type=pdf)
- [Neural Style Transfer: A Review](https://arxiv.org/pdf/1705.04058)
- [Deep Photo Style Transfer](https://arxiv.org/abs/1703.07511)
- [Controlling Perceptual Factors in Neural Style Transfer](https://arxiv.org/abs/1611.07865)
- [Instance Normalization: The Missing Ingredient for Fast Stylization](https://arxiv.org/abs/1607.08022)
- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/abs/1603.08155)
- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution: Supplementary Material](https://arxiv.org/abs/1603.08155)
- [A Pragmatic AI Approach to Creating Artistic Visual Variations by Neural Style Transfer](https://arxiv.org/abs/1705.04058)

## Learning Objectives
By the end of this project, you will be able to explain the following concepts clearly:

### General :
- **What is Neural Style Transfer?**
- **What is a Gram Matrix?**
- **How to calculate style cost**
- **How to calculate content cost**
- **What is TensorFlow’s Eager Execution?**
- **What is Gradient Tape and how do you use it?**
- **How to perform Neural Style Transfer**

## Requirements

### General :
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 16.04 LTS using Python 3.5
- Use `numpy` version 1.15 and `tensorflow` version 1.12
- Files must end with a new line
- First line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file is mandatory at the root of the project folder
- Code must follow `pycodestyle` style (version 2.4)
- Modules, classes, and functions should have proper documentation
- Only `numpy` and `tensorflow` imports are allowed unless stated otherwise
- All files must be executable

## Data:
- Use `golden_gate.jpg` for this project.
