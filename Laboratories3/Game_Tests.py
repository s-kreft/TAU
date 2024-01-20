import unittest
import Game
import keyboard

class GameTestCase(unittest.TestCase):

    def setUp(self) -> None:
        Game.PrepareGame()
        return super().setUp()

    def test_is_out_of_range_left(self):
        playerPositionX = 0

        Game.playerPositionX = 0
        key = keyboard.KeyboardEvent(name='left', event_type='down', scan_code=0)
        Game.GameMovements(key)

        self.assertEqual(playerPositionX, Game.playerPositionX)

    def test_is_out_of_range_up(self):
        playerPositionY = 0

        Game.playerPositionY = 0
        key = keyboard.KeyboardEvent(name='up', event_type='down', scan_code=0)
        Game.GameMovements(key)

        self.assertEqual(playerPositionY, Game.playerPositionY)


    def test_is_out_of_range_right(self):
        playerPositionX = 4

        Game.playerPositionX = 4
        key = keyboard.KeyboardEvent(name='right', event_type='down', scan_code=0)
        Game.GameMovements(key)

        self.assertEqual(playerPositionX, Game.playerPositionX)

    def test_is_out_of_range_down(self):
        playerPositionY = 4

        Game.playerPositionY = 4
        key = keyboard.KeyboardEvent(name='down', event_type='down', scan_code=0)
        Game.GameMovements(key)

        self.assertEqual(playerPositionY, Game.playerPositionY)

    def test_board_has_obstacles(self):
        flag = False
        if b'@' in Game.board:
            flag = True       
        self.assertTrue(flag)
    
    def test_player_cant_go_through_obstacle_right(self):
        playerPositionX = 0
        Game.playerPositionX = 0
        Game.playerPositionY = 0
        Game.board[0][1] = '@'

        key = keyboard.KeyboardEvent(name='right', event_type='down', scan_code=0)
        Game.GameMovements(key)
        self.assertEqual(playerPositionX, Game.playerPositionX)

    def test_player_cant_go_through_obstacle_left(self):
        playerPositionX = 3
        Game.playerPositionX = 3
        Game.playerPositionY = 0
        Game.board[0][2] = '@'

        key = keyboard.KeyboardEvent(name='left', event_type='down', scan_code=0)
        Game.GameMovements(key)
        self.assertEqual(playerPositionX, Game.playerPositionX)

    def test_player_cant_go_through_obstacle_up(self):
        playerPositionY = 1
        Game.playerPositionX = 0
        Game.playerPositionY = 1
        Game.board[0][0] = '@'

        key = keyboard.KeyboardEvent(name='up', event_type='down', scan_code=0)
        Game.GameMovements(key)
        self.assertEqual(playerPositionY, Game.playerPositionY)
    
    def test_player_cant_go_through_obstacle_down(self):
        playerPositionY = 0
        Game.playerPositionX = 0
        Game.playerPositionY = 0
        Game.board[1][0] = '@'

        key = keyboard.KeyboardEvent(name='down', event_type='down', scan_code=0)
        Game.GameMovements(key)
        self.assertEqual(playerPositionY, Game.playerPositionY)
    
    
    def test_game_is_winnable(self):
        Game.playerPositionX = Game.endPositionX
        Game.playerPositionY = Game.endPositionY

        Game.Gameplay()
        self.assertTrue(Game.win)


