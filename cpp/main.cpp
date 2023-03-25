#include <iostream>
#include <map>

int main()
{
    std::map<std::string, std::string> dict;
    dict["hello"] = "world";
    dict["foo"] = "bar";
    for(auto& pair : dict)
        std::cout << pair.first << " " << pair.second << std::endl;
    return 0;
}