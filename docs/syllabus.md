---
layout: page
title: "Course Syllabus"
---

# Introduction to Data Science and Advanced Programming  
HEC Lausanne, Fall Semester 2025  

This advanced course introduces students to the Python programming language, core concepts of statistical learning, and high-performance computing. It is designed for Master's students in Economics and Finance to build the computational and analytical skills necessary for modern quantitative analysis. 

The course consists of three 45-minute lecture sessions and one 45-minute hands-on session each week. 

<!-- --- -->

## Course Objectives  

By the end of this course, you should be able to: 

- Write clean, efficient, and well-documented Python code. 
- Manipulate and analyze data using NumPy and Pandas.  
- Create insightful visualizations with Matplotlib and Seaborn.  
- Understand the fundamental theory of statistical learning, including the bias–variance trade-off and model assessment.  
- Implement and evaluate machine learning models for regression, classification, and clustering using scikit-learn.  
- Use tree-based methods and ensemble learning.  
- Gain awareness of deep learning concepts and implement a simple neural network.  
- Apply basic high-performance computing (HPC) techniques to accelerate Python code.  
- Independently manage and execute a data science project from conception to presentation.  

<!-- --- -->

## Meeting time and location  
- **Time:** Mondays, 12:30–16:00 
- **Place:** Internef 263 

**TA sessions:** Weekly on Mondays (15:15–16:00) with Anna Smirnova. Individual TA sessions available on Fridays upon request. 

---

## Class enrollment on the [Nuvolos Cloud](https://nuvolos.cloud/)

* All lecture materials (slides, codes, and further readings) will be distributed via the [Nuvolos Cloud](https://nuvolos.cloud/).
* To enroll in this class, please click on this [enrollment key](https://app.nuvolos.cloud/enroll/class/RshD654gzU4), and follow the steps.

<!-- --- -->

<!-- ## Video to get started with Nuvolos 

* First steps on Nuvolos: 

<iframe src="https://player.vimeo.com/video/513310246" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe> -->

---

## Approximate Schedule  

### Part I: Python Foundations (Weeks 1–6)  

**Week 0 and Week 1 (Sep 15): Course Overview & Setup**  
- Introduction to the course  
- Structure, grading, and capstone project  
- Introduction to Nuvolos cloud computing platform  
- Unix/Linux basics  

**Week 2 (Sep 22): No Class**  
- *Swiss Federal Fast (Public Holiday)*  

**Week 3 (Sep 29): Python Fundamentals I**  
- Python basics (variables, types)  
- Control flow (loops, branching)  
- Strings and data structures (lists, tuples, dictionaries)  
- Productivity: Git version control  

**Week 4 (Oct 6): Python Fundamentals II**  
- Functions and recursion  
- Object-Oriented Programming (OOP) basics: classes & inheritance  

**Week 5 (Oct 13): Special Session: Generative AI**  
- Hands-on: Large Language Models & autonomous agents  
- Led by Anna Smirnova  

**Week 6 (Oct 20): Scientific Computing in Python**   
- NumPy arrays and vectorization  
- Pandas: data cleaning, transformation, grouping  
- Jupyter notebooks  

---

### Part II: Statistical Learning (Weeks 7–12)  

**Week 7 (Oct 27): Introduction to Statistical Learning & Visualization**  
- *ISL Ch. 2* – Statistical learning framework, bias–variance trade-off  
- Assessing model accuracy  
- Data visualization with Matplotlib & Seaborn  
- Further Reading: ISL Ch. 2  
- Further Reading: PML Ch. 1 (Introduction), PML Ch. 6.1–6.2 (Linear regression basics)  

**Week 8 (Nov 3): Linear Regression**  
- Simple & multiple regression, inference, diagnostics  
- Hands-on: regression with scikit-learn (economic dataset)  
- Further Reading: ISL Ch. 3  
- Further Reading: PML Ch. 6.3–6.5 (Bayesian linear regression, uncertainty, model comparison)  

**Week 9 (Nov 10): Classification**  
- Logistic regression, LDA, QDA, kNN  
- Hands-on: credit scoring / bankruptcy prediction example  
- Further Reading: ISL Ch. 4  
- Further Reading: PML Ch. 8.1–8.4 (Logistic regression, generative vs discriminative classifiers), PML Ch. 8.5 (Bayesian logistic regression, optional)  

**Week 10 (Nov 17): Model Validation & Regularization**  
- Train/test splits, cross-validation, bootstrap  
- Ridge regression and Lasso  
- Hands-on: feature selection in high-dimensional data  
- Further Reading: ISL Ch. 5–6  
- Further Reading: PML Ch. 7.1–7.3 (Overfitting, generalization, cross-validation), PML Ch. 6.6 (Regularization as priors: ridge ↔ Gaussian, lasso ↔ Laplace)  

**Week 11 (Nov 24): Tree-Based Methods**    
- Decision trees, bagging, random forests, boosting  
- Hands-on: random forests for portfolio or risk prediction  
- Further Reading: ISL Ch. 8  
- Further Reading: PML Ch. 9.1–9.3 (Decision trees and ensembles)  

**Week 12 (Dec 1): Unsupervised Learning**   
- PCA and clustering (K-means, hierarchical)  
- Hands-on: PCA on macro-finance panel data  
- Further Reading: ISL Ch. 10  
- Further Reading: PML Ch. 10.1–10.4 (PCA as latent factor model), PML Ch. 11.1–11.3 (Clustering, mixture models, EM algorithm)  

---

### Part III: Advanced Programming & Wrap-Up  

**Week 13 (Dec 8): High-Performance Computing & Deep Learning Primer**   

- **Deep Learning Primer**  
  - Neural networks: intuition & architecture  
  - Gradient descent and backpropagation (conceptual)  
  - PyTorch demo: a simple multilayer perceptron for classification/regression  
  - Applications in economics & finance (forecasting, text, panel data)  
  - Further Reading: ISL Ch. 10  
  - Further Reading: PML Ch. 16 (Neural networks), PML Ch. 17 (Deep learning, optimization & generalization)  

- **High-Performance Computing**  
  - Why performance matters in economics & finance  
  - Vectorization in NumPy  
  - JIT compilation with Numba  
  - Parallelization (multiprocessing, multithreading)  
  - GPU acceleration (overview with JAX/PyTorch)  
  - Hands-on: speeding up a Monte Carlo simulation  

**Week 14 (Dec 15): Capstone Project Presentations**  
- Students voluntarily present their projects  
- Wrap-up and course summary  

<!-- ![Young Enthusiastic Professor](./fig/programming_wrapup.png) -->

---

## Grading

* Every student has to provide a **capstone project** that illustrates what was learned.  
* Each student individually has to propose a data science project and work on it over the course of the semester.  
* The due date to submit the project is in the last week of the semester.  
* The deliverables are:  
    - i) a report of about 10 pages lengths.  
    - ii) a GitHub repository with the related code and data.  
    - iii) a video recording of a maximum of 10 minutes length that presents the project, the findings, etc.  
