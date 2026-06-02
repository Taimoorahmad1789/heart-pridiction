# Heart Prediction

Streamlit dashboard for cardiac risk assessment using a pre-trained machine learning pipeline and SHAP explanations.

## Features
- Predicts heart disease risk probability and risk level (low/moderate/high)
- Provides SHAP-based feature impact insights and visualization
- Exports a downloadable CSV diagnostic report

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run
```bash
streamlit run app.py
```

## Project Structure
- `app.py` — Streamlit UI and workflow
- `models.py` — model loading and prediction utilities
- `utils.py` — input preparation and report generation
- `config.py` — configuration constants
- `pipeline.pkl` — trained model pipeline
- `shap_explainer.pkl` — SHAP explainer artifact
- `heart_disease*.xls` — dataset files (reference)

## Notes
Ensure `pipeline.pkl` and `shap_explainer.pkl` exist in the project root before running the app.