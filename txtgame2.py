import random, time


def printFightAnimation(text):
    # --- ПОЧАТОК АНІМАЦІЇ ---
    time.sleep(1)
    frames = [
        "⚔️  Замах!", 
        "⚔️⚔️", 
        "⚔️⚔️⚔️",  
        "⚔️⚔️⚔️⚔️", 
        "⚔️⚔️⚔️⚔️⚔️",
        "💥 БАЦ!" + text
    ]
    for frame in frames:
        print(f"\r{frame:<15}", end="", flush=True)
        time.sleep(0.6)
    print()  # Фіксуємо рядок


hero = {
    "name": "Воин грома",
    "health": 100,
    "damage": 18,
    "maxhealth": 100,
    "superdamage": 30
}
goblin = {
    "name": "Пердулет",
    "health": 100,
    "damage": 20,
}
while True:

    vibor = input("ЧТО ВЫ ХОТИТИ СДЕЛАТЬ: 1 - атаковать 2 - лечиться (введите 1 или 2) : ")
    if vibor == "1": #атакуем
        superudar = random.randint(1,10)
        if superudar == 2:
            print("СУПЕР УДАР АКТИВИРОВАН")
            dmhero = random.randint(15,hero["superdamage"])
        else:
            dmhero = random.randint(1,hero["damage"])

        print("")
        print("Герой атакует")
        text = f"Герой ударил Гоблина с силой: {dmhero}. Здоровья Гоблин уменьшилось с: {goblin['health']} до: {goblin['health'] - dmhero}"
        printFightAnimation(text)        
        goblin["health"] = goblin["health"] - dmhero
    elif vibor == "2": #лечимся
        health = random.randint(5, 10)
        print("Герой добавил себе: ", health, " здоровья. Здоровья героя увеличилось с: ", hero["health"], " до: ", hero["health"] + health)
        hero["health"] = hero["health"] + health    
        if hero["health"] >= hero["maxhealth"]:
            hero["health"] = hero["maxhealth"]


    if goblin["health"] <= 0:
        print("Герой переміг!!!!!!!!!!" )
        break

    dmgoblin = random.randint(1,goblin["damage"])    
    print("")                        
    print("Гоблін атакует")
    text = f"Гоблін ударив героя с силой: {dmgoblin}. Здоровья героя уменьшилось с: {hero['health']} до: {hero['health'] - dmgoblin}"
    printFightAnimation(text)
    hero["health"] = hero["health"] - dmgoblin
    if hero["health"] <= 0:
        print("Гоблін переміг!!!!!!!!!!" )
        break
    elif goblin["health"] <= 20:
        gbhealth = random.randint(0, 10)
        if gbhealth > 0:
            print("Гоблин добавил себе: ", gbhealth, " здоровья. Здоровья гоблина увеличилось с: ", goblin["health"], " до: ", goblin["health"] + gbhealth)
            goblin["health"] = goblin["health"] + gbhealth


    print("")
    print(f"{'':<10} | {'Герой':<10} | {'Гоблин':<10}")
    print(f"{'':-<10}-+-{'':-<10}-+-{'':-<10}")
    print(f"{'Имя':<10} | {hero['name']:<10} | {goblin['name']:<10}")
    print(f"{'Здоровье':<10} | {hero['health']:<10} | {goblin['health']:<10}")
    print("")
    print(f"{'-':-<30} Раунд завершен! {'-':-<30}")
    print("")

print("кінець!")