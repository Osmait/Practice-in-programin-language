import { assertEquals } from "https://deno.land/std@0.192.0/testing/asserts.ts";
function removeDuplicate(nums: number[]): number {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == nums[i + 1]) {
      nums.splice(i, 1);
    }
  }
  console.log(nums);
  return nums.length;
}

Deno.test("Remove Duplicate", () => {
  const nums = [1, 1, 2, 2];
  const expect = [1, 2];
  const k = removeDuplicate(nums);
  assertEquals(k, 2);
  for (let i = 0; i < nums.length; i++) {
    assertEquals(nums[i], expect[i]);
  }
});
