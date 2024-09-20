import tkinter
import random
from random import randint
import math

# Дополнительные задачи
# Пятиконечная звезда

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
p1 = (400.0, 300.0)
p2 = (331, 395)
p3 = (219, 359)
p4 = (200, 241)
p5 = (330, 205)
canvas.create_line(p1, p3, p5, p2, p4, p1, fill='red')
canvas.pack()
master.mainloop()

# Шахматное поле
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', width=600, height=600)
siz = 600 // 8
for i in range(8):
    for k in range(8):
        x1 = k * siz
        y1 = i * siz
        x2 = x1 + siz
        y2 = y1 + siz
        c = 'white' if (i + k) % 2 == 0 else 'black'
        canvas.create_rectangle(x1, y1, x2, y2, fill=c)
canvas.pack()
master.mainloop()

# Доска с шашками
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=800, width=800)
for k in range(100, 800, 200):
    canvas.create_oval(k, 100, k + 100, 200, fill='red')
for k in range(100, 800, 200):
    canvas.create_oval(k, 500, k + 100, 600, fill='blue')
    canvas.create_oval(k, 700, k + 100, 800, fill='blue')
for k in range(0, 700, 200):
    canvas.create_oval(k, 600, k + 100, 700, fill='blue')
for k in range(100, 800, 100):
    canvas.create_line((k, 0), (k, 800), fill='black')
for k in range(100, 800, 100):
    canvas.create_line((0, k), (800, k), fill='black')
for k in range(0, 700, 200):
    canvas.create_oval(k, 200, k + 100, 300, fill='red')
    canvas.create_oval(k, 0, k + 100, 100, fill='red')
canvas.pack()
master.mainloop()


# Круг случайного размера
def draw(event):
    canvas.create_oval((random.randint(1, 600), random.randint(1, 600)),
                       (random.randint(1, 600), random.randint(1, 600)), fill='red')
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<Button-1>", draw)
master.mainloop()


# Keysym, keycode
def show_key(event):
    text = ', '.join(map(str, [event.keysym, event.char, event.keysym_num, event.keycode]))
    label.config(text=text)


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()


# Кружок. Реакция на стрелки
def key_pressed(event):
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    elif event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    elif event.keysym == 'Right':
        canvas.move(oval, 10, 0)


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='red')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()


# Кружок. Зеленеет в центре
def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    if canvas.coords(oval)[1] < 50:
        canvas.itemconfig(oval, fill='red')
    if canvas.coords(oval)[1] == 300:
        canvas.itemconfig(oval, fill='green')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()


# Кружок. Меняет цвет
def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))
        canvas.itemconfig(oval, fill='green')
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    if event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    if event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    if canvas.coords(oval)[1] < 200 or canvas.coords(oval)[1] > 400 \
            or canvas.coords(oval)[2] < 210 or canvas.coords(oval)[2] > 410:
        canvas.itemconfig(oval, fill='red')
    elif canvas.coords(oval)[1] > 200 or canvas.coords(oval)[1] < 400 \
            or canvas.coords(oval)[2] > 210 or canvas.coords(oval)[2] < 410:
        canvas.itemconfig(oval, fill='green')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()

# Кружок. Выход за границы

# N-конечная звезда
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.pack()
i = 100
num = int(input('Количество лучей: '))
for k in range(num):
    if num % 2 == 0:
        k1 = (k + num / 2 - 1) % num
    else:
        k1 = (k + (num - 1) / 2) % num

    p1 = (300 + i * math.cos(2 * 3.14 * k / num), 300 + i * math.sin(2 * 3.14 * k / num))
    p2 = (300 + i * math.cos(2 * 3.14 * k1 / num), 300 + i * math.sin(2 * 3.14 * k1 / num))
    canvas.create_line(p1, p2, fill='red')
master.mainloop()


# Игра
def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])


def do_nothing():
    pass


def check_move():
    if canvas.coords(player) == canvas.coords(leave):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)


def always_right():
    return step, 0


