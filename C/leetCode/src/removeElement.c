#include <stdio.h>

#define ANSI_COLOR_RED "\x1b[31m"
#define ANSI_COLOR_GREEN "\x1b[32m"

int removeElement(int *nums, int val, int length)
{
    int k = 0;

    for (int i = 0; i < length; i++)
    {
        if (nums[i] != val)
        {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}

void test_passed(const char *test_name)
{
    printf(ANSI_COLOR_GREEN "[PASSED] %s ok\n", test_name);
}

void test_failed(const char *test_name)
{
    printf(ANSI_COLOR_RED "[FAILED] %s\n", test_name);
}
void assertEqualArray(int expected_result[], int arr2[], int k)
{
    int i;
    for (i = 0; i < k; i++)
    {
        if (arr2[i] != expected_result[i])
        {
            test_failed("test_merge_sorted_array");
            return;
        }
    }

    test_passed("test_merge_sorted_array");
}

int main()
{
    int nums[] = {3, 2, 2, 3};
    int val = 3;
    int length = sizeof(nums) / sizeof(nums[0]);
    int k = removeElement(nums, val, length);

    int expected = 2;
    if (k == expected)
    {
        test_passed("Test Value");
    }
    else
    {
        test_failed("test value");
    }

    int expectedArray[2] = {2, 2};
    assertEqualArray(nums, expectedArray, k);

    return 0;
}
