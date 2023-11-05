function longestCommonPrefix(strs: string[]): string {
  if (strs == null || strs.length === 0) {
    return "";
  }
  const shortest = strs.reduce((a, b) => (a.length < b.length ? a : b));
  for (let i = 0; i < shortest.length; i++) {
    const c = shortest.charAt(i);
    for (const other of strs) {
      if (other.charAt(i) !== c) {
        return shortest.substring(0, i);
      }
    }
  }
  return shortest;
}
