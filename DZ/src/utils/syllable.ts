export function syllable(word: string): string[] {
  const vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь'];
  const consonants = [
    'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
    'н', 'п', 'р', 'с', 'т', 'ф', 'ц', 'ч', 'х', 'ш', 'щ'
  ];
  const complexSyllables = ['дз'];
  const special = ['ъ'];
  

  const arr = word.toLowerCase().split('');
  const syllables: string[] = [];
  let currentSyllable: string[] = [];

  function endSyllable() {
    syllables.push(currentSyllable.join(''));
    currentSyllable = [];
  }

  function addLetter(letter: string) {
    currentSyllable.push(letter);
  }

  arr.forEach((letter) => {
    if (vowels.includes(letter)) {
      addLetter(letter);
      endSyllable();
    } else if (
      consonants.includes(letter) &&
      complexSyllables.includes(currentSyllable.join('') + letter)
    ) {
      addLetter(letter);
    } else if (
      consonants.includes(letter) &&
      currentSyllable.length !== 0
    ) {
      if (
        currentSyllable[0] === letter &&
        syllables.length === 0
      ) {
        return;
      }
      endSyllable();
      addLetter(letter);
    } else if (
      consonants.includes(letter) &&
      currentSyllable.length === 0
    ) {
      addLetter(letter);
    } else if (special.includes(letter)) {
      endSyllable();
    }
  });

  if (currentSyllable.length) {
    endSyllable();
  }

  return syllables;
}
