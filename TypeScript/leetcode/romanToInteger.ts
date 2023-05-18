function romanToInt(s: string): number {
  const romanMap: Record<string, number> = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let result = 0;
  for (let i = 0; i < s.length; i++) {
    const value = romanMap[s[i]];
    if (i < s.length - 1 && value < romanMap[s[i + 1]]) {
      result -= value;
    } else {
      result += value;
    }
  }
  return result;
}
