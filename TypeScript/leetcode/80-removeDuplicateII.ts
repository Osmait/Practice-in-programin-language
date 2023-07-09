import { assertEquals } from "https://deno.land/std@0.192.0/testing/asserts.ts";

function removeDuplicateII(nums: number[]): number {
  if (nums.length <= 2) return nums.length;

  let k = 2;

  for (let i = 2; i < nums.length; i++) {
    if (nums[i] != nums[k - 2]) {
      nums[k] = nums[i];
      k++;
    }
  }

  return k;
}

console.log(removeDuplicateII([1, 1, 1, 2, 2, 3]));

Deno.test("remove Duplicate II", () => {
  const nums = [1, 1, 1, 2, 2, 3];
  const expect = [1, 1, 2, 2, 3];
  const k = removeDuplicateII(nums);
  console.log(k);
  assertEquals(k, 5);
  for (let i = 0; i < k; i++) {
    assertEquals(nums[i], expect[i]);
  }
});
