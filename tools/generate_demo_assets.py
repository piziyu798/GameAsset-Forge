from pathlib import Path
from PIL import Image, ImageDraw


BASE_DIR = Path("assets/demo_samples")

ASSETS = {
    "characters": [
        "knight_hero", "mage_character", "archer_character", "robot_character",
        "ninja_character", "witch_character", "merchant_character", "villager_character"
    ],
    "enemies": [
        "green_slime", "forest_goblin", "cave_bat", "skeleton_enemy",
        "mushroom_monster", "wolf_enemy", "ghost_enemy", "robot_enemy"
    ],
    "items": [
        "gold_coin", "red_potion", "blue_potion", "golden_key",
        "treasure_chest", "wooden_sword", "magic_staff", "shield"
    ],
    "tiles": [
        "grass_tile", "stone_road_tile", "dirt_tile", "water_tile", "wall_tile"
    ],
    "ui": [
        "hp_bar", "start_button", "inventory_icon", "pause_button"
    ],
    "backgrounds": [
        "forest_background", "dungeon_background", "village_background"
    ]
}


OUTLINE = (30, 30, 36, 255)
SKIN = (238, 180, 125, 255)
WHITE = (245, 245, 235, 255)


def canvas(size=(64, 64), transparent=True):
    bg = (0, 0, 0, 0) if transparent else (255, 255, 255, 255)
    return Image.new("RGBA", size, bg)


def save(img, category, name):
    out_dir = BASE_DIR / category
    out_dir.mkdir(parents=True, exist_ok=True)
    img.save(out_dir / f"{name}.png")


def rect(d, xy, fill, outline=OUTLINE, width=2):
    d.rectangle(xy, fill=fill, outline=outline, width=width)


def ellipse(d, xy, fill, outline=OUTLINE, width=2):
    d.ellipse(xy, fill=fill, outline=outline, width=width)


def draw_face(d, x1=26, y1=20):
    d.rectangle((x1, y1, x1 + 3, y1 + 3), fill=OUTLINE)
    d.rectangle((x1 + 9, y1, x1 + 12, y1 + 3), fill=OUTLINE)
    d.rectangle((x1 + 5, y1 + 7, x1 + 8, y1 + 8), fill=(120, 60, 55, 255))


def draw_basic_body(d, body_color):
    rect(d, (25, 18, 39, 32), SKIN)
    draw_face(d)
    rect(d, (23, 33, 41, 50), body_color)
    rect(d, (17, 34, 24, 45), body_color)
    rect(d, (40, 34, 47, 45), body_color)
    rect(d, (25, 50, 31, 58), OUTLINE, outline=OUTLINE, width=1)
    rect(d, (33, 50, 39, 58), OUTLINE, outline=OUTLINE, width=1)


