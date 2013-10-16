# post order to traverse trees
def postTrav(subtree):
	if subtree is not None:
		postTrav(subtree.left)
		postTrav(subtree.right)
		print subtree.data,

# previous order to traverse trees
def preTrav(subtree):
	if subtree is not None:
		print subtree.data,
		preTrav(subtree.left)
		preTrav(subtree.right)

# inorder to traverse trees
def inTrav(subtree):
	if subtree is not None:
		inTrav(subtree.left)
		print subtree.data,
		inTrav(subtree.right)

def find(tree, data):
	if tree is not None:
		if tree.data == data:
			print True
			return
		find(tree.left, data)
		find(tree.right, data)

if __name__ == '__main__':
	from binary_tree import binaryTree
	bt = binaryTree(4, binaryTree(3, binaryTree(2), binaryTree(5)), binaryTree(5, binaryTree(1), binaryTree(6)))
        print 'inorder:', inTrav(bt)
	print 'postorder:', postTrav(bt)
	print 'previous order:', preTrav(bt)
	find(bt, 1)
