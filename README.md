# Final-Report
 LIGHTWEIGHT ML-BASED IDS FOR IOT ENVIRONMENTS 

 # Lightweight ML-Based Intrusion Detection System for IoT Environments

## Overview

This project presents a lightweight machine learning-based Intrusion Detection System (IDS) designed for Internet of Things (IoT) environments. The research focuses on reducing computational complexity while maintaining effective intrusion detection capability suitable for resource-constrained edge devices.

The system combines:
- Feature selection
- Machine learning classification
- Lightweight deployment validation

to develop an efficient IDS capable of operating within constrained IoT environments.

Note: The CIC-IoT2023 dataset was not uploaded to this repository due to its large size.




---

## Research Objectives

The objectives of this research include:
- Reducing computational overhead in IoT intrusion detection
- Evaluating lightweight machine learning approaches
- Comparing multiple machine learning models
- Validating practical deployment capability

---

## Dataset

The project uses the **CIC-IoT2023 dataset**, which contains modern IoT network traffic and multiple cyber-attack categories including:
- DDoS attacks
- DoS attacks
- Mirai botnet traffic
- DNS spoofing
- Reconnaissance attacks
- SQL Injection
- Command Injection

Dataset preprocessing included:
- Duplicate removal
- Missing value handling
- Binary label mapping
- Feature scaling
- Numeric feature extraction

---

## Feature Selection

A Mutual Information-based feature selection approach inspired by the Minimum Redundancy Maximum Relevance (mRMR) technique was implemented to reduce dimensionality and improve lightweight operational performance.

The top 20 most relevant traffic features were selected for model training.

---

## Machine Learning Models

The following machine learning models were implemented and evaluated:

- Decision Tree
- Random Forest
- Logistic Regression
- Gradient Boosting

The models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- False Positive Rate

---

## Lightweight Evaluation Metrics

In addition to classification performance, lightweight deployment metrics were evaluated including:
- Model size
- Training time
- Inference time
- CPU usage
- Memory usage

---

## Final Model

Gradient Boosting was selected as the final deployment model because it achieved the best balance between:
- Detection capability
- Lightweight operational efficiency
- Deployment suitability

### Final Gradient Boosting Results
| Metric | Value |
|---|---|
| Accuracy | 99.59% |
| Precision | 99.82% |
| Recall | 99.75% |
| F1-Score | 99.79% |
| ROC-AUC | 0.999433 |
| Model Size | 76.45 KB |

---

## Deployment Validation

The trained model was exported using Joblib and deployed within an Ubuntu 24.01 Virtual Machine environment to validate lightweight deployment feasibility.

Deployment testing included:
- Loading the trained IDS model
- Loading unseen traffic samples
- Generating intrusion predictions
- Monitoring lightweight operational metrics

---

## Technologies Used

- Python
- Google Colab
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Joblib
- Ubuntu 24.01
- VirtualBox

---

## Repository Structure

```bash
/project-root
│
├── dataset_processing/
├── feature_selection/
├── models/
├── deployment/
├── results/
├── screenshots/
├── gb_ids_model.pkl
├── deployment_test.csv
├── deployment_labels.csv
├── test_model.py
└── README.md

Running the deployment script
activate the virtual environment and run
python3 test_model.py

Author

Oyewale Mayowa
MSc CyberSecurity Dissertation Project

Disclaimer

This project was developed strictly for academic and research purposes.