* We will award the grades based on whether the capstone project demonstrates an understanding of the material. **There will be no exams**.  
* There will be possibilities to collect ``bonus points'' via homework assignments.  

---

## Lecturer

* [Simon Scheidegger](https://sites.google.com/site/simonscheidegger/) (University of Lausanne, Department of Economics)  
    - Simon Scheidegger: <simon.scheidegger@unil.ch>  

---
    
## TAs and support
- Anna Smirnova <anna.smirnova@unil.ch> 
-  
- Nuvolos Support: <support@nuvolos.cloud>  

---

## Google document for the QA sessions:

* [Google Doc](https://docs.google.com/spreadsheets/d/1JnbT8enDgKhR6Rfje0CjtCyMwWXdHXim4iZMpn0QE-A/edit#gid=0)

---

## References  

- Guttag, *Introduction to Computation and Programming Using Python*, MIT Press 
- Langtangen, *A Primer on Scientific Programming with Python*, Springer 
- Goodfellow, Bengio, Courville, [*Deep Learning*, MIT Press](http://www.deeplearningbook.org)  
- Murphy, [*Probabilistic Machine Learning: An Introduction*, MIT Press](http://probml.github.io/book1) 
- James, Witten, Hastie, Tibshirani, *An Introduction to Statistical Learning*, 2nd Edition – [statlearning.com](https://www.statlearning.com)  

---

<!-- ## Auxiliary materials 

| Session #        |  Title     | Screencast  |
|:-------------: |:-------------:| :-----:|
|   1 	| Git intro | <iframe src="https://player.vimeo.com/video/516690761" width="640" height="400" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>|  
|   1 	| Terminal intro | <iframe src="https://player.vimeo.com/video/516691661" width="640" height="400" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>|   -->
