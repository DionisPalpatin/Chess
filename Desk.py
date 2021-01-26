import pygame as pg

try:
    size, n = map(int, input().split())
    step = int(str(size // n))


    pg.init()
    window = pg.display.set_mode((size, size), pg.SHOWN)
    window.fill((255, 255, 255))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


       
        if n % 2:
            countX = 1
            for x in range(0, size, step):
                countY = 1
                for y in range(0, size, step):
                    if countX % 2:
                        if countY % 2:
                            pg.draw.rect(window, (0, 0, 0), (x, y, step, step), 0)
                        else:
                            pg.draw.rect(window, (255, 255, 255), (x, y, step, step), 0)
                    else:
                        if not countY % 2:
                            pg.draw.rect(window, (0, 0, 0), (x, y, step, step), 0)
                        else:
                            pg.draw.rect(window, (255, 255, 255), (x, y, step, step), 0)
                    countY += 1
                countX += 1
        else:
            countX = 1
            for x in range(0, size, step):
                countY = 1
                for y in range(0, size, step):
                    if countX % 2:
                        if not countY % 2:
                            pg.draw.rect(window, (0, 0, 0), (x, y, step, step), 0)
                        else:
                            pg.draw.rect(window, (255, 255, 255), (x, y, step, step), 0)
                    else:
                        if countY % 2:
                            pg.draw.rect(window, (0, 0, 0), (x, y, step, step), 0)
                        else:
                            pg.draw.rect(window, (255, 255, 255), (x, y, step, step), 0)
                    countY += 1
                countX += 1
        

        pg.display.update()
        pg.time.delay(10)
except:
    print("Unsupported input format")