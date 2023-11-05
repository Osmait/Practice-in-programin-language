export const nthFibonacci = (number: number): number => {
  if (number < 0) {
    throw "Number should be greater than 0";
  }
  if (number === 0) {
    return 0;
  }
  let a = 0,
    b = 0;
  for (let i = 1; i < number; ++i) {
    const c = a + b;
    a = b;
    b = c;
  }
  return b;
};

export const nthFibonacciRecursively = (number: number): number => {
  if (number === 0) {
    return 0;
  }

  if (number <= 2) {
    return 1;
  }

  return (
    nthFibonacciRecursively(number - 1) + nthFibonacciRecursively(number - 2)
  );
};
