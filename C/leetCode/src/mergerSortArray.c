#include <stdio.h>

#define ANSI_COLOR_RED "\x1b[31m"
#define ANSI_COLOR_GREEN "\x1b[32m"

void merge_sorted_array(int *nums1, int *nums2, int m, int n) {
  int p1 = m - 1;
  int p2 = n - 1;
  int p = m + n - 1;

  while (p1 >= 0 && p2 >= 0) {
    if (nums1[p1] >= nums2[p2]) {
      nums1[p] = nums1[p1];
      p1--;
    } else {
      nums1[p] = nums2[p2];
      p2--;
    }
    p--;
  }

  while (p2 >= 0) {
    nums1[p] = nums2[p2];
    p--;
    p2--;
  }
}

void view(int *arr, int len) {
  for (int i = 0; i < len; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

void test_passed(const char *test_name) {
  printf(ANSI_COLOR_GREEN "[PASSED] %s ok\n", test_name);
}

void test_failed(const char *test_name) {
  printf(ANSI_COLOR_RED "[FAILED] %s\n", test_name);
}

void test_merge_sorted_array() {
  int nums1[9] = {1, 2, 3, 0, 0, 0};
  int nums2[3] = {2, 5, 6};
  int m = 3;
  int n = 3;

  merge_sorted_array(nums1, nums2, m, n);

  // Verificar si el resultado es igual al array esperado
  int expected_result[6] = {1, 2, 2, 3, 5, 6};
  assertEqualArray(expected_result, nums1);
}

void assertEqualArray(int expected_result[], int arr2[]) {
  int i;
  for (i = 0; i < 6; i++) {
    if (arr2[i] != expected_result[i]) {
      test_failed("test_merge_sorted_array");
      return;
    }
  }

  test_passed("test_merge_sorted_array");
}

int main() {
  test_merge_sorted_array();

  return 0;
}
