class Solution {
    public int minDistance(String word1, String word2) {

        int row = word2.length() + 1;
        int col = word1.length() + 1;

        int[][] dp = new int[row][col];

        dp[0][0] = 0;

        for (int i = 1; i < row; i++){
            dp[i][0] = i;
        }

        for (int j= 1; j< col; j++){
            dp[0][j] = j;
        }

        for (int i=1; i< row; i++){
            for (int j=1; j< col; j++){

                if (word1.charAt(j-1) == word2.charAt(i-1)){
                    dp[i][j] = dp[i-1][j-1];
                }

                else{
                    int left = dp[i][j-1];
                    int top = dp[i-1][j];
                    int diagonal = dp[i-1][j-1];

                    dp[i][j] = 1 +  Math.min(diagonal, Math.min(top, left));
                }

            }
        }

        return dp[row-1][col-1];
    }
}