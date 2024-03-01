// #include <stdio.h>
// #include <limits.h>
// #include <float.h>

// int main() {
//     printf("Data Type     Size (bytes)   Minimum Value            Maximum Value\n");
//     printf("----------------------------------------------------------------\n");

//     // Integer types
//     printf("int           %lu            %d                     %d\n", sizeof(int), INT_MIN, INT_MAX);
//     printf("long int      %lu            %ld                    %ld\n", sizeof(long int), LONG_MIN, LONG_MAX);
//     printf("short int     %lu            %d                     %d\n", sizeof(short int), SHRT_MIN, SHRT_MAX);

//     // Floating-point types
//     printf("float         %lu            %e            %e\n", sizeof(float), FLT_MIN, FLT_MAX);
//     printf("double        %lu            %e            %e\n", sizeof(double), DBL_MIN, DBL_MAX);

//     return 0;
// } - Способ 1.

// #include <iostream>
// #include <limits>

// int main() {
//     std::cout << "Using Standard Library Constants:\n";
//     std::cout << "int: " << std::numeric_limits<int>::min() << " to " << std::numeric_limits<int>::max() << std::endl;
//     std::cout << "long int: " << std::numeric_limits<long int>::min() << " to " << std::numeric_limits<long int>::max() << std::endl;
//     std::cout << "short int: " << std::numeric_limits<short int>::min() << " to " << std::numeric_limits<short int>::max() << std::endl;
//     std::cout << "float: " << -std::numeric_limits<float>::max() << " to " << std::numeric_limits<float>::max() << std::endl;
//     std::cout << "double: " << -std::numeric_limits<double>::max() << " to " << std::numeric_limits<double>::max() << std::endl;
//     return 0;
// } 
// - Способ 2.

#include <stdio.h>
#include <limits.h>
#include <float.h>

int main() {
    printf("Using Custom Computation (C):\n");
    int int_min = -(1 << (sizeof(int) * CHAR_BIT - 1));
    int int_max = (1 << (sizeof(int) * CHAR_BIT - 1)) - 1;
    long long_min = -(1LL << (sizeof(long) * CHAR_BIT - 1));
    long long_max = (1LL << (sizeof(long) * CHAR_BIT - 1)) - 1;
    short short_min = -(1 << (sizeof(short) * CHAR_BIT - 1));
    short short_max = (1 << (sizeof(short) * CHAR_BIT - 1)) - 1;

    printf("int: %d to %d\n", int_min, int_max);
    printf("long int: %ld to %ld\n", long_min, long_max);
    printf("short int: %d to %d\n", short_min, short_max);
    printf("float: %E to %E\n", -FLT_MAX, FLT_MAX);
    printf("double: %E to %E\n", -DBL_MAX, DBL_MAX);

    return 0;
} 
// - Способ 3.



