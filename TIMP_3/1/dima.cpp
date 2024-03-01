#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
#include <windows.h>

// Функция для регистронезависимой проверки, содержит ли строка введенное слово или символ
bool containsSearchTerm(const std::string& str, const std::string& searchTerm) {
    std::string lowercaseStr = str;
    std::transform(lowercaseStr.begin(), lowercaseStr.end(), lowercaseStr.begin(), ::tolower);
    std::string lowercaseSearchTerm = searchTerm;
    std::transform(lowercaseSearchTerm.begin(), lowercaseSearchTerm.end(), lowercaseSearchTerm.begin(), ::tolower);

    return lowercaseStr.find(lowercaseSearchTerm) != std::string::npos;
}

int main() {
    SetConsoleOutputCP(65001);
    std::vector<std::string> data = {"apple", "banana", "cherry", "Date", "grape","231212","121212asdasd","asdasd123123"};

    std::string searchTerm;
    std::cout << "Введите слово или символ для поиска: ";
    std::cin >> searchTerm;

    // Поиск: находим элементы, содержащие введенное слово или символ (регистронезависимо)
    std::vector<std::string> results;
    std::copy_if(data.begin(), data.end(), std::back_inserter(results),
                 [searchTerm](const std::string& str) {
                     return containsSearchTerm(str, searchTerm);
                 });

    // Вывод результата
    std::cout << "Результаты поиска:" << std::endl;
    for (const std::string& result : results) {
        std::cout << result << std::endl;
    }

    return 0;
}

