import os
import shutil
original = r'tree4.dot'
target = r'./graphviz/tree4.dot'
shutil.copyfile(original, target)
os.chdir("./graphviz/")
os.system("dot -Tpdf tree4.dot -o tree4.pdf")
original = r'tree4.pdf'
target = r'../tree4.pdf'
shutil.copyfile(original, target)
print("The .pdf file of the priority tree successfully generated")

#Command to generate the tree in a .pdf: dot -Tpdf tree1.dot -o tree1.pdf
#https://pypi.org/project/decision-tree-id3/