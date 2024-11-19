import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    fbg_img=pg.transform.flip(bg_img,True,False)
    kokaton=pg.image.load("fig/3.png")
    kokaton=pg.transform.flip(kokaton,True,False)
    tmr = 0
    # (width,height)=bg_img.get_size()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        bg_start=-(tmr%3200)
        screen.blit(bg_img, [bg_start, 0])
        screen.blit(fbg_img,[bg_start+1600,0])
        screen.blit(bg_img, [bg_start+3200, 0])
        screen.blit(fbg_img,[bg_start+4800,0])
        screen.blit(kokaton,[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()