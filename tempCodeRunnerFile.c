#include <stdio.h>

// Function to find and print all subsets whose sum equals target
void subsetSum(int arr[], int n, int index, int target, int subset[], int size, int sum)
{
    // If current sum matches target, print the subset
    if (sum == target)
    {
        printf("{ ");
        for (int i = 0; i < size; i++)
            printf("%d ", subset[i]);
        printf("}\n");
        return;
    }

    // If all elements are processed OR sum exceeds target, stop exploring this path
    if (index == n || sum > target)
        return;

    // INCLUDE current element in subset
    subset[size] = arr[index];
    subsetSum(arr, n, index + 1, target, subset, size + 1, sum + arr[index]);

    // EXCLUDE current element and move to next
    subsetSum(arr, n, index + 1, target, subset, size, sum);
}

int main()
{
    int n;

    // Input number of elements
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];

    // Input array elements
    printf("Enter elements:\n");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    int target;

    // Input target sum
    printf("Enter target sum: ");
    scanf("%d", &target);

    int subset[n];   // Temporary array to store current subset

    printf("Subsets with given sum are:\n");

    // Initial call to recursive function
    subsetSum(arr, n, 0, target, subset, 0, 0);

    return 0;
}