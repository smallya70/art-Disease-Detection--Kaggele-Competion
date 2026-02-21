# Heart Disease Detection

Simple exploratory project for heart disease prediction using the Kaggle-style train/test dataset in the `data/` folder.

## Project Structure

- `data/train.csv` - training dataset
- `data/test.csv` - test dataset
- `heart_disease.py` - exploratory analysis script (data inspection + visualizations)
- `heart_disease.ipynb` - notebook version of the workflow
- `explore_train.ipynb` - additional EDA notebook

## Setup

1. Create and activate your virtual environment (you already use `.venv`).
2. Install dependencies:

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

## Run

### Python script

```bash
python heart_disease.py
```

### Notebooks

```bash
jupyter notebook
```

Open `heart_disease.ipynb` or `explore_train.ipynb` from the Jupyter UI.

## Notes

- The current script focuses on EDA and plotting.
- Ensure the working directory is the project root so relative paths like `./data/train.csv` resolve correctly.