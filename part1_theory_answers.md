# Part 1: Theoretical Understanding

## Q1: TensorFlow vs PyTorch Differences

| Feature              | TensorFlow                        | PyTorch                           |
|----------------------|------------------------------------|------------------------------------|
| Execution Style      | Static graph (optimized for deployment) | Dynamic graph (easier for research) |
| Debugging            | Harder with sessions              | Easier, Pythonic                   |
| Visualization        | TensorBoard                       | TorchVision                       |
| Use Case             | Great for production              | Great for research and prototyping |

**When to use which?**
- Choose **TensorFlow** if deploying models at scale (e.g., mobile apps, cloud APIs).
- Choose **PyTorch** if working on academic or experimental research.

---

## Q2: Jupyter Notebooks Use Cases

1. **Exploratory Data Analysis**: Run and visualize code step-by-step with plots and dataframes.
2. **Model Prototyping**: Rapid testing and tuning of ML models in an interactive, readable format.

---

## Q3: spaCy vs Python String Methods

- Python string methods (e.g., `split`, `find`) are basic and don’t understand language structure.
- **spaCy** provides advanced NLP features:
  - Named Entity Recognition (NER)
  - Part-of-speech tagging
  - Lemmatization
  - Faster and more accurate for real NLP tasks

---

## Q4: Scikit-learn vs TensorFlow Comparison

| Feature              | Scikit-learn                     | TensorFlow                        |
|----------------------|----------------------------------|-----------------------------------|
| Application Type     | Classical ML (e.g., Decision Trees, SVM) | Deep Learning (e.g., CNNs, RNNs) |
| Beginner Friendly    | Yes                              | Medium                            |
| Community Support    | Excellent for ML beginners       | Strong for DL and deployment      |