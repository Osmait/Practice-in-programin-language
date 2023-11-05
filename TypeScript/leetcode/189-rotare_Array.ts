import { assertEquals } from "https://deno.land/std@0.192.0/testing/asserts.ts";
function array_rotate(nums: number[], k: number): void {
  const n = nums.length;
  k = k % n;
  reverse(nums, 0, n - 1);
  reverse(nums, 0, k - 1);
  reverse(nums, k, n - 1);
}

function reverse(nums: number[], start: number, end: number): void {
  while (start < end) {
    let temp = nums[start];
    nums[start] = nums[end];
    nums[end] = temp;
    start++;
    end--;
  }
}

Deno.test("test Array Rotate", () => {
  let nums = [1, 2];
  const k = 3;
  array_rotate(nums, k);
  assertEquals(nums, [2, 1]);
});
