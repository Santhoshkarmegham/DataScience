# House Price ML Project

## Files

- `house_price_ml_dataset.csv` — training dataset
- `house_price_prediction.ipynb` — complete ML notebook
- `app.py` — Streamlit prediction interface
- `requirements.txt` — required Python packages

## Setup

Open Terminal in this folder and run:

```bash
python -m pip install -r requirements.txt
```

## Train and save the model

Open `house_price_prediction.ipynb` in Jupyter Notebook or VS Code and run every cell.

This creates:

```text
house_price_model.pkl
```

## Start the Streamlit application

```bash
streamlit run app.py
```

Open the local URL displayed in Terminal.
