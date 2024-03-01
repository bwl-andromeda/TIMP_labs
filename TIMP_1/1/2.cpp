#include <iostream>
#include <limits>

int main() {
    setlocale(LC_ALL,"Ru");
    double number;

    std::cout << "Введите число: ";
    std::cin >> number;

    if (number >= std::numeric_limits<char>::min() && number <= std::numeric_limits<char>::max()) {
        std::cout << "Наименьший тип данных: char" << std::endl;
    } else if (number >= std::numeric_limits<short>::min() && number <= std::numeric_limits<short>::max()) {
        std::cout << "Наименьший тип данных: short" << std::endl;
    } else if (number >= std::numeric_limits<int>::min() && number <= std::numeric_limits<int>::max()) {
        std::cout << "Наименьший тип данных: int" << std::endl;
    } else if (number >= std::numeric_limits<long long>::min() && number <= std::numeric_limits<long long>::max()) {
        std::cout << "Наименьший тип данных: long long" << std::endl;
    } else if (number >= -std::numeric_limits<float>::max() && number <= std::numeric_limits<float>::max()) {
        std::cout << "Наименьший тип данных: float" << std::endl;
    } else if (number >= -std::numeric_limits<double>::max() && number <= std::numeric_limits<double>::max()) {
        std::cout << "Наименьший тип данных: double" << std::endl;
    } else {
        std::cout << "Такого типа данных не существует для данного числа." << std::endl;
    }

    return 0;
}
