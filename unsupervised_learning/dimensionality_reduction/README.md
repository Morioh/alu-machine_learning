# Dimensionality Reduction Techniques

## Resources
To gain a deep understanding of dimensionality reduction techniques, refer to the following resources:

### Read or Watch:
1. **[Dimensionality Reduction For Dummies — Part 1: Intuition](#)**
2. **[Singular Value Decomposition](#)**
3. **[Understanding SVD (Singular Value Decomposition)](#)**
4. **[Intuitively, what is the difference between Eigendecomposition and Singular Value Decomposition?](#)**
5. **[Dimensionality Reduction: Principal Components Analysis, Part 1](#)**
6. **[Dimensionality Reduction: Principal Components Analysis, Part 2](#)**
7. **[StatQuest: t-SNE, Clearly Explained](#)**
8. **[t-SNE tutorial Part 1](#)**
9. **[t-SNE tutorial Part 2](#)**
10. **[How to Use t-SNE Effectively](#)**

### Definitions to Skim:
- **Dimensionality Reduction**
- **Principal Component Analysis (PCA)**
- **Eigendecomposition of a Matrix**
- **Singular Value Decomposition (SVD)**
- **Manifold** (check this out if you're unfamiliar with this term)
- **Kullback–Leibler Divergence**
- **T-distributed Stochastic Neighbor Embedding (t-SNE)**

### As References:
- **[numpy.cumsum](#)**
- **[Visualizing Data Using t-SNE (Paper)](#)**
- **[Visualizing Data Using t-SNE (Video)](#)**

### Advanced:
- **[Kernel Principal Component Analysis](#)**
- **[Nonlinear Dimensionality Reduction: KPCA](#)**

## Learning Objectives
By the end of this project, you should be able to answer the following questions:
- What is eigendecomposition?
- What is singular value decomposition?
- What is the difference between EIG and SVD?
- What is dimensionality reduction and what are its purposes?
- What is principal components analysis (PCA)?
- What is t-distributed stochastic neighbor embedding (t-SNE)?
- What is a manifold?
- What is the difference between linear and non-linear dimensionality reduction?
- Which techniques are linear/non-linear?

## Requirements
### General Requirements:
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 16.04 LTS using Python 3.5
- Files will be executed with `numpy` version 1.15
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code must adhere to `pycodestyle` (version 2.4)
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside classes) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Unless otherwise noted, no imports are allowed except `import numpy as np`
- All files must be executable
- Code should minimize operations to avoid floating point errors

### Data
Please test your main files with the following datasets:
- `mnist2500_X.txt`
- `mnist2500_labels.txt`

### Watch Out!
Just like Python lists, `np.ndarrays` are mutable objects:

```python
>>> vector = np.ones((100, 1))
>>> m1 = vector[55]
>>> m2 = vector[55, 0]
>>> vector[55] = 2
>>> m1
array([2.])
>>> m2
1.0