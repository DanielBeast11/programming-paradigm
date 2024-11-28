const singlesConsonants: string[] = [
    'б',
    'в',
    'г',
    'д',
    'з',
    'й',
    'к',
    'м',
    'н',
    'п',
    'р',
    'с',
    'т',
    'ф',
    'ц',
    'ч',
    'х',
    'щ',
    'ш'
  ];
  
  const doubleConsonants: string[] = ['н', 'м'];
  
  export function prepareDoubles(syllable: string, index: number, syllables: string[]): string {
    if (
      singlesConsonants.includes(syllable) &&
      !doubleConsonants.includes(syllable)
    ) {
      return '+';
    }
    return syllable;
  }