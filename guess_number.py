from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


class GuessNumberGame:
    def __init__(self, username: str) -> None:
        self.username = username
        self.total_games = 0
        self.start_time = dt.now()

    @access_control
    def get_statistics(self) -> None:
        game_time = dt.now() - self.start_time
        print(f'Общее время игры: {game_time}, текущая игра - №{self.total_games}')

    @access_control
    def get_right_answer(self, number: int) -> None:
        print(f'Правильный ответ: {number}')

    def check_number(self, guess: int, number: int) -> bool:
        if guess == number:
            print(f'Отличная интуиция, {self.username}! Вы угадали число :)')
            return True
        if guess < number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False

    def play_game(self) -> None:
        self.total_games += 1
        number = randint(1, 100)
        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop".'
        )
        while True:
            user_input = input('Введите число или команду: ').strip().lower()
            match user_input:
                case 'stop':
                    break
                case 'stat':
                    self.get_statistics()
                case 'answer':
                    self.get_right_answer(number)
                case _:
                    try:
                        guess = int(user_input)
                    except ValueError:
                        print(UNKNOWN_COMMAND)
                        continue
                    if self.check_number(guess, number):
                        break

    def start(self) -> None:
        while True:
            self.play_game()
            play_again = input(f'\nХотите сыграть ещё? (yes/no): ')
            if play_again.strip().lower() not in ('y', 'yes'):
                break


def main() -> None:
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
    if username == ADMIN_USERNAME:
        print(
            '\nДобро пожаловать, создатель! '
            'Во время игры вам доступны команды "stat", "answer".'
        )
    else:
        print(f'\n{username}, добро пожаловать в игру!')
    game = GuessNumberGame(username)
    game.start()


if __name__ == '__main__':
    main()
