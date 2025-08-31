class Solution {
public:
    int climbStairs(int n) {
        map<int, int> memo;
        rec(n, memo);
        
        for (const auto& [key, value] : memo)
            std::cout << key << " " << value << endl;

        return  memo[n];
    }

    int rec(int n, map<int, int>& memo) {
        if (n < 0) return 0;
        if (n == 0) return 1;

        if (!memo.contains(n)) 
            memo[n] = rec(n - 1, memo) + rec(n - 2, memo);
        return memo[n];
    }
};