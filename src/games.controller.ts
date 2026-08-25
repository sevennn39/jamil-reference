import { Body, Controller, Get, Post } from '@nestjs/common';
import { GamesService } from './games.service';

@Controller('api/games')
export class GamesController {
  constructor(private readonly gamesService: GamesService) {}

  @Get('coin-flip')
  coinFlip() {
    return this.gamesService.coinFlip();
  }

  @Get('fun-fact')
  funFact() {
    return this.gamesService.funFact();
  }

  @Get('prediction')
  prediction() {
    return this.gamesService.prediction();
  }

  @Post('high-low')
  playHighLow(@Body() body: { guess?: string }) {
    return this.gamesService.highLow(body.guess ?? '');
  }

  @Post('quiz')
  quiz(@Body() body: { questionOne?: string; questionTwo?: string; questionThree?: string }) {
    return this.gamesService.quiz(body);
  }
}
