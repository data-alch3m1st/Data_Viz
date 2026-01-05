# data_viz standalone code scratchpad #

'''
    Note: This is NOT an actual script meant to be run as-is; rather it is a simplified 'scratchpad' type mini-repo where I can keep and splendid and quirky bits of data visualization code that I find useful or interesting for future reference.
    
    Let the viz begin!
'''
# Misc setups, adjustments, etc.:

# Setting up plot/grid style:

plt.style.available 
# ^^^ This will show the plt styles which are available (the names arent intuitive, so its definitely helpful!)

sns.set_style('darkgrid')
plt.style.use('seaborn-v0_8-darkgrid')

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# Seaborn Plots #

# Simple side-by-side histplot & boxplot (same df, single col;)

fig, ax = plt.subplots(1, 2, figsize=(8, 4))

sns.histplot(df, ax=ax[0])
sns.boxplot(df, ax=ax[1])

plt.tight_layout()
plt.show();

# ........................................................................................... #

# Side-by-side boxplots with Seaborn (from two diff't dataframes):

fig, ax = plt.subplots(
    1, 2 # 1 row, 2 columns
    , figsize=(12, 6)
    , sharey=True  # Uncomment to share y-axis
    )

sns.boxplot((df['GarageArea']), ax=ax[0])
sns.boxplot((df2['GarageArea']), ax=ax[1])

ax[0].set_title('Boxplot of GarageArea - with Outliers') 
ax[1].set_title('Boxplot of GarageArea - without Outliers')

plt.tight_layout()
plt.show();

# ........................................................................................... #

# PLOTTING ALL DF NUMERIC COLS AT SCALE (either histplots or boxplots;) AWESOME Loop for plotting ALL numeric cols in a df to see distributions (histplots) or outliers (boxplots) #

# NUMERIC COLS LOOP—BOXPLOT:

# Automatically select all numerical cols from a df:
numeric_cols = df.select_dtypes(include=np.number).columns

# Set the max number of plots per row:
max_cols = 3 # Adjust as needed, but keep space and visibility/readability in mind;

plt.style.use('seaborn-v0_8-darkgrid')

# Calculate the number of rows needed based on the number of numeric columns:
num_plots = len(numeric_cols)
num_rows = int(np.ceil(num_plots / max_cols) ) # Ceiling division

# Generate a list of colors; (one color per column)
colors = sns.color_palette("husl", num_plots) # Use Seaborn color palette for distinct colors;

# Create subplots with calculated rows and fixed columns:
fig, axes = plt.subplots(
    num_rows
    , max_cols
    , figsize=(max_cols * 4, num_rows * 4)
    , sharey=False # Adjust as needed; 
    )

# Flatten the axes array for easy iteration:
axes = axes.flatten()

# Loop through each numeric columns, colors and axes:
for i, (col, color) in enumerate(zip(numeric_cols, colors)):
    sns.boxplot(
        data=df
        , y=col # can manipulate the orientation by assignment of 'x' / 'y';
        , ax=axes[i]
        , color=color
#         , orient="h"
        )
    axes[i].set_title(f'Boxplot of {col}')
    
# Hide any unused axes (if num_plots < num_rows * max_cols):
for j in range(num_plots, len(axes)):
    fig.delaxes(axes[j])
    
# Adjust layout and display the plot(s):
plt.style.use('seaborn-v0_8-darkgrid')
plt.tight_layout()
plt.show();


# ........................................................................................... #

# HISTPLOT LOOP #

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

# NUMERIC COLS LOOP—HISTPLOT:

# Automatically select all numerical cols from a df:
numeric_cols = df.select_dtypes(include=np.number).columns

# Set the max number of plots per row:
max_cols = 3 # Adjust as needed, but keep space and visibility/readability in mind;

# Calculate the number of rows needed based on the number of numeric columns:
num_plots = len(numeric_cols)
num_rows = int(np.ceil(num_plots / max_cols) ) # Ceiling division

# Generate a list of colors; (one color per column)
colors = sns.color_palette("husl", num_plots) # Use Seaborn color palette for distinct colors;

