import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


class HealthAnalyzer:
    """
    A class for analysing the health study dataset.

    It can show descriptive statistics, make simple plots,
    and run regression models.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Parameters
        ----------
        df : pd.DataFrame
            The cleaned dataset.
        """
        self.df = df.copy()

    def descriptive_stats(self, columns=None) -> pd.DataFrame:
        """
        Return simple summary statistics for the selected columns.

        Parameters
        ----------
        columns : list of str, optional
            Which columns to include. If None, a default list is used.

        Returns
        -------
        pd.DataFrame
            A table with mean, median, std, min and max.
        """

        if columns is None:
            columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]

        desc = (
            self.df[columns]
            .agg(["mean", "median", "std", "min", "max"])
            .T.round(2)
            .sort_values("mean", ascending=False)
        )
        return desc

    def plot_systolic_hist(self):
        """
        Plot the distribution of systolic blood pressure.
        """
        bp = self.df["systolic_bp"]

        fig, ax = plt.subplots()
        ax.hist(bp, bins=30, edgecolor="black", alpha=0.7)

        ax.set_title("Distribution of Systolic Blood Pressure")
        ax.set_xlabel("Systolic Blood Pressure (mmHg)")
        ax.set_ylabel("Frequency")
        ax.grid(axis="y", alpha=0.3)

        ax.text(
            0.98,
            0.96,
            f"n = {len(bp)}\n"
            f"mean = {bp.mean():.1f}\n"
            f"median = {bp.median():.1f}\n"
            f"sd = {bp.std():.1f}",
            transform=ax.transAxes,
            ha="right",
            va="top",
            bbox=dict(
                boxstyle="round",
                facecolor="lightgray",
                alpha=0.8,
                edgecolor="gray",
            ),
        )


        plt.tight_layout()
        plt.show()

    def plot_weight_by_sex(self):
        """
        Plot the distribution of weight separated by sex, with group summaries.
        """
        df = self.df

        fig, ax = plt.subplots()
        sns.boxplot(
            data=df,
            x="sex",
            y="weight",
            ax=ax,
            showmeans=True,
        )

        ax.set_xticklabels(["Female", "Male"])
        ax.set_title("Distribution of Weight by Sex")
        ax.set_xlabel("Sex")
        ax.set_ylabel("Weight (kg)")
        ax.grid(axis="y", alpha=0.3)

        n_m = df.loc[df["sex"] == "M", "weight"].count()
        n_f = df.loc[df["sex"] == "F", "weight"].count()
        mean_m = df.loc[df["sex"] == "M", "weight"].mean()
        mean_f = df.loc[df["sex"] == "F", "weight"].mean()
        med_m = df.loc[df["sex"] == "M", "weight"].median()
        med_f = df.loc[df["sex"] == "F", "weight"].median()

        ax.text(
            0.5, 0.96,
            f"Male: {n_m}, mean = {mean_m:.1f}\n"
            f"Female: {n_f}, mean = {mean_f:.1f}",
            transform=ax.transAxes,
            ha="center",
            va="top",
            bbox=dict(
                boxstyle="round",
                facecolor="lightgray",
                alpha=0.8
            )
        )

        plt.tight_layout()
        plt.show()


    def plot_smoker_counts(self):
        """
        Plot the number of smokers vs non-smokers, with counts and percentages.
        """
        counts = self.df["smoker"].value_counts().reindex(["No", "Yes"])
        total = counts.sum()
        perc_no = counts["No"] / total * 100
        perc_yes = counts["Yes"] / total * 100

        fig, ax = plt.subplots()
        ax.bar(counts.index, counts.values, edgecolor="black")

        ax.set_title("Number of Smokers vs Non-Smokers")
        ax.set_xlabel("Smoking status")
        ax.set_ylabel("Count")
        ax.grid(axis="y", alpha=0.3)

        ax.text(
            0.98,
            0.96,
            f"No:  {counts['No']} ({perc_no:.1f}%)\n"
            f"Yes: {counts['Yes']} ({perc_yes:.1f}%)",
            transform=ax.transAxes,
            ha="right",
            va="top",
            bbox=dict(boxstyle="round", facecolor="lightgray", alpha=0.85),
        )

        plt.tight_layout()
        plt.show()


    def plot_bp_vs_age_by_smoking(self):
        """
        Scatter plot of systolic blood pressure vs age, coloured by smoking status.
        """
        df = self.df

        fig, ax = plt.subplots()
        sns.scatterplot(
            data=df,
            x="age",
            y="systolic_bp",
            hue="smoker",
            alpha=0.7,
            ax=ax,
        )

        ax.set_title("Systolic Blood Pressure vs Age by Smoking Status")
        ax.set_xlabel("Age (years)")
        ax.set_ylabel("Systolic Blood Pressure (mmHg)")
        ax.grid(alpha=0.3)

        plt.tight_layout()
        plt.show()

    def fit_bp_regression(self, features=None):
        """
        Fit a regression model that predicts systolic blood pressure
        from the selected features.

        Parameters
        ----------
        features : list of str, optional
            Columns to use in the model. Default is ["age", "weight"].

        Returns
        -------
        dict
            A dictionary with the model results.
        """

        if features is None:
            features = ["age", "weight"]

        X = self.df[features].values
        y = self.df["systolic_bp"].values

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        model = LinearRegression()
        model.fit(X_scaled, y)

        r_squared = model.score(X_scaled, y)

        coef_series = pd.Series(model.coef_, index=features, name="coefficient")

        return {
            "model": model,
            "scaler": scaler,
            "features": features,
            "coefficients": coef_series,
            "intercept": model.intercept_,
            "r_squared": r_squared,
        }
