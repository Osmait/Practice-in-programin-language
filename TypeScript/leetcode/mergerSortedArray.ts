import { assertEquals } from "https://deno.land/std@0.192.0/testing/asserts.ts";

export function mergerSorted(
  num1: number[],
  num2: number[],
  m: number,
  n: number
): void {
  let p1 = m - 1;
  let p2 = n - 1;
  let p = m + n - 1;

  while (p1 >= 0 && p2 >= 0) {
    if (num1[p1] >= num2[p2]) {
      num1[p] = num1[p1];
      p1--;
    } else {
      num1[p] = num2[p2];
      p2--;
    }
    p--;
  }
  while (p2 > 0) {
    num1[p] = num2[p2];
    p--;
    p2--;
  }
}

Deno.test("mergerSorted", () => {
  const result = [1, 2, 2, 3, 5, 6];
  const num1 = [1, 2, 3, 0, 0, 0];
  const num2 = [2, 5, 6];
  const m = 3;
  const n = 3;
  mergerSorted(num1, num2, m, n);
  assertEquals(result, num1);
});
