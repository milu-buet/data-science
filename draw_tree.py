##-------------------------------------------------------------------------
# conda install python-graphviz
# Draw a decision tree:
# dot -Tpng -o output.png output.dot -Gdpi=200
##-------------------------------------------------------------------------
from sklearn.tree import export_graphviz
import os, subprocess, sys
def visualize_tree(tree, feature_names, output):
	with open(output+".dot", 'w') as f:
		export_graphviz(tree, out_file=f, feature_names=feature_names, filled=True, rounded=True)
		command = ["dot", "-Tpng", output+".dot", "-o", output + ".png", "-Gdpi=200"]
	try:
		if sys.platform.startswith('win'):
			subprocess.check_call(command, shell=True)
		else:
			subprocess.check_call(command)
	except:
		exit("Could not run dot, ie graphviz, to produce visualization")
	print('File saved to {}.png'.format(output))