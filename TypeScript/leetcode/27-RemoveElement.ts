import { assertEquals } from "https://deno.land/std@0.192.0/testing/asserts.ts";

function removeElement(nums: number[], val: number): number {
  let k = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != val) {
      nums[k] = nums[i];
      k++;
    }
  }
  return k;
}

Deno.test("TestRemoveElement", () => {
  const nums = [3, 2, 2, 3];
  const val = 3;
  const k = removeElement(nums, val);
  const expect = 2;
  const expectedNums = [2, 2];
  assertEquals(k, expect);
  for (let i = 0; i < k; i++) {
    assertEquals(nums[i], expectedNums[i]);
  }
});