# Create subplots with calculated rows and fixed columns:
fig, axes = plt.subplots(
    num_rows
    , max_cols
    , figsize=(max_cols * 4, num_rows * 4)
    , sharey=False # Adjust as needed; 
    )

# Flatten the axes array for easy iteration:
axes = axes.flatten()

# Loop through each numeric columns, colors and axes:
for i, (col, color) in enumerate(zip(numeric_cols, colors)):
    sns.histplot(
        df[col]
        , kde=True
        , ax=axes[i]
        , color=color
        )
    
    axes[i].set_title(f'Boxplot of {col}')
#     axes[i].grid() # remove; not actually showing grid!
#     plt.style.use('seaborn-v0_8-darkgrid') # Can set preferred style in the loop or outside (added @ end;)
    
# Hide any unused axes (if num_plots < num_rows * max_cols):
for j in range(num_plots, len(axes)):
    fig.delaxes(axes[j])
    
# Adjust layout and display the plot(s):
plt.style.use('seaborn-v0_8-darkgrid')
plt.tight_layout()
plt.show();


# NOW—the same histplot & boxplot, but in a script which can be applied to either!!!

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_numeric_cols(
    df: pd.DataFrame
    , plot_type: str = "boxplot"
    , max_cols: int = 3
    , figsize: tuple = (12, 8)
    , sharey: bool = False
    , palette: str = "husl"
    , orient: str = "v"
):
    """
    Plot all numeric columns in a DataFrame as boxplots or histplots.

    Parameters:
    -----------
    df : pd.DataFrame
        The DataFrame containing the data to plot.
    plot_type : str, optional (default="boxplot")
        Type of plot: "boxplot" or "histplot".
    max_cols : int, optional (default=3)
        Maximum number of plots per row.
    figsize : tuple, optional (default=(12, 8))
        Figure size (width, height) in inches.
    sharey : bool, optional (default=False)
        If True, y-axes will be shared across all subplots.
    palette : str, optional (default="husl")
        Seaborn color palette to use.
    orient : str, optional (default="v")
        Orientation of the plot: "v" (vertical) or "h" (horizontal).
    """
    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=np.number).columns
    num_plots = len(numeric_cols)

    # Calculate number of rows needed
    num_rows = int(np.ceil(num_plots / max_cols))

    # Generate colors
    colors = sns.color_palette(palette, num_plots)

    # Create subplots
    fig, axes = plt.subplots(
        num_rows, max_cols, figsize=figsize, sharey=sharey
    )
    axes = axes.flatten()

    # Plot each numeric column
    for i, (col, color) in enumerate(zip(numeric_cols, colors)):
        if plot_type == "boxplot":
            sns.boxplot(data=df, y=col, ax=axes[i], color=color, orient=orient)
            axes[i].set_title(f"Boxplot of {col}")
        elif plot_type == "histplot":
            sns.histplot(data=df, x=col, ax=axes[i], color=color, kde=True)
            axes[i].set_title(f"Histogram of {col}")
        else:
            raise ValueError("plot_type must be 'boxplot' or 'histplot'")

    # Hide unused axes
    for j in range(num_plots, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout and display
    plt.style.use("seaborn-v0_8-darkgrid")
    plt.tight_layout()
    plt.show();
    
# Example usage:
plot_numeric_cols(
    df, plot_type="boxplot"
    , max_cols=4
    , figsize=(16, 12)
    , sharey=False
    , palette="Set2"
    , orient="v"
    )

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# Machine Learning Useful Plots #

# ........................................................................................... #

# To do a side-by-side, normalized Confusion Matrix (CM) comparison after running a 'GridSearchCV' so show the 'base' model vs. the 'best' (Best vs. Base):
# (using sklearn.metricsConfusionMatrixDisplay) 

import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import ConfusionMatrixDisplay

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ConfusionMatrixDisplay.from_estimator(
    best_model, scaled_X_test, y_test, cmap='Blues', ax=ax[0]
)

ConfusionMatrixDisplay.from_estimator(
    svc, scaled_X_test, y_test, cmap='Reds', ax=ax[1]
)

ax[0].set_title('Best Model')
ax[1].set_title('Base Model')

plt.tight_layout()
plt.show();

# ........................................................................................... #

# PrecisionRecallDisplay.from_estimator(best_xgb, X_test, y_test)
# To do a side-by-side, normalized PRC comparison (Best vs. Base):

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

PrecisionRecallDisplay.from_estimator(
    best_xgb, X_test, y_test, ax=ax[0]
)

PrecisionRecallDisplay.from_estimator(
    xgb_clf, X_test, y_test, ax=ax[1]
)

ax[0].set_title('Best Model (Precision Recall Curve)')
ax[1].set_title('Base Model (Precision Recall Curve)')

plt.tight_layout()
plt.show();

# ........................................................................................... #

# RocCurveDisplay.from_estimator(best_xgb, X_test, y_test);
# To do a side-by-side, normalized ROC/AUC comparison (Best vs. Base):

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

RocCurveDisplay.from_estimator(
    best_xgb, X_test, y_test, ax=ax[0]
)

RocCurveDisplay.from_estimator(
    xgb_clf, X_test, y_test, ax=ax[1]
)

ax[0].set_title('Best Model (ROC/AUC Curve)')
ax[1].set_title('Base Model (ROC/AUC Curve)')

plt.tight_layout()
plt.show();


# ........................................................................................... #
# FEATURE IMPORTANCES PLOT (for ML Models) #

# Using basing plt:

# Updated, more efficient and universally applicable "Feature Importances" plot, (for Best) which uses a dataframe, rather than piecemeal bits and indices;

feature_importances = pd.DataFrame({
    "Feature": X.columns
    , "Importance": best_xgb.feature_importances_
}).sort_values(
    by="Importance", ascending=False)

plt.figure(figsize=(10, 8))
sns.barplot(
    x="Importance", y="Feature"
    , data=feature_importances.head(15)
    , palette="inferno"
)

plt.title('Top 15 Feature Importances')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.grid()
plt.show();

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# And now - with plotly express!

import plotly.express as px

# Create a dataframe for feature importances
feature_importances = pd.DataFrame({
    "Feature": X.columns
    , "Importance": best_xgb.feature_importances_
}).sort_values(
    by="Importance"
    , ascending=False)

# Select the top 15 features
top_features = feature_importances.head(15)

# Create the bar chart
fig = px.bar(
    top_features
    , x="Importance"
    , y="Feature"
    , orientation="h"  # Horizontal bar chart
    , title="Top 15 Feature Importances"
    , color="Importance"  # Add color based on importance
    , color_continuous_scale="viridis_r"  # Match the seaborn palette
)

# Update layout for better appearance
fig.update_layout(
    xaxis_title="Importance"
    , yaxis_title="Feature"
    , yaxis=dict(
        autorange="reversed")  # Reverse the y-axis for a similar order to Seaborn
    , template="seaborn"  # Clean background style
)

# Show the figure
fig.show();

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Feature importances plot Option 3: yellowbrick (seems to accomplish in less code!)

from yellowbrick.model_selection import (FeatureImportances, )
plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots(figsize=(10, 8))
fi_viz = FeatureImportances(
    best_xgb, topn=15
    , colormap='RdBu'
)
fi_viz.fit(X_train, y_train)
fi_viz.show();


# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

# PLOTLY EXPRESS #

# px scatter plot to viz in/out flows:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

fig = px.scatter(
    dataframe=df
    , x='date'
    , y='value'
    , width=1200, height=1000
    , color='direction' # for in/out flows (df would need a 'direction' col with 'in'/'out' values)
    , opacity=0.5
    , size='abs_val_USD'
    . title='BTC Transfers (In/Out)'
    , hover_data={
        'date': '|%Y-%m-%d %H:%M'
        , 'abs_val_USD': ':$,.2f'
        , 'receiving_address': True
        , 'counterparty_address': True
        }
    , labels={
        'abs_val_native': 'Amount Native Asset (BTC)'
        , 'abs_val_USD': 'Amount USD'
        }
    , size_max=100
    )
    
fig.show()




# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

