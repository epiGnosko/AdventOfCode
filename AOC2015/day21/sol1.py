def playerwins():
    global Boss, Player
    CurBoss = Boss.copy()
    while CurBoss["hitpoints"] > 0 and Player["hitpoints"] > 0:
        CurBoss["hitpoints"] -= Player["damage"] - CurBoss["armor"]
        Player["hitpoints"] -= CurBoss["damage"] - Player["armor"]
    return CurBoss["hitpoints"] <= 0

def cost(selection):
    cost = 0
    for i in selection:
        cost += i["cost"] 
    return cost

def damage(selection):
    damage = 0
    for i in selection:
        damage += i["damage"] 
    return damage

def armor(selection):
    armor = 0
    for i in selection:
        armor += i["armor"] 
    return armor

Boss = {
    "hitpoints" : 104, 
    "damage" : 8,
    "armor" : 1
}

BasePlayer = {
    "hitpoints" : 100,
    "damage" : 0,
    "armor" : 0
}

Player = {
    "hitpoints" : 100,
    "damage" : 0,
    "armor" : 0
}

Weapons={
    "None": {
        "cost": 0,
        "damage": 0,
        "armor": 0,
    },
	"Dagger" : {
		"cost" : 8,
		"damage" : 4,
		"armor" : 0
	},
	"Shortsword" : {
		"cost" : 10,
		"damage" : 5,
		"armor" : 0
	},
	"Warhammer" : {
		"cost" : 25,
		"damage" : 6,
		"armor" : 0
	},
	"Longsword" : {
		"cost" : 40,
		"damage" : 7,
		"armor" : 0
	},
	"Greataxe" : {
		"cost" : 74,
		"damage" : 8,
		"armor" : 0
	},
}

Armor = {
    "None": {
        "cost": 0,
        "damage": 0,
        "armor": 0,
    },
	"Leather" : {
		"cost" : 13,
		"damage" : 0,
		"armor" : 1
	},
	"Chainmail" : {
		"cost" : 31,
		"damage" : 0,
		"armor" : 2
	},
	"Splintmail" : {
		"cost" : 53,
		"damage" : 0,
		"armor" : 3
	},
	"Bandedmail" : {
		"cost" : 75,
		"damage" : 0,
		"armor" : 4
	},
	"Platemail" : {
		"cost" : 102,
		"damage" : 0,
		"armor" : 5
	},
}

Rings ={
    "Nonea": {
        "cost": 0,
        "damage": 0,
        "armor": 0,
    },
    "Noneb": {
        "cost": 0,
        "damage": 0,
        "armor": 0,
    },
	"Damage+1" : {
		"cost" : 25,
		"damage" : 1,
		"armor" : 0
	},
	"Damage+2" : {
		"cost" : 50,
		"damage" : 2,
		"armor" : 0
	},
	"Damage+3" : {
		"cost" : 100,
		"damage" : 3,
		"armor" : 0
	},
	"Defense+1" : {
		"cost" : 20,
		"damage" : 0,
		"armor" : 1
	},
	"Defense+2" : {
		"cost" : 40,
		"damage" : 0,
		"armor" : 2
	},
	"Defense+3" : {
		"cost" : 80,
		"damage" : 0,
		"armor" : 3
	},
}

possible = []

for i in Weapons:
    for j in Armor:
        for k in Rings:
            for l in Rings:
                if k != l:
                    possible.append([Weapons[i], Armor[j], Rings[k],Rings[l]])

possible.sort(key= lambda x: cost(x))

for i in possible:
    Player["hitpoints"] = BasePlayer["hitpoints"]
    Player["damage"] = BasePlayer["damage"] + damage(i)
    Player["armor"] = BasePlayer["armor"] + armor(i)
    if playerwins():
        print(cost(i))
        break
