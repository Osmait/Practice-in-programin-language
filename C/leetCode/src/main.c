#include "include/containtDuplicate.h"
#include <stdio.h>

int main() {
  int nums[5] = {1, 2, 3, 4, 1};
  bool result = containsDuplicate(nums, 5);
  printf("%d", result);
  return 0;
}
