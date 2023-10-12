function firstNonConsecutiv(arr: number[]): number | null {
  for (let i = 0; i < arr.length; i++) {
    const current = arr[i] + 1;
    if (i < arr.length - 1) {
      const next = arr[i + 1];
      if (current != next) {
        return next;
      }
    }
  }
  return null;
}

console.log(firstNonConsecutiv([1, 2, 3, 4, 6, 7, 8]));

function nameShuffler(s: string): string {
  return s.split(" ").reverse().join(" ");
}

function GetSum(a: number, b: number): number {
  return Number(((a + b) * (Math.abs(a - b) + 1)) / 2);
}

function simpleMultiplication(number: number): number {
  return number % 2 === 0 ? number * 8 : number * 9;
}

function oddOrEven(n: number[]): string {
  return n.reduce((a, b) => a + b, 0) % 2 === 0 ? "even" : "odd";
}

function rowWeigths(n: number[]): number[] {
  let a: number = 0;
  let b: number = 0;

  for (let i = 0; i < n.length; i++) {
    if (n[i] % 2 === 0) a += n[i];
    else b += n[i];
  }
  return [a, b];
}

function predictAge(...ages: number[]): number {
  return Math.floor(Math.sqrt(ages.reduce((a, b) => a + b * b, 0)) / 2);
}

console.log(predictAge(65, 60, 75, 55, 60, 63, 64, 45));

function getmiddle(s: string): string {
  const middle = s.length / 2;
  return s.length % 2 === 0
    ? s.substring(middle - 1, middle + 1)
    : s.substring(middle, middle + 1);
}

function CalculateAge(birth: number, yearTo: number): String {
  const age = yearTo - birth;
  if (age === 0) return "You were born this very year!";
  if (age > 0) return `You are ${age} year${age > 1 ? "s" : ""} old`;
  return `You will be born in ${-age} year${-age > 1 ? "s" : ""}`;
}
function evaporator(
  content: number,
  evapPerDay: number,
  threshold: number
): number {
  let days = 0;
  const limit = content * (threshold / 100);
  while (content > limit) {
    content -= content * (evapPerDay / 100);
    days++;
  }
  return days;
}

function MaxAbsLengthDiff(a1: String[], a2: String[]): number {
  if (a1.length === 0 || a2.length === 0) return -1;
  const a1Sorted = a1.sort();
  const a2Sorted = a2.sort();
  const a1SortedLength = a1Sorted.length;
  const a2SortedLength = a2Sorted.length;
  let max = 0;
  for (let i = 0; i < a1SortedLength; i++) {
    const diff = Math.abs(a1Sorted[i].length - a2Sorted[i].length);
    if (diff > max) max = diff;
  }
  return max;
}

function CalculartePetYears(humanYears: number): number[] {
  if (humanYears === 1) return [1, 15, 15];
  if (humanYears === 2) return [2, 24, 24];
  return [humanYears, 24 + (humanYears - 2) * 4, 24 + (humanYears - 2) * 5];
}
