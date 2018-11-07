import libtcodpy as libtcod
from input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all

def main():
    screen_width = 80
    screen_height = 50

    player = Entity(screen_width // 2, screen_height // 2, '@', libtcod.white)
    npc = Entity(screen_width // 2 - 5, screen_height // 2, '@', libtcod.yellow)
    entities = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png'
                                    ,libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD
                                   )

    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial', False)

    con = libtcod.console_new(screen_width, screen_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, screen_width, screen_height)
        libtcod.console_flush()
        clear_all(con, entities)

        action = handle_keys(key)
        move = action.get('move') #returns relative coordinates as a tuple if the action was 'move'
        exit_game = action.get('exit') #gets True if action was 'exit'
        fullscreen = action.get('fullscreen') #gets True if action was 'fullscreen'

        if move:
            dx, dy = move
#            player_x += dx
#            player_y += dy
            player.move(dx, dy)

#        if key.vk == libtcod.KEY_ESCAPE:
        if exit_game:
            return True

        if fullscreen:
           libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen()) 

if __name__ == '__main__':
    main()

# I am up to the part of chapter 2 where he defines map_width, etc.
# This is a test edit on 8 November 2018, to see if GitHub for Desktop highlights this new change made locally.
