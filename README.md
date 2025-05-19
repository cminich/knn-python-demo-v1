# Nearest Neighbor Demo 1 (Python + cmu-graphics)

This repository contains a simple educational demonstration of the **k-Nearest Neighbor (kNN)** algorithm implemented in **Python** using the **cmu-graphics** package. It's designed by **Mr. Minich** for use in **high school** or **introductory college-level** computer science and data science courses, as well as for **curious adults** exploring machine learning concepts.

---

## 📘 Overview

```python
# Nearest Neighbor Demo 1
# This Python program, that uses the pyGame-based cmu-graphics package, is
# used by Mr. Minich to help introductory computer programming students and 
# curious laymen adults understand the nearest neighbor algorithm.
# This version of the demo program classifies favorite drinks by their
# sweetness and caffeine level features.
```

This interactive program classifies a set of **favorite drinks** using two numerical features:

- **Sweetness level**
- **Caffeine content**

By applying the nearest neighbor algorithm, the program assigns a user-defined drink to a category based on its proximity to known examples. The graphical interface allows students to experiment with inputs and understand how the algorithm behaves.

---

## 💡 Educational Goals

- Understand how **distance-based classification** works
- Visualize the concept of **feature space**
- Explore how new data points are classified using training examples
- Provide hands-on experience with **cmu-graphics**, a beginner-friendly graphics package

---

## 🛠 Requirements

- Python 3.9 or later
- [`cmu-graphics`](https://pypi.org/project/cmu-graphics/)

Install the graphics package with:

```bash
pip install cmu-graphics
```

---

## ▶️ How to Run

Clone or download the repository, then run:

```bash
git clone https://github.com/yourusername/nearest-neighbor-demo1-python.git
cd nearest-neighbor-demo1-python
python main.py
```

This will open a graphical window where you can:
- View a plot of existing drink data
- Input a new drink's sweetness and caffeine levels
- Observe classification by nearest neighbor

---

## 📁 Project Structure

```
nearest-neighbor-demo1-python/
├── main.py                # Core program logic and graphical interface
├── drinks_data.py         # Stores drink examples with their features and labels
├── README.md              # This documentation file
├── assets/                # Optional: drink icons, visuals for demo
└── data/                  # Optional: extended datasets (CSV/JSON)
```

---

## 🔄 Future Extensions

This project is intentionally kept simple for educational use, but here are ideas to expand it:

- Allow `k > 1` (k-nearest neighbors instead of just 1)
- Add options for different distance metrics (Euclidean vs. Manhattan)
- Support saving and loading custom drink examples
- Compare predictions against scikit-learn's kNN classifier
- Port this demo to Java and C++ with similar GUI structure

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute for educational and personal projects.

---

## 👨‍🏫 About the Author

**Curt Minich**  
Veteran Computer Science Teacher | Adjunct Professor | AI/ML Educator

- GitHub: [@yourusername](https://github.com/cminich)
- Website: [minich.com](https://minich.com) 

---

## 🧠 Related Projects

- [kNN Java Demo (Coming Soon)](https://github.com/cminich/knn-java-demo)
- [kNN C++ Demo (Coming Soon)](https://github.com/cminich/knn-cpp-demo)

---