def draw_character(name):
    img = canvas()
    d = ImageDraw.Draw(img)

    if name == "knight_hero":
        draw_basic_body(d, (55, 105, 205, 255))
        rect(d, (23, 13, 41, 20), (155, 155, 165, 255))
        d.rectangle((24, 15, 40, 17), fill=(210, 210, 220, 255))
        d.line((48, 28, 55, 17), fill=(220, 220, 230, 255), width=3)
        d.line((46, 30, 52, 36), fill=(120, 80, 40, 255), width=2)
        ellipse(d, (12, 35, 23, 49), (90, 130, 210, 255), width=2)

    elif name == "mage_character":
        draw_basic_body(d, (95, 65, 175, 255))
        d.polygon([(32, 5), (20, 23), (44, 23)], fill=(120, 80, 220, 255), outline=OUTLINE)
        d.rectangle((23, 21, 41, 24), fill=(80, 50, 150, 255))
        d.line((47, 25, 51, 51), fill=(125, 80, 40, 255), width=3)
        ellipse(d, (46, 12, 56, 22), (170, 110, 255, 255), width=2)

    elif name == "archer_character":
        draw_basic_body(d, (55, 145, 85, 255))
        d.rectangle((24, 14, 40, 18), fill=(115, 75, 35, 255))
        d.arc((43, 20, 58, 50), 90, 270, fill=(160, 95, 45, 255), width=3)
        d.line((50, 24, 50, 46), fill=(230, 220, 190, 255), width=1)
        d.line((18, 30, 10, 22), fill=(160, 95, 45, 255), width=2)

    elif name == "robot_character":
        rect(d, (23, 15, 41, 32), (105, 180, 200, 255))
        d.rectangle((28, 22, 31, 25), fill=(20, 60, 75, 255))
        d.rectangle((35, 22, 38, 25), fill=(20, 60, 75, 255))
        d.rectangle((30, 28, 36, 29), fill=(20, 60, 75, 255))
        rect(d, (22, 34, 42, 51), (95, 165, 185, 255))
        rect(d, (15, 36, 23, 47), (105, 180, 200, 255))
        rect(d, (41, 36, 49, 47), (105, 180, 200, 255))
        rect(d, (26, 51, 31, 58), (80, 95, 110, 255), width=1)
        rect(d, (34, 51, 39, 58), (80, 95, 110, 255), width=1)
        d.line((32, 15, 32, 8), fill=OUTLINE, width=2)
        ellipse(d, (29, 5, 35, 11), (235, 80, 80, 255), width=1)

    elif name == "ninja_character":
        rect(d, (23, 15, 41, 32), (35, 35, 48, 255))
        d.rectangle((27, 21, 37, 25), fill=SKIN)
        d.rectangle((29, 22, 31, 24), fill=OUTLINE)
        d.rectangle((35, 22, 37, 24), fill=OUTLINE)
        rect(d, (23, 33, 41, 50), (35, 35, 48, 255))
        rect(d, (17, 35, 24, 46), (35, 35, 48, 255))
        rect(d, (40, 35, 47, 46), (35, 35, 48, 255))
        d.line((47, 32, 55, 24), fill=(210, 210, 220, 255), width=2)

    elif name == "witch_character":
        draw_basic_body(d, (115, 65, 160, 255))
        d.polygon([(32, 5), (19, 24), (45, 24)], fill=(90, 45, 140, 255), outline=OUTLINE)
        d.rectangle((22, 23, 42, 26), fill=(60, 35, 95, 255))
        d.line((47, 27, 53, 50), fill=(120, 80, 40, 255), width=3)
        d.ellipse((51, 13, 58, 20), fill=(255, 210, 80, 255), outline=OUTLINE)

    elif name == "merchant_character":
        draw_basic_body(d, (175, 105, 55, 255))
        rect(d, (22, 13, 42, 19), (140, 85, 40, 255))
        d.rectangle((24, 10, 40, 13), fill=(180, 120, 60, 255))
        ellipse(d, (44, 37, 55, 52), (150, 90, 40, 255), width=2)
        d.rectangle((47, 40, 52, 44), fill=(245, 190, 50, 255))

    elif name == "villager_character":
        draw_basic_body(d, (80, 140, 85, 255))
        d.rectangle((23, 13, 41, 18), fill=(105, 70, 35, 255))
        d.rectangle((22, 18, 25, 24), fill=(105, 70, 35, 255))
        d.rectangle((39, 18, 42, 24), fill=(105, 70, 35, 255))

    return img


