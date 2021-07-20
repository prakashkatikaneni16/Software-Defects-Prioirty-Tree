import six
import sys
sys.modules['sklearn.externals.six'] = six
from id3 import Id3Estimator
from id3 import export_graphviz
import pandas as pd
col_names = ['pfuncaffec','workfaffec','severity','custsaffec','priority']
# load dataset
bugdtls = pd.read_csv("data121a.csv", header=None, names=col_names)
#split dataset in features and target variable
feature_cols = ['pfuncaffec','workfaffec','severity','custsaffec']
X = bugdtls[feature_cols] # Features
y = bugdtls.priority # Target variable

#bunch = load_breast_cancer()
#print(bunch)
estimator = Id3Estimator()
estimator.fit(X, y)
export_graphviz(estimator.tree_, 'tree4.dot', feature_names = X.columns)
print("The dot file is successfully generated")


#Command to generate the tree in a .pdf: dot -Tpdf tree1.dot -o tree1.pdf
#https://pypi.org/project/decision-tree-id3/