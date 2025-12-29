# data_viz standalone code scratchpad #

'''
    Note: This is NOT an actual script meant to be run as-is; rather it is a simplified 'scratchpad' type mini-repo where I can keep and splendid and quirky bits of data visualization code that I find useful or interesting for future reference.
    
    Let the viz begin!
'''

# Machine Learning Useful Plots #

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