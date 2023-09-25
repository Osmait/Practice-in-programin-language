const isAlienSorted = (palabras: string[], orden: string): boolean => {
  // Crear mapa del diccionario alienigena
  let mapa_diccionario = new Map();
  for (let i = 0; i < orden.length; i++) {
    mapa_diccionario[orden[i]] = i;
  }

  // Revisar el orden de las palabras
  for (let i = 1; i < palabras.length; i++) {
    // T = 0(n)   S = 0(m)
    if (!comparar(palabras[i - 1], palabras[i], mapa_diccionario)) return false;
  }
  return true;
};

// O(longitud de la palabra mÃ¡s larga)
const comparar = (
  palabra1: string,
  palabra2: string,
  mapa_diccionario: Map<string, number>
): boolean => {
  const longitud = Math.min(palabra1.length, palabra2.length);
  for (let i = 0; i < longitud; i++) {
    if (mapa_diccionario[palabra1[i]] < mapa_diccionario[palabra2[i]]) {
      return true;
    }
    if (mapa_diccionario[palabra1[i]] > mapa_diccionario[palabra2[i]]) {
      return false;
    }
  }
  return palabra1.length <= palabra2.length;
};
