# Heart Prediction (Heart AI Pro)

Streamlit-based dashboard for cardiac risk assessment using a pre-trained scikit-learn pipeline and SHAP explainability.

## Overview
This project provides an interactive web app that estimates cardiac risk from clinical inputs, visualizes the probability distribution, and surfaces model-driven insights with SHAP. The repository includes pre-trained model artifacts so you can run the app immediately.

## Features
- Interactive input form for key clinical indicators
- Risk probability and level classification
- SHAP explainability with waterfall plot
- Downloadable CSV diagnostic report

## Project Structure
| File | Purpose |
| --- | --- |
| `app.py` | Streamlit UI and orchestration |
| `config.py` | App settings, thresholds, and ranges |
| `models.py` | Model loading, prediction, and SHAP helpers |
| `utils.py` | Input assembly and report generation |
| `pipeline.pkl` | Trained model pipeline |
| `shap_explainer.pkl` | SHAP explainer |
| `heart_disease*.xls` | Sample datasets |
| `shap_summary_plot.png` | Example SHAP summary visualization |

## Getting Started
### Prerequisites
- Python 3.9+ recommended

### Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run the App
```bash
streamlit run app.py
```

## Usage
1. Adjust patient inputs in the left panel.
2. Click **Generate Diagnostic Report** to view risk results.
3. Explore SHAP insights and download the CSV report if needed.

## Configuration
Update thresholds, default values, and UI settings in `config.py`. If you replace the model artifacts, ensure the feature schema matches the input DataFrame generated in `utils.py`.# heart_pridiction
