class Solution {
public:
    int climbStairs(int n) {
        map<int, int> memo;
        rec(n, memo);
        return iterative(n);
        return  memo[n];
    }

    int rec(int n, map<int, int>& memo) {
        if (n < 0) return 0;
        if (n == 0) return 1;

        if (!memo.contains(n)) 
            memo[n] = rec(n - 1, memo) + rec(n - 2, memo);
        return memo[n];
    }

    int iterative(int n) {
        map<int, int> memo;
        memo[1] = 1;
        memo[2] = 2;

        for (int i = 3; i <= n; i++) {
            memo[i] = memo[i-1] + memo[i-2];
        }

        return memo[n];
    }
};