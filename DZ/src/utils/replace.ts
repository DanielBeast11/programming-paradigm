export function replace(
  syllable: string,
  index: number,
  syllables: string[]
): string {
  console.log(`Processing syllable: ${syllable}, index: ${index}`);

  if (singlesConsonants[syllable]) {
    return singlesConsonants[syllable];
  }

  if (pairs[syllable]) {
    const replacement = pairs[syllable];
    const result = Array.isArray(replacement) ? replacement.join('') : replacement;
    return result;
  }

  let result = syllable;
  for (const searchChars in replacePairs) {
    if (Object.prototype.hasOwnProperty.call(replacePairs, searchChars)) {
      const regex = new RegExp(searchChars, 'g');
      const replaced = result.replace(regex, replacePairs[searchChars]);
      if (replaced !== result) {
        result = replaced;
      }
    }
  }
  
  return result;
}




  
  const pairs: Record<string, string | string[]> = {
    'мы': ['му', 'и'],
    'ху': 'фу',
    'фу': 'фу',
    'цы': 'цу',
    'ть': 'чи',
    'чи': 'чи',
    'ча': 'тя',
    'чу': 'тю',
    'чо': 'тё',
    'ти': 'чи',
    'ту': 'цу',
    'цу': 'цу',
    'ди': 'дзи',
    'ду': 'зу',
    'жу': 'зю',
    'жо': 'зё',
    'жа': 'дзя',
    'зя': 'дзя',
    'зю': 'дзю',
    'зё': 'дзё',
    'жэ': 'зэ',
    'ша': 'ся',
    'ща': 'ся',
    'шу': 'сю',
    'щу': 'сю',
    'щи': 'щи',
    'ши': 'щи',
    'си': 'щи',
    'що': 'сё',
    'шо': 'сё',
  };
  
  const replacePairs: Record<string, string> = {
    'ь': 'и',
    'щ': 'с',
    'ш': 'с',
    'йо': 'ё',
    'йу': 'ю',
    'йа': 'я',
    'в': 'б',
    'л': 'р',
    'ы': 'у',
    'е': 'э',
    'ц': 'т',
    'ч': 'т',
    'ф': 'х',
    'ж': 'з',
  };
  
  const singlesConsonants: Record<string, string> = {
    'б': 'бу',
    'в': 'бу',
    'г': 'гу',
    'д': 'до',
    'ж': 'зу',
    'з': 'зу',
    'й': 'и',
    'к': 'ку',
    'л': 'ру',
    'м': 'му',
    'п': 'пу',
    'р': 'ру',
    'с': 'су',
    'т': 'то',
    'ф': 'фу',
    'ц': 'цу',
    'ч': 'чи',
    'х': 'хо',
    'ш': 'щи',
    'щ': 'щи'
  };
  