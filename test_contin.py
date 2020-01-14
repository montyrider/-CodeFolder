from unittest import TestCase
from configparser import ConfigParser
import contin

class Test():

    def test_save_game_state(self):
        fileName = "game_state.conf"

        contin.saveGameState(fileName, "testData")



    def main(self):
        self.test_save_game_state()

if __name__ == '__main__':
    Test().main()
