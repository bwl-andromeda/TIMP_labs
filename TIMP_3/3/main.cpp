#include <iostream>
#include <cstdlib>

using namespace std;

struct Node {
    int data;
    int row;
    int col;
    Node* next;
};

void addNode(Node*& head, int data, int row, int col) {
    Node* newNode = new Node;
    newNode->data = data;
    newNode->row = row;
    newNode->col = col;
    newNode->next = head;
    head = newNode;
}

void printMatrix(Node** sparseMatrix, int numRows, int numCols) {
    // Create a 2D array to store the sparse matrix values
    int** resultMatrix = new int*[numRows];
    for (int i = 0; i < numRows; i++) {
        resultMatrix[i] = new int[numCols];
        for (int j = 0; j < numCols; j++) {
            resultMatrix[i][j] = 0;
        }
    }

    // Fill the result matrix with values from the sparse matrix
    for (int i = 0; i < numRows; i++) {
        Node* current = sparseMatrix[i];
        while (current != nullptr) {
            resultMatrix[current->row][current->col] = current->data;
            current = current->next;
        }
    }

    // Print the result matrix
    cout << "Матрица:\n";
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numCols; j++) {
            cout << resultMatrix[i][j] << " ";
        }
        cout << "\n";
    }

    // Clean up memory for the result matrix
    for (int i = 0; i < numRows; i++) {
        delete[] resultMatrix[i];
    }
    delete[] resultMatrix;
}


int main() {
    setlocale(LC_ALL,"Russian");
    int numRows, numCols;
    cout << "Введите количество строк матрицы:";
    cin >> numRows;
    cout << "Введите количество столбцов матрицы:";
    cin >> numCols;

    // Dynamic array for the matrix
    int** matrix = new int*[numRows];
    for (int i = 0; i < numRows; i++) {
        matrix[i] = new int[numCols];
    }

    // Initialize the matrix with random values
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numCols; j++) {
            matrix[i][j] = rand() % 10;
        }
    }

    // Dynamic array for the sparse matrix
    Node** sparseMatrix = new Node*[numRows];
    for (int i = 0; i < numRows; i++) {
        sparseMatrix[i] = nullptr;
    }

    // Convert the matrix to a sparse matrix
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numCols; j++) {
            if (matrix[i][j] != 0) {
                addNode(sparseMatrix[i], matrix[i][j], i, j);
            }
        }
    }

    // Print the matrix using the printMatrix function
    printMatrix(sparseMatrix, numRows, numCols);

    // Clean up memory
    for (int i = 0; i < numRows; i++) {
        Node* current = sparseMatrix[i];
        while (current != nullptr) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }

    for (int i = 0; i < numRows; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;

    delete[] sparseMatrix;

    return 0;
}
