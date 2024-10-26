# Hyperparameter Tuning and Bayesian Optimization

## Resources

To dive into hyperparameter tuning, Gaussian Processes, and Bayesian Optimization, refer to these materials:

### Articles and Guides
- **Hyperparameter Tuning**
  - Hyperparameter Tuning in Practice
  - Orthogonalization
  - Single Number Evaluation Metric
  - Satisficing and Optimizing Metrics

- **Gaussian Processes and Kriging**
  - Gaussian process
  - Kriging
  - Machine learning - Introduction to Gaussian processes
  - Machine learning - Gaussian processes
  - Quick Start to Gaussian Process Regression

- **Bayesian Optimization**
  - Machine learning - Bayesian optimization and multi-armed bandits
  - Bayesian Optimization
  - A Tutorial on Bayesian Optimization

- **GPy and GPyOpt Documentation**
  - GPy documentation
  - GPy.kern.src
  - GPy.plotting.gpy_plot
  - GPyOpt documentation
  - GPyOpt.methods.bayesian_optimization
  - GPyOpt.core.task.space

## Learning Objectives

This project covers essential topics in hyperparameter tuning, Gaussian Processes, and Bayesian optimization:

- **Hyperparameter Tuning**:
  - Understanding hyperparameter tuning
  - Approaches to tuning: random search and grid search

- **Gaussian Processes**:
  - Defining a Gaussian Process
  - Understanding mean and kernel functions
  - Gaussian Process Regression (also known as Kriging)

- **Bayesian Optimization**:
  - Concepts and applications of Bayesian Optimization
  - Acquisition functions, including Expected Improvement, Knowledge Gradient, and Entropy Search/Predictive Entropy Search

- **GPy and GPyOpt Libraries**:
  - Using GPy for Gaussian Process modeling
  - Using GPyOpt for Bayesian Optimization tasks

## Requirements

### General
- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 16.04 LTS with Python 3.5
- **Libraries**: numpy (version 1.15) only, import as `import numpy as np`
- **Style Guide**: Code should follow `pycodestyle` (version 2.4) but may ignore error E741
- **File Specifications**:
  - All files must end with a new line
  - The first line should be `#!/usr/bin/env python3`
  - All files must be executable
  - Documentation is required for all modules, classes, and functions

### Documentation
- Use `python3 -c 'print(__import__("my_module").__doc__)'` to view module documentation.
- Use `python3 -c 'print(__import__("my_module").MyClass.__doc__)'` for class documentation.
- Use `python3 -c 'print(__import__("my_module").my_function.__doc__)'` for function documentation (inside or outside classes).

### Installation
Ensure the required libraries are installed:

```bash
pip install --user GPy
pip install --user gpyopt