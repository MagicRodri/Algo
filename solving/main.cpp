#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <bitset>

const int MAX_N = 20;

int n;
std::vector<int> v;
std::unordered_map<std::bitset<MAX_N>, int> dp;

void op1(std::vector<int>& w, int i, int j) {
    std::reverse(w.begin() + i, w.begin() + j + 1);
}


void op2(std::vector<int>& w, int i, int j) {
    std::reverse(w.begin() + i, w.begin() + i + 2);
    std::reverse(w.begin() + i + 2, w.begin() + j + 1);
}

// fonction de recherche en profondeur avec élagage
int dfs(std::vector<int>& w, std::bitset<MAX_N>& visited) {
    if(visited.count() == n) {
        return 0;
    }

    if(dp.find(visited) != dp.end()) {
        return dp[visited];
    }

    int ans = n; // n est la valeur maximale possible
    for(int i = 0; i < n; ++i) {
        if(!visited.test(i)) {
            visited.set(i);
            for(int j = i+1; j < n; ++j) {
                if(!visited.test(j)) {
                    std::vector<int> copy(w);
                    op1(copy, i, j);
                    if(std::is_sorted(copy.begin(), copy.end())) {
                        ans = std::min(ans, 1 + dfs(copy, visited));
                    } else {
                        op2(copy, i, j);
                        if(std::is_sorted(copy.begin(), copy.end())) {
                            ans = std::min(ans, 2 + dfs(copy, visited));
                        }
                    }
                }
            }
            visited.reset(i);
        }
    }

    dp[visited] = ans;
    return ans;
}

int main() {
    std::cin >> n;
    v.resize(n);
    for(int i = 0; i < n; ++i) {
        std::cin >> v[i];
    }

    std::bitset<MAX_N> visited;
    int ans = dfs(v, visited);
    std::cout << ans << std::endl;

    return 0;
}
