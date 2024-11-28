import {replace} from './replace';
import {syllable} from './syllable';
import {katakanize} from './katakanize';
import {prepareDoubles} from './prepare_doubles';

export function transform(word: string): [string[], string[], string[]] {
  const chain: string[] = [word];

  // Разбиение на слоги
  let syllables: string[] = syllable(word);
  chain.push(syllables.join('-'));

  // Трансформация под произношение
  syllables = syllables.map((syl) => replace(syl, 0, syllables)) as string[];
  syllables = flat(syllables);
  chain.push(syllables.join('-'));

  // Обработка для катаканизации
  const prepared: string[] = syllables.map((syl) => prepareDoubles(syl, 0, syllables));
  chain.push(prepared.join('-'));

  // Катаканизация
  const katakana: string[] = prepared.map((syl) => katakanize(syl, 0, syllables));
  chain.push(katakana.join(''));

  return [katakana, syllables, chain];
}

function flat(syllables: (string | string[])[]): string[] {
  const result: string[] = [];
  syllables.forEach((syllable) => {
    if (typeof syllable === 'string') {
      result.push(syllable);
    } else {
      syllable.forEach((newSyllable) => {
        result.push(newSyllable);
      });
    }
  });

  return result;
}
