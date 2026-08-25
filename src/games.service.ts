import { Injectable } from '@nestjs/common';

const FUN_FACTS = [
  'Cat urine glows under a blacklight.',
  "A shrimp's heart is in its head.",
  'Dreamt is the only English word that ends in the letters mt.',
  'A dime has 118 ridges around the edge.',
  'A crocodile cannot stick its tongue out.',
  "The 'sixth sick sheik's sixth sheep's sick' is believed to be the toughest tongue twister in the English language.",
];

const PREDICTIONS = [
  "You'll have a great day!",
  'Someone will derail your plans...',
  "Things won't work out how you think.",
  'You may end up tired by the end of the day.',
  "It'll just be a day.",
  'You may run into some issues.',
];

@Injectable()
export class GamesService {
  coinFlip() {
    return { result: Math.random() < 0.5 ? 'Heads!' : 'Tails!' };
  }

  funFact() {
    return { fact: this.randomItem(FUN_FACTS) };
  }

  prediction() {
    return { prediction: this.randomItem(PREDICTIONS) };
  }

  highLow(guess: string) {
    const startingNumber = this.randomNumber();
    const nextNumber = this.randomNumber();
    const actualDirection = nextNumber > startingNumber ? 'Higher' : nextNumber < startingNumber ? 'Lower' : 'Same';

    return {
      startingNumber,
      nextNumber,
      guess,
      actualDirection,
      correct: guess === actualDirection,
      message: actualDirection === 'Same'
        ? `It was the same! [${nextNumber}]`
        : `It was ${actualDirection.toLowerCase()}! [${nextNumber}]`,
    };
  }

  quiz(answers: { questionOne?: string; questionTwo?: string; questionThree?: string }) {
    const results = [
      this.checkAnswer(answers.questionOne, 'canberra', 'Canberra is the capital of Australia.'),
      this.checkAnswer(answers.questionTwo, '348', '12 x 29 = 348.'),
      this.checkAnswer(answers.questionThree, 'mitochondria', 'The mitochondria are the powerhouse of the cell.'),
    ];

    return {
      score: results.filter((result) => result.correct).length,
      results,
    };
  }

  private randomNumber() {
    return Math.floor(Math.random() * 12) + 1;
  }

  private randomItem<T>(items: T[]) {
    return items[Math.floor(Math.random() * items.length)];
  }

  private checkAnswer(answer: string | undefined, expected: string, explanation: string) {
    const correct = answer?.trim().toLowerCase() === expected;
    return {
      correct,
      message: correct ? `Correct! ${explanation}` : `Not quite. The correct answer is ${expected[0].toUpperCase()}${expected.slice(1)}.`,
    };
  }
}
