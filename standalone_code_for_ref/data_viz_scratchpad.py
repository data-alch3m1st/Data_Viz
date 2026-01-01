# data_viz standalone code scratchpad #

'''
    Note: This is NOT an actual script meant to be run as-is; rather it is a simplified 'scratchpad' type mini-repo where I can keep and splendid and quirky bits of data visualization code that I find useful or interesting for future reference.
    
    Let the viz begin!
'''
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

# NUMERIC COLS BOXPLOT LOOP #

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
    sns.boxplot(
        data=df
        , x=col # can manipulate the orientation by assignment of 'x' / 'y';
        , ax=axes[i]
        , color=color
#         , orient="h"
        )
    axes[i].set_title(f'Boxplot of {col}')
    axes[i].grid()
    
# Hide any unused axes (if num_plots < num_rows * max_cols):
for j in range(num_plots, len(axes)):
    fig.delaxes(axes[j])
    
# Adjust layout and display the plot(s):
plt.tight_layout()
plt.show();



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
    axes[i].grid()
    
# Hide any unused axes (if num_plots < num_rows * max_cols):
for j in range(num_plots, len(axes)):
    fig.delaxes(axes[j])
    
# Adjust layout and display the plot(s):
plt.tight_layout()
plt.show();

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
