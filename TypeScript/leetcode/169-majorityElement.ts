import { assertEquals } from "https://deno.land/std@0.192.0/testing/asserts.ts";

function majorityelement1(nums: number[]): number {
  const numMap: Map<number, number> = new Map();
  const numMax: Map<string, number> = new Map();
  numMax.set("key", 0);
  numMax.set("max", 0);

  for (const n of nums) {
    numMap.set(n, (numMap.get(n)! || 0) + 1);
  }
  for (const [key, value] of numMap) {
    if (value > numMax.get("max")!) {
      numMax.set("max", value);

      numMax.set("key", key);
    }
  }
  return numMax.get("max")!;
}

function majorityelement2(nums: number[]): number {
  let res = 0;
  let count = 0;

  for (const n of nums) {
    if (count === 0) {
      res = n;
    }
    count += n === res ? 1 : -1;
  }
  return res;
}

function majorityelement3(nums: number[]): number {
  const count: Map<number, number> = new Map();
  let res = 0;
  let maxCount = 0;
  for (const n of nums) {
    count.set(n, (count.get(n) || 0) + 1);
    res = count.get(n)! > maxCount ? n : res;
    maxCount = Math.max(count.get(n)!, maxCount);
  }
  return res;
}

Deno.test("majorityelement1", () => {
  const nums = [1, 2, 2];
  const n = majorityelement1(nums);
  const n2 = majorityelement2(nums);
  const n3 = majorityelement3(nums);
  assertEquals(n, 2);
  assertEquals(n3, 2);
  assertEquals(n2, 2);
});
