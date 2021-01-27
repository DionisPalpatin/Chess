import pygame as pg

try:
    size, n = map(int, input().split())
    if size % n:
        size //= 0
    else:
        step = size // n
    #так как мне надо, чтобы вылезала ошибка, если длина грани не
    #кратна количетсву квадратов, то я просто создаю эту ошибку.
    #просто у меня не получилось без if проверять

    pg.init()
    window = pg.display.set_mode((size, size), pg.SHOWN)
    window.fill((255, 255, 255))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


        
        main_x, main_y = 0, size - step
        for i in range(n):
            for x in range(main_x, size, 2 * step):
                pg.draw.rect(window, (0, 0, 0), (x, main_y, step, step), 0)
            for y in range(main_y, -1, -2 * step):
                pg.draw.rect(window, (0, 0, 0), (main_x, y, step, step), 0)
            main_x += step
            main_y -= step               
            

        pg.display.update()
        pg.time.delay(10)
except:
   print("Unsupported input format")