def draw_enemy(name):
    img = canvas()
    d = ImageDraw.Draw(img)

    if name == "green_slime":
        ellipse(d, (15, 26, 49, 52), (70, 190, 85, 255), width=2)
        d.ellipse((24, 34, 28, 38), fill=OUTLINE)
        d.ellipse((36, 34, 40, 38), fill=OUTLINE)
        d.arc((27, 37, 38, 46), 0, 180, fill=OUTLINE, width=2)
        d.ellipse((24, 28, 33, 33), fill=(130, 230, 130, 180))

    elif name == "forest_goblin":
        d.polygon([(22, 23), (8, 18), (20, 31)], fill=(80, 155, 75, 255), outline=OUTLINE)
        d.polygon([(42, 23), (56, 18), (44, 31)], fill=(80, 155, 75, 255), outline=OUTLINE)
        ellipse(d, (18, 18, 46, 44), (75, 165, 70, 255), width=2)
        d.rectangle((25, 29, 28, 32), fill=OUTLINE)
        d.rectangle((36, 29, 39, 32), fill=OUTLINE)
        d.polygon([(32, 32), (29, 37), (35, 37)], fill=(50, 120, 50, 255), outline=OUTLINE)
        rect(d, (24, 44, 40, 54), (95, 70, 45, 255), width=2)

    elif name == "cave_bat":
        d.polygon([(32, 28), (8, 14), (15, 34), (7, 50), (28, 40)], fill=(42, 42, 58, 255), outline=OUTLINE)
        d.polygon([(32, 28), (56, 14), (49, 34), (57, 50), (36, 40)], fill=(42, 42, 58, 255), outline=OUTLINE)
        ellipse(d, (24, 22, 40, 42), (55, 55, 75, 255), width=2)
        d.polygon([(26, 22), (29, 13), (33, 23)], fill=(55, 55, 75, 255), outline=OUTLINE)
        d.polygon([(38, 22), (35, 13), (31, 23)], fill=(55, 55, 75, 255), outline=OUTLINE)
        d.rectangle((28, 30, 30, 32), fill=(255, 70, 70, 255))
        d.rectangle((35, 30, 37, 32), fill=(255, 70, 70, 255))

    elif name == "skeleton_enemy":
        rect(d, (23, 12, 41, 30), (220, 220, 205, 255))
        d.rectangle((27, 19, 31, 24), fill=OUTLINE)
        d.rectangle((34, 19, 38, 24), fill=OUTLINE)
        d.rectangle((30, 26, 36, 28), fill=OUTLINE)
        d.line((32, 30, 32, 50), fill=(220, 220, 205, 255), width=4)
        for y in [35, 40, 45]:
            d.line((23, y, 41, y), fill=(220, 220, 205, 255), width=2)
        d.line((25, 36, 15, 48), fill=(220, 220, 205, 255), width=3)
        d.line((39, 36, 49, 48), fill=(220, 220, 205, 255), width=3)

    elif name == "mushroom_monster":
        d.pieslice((14, 12, 50, 42), 180, 360, fill=(190, 65, 65, 255), outline=OUTLINE, width=2)
        d.rectangle((22, 32, 42, 50), fill=(230, 220, 190, 255), outline=OUTLINE, width=2)
        d.ellipse((22, 21, 27, 26), fill=(245, 220, 190, 255))
        d.ellipse((37, 19, 43, 25), fill=(245, 220, 190, 255))
        d.rectangle((27, 39, 30, 42), fill=OUTLINE)
        d.rectangle((35, 39, 38, 42), fill=OUTLINE)

    elif name == "wolf_enemy":
        d.polygon([(14, 39), (22, 25), (42, 25), (52, 37), (45, 46), (25, 46)],
                  fill=(90, 95, 110, 255), outline=OUTLINE)
        d.polygon([(22, 25), (18, 14), (29, 25)], fill=(90, 95, 110, 255), outline=OUTLINE)
        d.polygon([(39, 25), (45, 15), (47, 30)], fill=(90, 95, 110, 255), outline=OUTLINE)
        d.rectangle((42, 32, 45, 35), fill=OUTLINE)
        d.line((14, 40, 7, 33), fill=(90, 95, 110, 255), width=4)
        d.rectangle((24, 46, 28, 55), fill=OUTLINE)
        d.rectangle((40, 46, 44, 55), fill=OUTLINE)

    elif name == "ghost_enemy":
        d.ellipse((18, 10, 46, 42), fill=(210, 220, 255, 205), outline=OUTLINE, width=2)
        d.polygon([(18, 32), (23, 54), (30, 43), (37, 54), (46, 32)],
                  fill=(210, 220, 255, 205), outline=OUTLINE)
        d.rectangle((26, 25, 30, 31), fill=OUTLINE)
        d.rectangle((36, 25, 40, 31), fill=OUTLINE)

    elif name == "robot_enemy":
        rect(d, (18, 17, 46, 45), (105, 135, 150, 255), width=2)
        d.rectangle((24, 28, 29, 33), fill=(255, 70, 70, 255))
        d.rectangle((36, 28, 41, 33), fill=(255, 70, 70, 255))
        d.rectangle((27, 38, 39, 40), fill=OUTLINE)
        d.line((32, 17, 32, 8), fill=OUTLINE, width=2)
        d.ellipse((29, 5, 35, 11), fill=(255, 70, 70, 255), outline=OUTLINE)

    return img


