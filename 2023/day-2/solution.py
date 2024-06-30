from dataclasses import dataclass


@dataclass
class GameSet():
    green: int
    red: int
    blue: int


@dataclass
class Game():
    id: int
    gamesets: list[GameSet]

@dataclass
class Configuration(GameSet):

    def power(self):
        return self.red * self.green * self.blue


def sample_parser(sample: list[str]) -> list[Game]:
    games: list[Game] = []
    for game in sample:
        game_sets: list[GameSet] = []
        id, sets = game.split(':')
        for s in sets.split(';'):
            color_map = {'red': 0, 'green': 0, 'blue': 0}
            colors = s.split(',')
            for color in colors:
                amount, name = color.strip().split(' ')
                color_map[name] = int(amount)
            game_sets.append(GameSet(**color_map))
        games.append(Game(id=int(id.split(' ')[-1]), gamesets=game_sets))
    return games


def is_game_possible(game: Game, configuration: Configuration ) -> bool:
    for gameset in game.gamesets:
        if gameset.red > configuration.red or gameset.green > configuration.green or gameset.blue > configuration.blue:
            return False
    return True


def get_minimum_configuration(game: Game) -> Configuration:
    max_red = max_green = max_blue = 0
    for gameset in game.gamesets:
        max_red = max(gameset.red, max_red)
        max_green = max(gameset.green, max_green)
        max_blue = max(gameset.blue, max_blue)
    return Configuration(red=max_red, green=max_green, blue=max_blue)


if __name__ == "__main__":

    with open("input", "r") as f:
        sample = f.read().splitlines()

    with open("test", "r") as f:
        test = f.read().splitlines()

    configuration = Configuration(red=12, green=13, blue=14)

    # solution 1
    games = sample_parser(sample)
    print(sum(game.id for game in games if is_game_possible(game, configuration)))

    # solution 2
    configurations = [get_minimum_configuration(game) for game in games]
    print(sum(c.power() for c in configurations))


