#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

// Структура для узла матрицы
struct Node {
    int data;          // Данные узла (значение элемента матрицы)
    Node* next;        // Указатель на следующий элемент в строке
    Node* previous;    // Добавлен указатель на предыдущий элемент
};

// Структура для строки матрицы
struct Row {
    Node* firstNode;    // Указатель на первый элемент в строке
    Row* nextRow;       // Указатель на следующую строку
};

// Функция для создания мультиматрицы заданных размеров
Row* createMultilist(int numRows, int numCols) {
    Row* firstRow = nullptr;  // Указатель на первую строку
    Row* currRow = nullptr;   // Указатель на текущую строку

    for (int i = 0; i < numRows; ++i) {
        Row* newRow = new Row;
        newRow->firstNode = nullptr;
        newRow->nextRow = nullptr;
        Node* currNode = nullptr;

        for (int j = 0; j < numCols; ++j) {
            Node* newNode = new Node;
            newNode->data = rand() % 10;
            newNode->next = nullptr;
            newNode->previous = nullptr;  // Инициализируем указатель на предыдущий элемент

            if (newRow->firstNode == nullptr) {
                newRow->firstNode = newNode;
                currNode = newNode;
            } else {
                currNode->next = newNode;
                newNode->previous = currNode;  // Устанавливаем указатель на предыдущий элемент
                currNode = newNode;
            }
        }

        if (currRow == nullptr) {
            firstRow = newRow;
            currRow = newRow;
        } else {
            currRow->nextRow = newRow;
            currRow = newRow;
        }
    }

    return firstRow;
}

// Функция для освобождения памяти, выделенной под мультиматрицу
void freeMultilist(Row* firstRow) {
    while (firstRow != nullptr) {
        Node* currNode = firstRow->firstNode;
        while (currNode != nullptr) {
            Node* nextNode = currNode->next;
            delete currNode;
            currNode = nextNode;
        }
        Row* nextRow = firstRow->nextRow;
        delete firstRow;
        firstRow = nextRow;
    }
}

// Функция для умножения двух мультиматриц и сохранения результата в третьей
void multiplyMultilists(Row* firstRow1, Row* firstRow2, int numRows1, int numCols1, int numRows2, int numCols2, Row* result) {
    if (numCols1 != numRows2) {
        cout << "Умножение матриц невозможно при заданных размерах матриц.\n";
        return;
    }

    Row* currRowResult = result;

    while (currRowResult != nullptr) {
        Node* currNodeResult = currRowResult->firstNode;
        Row* currRow1 = firstRow1;
        Row* currRow2 = firstRow2;

        while (currNodeResult != nullptr) {
            if (currRow1 == nullptr || currRow2 == nullptr) {
                cout << "-----------------------\n";
                return;
            }

            Node* currNode1 = currRow1->firstNode;
            Node* currNode2 = currRow2->firstNode;

            int sum = 0;
            for (int k = 0; k < numCols1; ++k) {
                if (currNode1 != nullptr && currNode2 != nullptr) {
                    sum += currNode1->data * currNode2->data;
                    currNode1 = currNode1->next;
                    currNode2 = currNode2->next;
                } else {
                    cout << "---------------------\n";
                    return;
                }
            }

            currNodeResult->data = sum;

            currNodeResult = currNodeResult->next;
            currRow1 = currRow1->nextRow;
            currRow2 = currRow2->nextRow;
        }

        currRowResult = currRowResult->nextRow;
    }
}

// Функция для вывода мультиматрицы на экран
void printMultilist(Row* firstRow) {
    Row* currRow = firstRow;
    while (currRow != nullptr) {
        Node* currNode = currRow->firstNode;
        while (currNode != nullptr) {
            cout << currNode->data << " ";
            currNode = currNode->next;
        }
        cout << endl;
        currRow = currRow->nextRow;
    }
}

// Основная функция
int main() {
    srand(time(0));
    int numRows1, numCols1, numRows2, numCols2;

    // Ввод размеров матриц
    cout << "Введите количество строк и столбцов для первой матрицы: ";
    cin >> numRows1 >> numCols1;
    cout << "Введите количество строк и столбцов для второй матрицы: ";
    cin >> numRows2 >> numCols2;

    // Создание и вывод первой мультиматрицы
    Row* firstRow1 = createMultilist(numRows1, numCols1);
    cout << "Первая матрица:\n";
    printMultilist(firstRow1);

    // Создание и вывод второй мультиматрицы
    Row* firstRow2 = createMultilist(numRows2, numCols2);
    cout << "Вторая матрица:\n";
    printMultilist(firstRow2);

    // Создание мультиматрицы для результата умножения
    Row* result = createMultilist(numRows1, numCols2);

    // Умножение матриц и вывод результата
    multiplyMultilists(firstRow1, firstRow2, numRows1, numCols1, numRows2, numCols2, result);
    cout << "Результат умножения матриц:\n";
    printMultilist(result);

    // Освобождение памяти
    freeMultilist(firstRow1);
    freeMultilist(firstRow2);
    freeMultilist(result);

    return 0;
}