def random_move():
    return random.choice([(step, 0), (-step, 0), (0, step), (0, -step)])


def prepare_and_start():
    global player, leave, fires
    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    exit_pos = (random.randint(1, N_X - 1) * step,
                random.randint(1, N_Y) * step)
    player = canvas.create_oval(
        (player_pos[0], player_pos[1]),
        (player_pos[0] + step, player_pos[1] + step),
        fill='green')
    leave = canvas.create_oval(
        (exit_pos[0], exit_pos[1]),
        (exit_pos[0] + step, exit_pos[1] + step),
        fill='yellow')
    n_fires = 6
    fires = []
    for i in range(n_fires):
        fire_pos = (random.randint(1, N_X - 1) * step,
                    random.randint(1, N_Y - 1) * step)
        fire = canvas.create_oval(
            (fire_pos[0], fire_pos[1]),
            (fire_pos[0] + step, fire_pos[1] + step),
            fill='red')
        fires.append(fire)
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    elif event.keysym == 'Down':
        move_wrap(player, (0, step))
    elif event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    elif event.keysym == 'Right':
        move_wrap(player, (step, 0))
    check_move()


master = tkinter.Tk()
step = 60
N_X = 10
N_Y = 10
label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas = tkinter.Canvas(master, bg='blue',
                        height=N_X * step, width=N_Y * step)
canvas.pack()
restart = tkinter.Button(master, text="Начать заново",
                         command=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()

player_pos = (random.randint(0, N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)
exit_pos = (random.randint(0, N_X - 1) * step,
            random.randint(0, N_Y - 1) * step)

player = canvas.create_oval((player_pos[0], player_pos[1]),
                            (player_pos[0] + step, player_pos[1] + step),
                            fill='green')
leave = canvas.create_oval((exit_pos[0], exit_pos[1]),
                           (exit_pos[0] + step, exit_pos[1] + step),
                           fill='yellow')

label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()


# Игра. Доработка 1
def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])


def do_nothing():
    pass


def check_move():
    if canvas.coords(player) == canvas.coords(leave):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)


def always_right():
    return step, 0


def random_move():
    return random.choice([(step, 0), (-step, 0), (0, step), (0, -step)])


def prepare_and_start():
    global player, leave, fires
    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    exit_pos = (random.randint(1, N_X - 1) * step,
                random.randint(1, N_Y) * step)
    player = canvas.create_oval(
        (player_pos[0], player_pos[1]),
        (player_pos[0] + step, player_pos[1] + step),
        fill='green')
    leave = canvas.create_oval(
        (exit_pos[0], exit_pos[1]),
        (exit_pos[0] + step, exit_pos[1] + step),
        fill='yellow')
    n_fires = 6
    fires = []
    for i in range(n_fires):
        fire_pos = (random.randint(1, N_X - 1) * step,
                    random.randint(1, N_Y - 1) * step)
        fire = canvas.create_oval(
            (fire_pos[0], fire_pos[1]),
            (fire_pos[0] + step, fire_pos[1] + step),
            fill='red')
        fires.append(fire)
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    elif event.keysym == 'Down':
        move_wrap(player, (0, step))
    elif event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    elif event.keysym == 'Right':
        move_wrap(player, (step, 0))
    check_move()


master = tkinter.Tk()
step = 60
N_X = 10
N_Y = 10
label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas = tkinter.Canvas(master, bg='blue',
                        height=N_X * step, width=N_Y * step)
canvas.pack()
restart = tkinter.Button(master, text="Начать заново",
                         command=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()

player_pos = (random.randint(0, N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)
exit_pos = (random.randint(0, N_X - 1) * step,
            random.randint(0, N_Y - 1) * step)

player = canvas.create_oval((player_pos[0], player_pos[1]),
                            (player_pos[0] + step, player_pos[1] + step),
                            fill='green')
leave = canvas.create_oval((exit_pos[0], exit_pos[1]),
                           (exit_pos[0] + step, exit_pos[1] + step),
                           fill='yellow')

label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
# Игра. Доработка 2

# Игра. Доработка 3
