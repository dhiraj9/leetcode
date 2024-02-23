class Solution {
    char[][] matrix;
    char[] letters;
    boolean[][] visited;
    public boolean exist(char[][] board, String word) {
        matrix = board;
        letters = word.toCharArray();
        int rowLen = board.length;
        int colLen = board[0].length;
        for (int i = 0; i < rowLen; i++) {
            for (int j = 0; j < colLen; j++) {
                visited = new boolean[rowLen][colLen];
                if (dfs(i, j, 0)) return true;
            }
        }
        return false;
    }
    private boolean dfs(int curRow, int curCol, int curIndex) {
        if (curIndex == letters.length) return true;
        if (curCol < 0 || curCol >= matrix[0].length) return false;
        if (curRow < 0 || curRow >= matrix.length) return false;
        if (matrix[curRow][curCol] != letters[curIndex]) return false;
        if (visited[curRow][curCol]) return false;
        visited[curRow][curCol] = true;
        boolean top = dfs(curRow - 1, curCol, curIndex + 1);
        boolean down = dfs(curRow + 1, curCol, curIndex + 1);
        boolean left = dfs(curRow, curCol - 1, curIndex + 1);
        boolean right = dfs(curRow, curCol + 1, curIndex + 1);
        boolean ans = top || down || left || right;
        if (!ans) visited[curRow][curCol] = false;
        return ans;
    }
}
