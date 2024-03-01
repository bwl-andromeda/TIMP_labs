#include <iostream>
#include <vector>
#include <chrono>
using namespace std;

static const int N = 20000;

// Функция для версии программы с массивом
void arrayVersion() {
    int a[N];
    for (int i = 2; i < N; i++) {
        a[i] = 1;
    }
    for (int i = 2; i < N; i++) {
        if (a[i]) {
            for (int j = i; j * i < N; j++) {
                a[i * j] = 0;
            }
        }
    }
}

// Функция для версии программы с std::vector
void vectorVersion() {
    vector<int> a(N, 1);
    for (int i = 2; i < N; i++) {
        if (a[i]) {
            for (int j = i; j * i < N; j++) {
                a[i * j] = 0;
            }
        }
    }
}

int main() {
    // Измерение времени выполнения для версии с массивом в тиках
    auto startArray = chrono::high_resolution_clock::now();
    arrayVersion();
    auto endArray = chrono::high_resolution_clock::now();
    chrono::nanoseconds durationArray = chrono::duration_cast<chrono::nanoseconds>(endArray - startArray);

    // Измерение времени выполнения для версии с std::vector в тиках
    auto startVector = chrono::high_resolution_clock::now();
    vectorVersion();
    auto endVector = chrono::high_resolution_clock::now();
    chrono::nanoseconds durationVector = chrono::duration_cast<chrono::nanoseconds>(endVector - startVector);

    // Вывод результатов
    cout << "Runtime for the array version: " << durationArray.count() << " nanoseconds" << endl;
    cout << "Execution time of version with std::vector: " << durationVector.count() << " nanoseconds" << endl;

    if (durationArray < durationVector) {
        cout << "Array version is faster." << endl;
    } else if (durationArray > durationVector) {
        cout << "Version with std::vector is faster\n" << endl;
    } else {
        cout << "Версии выполняются примерно за одинаковое время." << endl;
    }

    return 0;
}
