class Solution {
public:
    int maxProfit(const std::vector<int>& prices) {
    if (prices.empty()) {
        return 0;  // No prices available, so no profit can be made
    }

    int minPrice = prices[0];
    int maxProfit = 0;

    for (int i = 1; i < prices.size(); i++) {
        int currentPrice = prices[i];

        if (currentPrice < minPrice) {
            minPrice = currentPrice;  // Update the minimum price
        } else {
            int profit = currentPrice - minPrice;
            maxProfit = std::max(maxProfit, profit);  // Update the maximum profit
        }
    }

    return maxProfit;
}
};