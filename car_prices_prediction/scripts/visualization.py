import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def make_barplot(data_df, categorical_features, nb_cat_per_feature_to_plot):
    '''
    Create barplot for each categorical feature in the given DataFrame.

    Parameters
    ----------
    data_df : pd.DataFrame
        The DataFrame containing the data.
    categorical_features : list
        List of column names for numerical features.
    nb_cat_per_feature_to_plot : int
        Number of category to plot per feature.

    Returns
    -------
    None
    '''
    for feature in categorical_features:
        plt.figure(figsize=(10, 5))
        count = data_df[feature].value_counts().nlargest(nb_cat_per_feature_to_plot)
        sns.barplot(x=count.index, y=count.values)
        plt.ylabel(f"Count of '{feature }'")
        plt.xlabel(f"{feature }")
        plt.title(f"Count of unique categories in column '{feature }'")
        plt.xticks(rotation=90)
        plt.show()


def make_hist(data_df, numerical_features, bins=100):
    '''
    Create histograms for each numerical feature in the DataFrame.

    Parameters
    ----------
    data_df : pd.DataFrame
        The DataFrame containing the data.
    numerical_features : list
        List of column names for numerical features.
    bins : int, optional
        Number of bins (bars) for the histogram. Default is 10.

    Returns
    -------
    None
    '''
    for feature in numerical_features:
        plt.figure(figsize=(10, 5))
        plt.hist(data_df[feature].to_numpy(), bins=bins)
        plt.xlabel(f'{feature}')
        plt.ylabel('Fraction of data')
        plt.show()


def make_box_for_discrete_features(X_df, discrete_features, y_df):
    '''
    Create boxplots for each discrete feature against a target variable.

    Parameters
    ----------
    X_df : pd.DataFrame
        DataFrame containing the data.
    discrete_features : list of str
        List of column names for categorical features.
    y_df : pd.Series
        Series representing the target variable.

    Returns
    -------
    None
    '''
    for feature in  discrete_features:
        colors = sns.color_palette("husl", n_colors=len(X_df[feature].unique()))
        plt.figure(figsize=(20, 7))
        sns.boxplot(data=None, y=y_df, x=X_df[feature], palette=colors)
        plt.ylabel(y_df.name)
        plt.xlabel(feature)
        plt.xticks(rotation=90, fontsize=8)
        plt.ylim(-1000,180000)
        plt.show()


def make_box_for_continuous_features(X_df, numeric_continious_features, y_df, bins=100, ylim=(-1000,180000)):
    '''
    Create boxplots for continuous features by binning the data into intervals.

    Parameters
    ----------
    X_df : pd.DataFrame
        DataFrame containing the data.
    numeric_continuous_features : list of str
        List of column names for continuous numerical features.
    y_df : pd.Series
        Series representing the target variable.
    bins : int, optional
        Number of bins for binning continuous features. Default is 100.
    ylim : tuple of (float, float), optional
        y-axis limits for the plots. Default is (-1000, 180000).

    Returns
    -------
    None
    '''
    data_to_plot = X_df.copy()

    for feature in  numeric_continious_features:
        # ---- Build bins
        #
        data_to_plot[f'{feature}_bins'] = pd.cut(data_to_plot[feature], bins=bins)
        colors = sns.color_palette("husl", n_colors=bins)
        # ---- Plot
        #
        plt.figure(figsize=(20, 7))
        sns.boxplot(data=None, y=y_df, x=data_to_plot[f'{feature}_bins'], palette=colors)
        plt.xlabel(f'{feature}_bins')
        plt.ylabel(y_df.name)
        plt.xticks(rotation=90, fontsize=8)
        plt.ylim(ylim)
        plt.show()