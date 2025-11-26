import pandas as pd

REQUIRED_COLUMNS = ["age", "weight", "height", "systolic_bp", "cholesterol"]


def load_and_clean_data(path: str) -> pd.DataFrame:
    """
    Load the health study dataset and apply basic cleaning and encoding.

    Parameters
    ----------
    path : str
        Relative path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe with consistent dtypes and categories.
    """
    df = pd.read_csv(path)

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    else:
        print("All required columns are present.")

    df["sex"] = (
        df["sex"]
        .astype(str)
        .str.strip()
        .str.upper()
        .replace({"FEMALE": "F", "MALE": "M"})
        .astype("category")
    )

    df["smoker"] = (
        df["smoker"]
        .astype(str)
        .str.strip()
        .str.title()
        .replace({"Y": "Yes", "N": "No"})
        .astype("category")
    )

    df["sex"] = df["sex"].cat.set_categories(["F", "M"])
    df["smoker"] = df["smoker"].cat.set_categories(["No", "Yes"])

    df["disease"] = df["disease"].astype(int)

    return df

