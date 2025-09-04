#include <cmath>

class Solution {
public:
    int findClosest(int x, int y, int z) {
        int distance_xz = std::abs(x - z);
        int distance_yz = std::abs(y - z);

        if (distance_xz > distance_yz)
            return 2;
        if ((distance_xz < distance_yz))
            return 1;
        return 0;
    }
};