# Clustering and Gaussian Mixture Models

## Resources
For a comprehensive understanding of clustering techniques and Gaussian Mixture Models (GMM), explore the following resources:

### Read or Watch:
1. **[Understanding K-means Clustering in Machine Learning](#)**
2. **[K-means Clustering: How It Works](#)**
3. **[How Many Clusters?](#)**
4. **[Bimodal Distribution](#)**
5. **[Gaussian Mixture Model](#)**
6. **[EM Algorithm: How It Works](#)**
7. **[Expectation Maximization: How It Works](#)**
8. **[Mixture Models 4: Multivariate Gaussians](#)**
9. **[Mixture Models 5: How Many Gaussians?](#)**
10. **[Gaussian Mixture Model (GMM) Using Expectation Maximization (EM) Technique](#)**
11. **[What is Hierarchical Clustering?](#)**
12. **[Hierarchical Clustering](#)**

### Definitions to Skim:
- **Cluster Analysis**
- **K-means Clustering**
- **Multimodal Distribution**
- **Mixture Model**
- **Expectation–Maximization Algorithm**
- **Hierarchical Clustering**
- **Ward’s Method**
- **Cophenetic Distance**

### References:
- **[scikit-learn](#)**
- **[Clustering](#)**
- **[sklearn.cluster.KMeans](#)**
- **[Gaussian Mixture Models](#)**
- **[sklearn.mixture.GaussianMixture](#)**
- **[scipy](#)**
- **[scipy.cluster.hierarchy](#)**
- **[scipy.cluster.hierarchy.linkage](#)**
- **[scipy.cluster.hierarchy.fcluster](#)**
- **[scipy.cluster.hierarchy.dendrogram](#)**

## Learning Objectives
By the end of this project, you should be able to answer the following questions:
- What is a multimodal distribution?
- What is a cluster?
- What is cluster analysis?
- What is the difference between “soft” and “hard” clustering?
- What is K-means clustering?
- What are mixture models?
- What is a Gaussian Mixture Model (GMM)?
- What is the Expectation-Maximization (EM) algorithm?
- How do you implement the EM algorithm for GMMs?
- What is cluster variance?
- What is the mountain/elbow method?
- What is the Bayesian Information Criterion?
- How do you determine the correct number of clusters?
- What is hierarchical clustering?
- What is agglomerative clustering?
- What is Ward’s method?
- What is Cophenetic distance?
- What is scikit-learn?
- What is scipy?

## Requirements
### General Requirements:
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 16.04 LTS using Python 3.5
- Files will be executed with `numpy` version 1.15, `scikit-learn` version 0.21, and `scipy` version 1.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code must adhere to `pycodestyle` (version 2.4)
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside classes) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Unless otherwise noted, no imports are allowed except `import numpy as np`
- All files must be executable
- Code should minimize operations

### Installing Dependencies:
- **Installing scikit-learn 0.21.x:**
  ```bash
  pip install --user scikit-learn==0.21