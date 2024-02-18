 class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> answer = new ArrayList<>();
        if (root == null) return answer;
        ArrayDeque<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);
        List<List<Integer>> levels = new ArrayList<>();
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.remove();
                level.add(node.val);
                if (node.left != null)
                    queue.add(node.left);
                if (node.right != null)
                    queue.add(node.right);
            }
            levels.add(level);
        }
        boolean leftToRight = true;
        for (int i = 0; i < levels.size(); i++) {
            if (!leftToRight)
                Collections.reverse(levels.get(i));
            leftToRight = !leftToRight;
        }
        return levels;
    }
}