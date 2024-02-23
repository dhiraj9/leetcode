class Solution {
    public boolean isValidBST(TreeNode root) {
        List<Integer> inOrderList = new LinkedList<>();
        helper(root, inOrderList);
        int prev = inOrderList.get(0);
        for (int i = 1; i < inOrderList.size(); i++) {
            if (inOrderList.get(i) <= prev) return false;
            prev = inOrderList.get(i);
        }
        return true;
    }
    void helper(TreeNode treeNode, List<Integer> inOrderList) {
        if (treeNode == null) return;
        helper(treeNode.left, inOrderList);
        inOrderList.add(treeNode.val);
        helper(treeNode.right, inOrderList);
    }
}