def draw_item(name):
    img = canvas()
    d = ImageDraw.Draw(img)

    if name == "gold_coin":
        ellipse(d, (17, 12, 47, 52), (245, 190, 45, 255), width=2)
        d.ellipse((25, 19, 39, 45), outline=(255, 235, 120, 255), width=2)
        d.line((32, 19, 32, 45), fill=(180, 120, 35, 255), width=2)

    elif name in {"red_potion", "blue_potion"}:
        liquid = (220, 65, 65, 255) if name == "red_potion" else (60, 135, 235, 255)
        rect(d, (26, 10, 38, 20), (185, 185, 195, 255), width=2)
        d.rounded_rectangle((19, 21, 45, 53), radius=7, fill=liquid, outline=OUTLINE, width=2)
        d.rectangle((23, 27, 41, 37), fill=liquid)
        d.ellipse((25, 25, 32, 32), fill=(255, 255, 255, 90))

    elif name == "golden_key":
        d.ellipse((13, 23, 31, 41), outline=(245, 190, 45, 255), width=5)
        d.line((30, 32, 53, 32), fill=(245, 190, 45, 255), width=5)
        d.line((46, 32, 46, 42), fill=(245, 190, 45, 255), width=3)
        d.line((52, 32, 52, 39), fill=(245, 190, 45, 255), width=3)

    elif name == "treasure_chest":
        rect(d, (14, 28, 50, 52), (120, 70, 35, 255), width=2)
        d.rounded_rectangle((14, 17, 50, 33), radius=5, fill=(165, 95, 45, 255), outline=OUTLINE, width=2)
        d.rectangle((29, 31, 36, 40), fill=(245, 190, 45, 255), outline=OUTLINE)
        d.line((16, 29, 48, 29), fill=(220, 160, 70, 255), width=2)

    elif name == "wooden_sword":
        d.line((19, 49, 46, 19), fill=(220, 220, 230, 255), width=6)
        d.line((19, 49, 46, 19), fill=OUTLINE, width=2)
        d.line((24, 50, 14, 40), fill=(120, 75, 40, 255), width=5)
        d.line((18, 43, 30, 55), fill=(190, 140, 70, 255), width=3)

    elif name == "magic_staff":
        d.line((21, 54, 43, 17), fill=(125, 80, 40, 255), width=4)
        ellipse(d, (38, 8, 53, 23), (155, 85, 240, 255), width=2)
        d.ellipse((42, 12, 48, 18), fill=(230, 210, 255, 180))

    elif name == "shield":
        d.polygon([(32, 10), (49, 18), (45, 44), (32, 56), (19, 44), (15, 18)],
                  fill=(75, 125, 220, 255), outline=OUTLINE)
        d.line((32, 12, 32, 54), fill=(170, 200, 255, 255), width=2)

    return img


def draw_tile(name):
    img = canvas()
    d = ImageDraw.Draw(img)

    if name == "grass_tile":
        d.rectangle((2, 2, 62, 62), fill=(70, 150, 70, 255), outline=(35, 85, 40, 255), width=3)
        for x in range(8, 58, 10):
            for y in range(9, 56, 12):
                d.line((x, y + 6, x + 3, y), fill=(120, 205, 100, 255), width=2)
                d.line((x + 3, y, x + 6, y + 6), fill=(55, 120, 55, 255), width=1)

    elif name == "stone_road_tile":
        d.rectangle((2, 2, 62, 62), fill=(105, 105, 115, 255), outline=(55, 55, 65, 255), width=3)
        stones = [(7, 8, 25, 22), (28, 7, 56, 22), (8, 25, 35, 40), (38, 25, 56, 41), (7, 43, 28, 57), (31, 44, 56, 57)]
        for s in stones:
            d.rectangle(s, outline=(145, 145, 155, 255), width=2)

    elif name == "dirt_tile":
        d.rectangle((2, 2, 62, 62), fill=(125, 80, 45, 255), outline=(70, 45, 25, 255), width=3)
        for x, y in [(10, 12), (23, 19), (42, 15), (18, 37), (50, 42), (36, 52), (9, 49)]:
            d.rectangle((x, y, x + 4, y + 3), fill=(170, 110, 60, 255))

    elif name == "water_tile":
        d.rectangle((2, 2, 62, 62), fill=(45, 130, 205, 255), outline=(25, 80, 150, 255), width=3)
        for y in [14, 27, 40, 53]:
            d.arc((8, y - 5, 26, y + 5), 0, 180, fill=(120, 205, 240, 255), width=2)
            d.arc((32, y - 5, 54, y + 5), 0, 180, fill=(120, 205, 240, 255), width=2)

    elif name == "wall_tile":
        d.rectangle((2, 2, 62, 62), fill=(95, 95, 105, 255), outline=(45, 45, 55, 255), width=3)
        for y in range(10, 60, 12):
            d.line((4, y, 60, y), fill=(135, 135, 145, 255), width=2)
        for row, y in enumerate(range(4, 56, 12)):
            offset = 0 if row % 2 == 0 else 12
            for x in range(4 + offset, 60, 24):
                d.line((x, y, x, y + 12), fill=(135, 135, 145, 255), width=2)

    return img


