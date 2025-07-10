# 🍕 Pizza Price Prediction

This is an simple interactive **Streamlit** web app that uses **Linear Regression** to predict the price of a pizza based on its diameter (in centimeters).

## ⚙ Features

- Predict pizza price based on user-input diameter
- Clean and intuitive **Streamlit** interface
- Clear explanation of how the model works

---

## 📊 About the Model

The model is a **Simple Linear Regression**, trained using a dataset (`pizzas.csv`) with two variables:

- `diametro`: pizza diameter (cm)
- `preco`: corresponding price (R$)

The learned formula is in the form:
price = a * diameter + b

## ▶️ How to Run the Project

1. Clone the repository:
```
git clone https://github.com/joaoeferrari/pizzas_value.git
cd your-repository
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the app:
```
streamlit run app.py
```
---
**Reference**: https://www.youtube.com/watch?v=bGwdwF1vlvQ
