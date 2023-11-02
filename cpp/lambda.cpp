#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

template <typename T>
void print(const T &v)
{
    for (auto el : v)
    {
        std::cout << el << " ";
    }
    std::cout << "\n";
}

int main()
{
    std::vector<int> a1{1, 5, -3, -2, 4, -7, 9};
    std::vector<std::string> a2{"kayak", "goal", "ete", "something"};
    print(a1);
    print(a2);
    std::sort(a1.begin(), a1.end(), [](auto a, auto b)
              { return std::abs(a) < std::abs(b); });
    auto count = std::count_if(a2.begin(), a2.end(), [](auto a)
                               {
        auto temp = a;
        std::reverse(temp.begin(),temp.end());
        return temp == a; });
    print(a1);
    std::cout << count;
    return 0;
}