def draw_ui(name):
    img = canvas()
    d = ImageDraw.Draw(img)

    if name == "hp_bar":
        d.rounded_rectangle((8, 23, 56, 41), radius=5, fill=(45, 45, 55, 255), outline=OUTLINE, width=2)
        d.rounded_rectangle((12, 27, 45, 37), radius=3, fill=(220, 65, 65, 255))
        d.rectangle((14, 29, 28, 31), fill=(255, 120, 120, 180))

    elif name == "start_button":
        d.rounded_rectangle((8, 19, 56, 45), radius=7, fill=(65, 155, 90, 255), outline=OUTLINE, width=2)
        d.polygon([(27, 26), (27, 38), (41, 32)], fill=WHITE)

    elif name == "inventory_icon":
        rect(d, (14, 14, 50, 50), (110, 75, 45, 255), width=2)
        d.line((14, 28, 50, 28), fill=OUTLINE, width=2)
        d.line((32, 14, 32, 50), fill=OUTLINE, width=2)
        d.rectangle((18, 18, 28, 26), fill=(245, 190, 45, 255))
        d.rectangle((36, 34, 46, 46), fill=(85, 135, 220, 255))

    elif name == "pause_button":
        d.rounded_rectangle((12, 12, 52, 52), radius=9, fill=(70, 90, 125, 255), outline=OUTLINE, width=2)
        d.rectangle((25, 22, 30, 42), fill=WHITE)
        d.rectangle((35, 22, 40, 42), fill=WHITE)

    return img


def draw_background(name):
    img = Image.new("RGBA", (256, 144), (0, 0, 0, 255))
    d = ImageDraw.Draw(img)

    if name == "forest_background":
        d.rectangle((0, 0, 256, 144), fill=(45, 88, 68, 255))
        d.rectangle((0, 92, 256, 144), fill=(55, 120, 60, 255))
        for x in range(-10, 260, 30):
            d.polygon([(x, 90), (x + 15, 42), (x + 32, 90)], fill=(35, 95, 55, 255))
        for x in range(15, 250, 42):
            d.rectangle((x + 11, 67, x + 19, 128), fill=(90, 55, 35, 255))
            d.ellipse((x - 4, 36, x + 35, 78), fill=(55, 135, 70, 255), outline=(35, 85, 45, 255))
        d.rectangle((0, 122, 256, 144), fill=(45, 105, 50, 255))

    elif name == "dungeon_background":
        d.rectangle((0, 0, 256, 144), fill=(42, 42, 52, 255))
        for y in range(0, 110, 24):
            for x in range(0, 256, 32):
                offset = 16 if (y // 24) % 2 else 0
                d.rectangle((x - offset, y, x + 31 - offset, y + 23), outline=(70, 70, 82, 255))
        d.rectangle((0, 105, 256, 144), fill=(35, 35, 42, 255))
        for x in [38, 200]:
            d.rectangle((x, 45, x + 8, 82), fill=(90, 60, 35, 255))
            d.polygon([(x - 7, 44), (x + 4, 25), (x + 15, 44)], fill=(235, 150, 45, 255))
            d.ellipse((x - 12, 20, x + 20, 52), fill=(235, 120, 35, 70))
        d.rectangle((108, 58, 148, 107), fill=(28, 28, 35, 255), outline=(75, 75, 85, 255), width=3)

    elif name == "village_background":
        d.rectangle((0, 0, 256, 80), fill=(90, 155, 205, 255))
        d.rectangle((0, 80, 256, 144), fill=(80, 150, 80, 255))
        d.polygon([(0, 80), (40, 48), (82, 80)], fill=(70, 120, 85, 255))
        d.polygon([(70, 82), (128, 40), (190, 82)], fill=(75, 130, 90, 255))
        d.rectangle((0, 116, 256, 144), fill=(95, 120, 65, 255))
        for x in [35, 105, 176]:
            d.rectangle((x, 70, x + 45, 108), fill=(155, 100, 60, 255), outline=OUTLINE, width=2)
            d.polygon([(x - 6, 70), (x + 22, 45), (x + 51, 70)], fill=(130, 55, 45, 255), outline=OUTLINE)
            d.rectangle((x + 18, 88, x + 29, 108), fill=(80, 55, 35, 255))
            d.rectangle((x + 6, 78, x + 16, 88), fill=(240, 210, 120, 255))

    return img


def build_all():
    for category, names in ASSETS.items():
        for name in names:
            if category == "characters":
                img = draw_character(name)
            elif category == "enemies":
                img = draw_enemy(name)
            elif category == "items":
                img = draw_item(name)
            elif category == "tiles":
                img = draw_tile(name)
            elif category == "ui":
                img = draw_ui(name)
            elif category == "backgrounds":
                img = draw_background(name)
            else:
                img = canvas()

            save(img, category, name)

    print("Generated demo assets:", sum(len(v) for v in ASSETS.values()))


if __name__ == "__main__":
    build_all()
