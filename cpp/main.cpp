#include <iostream>
#include <ctime>

int main()
{
    int num;
    int guess;
    int tries = 0;
    int number_range = 100;
    srand(time(0));
    num = rand() % number_range + 1;
    std::cout << "Guess My Number Game" << std::endl;
    do
    {
        std::cout << "Enter a guess between 1 and " << number_range << ": ";
        std::cin >> guess;
        tries++;
        if (guess > num)
        {
            std::cout << "Too high!" << std::endl;
        }
        else if (guess < num)
        {
            std::cout << "Too low!" << std::endl;
        }
        else
        {
            std::cout << "Correct! You got it in " << tries << " guesses!" << std::endl;
        }
    } while (guess != num);
    return 0;
}