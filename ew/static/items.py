import json
import os

from . import cfg as ewcfg
from ..model.hunting import EwSeedPacket
from ..model.hunting import EwTombstone
from ..model.item import EwFurniture
from ..model.item import EwGeneralItem
from ..model.item import EwItemDef
from ..model.item import EwPrankItem
from ..model.slimeoid import EwSlimeoidFood

"""
	The list of item definitions. Instances of items are always based on these
	skeleton definitions.
"""
item_def_list = [
	EwItemDef(
		# Unique item identifier. Not shown to players.
		item_type = "demo",

		# The name of the item that players will see.
		str_name = "Demo",

		# The description shown when you look at an item.
		str_desc = "A demonstration item."
	),

	EwItemDef(
		item_type = ewcfg.it_item,
		str_name = "{item_name}",
		str_desc = "{item_desc}",
		item_props = {
			'id_name': 'normalitem',
			'context': 'context',
			'item_name': 'Normal Item.',
			'item_desc': 'This is a normal item.',
			'ingredients': 'vegetable'
		}
	),

	# A customizable award object.
	EwItemDef(
		item_type = ewcfg.it_medal,
		str_name = "{medal_name}",
		str_desc = "{medal_desc}",
		soulbound = True,
		item_props = {
			'medal_name': 'Blank Medal',
			'medal_desc': 'An uninscribed medal with no remarkable features.'
		}
	),

	EwItemDef(
		item_type = ewcfg.it_questitem,
		str_name = "{qitem_name}",
		str_desc = "{qitem_desc}",
		soulbound = True,
		item_props = {
			'qitem_name': 'Quest Item',
			'qitem_desc': 'Something important to somebody.'
		}
	),

	EwItemDef(
		item_type = ewcfg.it_food,
		str_name = "{food_name}",
		str_desc = "{food_desc}",
		soulbound = False,
		item_props = {
			'food_name': 'Food Item',
			'food_desc': 'Food.',
			'recover_hunger': 0,
			'price': 0,
			'inebriation': 0,
			'vendor': None,
			'str_eat': 'You eat the food item.',
			'time_expir': ewcfg.std_food_expir,
			'time_fridged': 0,
		}
	),

	EwItemDef(
		item_type = ewcfg.it_weapon,
		str_name = "{weapon_name}",
		str_desc = "{weapon_desc}",
		soulbound = False,
		item_props = {
			'weapon_type': 'Type of weapon',
			'weapon_desc': 'It\'s a weapon of some sort.',
			'weapon_name': 'Weapon\'s name',
			'ammo': 0,
			'married': 'User Id',
			'kills': 0,
			'consecutive_hits': 0,
			'time_lastattack': 0,
			'totalkills': 0
		}
	),
	EwItemDef(
		item_type = ewcfg.it_cosmetic,
		str_name = "{cosmetic_name}",
		str_desc = "{cosmetic_desc}",
		soulbound = False,
		item_props = {
			'cosmetic_name': 'Cosmetic Item',
			'cosmetic_desc': 'Cosmetic Item.',
			'rarity': ewcfg.rarity_plebeian,
			'hue': "",
		}
	),
	EwItemDef(
		item_type = ewcfg.it_furniture,
		str_name = "{furniture_name}",
		str_desc = "{furniture_desc}",
		soulbound = False,
		item_props = {
			'furniture_name': 'Furniture Item',
			'furniture_place_desc': 'placed',
			'furniture_look_desc': 'it\'s there',
			'rarity': ewcfg.rarity_plebeian,
			'vendor': None,

		}
	),
	EwItemDef(
		item_type = ewcfg.it_book,
		str_name = "{title}",
		str_desc = "{book_desc}",
		soulbound = False,
		item_props = {
			"title": "Book",
			"author": "Boy",
			"date_published": 2000,
			"id_book": 69,
			"book_desc": "A book by AUTHOR, published on DAY."
		}
	)
]

# A map of item_type to EwItemDef objects.
item_def_map = {}

# Populate the item def map.
for item_def in item_def_list:
	item_def_map[item_def.item_type] = item_def

# List of normal items.
item_list = [
	EwGeneralItem(
		id_item = ewcfg.item_id_slimepoudrin,
		alias = [
			"poudrin",
		],
		context = "poudrin",
		str_name = "Slime Poudrin",
		str_desc = "A dense, crystalized chunk of precious slime.",
		acquisition = ewcfg.acquisition_mining,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_white,
		context = "dye",
		str_name = "White Dye",
		str_desc = "A small vial of white dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_yellow,
		context = "dye",
		str_name = "Yellow Dye",
		str_desc = "A small vial of yellow dye.",
		acquisition = ewcfg.acquisition_smelting,
	),

	EwGeneralItem(
		id_item = ewcfg.item_id_dye_orange,
		context = "dye",
		str_name = "Orange Dye",
		str_desc = "A small vial of orange dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_red,
		context = "dye",
		str_name = "Red Dye",
		str_desc = "A small vial of red dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_magenta,
		context = "dye",
		str_name = "Magenta Dye",
		str_desc = "A small vial of magenta dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_purple,
		context = "dye",
		str_name = "Purple Dye",
		str_desc = "A small vial of purple dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_blue,
		context = "dye",
		str_name = "Blue Dye",
		str_desc = "A small vial of blue dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_green,
		context = "dye",
		str_name = "Green Dye",
		str_desc = "A small vial of green dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_teal,
		context = "dye",
		str_name = "Teal Dye",
		str_desc = "A small vial of teal dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_rainbow,
		context = "dye",
		str_name = "***Rainbow Dye!!***",
		str_desc = "***A small vial of Rainbow dye!!***",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_pink,
		context = "dye",
		str_name = "Pink Dye",
		str_desc = "A small vial of pink dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_grey,
		context = "dye",
		str_name = "Grey Dye",
		str_desc = "A small vial of grey dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_cobalt,
		context = "dye",
		str_name = "Cobalt Dye",
		str_desc = "A small vial of cobalt dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_black,
		context = "dye",
		str_name = "Black Dye",
		str_desc = "A small vial of black dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_lime,
		context = "dye",
		str_name = "Lime Dye",
		str_desc = "A small vial of lime dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_cyan,
		context = "dye",
		str_name = "Cyan Dye",
		str_desc = "A small vial of cyan dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dye_brown,
		context = "dye",
		str_name = "Brown Dye",
		str_desc = "A small vial of brown dye.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_paint_copper,
		context = "dye",
		str_name = "Copper Paint",
		str_desc = "A small bucket of Copper Paint.",
		acquisition = ewcfg.acquisition_smelting,
		durability = 3
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_paint_chrome,
		context = "dye",
		str_name = "Chrome Paint",
		str_desc = "A small bucket of Chrome Paint.",
		acquisition = ewcfg.acquisition_smelting,
		durability = 3
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_paint_gold,
		context = "dye",
		str_name = "Gold Paint",
		str_desc = "A small bucket of Gold Paint.",
		acquisition = ewcfg.acquisition_smelting,
		durability = 3
	),
	EwGeneralItem(
		id_item = "bone",
		str_name = "Bone",
		str_desc = "A small nondescript bone. Traces of fresh slime in it indicate it must've belonged to one of the city's residents.",
		context = 'player_bone',
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_negapoudrin,
		str_name = "negapoudrin",
		str_desc = "A dense, crystalized slab of unholy negaslime.",
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_tradingcardpack,
		alias = [
			"tcp", # DUDE LOL JUST LIKE THE PROCRASTINATORS HOLY FUCKING SHIT I'M PISSING MYSELF RN
			"tradingcard",
			"trading",
			"card",
			"cardpack",
			"pack"
		],
		str_name = "Trading Cards",
		str_desc = "A pack of trading cards",
		price = 50000,
		vendors = [ewcfg.vendor_bazaar, ewcfg.vendor_glocksburycomics],
	),
	EwGeneralItem(
		id_item = "rightleg",
		context = 'slimexodia',
		str_name = "The Right Leg of The Forbidden {}".format(ewcfg.emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(ewcfg.emote_111),
	),
	EwGeneralItem(
		id_item = "leftleg",
		context = 'slimexodia',
		str_name = "Left Leg of The Forbidden {}".format(ewcfg.emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(ewcfg.emote_111),
	),
	EwGeneralItem(
		id_item = "slimexodia",
		context = 'slimexodia',
		str_name = "Slimexodia The Forbidden {}".format(ewcfg.emote_111),
		str_desc = "The centerpiece of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(ewcfg.emote_111),
	),
	EwGeneralItem(
		id_item = "rightarm",
		context = 'slimexodia',
		str_name = "Right Arm of The Forbidden {}".format(ewcfg.emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(ewcfg.emote_111),
	),
	EwGeneralItem(
		id_item = "leftarm",
		context = 'slimexodia',
		str_name = "Left Arm of The Forbidden {}".format(ewcfg.emote_111),
		str_desc = "One of the extremely rare, legendary Forbidden {} cards. Gazing upon the card and its accompanying "
				   "intense holographic sheen without the proper eyewear can have disastrous consequences. Yet, you do it anyway. "
				   "It’s just too beautiful not to.".format(ewcfg.emote_111),
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_forbidden111,
		str_name = "The Forbidden {}".format(ewcfg.emote_111),
		str_desc = ewcfg.theforbiddenoneoneone_desc.format(emote_111 = ewcfg.emote_111),
		acquisition = ewcfg.acquisition_smelting
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_stick,
		str_name = "stick",
		str_desc = "It’s just some useless, dumb stick.",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_faggot,
		str_name = "faggot",
		str_desc = "Wow, incredible! We’ve evolved from one dumb stick to several, all tied together for the sake of a retarded puesdo-pun! Truly, ENDLESS RIOT has reached its peak. It’s all downhill from here, folks.",
		acquisition = ewcfg.acquisition_smelting
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_doublefaggot,
		str_name = "double faggot",
		str_desc = "It's just a bundle of sticks, twice as long and hard as the two combined to form it. Hey, what are you chucklin' at?.",
		acquisition = ewcfg.acquisition_smelting
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_seaweed,
		str_name = "Seaweed",
		str_desc = "OH GOD IT'S A FUCKING SEAWEED!",
		acquisition = ewcfg.acquisition_bartering,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_oldboot,
		str_name = "Old Boot",
		str_desc = "OH GOD IT'S A FUCKING OLD BOOT!",
		acquisition = ewcfg.acquisition_bartering,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_tincan,
		str_name = "Tin Can",
		str_desc = "OH GOD IT'S A FUCKING TIN CAN!",
		acquisition = ewcfg.acquisition_bartering,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_leather,
		str_name = "Leather",
		str_desc = "A strip of leather.",
		acquisition = ewcfg.acquisition_smelting,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_ironingot,
		str_name = "Iron Ingot",
		str_desc = "A bar of iron",
		acquisition = ewcfg.acquisition_smelting,
		ingredients = "generic",
		context = 10,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dragonsoul,
		str_name = "Dragon Soul",
		str_desc = "A fearsome dragon soul, pried from the corpse of a Green Eyes Slime Dragon. It's just like Dark Souls! Wait... *just like* Dark Souls??? Maybe you can use this for something.",
		context = 'dragon soul',
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_monsterbones,
		str_name = "Monster Bones",
		str_desc = "A large set of bones, taken from the monsters that roam the outskirts. Tastes meaty.",
		context = 'monster bone',
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_bloodstone,
		str_name = "blood stone",
		str_desc = "Formed from the cracking of monster bones, it glistens in your palm with the screams of those whos bones comprise it. Perhaps it will be of use one day.",
		context = 'blood stone',
		acquisition = ewcfg.acquisition_smelting
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_tanningknife,
		context = "tool",
		str_name = "Tanning Knife",
		str_desc = "A tanning knife",
		acquisition = ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_string,
		str_name = "string",
		str_desc = "It’s just some string.",
		acquisition = ewcfg.acquisition_bartering,
		ingredients = "generic",
		context = 60,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_gameguide,
		alias = [
			"gg",
			"gameguide",
			"gamergate",
		],
		str_name = "The official unofficial ENDLESS RIOT Game Guide, Version III",
		str_desc = "A guide on all the game mechanics found in ENDLESS RIOT, accurate as of 7/19/2020. Use the !help command to crack it open.",
		vendors = [ewcfg.vendor_college],
		price = 10000,
	),
	EwGeneralItem(
		id_item=ewcfg.item_id_juviegradefuckenergybodyspray,
		context='repel',
		alias=[
			"regular body spray",
			"regbs",
			"regular repel",
			"juvie",
			"juviegrade",
			"juvie grade",
			"repel",
			"body spray",
			"bodyspray",
			"bs",
		],
		str_name="Juvie Grade FUCK ENERGY Body Spray",
		str_desc="A canister of perfume. Somehow doubles as a slime beast repellant. The label on the back says it lasts for three hours.",
		vendors=[ewcfg.vendor_glocksburycomics],
		price=10000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_superduperfuckenergybodyspray,
		context = 'superrepel',
		alias = [
			"superrepel",
			"super repel",
			"super duper body spray",
			"superbodyspray",
			"superduperbodyspray",
			"sdbs",
			"super",
		],
		str_name = "Super Duper FUCK ENERGY Body Spray",
		str_desc = "A canister of perfume. Somehow doubles as a slime beast repellant. The label on the back says it lasts for six hours.",
		vendors = [ewcfg.vendor_glocksburycomics],
		price = 20000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_gmaxfuckenergybodyspray,
		context = 'maxrepel',
		alias = [
			"maxrepel",
			"max repel",
			"g-max body spray",
			"gmaxbodyspray",
			"gmbs",
			"gmax",
			"g-max",
		],
		str_name = "G-Max FUCK ENERGY Body Spray",
		str_desc = "A canister of perfume. Somehow doubles as a slime beast repellant. The label on the back says it lasts for twelve hours.",
		vendors = [ewcfg.vendor_glocksburycomics],
		price = 40000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_costumekit,
		context = 'costumekit',
		alias = [
			"costumekit",
			"ck",
			"kit",
			"costume",
		],
		vendors = [ewcfg.vendor_rpcity],
		str_name = "Double Halloween Costume Kit",
		str_desc = "A package of all the necessary tools and fabrics needed to make the Double Halloween costume of your dreams.",
		price = 50000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_doublehalloweengrist,
		context = 'dhgrist',
		alias = [
			"grist"
		],
		str_name = "Double Halloween Grist",
		str_desc = "A mush of finely ground candy. Perhaps it can be forged into something special?",
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_whitelineticket,
		context = 'wlticket',
		alias = [
			"tickettohell"
		],
		str_name = "Ticket to the White Line",
		str_desc = "A large assortment of candy molded into one unholy voucher for access into the underworld. Use it in a White Line subway station... ***IF YOU DARE!!***",
		acquisition=ewcfg.acquisition_smelting,
	),
	EwGeneralItem(
		id_item=ewcfg.item_id_megaslimewrappingpaper,
		context=ewcfg.context_wrappingpaper,
		alias=[
			"mswp"
		],
		str_name="Megaslime Wrapping Paper",
		str_desc="Wrapping paper with Megaslimes plastered all over it. Blaargh!",
		price = 1000,
	),
	EwGeneralItem(
		id_item=ewcfg.item_id_greeneyesslimedragonwrappingpaper,
		context=ewcfg.context_wrappingpaper,
		alias=[
			"gesdwp"
		],
		str_name="Green Eyes Slime Dragon Wrapping Paper",
		str_desc="Wrapping paper with many images of the Green Eyes Slime Dragon printed on it. Powerful...",
		price = 1000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_phoebuswrappingpaper,
		context = ewcfg.context_wrappingpaper,
		alias = [
			"pwp"
		],
		str_name = "Phoebus Wrapping Paper",
		str_desc = "A set of wrapping paper with Slime Invictus on it. Yo, Slimernalia!",
		price = 1000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_slimeheartswrappingpaper,
		context = ewcfg.context_wrappingpaper,
		alias = [
			"shwp"
		],
		str_name = "Slime Hearts Wrapping Paper",
		str_desc = "Wrapping paper decorated with slime hearts. Cute!!",
		price = 1000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_slimeskullswrappingpaper,
		context = ewcfg.context_wrappingpaper,
		alias = [
			"sswp"
		],
		str_name = "Slime Skulls Wrapping Paper",
		str_desc = "A roll of wrapping paper with Slime Skulls stamped all over it. Spooky...",
		price = 1000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_shermanwrappingpaper,
		context = ewcfg.context_wrappingpaper,
		alias = [
			"swp"
		],
		str_name = "Sherman Wrapping Paper",
		str_desc = "Wrapping paper with Sherman, the SlimeCorp salaryman etched into it. Jesus Christ, how horrifying!",
		price = 1000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_slimecorpwrappingpaper,
		context = ewcfg.context_wrappingpaper,
		alias = [
			"scwp"
		],
		str_name = "SlimeCorp Wrapping Paper",
		str_desc = "A set of wrapping paper with that accursed logo printed all over it. What sort of corporate bootlicker would wrap a gift in this?",
		price = 1000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_pickaxewrappingpaper,
		context = ewcfg.context_wrappingpaper,
		alias = [
			"pawp"
		],
		str_name = "Pickaxe Wrapping Paper",
		str_desc = "A roll of wrapping paper with a bunch of pickaxes depicted on it. Perfect for Juvies who love to toil away in the mines.",
		price = 1000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_benwrappingpaper,
		context = ewcfg.context_wrappingpaper,
		alias = [
			"bwp"
		],
		str_name = "Ben Wrapping Paper",
		str_desc = "Wrapping paper with the Cop Killer printed on it. !dab !dab !dab",
		price = 1000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_munchywrappingpaper,
		context = ewcfg.context_wrappingpaper,
		alias = [
			"mwp"
		],
		str_name = "Munchy Wrapping Paper",
		str_desc = "Wrapping paper with the Rowdy Fucker printed on it. !THRASH !THRASH !THRASH",
		price = 1000,
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_gellphone,
		context = 'gellphone',
		alias = [
			"gell",
			"phone",
			"cellphone",
			"flipphone",
			"nokia"
		],
		str_name = "Gellphone",
		str_desc = "A cell phone manufactured by SlimeCorp. Turning it on allows you to access various apps and games.",
		vendors = [ewcfg.vendor_bazaar],
		price = 1000000
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_modelovaccine,
		context = ewcfg.item_id_modelovaccine,
		alias = [
			"vaccine",
			"cure",
		],
		str_name = "Modelovirus vaccine",
		str_desc = "It’s a rusty syringe containing a thick, dark-red substance. It begins to bubble slightly when you shake it. A few charred bits rise to the top. Looks yummy!",
		vendors = [ewcfg.vendor_lab],
		price = 1000000
	),
	EwGeneralItem(
		id_item = 'n2corpse',
		context = 'corpse',
		str_name = "N2's Corpse",
		str_desc = "The unzucked corpse of N2. All these bloodstains make his outfit even more gaudy than usual.",
		alias = [
			"n2"
		]
	),
EwGeneralItem(
		id_item = 'n6corpse',
		context = 'corpse',
		str_name = "N6's Corpse",
		str_desc = "The unzucked corpse of N6. Something is preventing her corpse from entering the Sewers.",
		alias = [
			"n6"
		]
	),
EwGeneralItem(
		id_item = 'n10corpse',
		context = 'corpse',
		str_name = "N10's Corpse",
		str_desc = "The unzucked corpse of N10. Something about lugging this body around feels like a mistake.",
		alias = [
			"n10"
		]
	),
EwGeneralItem(
		id_item = 'n11corpse',
		context = 'corpse',
		str_name = "N11's Corpse",
		str_desc = "The unzucked corpse of N11. You're having a rough time carrying it.",
		alias = [
			"n11"
		]
	),
EwGeneralItem(
		id_item = 'n12corpse',
		context = 'corpse',
		str_name = "N12's Corpse",
		str_desc = "The unzucked corpse of N12. At this point she's hardly recognizable.",
		alias = [
			"n12"
		]
	),
EwGeneralItem(
		id_item = 'n13corpse',
		context = 'corpse',
		str_name = "N13's Corpse",
		str_desc = "The unzucked corpse of N13. The bulb head looks so fragile but it's definitely not breaking anytime soon.",
		alias = [
			"n13"
		]
	),
EwGeneralItem(
		id_item = 'zucksyringe',
		context = 'syringe',
		str_name = "Zuckerberg Syringe",
		str_desc = "It's a high-powered syringe that can take a slimeboi and pressurize them into a steel canister. Be careful who you use this on.",
		alias = [
			"syringe",
			"needle",
			"zucker"
		]
	),
	EwSlimeoidFood(
		id_item = ewcfg.item_id_fragilecandy,
		alias = [
			"fragile",
		],
		str_name = "Fragile Candy",
		str_desc = "Increases Chutzpah and decreases Grit, when fed to a slimeoid.",
		vendors = [ewcfg.vendor_glocksburycomics, ewcfg.vendor_slimypersuits],
		price = 100000,
		increase = ewcfg.slimeoid_stat_chutzpah,
		decrease = ewcfg.slimeoid_stat_grit,
	),
	EwSlimeoidFood(
		id_item = ewcfg.item_id_rigidcandy,
		alias = [
			"rigid",
		],
		str_name = "Rigid Candy",
		str_desc = "Increases Grit and decreases Chutzpah, when fed to a slimeoid.",
		vendors = [ewcfg.vendor_glocksburycomics, ewcfg.vendor_slimypersuits],
		price = 100000,
		increase = ewcfg.slimeoid_stat_grit,
		decrease = ewcfg.slimeoid_stat_chutzpah,
	),
	EwSlimeoidFood(
		id_item = ewcfg.item_id_reservedcandy,
		alias = [
			"reserved",
		],
		str_name = "Reserved Candy",
		str_desc = "Increases Grit and decreases Moxie, when fed to a slimeoid.",
		vendors = [ewcfg.vendor_glocksburycomics, ewcfg.vendor_slimypersuits],
		price = 100000,
		increase = ewcfg.slimeoid_stat_grit,
		decrease = ewcfg.slimeoid_stat_moxie,
	),
	EwSlimeoidFood(
		id_item = ewcfg.item_id_recklesscandy,
		alias = [
			"reckless",
		],
		str_name = "Reckless Candy",
		str_desc = "Increases Moxie and decreases Grit, when fed to a slimeoid.",
		vendors = [ewcfg.vendor_glocksburycomics, ewcfg.vendor_slimypersuits],
		price = 100000,
		increase = ewcfg.slimeoid_stat_moxie,
		decrease = ewcfg.slimeoid_stat_grit,
	),
	EwSlimeoidFood(
		id_item = ewcfg.item_id_insidiouscandy,
		alias = [
			"insidious",
		],
		str_name = "Insidious Candy",
		str_desc = "Increases Chutzpah and decreases Moxie, when fed to a slimeoid.",
		vendors = [ewcfg.vendor_glocksburycomics, ewcfg.vendor_slimypersuits],
		price = 100000,
		increase = ewcfg.slimeoid_stat_chutzpah,
		decrease = ewcfg.slimeoid_stat_moxie,
	),
	EwSlimeoidFood(
		id_item = ewcfg.item_id_bluntcandy,
		alias = [
			"blunt",
		],
		str_name = "Blunt Candy",
		str_desc = "Increases Moxie and decreases Chutzpah, when fed to a slimeoid.",
		vendors = [ewcfg.vendor_glocksburycomics, ewcfg.vendor_slimypersuits],
		price = 100000,
		increase = ewcfg.slimeoid_stat_moxie,
		decrease = ewcfg.slimeoid_stat_chutzpah,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_creampie,
		str_name="Coconut Cream Pie",
		str_desc="A coconut cream pie, perfect for creaming all over someone!" + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} throws a cream pie at your face! How embarrassing, yet tasty!",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_waterballoon,
		str_name="Water Balloon",
		str_desc="A simple, yet effective water balloon. Aim for the groin for maximum effectiveness." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} throws a water balloon at your crotch. Haha, fucking piss your pants much?",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_bungisbeam,
		str_name="Bungis Beam",
		str_desc="A high-tech futuristic ray gun, with the uncanny ability to turn someone into Sky (Bungis)... or so the legends say." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} shoots you with a Bungis Beam! Slowly but surely, you transmogrify into Sky (Bungis)!!",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=10,
		side_effect="bungisbeam_effect",
	),
	EwPrankItem(
		id_item=ewcfg.item_id_circumcisionray,
		str_name="Circumcision Ray",
		str_desc="A powerful surgical tool in the form of a handgun. You're not really sure how it works, but testing it out on yourself seems unwise." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} fires off a Circumcision Ray at your genitals! Oh god, **IT BURNS!!** What the fuck is wrong with them?",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=25,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_cumjar,
		str_name="Cum Jar",
		str_desc="A jar full of seminal fluid. You think you can spot what looks like a My Little Pony figurine on the inside." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} chucks a Cum Jar in your general direction! The sticky white stuff gets everywhere!!",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=30,
		side_effect="cumjar_effect",
	),
	EwPrankItem(
		id_item=ewcfg.item_id_discounttransbeam,
		str_name="Discount Trans Beam",
		str_desc="A shitty knock-off of the real thing. Gotta work with the hand you're dealt, I guess." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} emits a Discount Trans Beam! You are imbued with a mild sense of gender dysphoria.",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_transbeamreplica,
		str_name="Legally Distinct Trans Beam Replica",
		str_desc="A scientifically perfected replica of the famous Trans Beam. Could SlimeCorp be responsible?\n\n**THIS IS A LEGALLY DISTINCT VERSION OF THE TRANS BEAM. IT IS IN NO WAY AN ACT OF PLAGIARISM AGAINST PARADOX CROCS OR THE PARADOX CROCS FAN CLUB TREEHOUSE LLC**" + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="***PSHOOOOOOOO!!!*** {} calls upon the all powerful **Trans Beam!** Your gender dysphoria levels are off the fucking charts!! You, dare I say it, might just be Transgendered now.",
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=50,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_bloodtransfusion,
		str_name="Blood Transfusion",
		str_desc="A packet of unknown blood hooked up to a syringe. They'll never see it coming." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} stabs you with a syringe and performs a Blood Transfusion! Who knows what kind of fucked up diseases they just gave you?!",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=30,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_transformationmask,
		str_name="Transformation Mask",
		str_desc="A mask used to transform into other people, somewhat visually reminiscent of the one used in The Mask (1994), starring Jim Carrey." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="***SSSSMMMMMMOOOOKKIIIN!!*** {} puts on their Transformation Mask and copies your likeness! While in disguise, they do all sorts of crazy, messed up shit and ruin your reputation completely!!",
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_emptychewinggumpacket,
		str_name="Empty Chewing Packet",
		str_desc="A packet of chewing gum, which, upon closer inspection, is completely empty. It's fool-proof, really." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} offers you a piece of Chewing Gum in these desperate times. HA, sike! The packet is completely empty, you fucking IDIOT!",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=10,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_airhorn,
		str_name="Air Horn",
		str_desc="A device capable of deafening those who get too close to it." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} blasts an Air Horn and ruptures your eardrums! What an asshole!",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_banggun,
		str_name="BANG! Gun",
		str_desc="A firearm that shoots out a tiny little flag. Also capable of shooting real bullets." + ewcfg.prank_type_text_instantuse,
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} points a gun at your! Oh, haha, it just shoots out a little flag with the word 'BANG!' on it, how cu-\n\n**The gun then ejects the flag and fires a bullet right into your foot.**",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_pranknote,
		str_name="Prank Note",
		str_desc="A mysterious notebook. It's said that if you write someone's name down in it, they get pranked hardcore.",
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} writes your name down in the Prank Note! You are almost instantly assaulted by a barrage of cream pies, water baloons, and air horns! Holy fucking shit!!",
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_bodynotifier,
		str_name="Body Notifier",
		str_desc="An item that notifies someone of their basic bodily functions.",
		prank_type=ewcfg.prank_type_instantuse,
		prank_desc="{} notifies you of your basic bodily functions.",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=15,
		side_effect="bodynotifier_effect"
	),
	EwPrankItem(
		id_item=ewcfg.item_id_chinesefingertrap,
		str_name="Chinese Finger Trap",
		str_desc="An item of oriental origin. Wrap it around someone's finger to totally prank them!" + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="Oh no! {} has ensnared you in a Chinese finger trap! Type **!loosenfinger** to escape!",
		response_desc_1="You try to separate your fingers but they are truly trapped. Type **!loosenfinger** to untrap yourself.",
		response_desc_2="The paper finger trap holds strong. Type **!loosenfinger** to break free.",
		response_desc_3="You pull your fingers apart with all your might, but the finger trap only grips tighter. Typing **!loosenfinger** might loosen your finger and help you escape.",
		response_desc_4="You surrender, resigning your fingers to be connected forever. You think about all the things you can still do with conjoined index fingers. You try to jack it but it doesn't quite work.",
		response_command="loosenfinger",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=2,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_japanesefingertrap,
		str_name="Japanese Finger Trap",
		str_desc="By all means it's an upgrade compared to the Chinese one. This one has barbs on the inside. Youch!" + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="気を付けて！ {}さんがあなたを日本の指トラップに捕らえました！ **!wigglefinger**タイプをする！",
		response_desc_1="指が閉じ込められます。閉じ込められるように、**!wigglefinger**と入力します。",
		response_desc_2="ペーパーフィンガートラップは強力です。 **!wigglefinger**と入力して自由にします。",
		response_desc_3="機械翻訳施設に閉じ込められているのを助けてください **!wigglefinger**。",
		response_desc_4="あなたは日本人になりました",
		response_command="wigglefinger",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=4,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_sissyhypnodevice,
		str_name="Sissy Hypno Device",
		str_desc="A VR headset with some rather dubious content being broadcast to it. Yeah, you better save this for when the chips are down and you really wanna fuck someone's day up." + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="Oh no! When you weren't looking, {} slipped a sissy hypno device onto your head and tightened the straps! Type **!takeoffheadset** to get out of there before your mind becomes corrupted!",
		response_desc_1="The sissy hypno device analyzes your brainwaves and finds you a perfect candidate to become a sissy. Type **!takeoffheadset** to stop the procedure.",
		response_desc_2="Your grey matter is probed by the tendrils of the sissy hypno device. You are about to sustain permanant sissyfication. Type **!takeoffheadset** now.",
		response_desc_3="You feel the sudden urge to don striped socks. **!takeoffheadset**.",
		response_desc_4="You have been fully hypnotized and are now 100% a sissy. **!takeoffheadset** will not help you any longer.",
		response_command="takeoffheadset",
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=6,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_piedpiperkazoo,
		str_name="Pied Piper Kazoo",
		str_desc="A musical instrument capable of summoning a swarm of rodents! Let's see what kind of trouble this thing can get you into." + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="Oh no! {} has sicced their rats on you. Type **!runfromtherats** to run from the rats.",
		response_desc_1="A rat peeks its head out of a nearby gutter and peers directly at you. You can get a headstart on him by typing **!runfromtherats**.",
		response_desc_2="Three rats crawl out of a trashcan and attempt to block your way. You could probably step over them, if you type **!runfromtherats**.",
		response_desc_3="About 15 or 16 rats encircle you. It looks grim, but you may still have a chance to **!runfromtherats**.",
		response_desc_4="A rat runs up your pant leg and bites your taint. You stumble and fall into what can only be described as a sea of rats.",
		response_command="runfromtherats",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=4,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_sandpapergloves,
		str_name="Sandpaper Gloves",
		str_desc="Gloves padded with sandpaper on the palms and fingers. Although it's capable of giving some real mean Indian burns, its slapping attacks are nothing to be scoffed at, either." + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="Oh no! {} approaches. It looks like they want a hi-five. Type **!dodgetheglove** to dodge their sandpaper glove.",
		response_desc_1="You don't know them that well... they might just be waving at you. Type **!dodgetheglove** to try and avoid an awkward situation.",
		response_desc_2="You raise your hand to wave back, but it seems they're waving at someone behind you. Type **!dodgetheglove** to sprint in the opposite direction as fast as possible.",
		response_desc_3="They stop waving, but are still approaching you with -- what you can now see is a sandpaper glove -- outstretched. Type **!dodgetheglove** to dodge their hand, matrix-style.",
		response_desc_4="{} reaches you, and slaps you across the face with their 80 grit, diamond powder, industry-standard sandpaper glove. It tears your facial dermis straight off.",
		response_command="dodgetheglove",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=3,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_ticklefeather,
		str_name="Tickle Feather",
		str_desc="A feather? For like, tickling people or some shit? Honestly, these pranks are starting to get a bit weird." + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="Oh no! Imminent tickling from {} approaching. Type **!dontlaugh** to not laugh.",
		response_desc_1="aaahahaaha it tickles **!dontlaugh**",
		response_desc_2="hehehehheh STOP **!dontlaugh**",
		response_desc_3="AAAAAHHAHAHAHHAHHAAH **!dontlaugh** HHEJHJHHAHAHAHA!",
		response_desc_4="OOOOOO OOOOO OOOO OOOOO OO OO O O O O OOO!",
		response_command="dontlaugh",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=2,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_genitalmutilationinstrument,
		str_name="Genital Mutilation Instrument",
		str_desc="A horrid, nightmarish mechanism which should have been hidden away off ages ago, but has somehow returned. Legends say the Double Headless Double Horseman had one in his possession." + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_desc_1="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_desc_2="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_desc_3="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_desc_4="{} has your genitals in an iron grip! Type **!resisttorture** to minimize the extreme pain!",
		response_command="resisttorture",
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=7,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_gamerficationasmr,
		str_name="Gamerfication ASMR",
		str_desc="An incredibly long recording of some depraved hypnotization method. You wouldn't wish this kind of thing on your worst enemy." + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="Oh no! {} approaches you with a 10-hour YouTube video of Gamerification ASMR. Type **!closeyourears** to try not to listen.",
		response_desc_1="woooOOOooo yooouuu are becooooming a gaaaamer. yoou playy temple ruuuun on the toiiiilet. **!closeyourears** to turn off the video.",
		response_desc_2="ooooooo yoooou seeeee a csgo major at a bar and kiiiinda enjoooy iiiit. **!closeyourears** to stop the damage any further.",
		response_desc_3="oooohhhhhh youuuuu plaaaaayyy dota 2 and flaaaame your teammates !votekick **!closeyourears**.",
		response_desc_4="yooouu suudeenly waant too speeend eeight houurs debuuugiiinng skyriiim moooodsss oooOOOoooo.",
		response_command="closeyourears",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=5,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_beansinacan,
		str_name="Beans In A Can",
		str_desc="A tin of beans. Warning: Place In A Microwave-Safe Container Before Heating." + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="Oh no! {} approches you with a can of Bush's Baked Beans in one hand, and a spoon in the other. They are making train noises. Type **!duckthebeans** to dodge the choo-choo.",
		response_desc_1="You ate the entire can of baked beans, but {} pulls out another can. This time it's Pinto Beans in Liquid. **!duckthebeans** so you don't have to eat slimy beans.",
		response_desc_2="You polish off another can of beans. {} pulls out an entire 8-layer Bean Dip and a bag of Tostito's. Honestly it looks pretty good, but you are full. Type **!duckthebeans** because you can't bear to eat anything more.",
		response_desc_3="Now {} pulls out a baggie of Jelly Beans. You think it could be a nice desert. Maybe you don't want to **!duckthebeans** this time.",
		response_desc_4="You finish off the Jelly Beans, but {} pulls out a handful of toe beans. It looks like they just poached them off a pack of furries. They still have hair on them. Absolutely disgusting.",
		response_command="duckthebeans",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=4,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_brandingiron,
		str_name="Branding Iron",
		str_desc="A big, red hot iron used for branding cattle. Is this how we're doing !vouches nowawadays?" + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="Oh no! {} lunges towards you with a white-hot branding iron. Type **!deflectthebrand** to attempt to knock it away.",
		response_desc_1="{} jabs you with the white-hot brand. It's only one letter, any tattoo artist could work it into another word. They still looks angry, and the brand is still yellow hot, so you should probably try to **!deflectthebrand**.",
		response_desc_2="{} drives the brand into you a few more times. It looks like they are trying to spell their name. Type **!deflectthebrand** before they can remember the last few letters.",
		response_desc_3="At this point it looks like {} is using you like a loose-leaf paper. They are taking Social Studies notes using an orange-hot metal rod on your flesh. Type **!deflectthebrand** before they can get to your face.",
		response_desc_4="You are fully covered in brands. You look like a human crossword puzzle, children run by and sharpie circles on you. You look down at your abdomen and notice a few choice epithets.",
		response_command="deflectthebrand",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=3,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_lasso,
		str_name="Lasso",
		str_desc="A rope with a hoop tied at the end. You're reminded of Quickdraw Saloon, if only because of the blatantly out-of-place cowboy theming this item represents." + ewcfg.prank_type_text_response,
		prank_type=ewcfg.prank_type_response,
		prank_desc="Aw shucks! {} is wavin' their lasso high in the air! Type **!escapethelasso** to git on out of their, partner!",
		response_desc_1="YEEHAW! {} lassos you up once! Type **!escapethelasso** and maybe you can walk away with your bounty intact!",
		response_desc_2="YEEEEHAAW!! {} lassos you up twice! Type **!escapethelasso** to buck away that twine!",
		response_desc_3="YEEEEEEHAAAW!!! {} lassos you up thrice! Holy hell, you're a goddamn rope mummy at this point, partner! Type **!escapethelasso** and maybe you can still *rope* your way out of this one!",
		response_desc_4="YYYYYYYYEEEEEEEEHHHHHHHAAAAAAWWWWWWW!!!!! {} has made a lasso cocoon out of you! There's no way out!!",
		response_command="escapethelasso",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=2,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_fakecandy,
		str_name="Fake Candy",
		str_desc="A bag of fake candy, disguised as candy from last year's Double Halloween",
		prank_type=ewcfg.prank_type_response,
		prank_desc="You see a bag of candy lying on the ground. Neaby, you can see {} cackling to themselves like a madman. Maybe it's best to **!ignorethecandy**.",
		response_desc_1="You scoop up the bag and ingest its contents instead. Yuck! These taste awful! Another bag of candy dropped close by catches your attention. **!ignorethecandy**.",
		response_desc_2="You eat the next bag of candy, which tastes even worse than the previous! Seriously, maybe you should stop being retarded and **!ignorethecandy**.",
		response_desc_3="You eat the third bag of candy in a row. Oh jesus fucking christ, you just cant help yourself at this point, and gobble up the awful confectionary without a second thought. Maybe it's time to **!ignorethecandy**.",
		response_desc_4="You eat the last and final bag of candy. They taste like literal dogshit. What the fuck were you thinking?",
		response_command="ignorethecandy",
		rarity=ewcfg.prank_rarity_heinous,
		gambit=2,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_crabarmy,
		str_name="Crab Army",
		str_desc="An army of crabs, ready to be snip and snap at will.",
		prank_type=ewcfg.prank_type_response,
		prank_desc="{} calls forth their Crab Army, and directs it towards you! Oh man, you better type **!jumpovercrabs** before it's too late!",
		response_desc_1="A lonesome crab snips and snaps at your leg! Ow, the pain is just brutal! Others are skittering closely behind, type **!jumpovercrabs**.",
		response_desc_2="A few more crabs come and attack your sides! Oh god! You gotta get these things off of you and **!jumpovercrabs** fast to make sure no more can latch on!!",
		response_desc_3="Five or six more crabs grab on with their snippers and squeeze tightly against your arms and face. Despite everything, it's still you. With determination in hand, maybe you can **!jumpovercrabs** and escape them before they clutch victory in their crustacean appendages.",
		response_desc_4="It's too late to **!jumpovercrabs** now. In light of their overwhelming victory against you, they hold a celebratory rave. The music they play, you will not soon forget.",
		response_command="jumpovercrabs",
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=4
	),
	EwPrankItem(
		id_item=ewcfg.item_id_whoopiecushion,
		str_name="Whoopie Cushion",
		str_desc="A classic tool of the pranking trade. You'd be surprised if anyone actually fell for it these days, though." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="You step on a Whoopie Cushion by mistake, emitting a noise most foul. Strangers and passersby look at you like you just shit your fucking pants.",
		trap_chance=35,
		rarity=ewcfg.prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_beartrap,
		str_name="Bear Trap",
		str_desc="A hunk of metal jaws, with a trigger plate in the middle. Stepping on it would be a bad idea." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="Oh fuck! You just stepped inside a bear trap! After several minutes of bleeding profusely, you manage to pry it open and lift out your numbed, chomped up ankle!",
		trap_chance=30,
		rarity=ewcfg.prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_bananapeel,
		str_name="Banana Peel",
		str_desc="A rotten leftover banana peel. God, can't people fucking clean up after themselves anymore?" + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="You slip and slide on a Banana Peel and land right on your tailbone! Oof, ouch, your bones!!",
		trap_chance=35,
		rarity=ewcfg.prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_windupbox,
		str_name="Wind-up Box",
		str_desc="One of those old-timey toys that somehow manages to scare the living daylights out of you. It has a jester on the inside, who by all means takes great joy in your fear, and the fear of others." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="What's this? You find a box with a crank on the side... hey! When you crank it, it starts to play music! This is pretty co- AH JESUS FUCK!!",
		trap_chance=35,
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=25,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_windupchatterteeth,
		str_name="Wind-up Chatter Teeth",
		str_desc="A set of plastic teeth that chomp away the more you wind up the little dial on the side. It chugs along on a pair of feet while the gears inside tick away." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="OUCH!! What the fuck? A pair of Wind-up Chatter Teeth are nipping at your heels! Shoo, you fucking wannabe memorabilia!",
		trap_chance=40,
		rarity=ewcfg.prank_rarity_heinous,
		gambit=15,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_snakeinacan,
		str_name="Snake In A Can",
		str_desc="An undeniable classic. Pop it open, and watch the color drain from some poor dim-wit's face as the vinyl-coated viper reaches for the skies." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="What the heck... no way! A can of peanuts! You just gotta unscrew the lid, and... ***!!!***\n\nAfter a brief lapse in consciousness, you awake to find yourself lying on the ground next to that shitty Snake In A Can you can't believe you fell for.",
		trap_chance=30,
		rarity=ewcfg.prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_landmine,
		str_name="Land Mine",
		str_desc="A round metal plate, charged with explosives. These are normally only reserved for tanks, but during Swilldermuk, civilians have been given clearance to use them at their personal discretion.",
		prank_type=ewcfg.prank_type_trap,
		prank_desc="**HOLY FUCKING SHIT!!** You just stepped on a God damn Land Mine! The blast knocks you on your ass and fractures several bones in the lower half of your body. Haha, fucking pranked, bro!!",
		trap_chance=40,
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_freeipad,
		str_name="Free Ipad",
		str_desc="A free iPad. On the back, there's a logo sticker for... Cinemassacre? Oh god, you better drop this thing before that cyborg puts you out of your misery." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc='Well what do ya know! A free iPad! You bend over to pick it up...\n\nENDLESS RIOT judges you harshly! He shoots out two shots of a non-lethal variant of the Bone-hurting-beam, which is even more embarrassing than if he had just killed you, honestly. He told you to shut up, but you didn\'t listen.\n\n**"OH LOOK, A FREE IPAD."**',
		trap_chance=35,
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_perfectlynormalfood,
		str_name="Perfectly Normal Food",
		str_desc="A plate of perfectly normal food, which in no way has been tampered with in any capacity" + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="Oh damn! A plate of perfectly normal food? Well, what could be the harm in having a bite, you wonder... **COUGH COUGH COUGH** OH GOD IT'S LACED WITH RAT POISON!",
		trap_chance=30,
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=30,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_pitfall,
		str_name="Pitfall Trap",
		str_desc="A round sphere, with an exclamation mark painted on. You don't really know how it works, but aparrently all you gotta do to set it up is dig a hole in the ground and throw it in." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="Ah fuck! The ground caves underneath you, causing you to fall inside a Pitfall Trap! After a moment or two, you manage to climb back up out of the pit it so deviously hid from sight.",
		trap_chance=40,
		rarity=ewcfg.prank_rarity_heinous,
		gambit=20,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_electrocage,
		str_name="Electro Cage",
		str_desc="A cage with iron bars that are hooked up to some kind of electrical current. Apparently they used to use these things at the Slime Circus, to keep all the beasts this thing housed tempered and in line." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="Oh shit. Before you know it, you're 3 steps too far into an Electro Cage. The door locks behind you, and you're forced to endure an agonizing 1 Million Volt shock, with a decent amount of Amps to back it up. Incidentally, the overstimulation also forces you to vacate your bladder, worsening the embarrassment of the situation.",
		trap_chance=40,
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=30,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_ironmaiden,
		str_name="Iron Maiden",
		str_desc="An ancient instrument of torture, in the form of a human-shaped closet with spears on the inside. Hauling it around is a pain in the fucking ass, so you hope someone at least gets tricked by it when the time comes." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="Like a complete fucking dumbass, you walk into a nearby Iron Maiden, which closes shut behind you. The spikes impale you on every limb and into every orifice, causing the whole thing to get damn near coated in slime on the inside. Try taking your eyes off your phone for once, dummy!",
		trap_chance=25,
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=50,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_signthatmakesyoubensaint,
		str_name="Sign That Makes You Ben Saint When You Read It",
		str_desc="An otherworldy artifact. Has the fantastical effect of transforming someone into Ben Saint, should they trigger its effects by reading what it says." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="Hey, there's a sign over in the distance. You squint to make out what it says... Oh no! Upon closer inspection, it's a Sign That Makes You Ben Saint When You Read It!",
		trap_chance=50,
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=15,
		side_effect = "bensaintsign_effect"
	),
	EwPrankItem(
		id_item=ewcfg.item_id_piebomb,
		str_name="Pie Bomb",
		str_desc="A bomb cleverly disguised as a Defective Coconut Cream Pie." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="Oh sweet! Another Defective Coconut Cream Pie for the taking!\n**BOOM!**\nAw man, someone set up a Pie Bomb and got you good!",
		trap_chance=30,
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=30,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_defectivealarmclock,
		str_name="Defective Alarm Clock",
		str_desc="A factory-rejected Alarm Clock. This thing just won't stop fucking beeping at you!!" + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc="BLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nBLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nBLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nBLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nBLAAAP BLAAAP BLAAAP BLAAAP BLAAAP\nYou crush the Defective Alarm Clock with your bare hands. Good fucking riddance.",
		trap_chance=40,
		rarity=ewcfg.prank_rarity_scandalous,
		gambit=15,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_freeipad_alt,
		str_name="Free Ipad...?",
		str_desc="A free iPad. On the back, there's a logo sticker for... Cinemassacre? Oh god, you better drop this thing before that android puts you out of your misery." + ewcfg.prank_type_text_trap,
		prank_type=ewcfg.prank_type_trap,
		prank_desc='Well what do ya know! A free iPad! You bend over to pick it up...\n\nENDLESS RIOT judges you harshly! He shoots out two shots of a non-lethal variant of the Bone-hurting-beam, which is even more embarrassing than if he had just killed you, honestly. He told you to shut up, but you didn\'t listen.\n\n**"It always... ends like this..."**\n\n**"OH LOOK, A FREE IPAD."**',
		trap_chance=35,
		rarity=ewcfg.prank_rarity_forbidden,
		gambit=45,
	),
	EwPrankItem(
		id_item=ewcfg.item_id_alligatortoy,
		str_name="Alligator Toy",
		str_desc="A toy alligator, where the objective is to brush its teeth without tripping its jaws. The top jaw on this one is mysteriously outfitted with razor blades instead of plastic, however.",
		prank_type=ewcfg.prank_type_trap,
		prank_desc='Oh hey! A toy alligator! You had so much fun with these as a kid! You just gotta press on the teeth in the right combination, and...\nOH JESUS CHRIST, THE RAZOR BLADES HIDDEN INSIDE BURY THEMSELVES INTO YOUR HAND!!',
		trap_chance=35,
		rarity=ewcfg.prank_rarity_heinous,
		gambit=20,
	),
	EwGeneralItem(
		id_item=ewcfg.item_id_swordofseething,
		str_name="SWORD OF SEETHING",
		str_desc="An ancient blade of legend. It's said to contain the foul malevolence of the Oozoth, sealed away long ago. The forces resting inside the sword are practically begging you to !use it, before its power fades away into nothingness, so you might as well get it over with.",
		context="swordofseething",
	),
	EwGeneralItem(
		id_item="brokensword",
		str_name="Broken Sword",
		str_desc="The lower half of a broken sword. A useless trinket now, but perhaps one day it can be turned into something useful.",
		context="brokensword",
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_prankcapsule,
		alias = [
			"prank",
			"capsule",
		],
		str_name = "Prank Capsule",
		str_desc = "A small little plastic capsule, which holds a devious prank item on the inside.",
		price = 20000,
		vendors = [ewcfg.vendor_vendingmachine],
		context = "prankcapsule"
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_cool_material,
		str_name = "Cool Beans",
		str_desc = "A couple of cool beans! Far out, man. Well, they aren’t really beans per se, more like little condensed nuggets of your crop. Whatever they are, they’re undeniably cool.",
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_tough_material,
		str_name = "Tough Nails",
		str_desc = "A handful of rusty nails caked in dried blood that were presumably waiting for you if you had eaten your crops instead of milling them. Damn, what a missed opportunity!",
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_smart_material,
		str_name = "Smart Cookies",
		str_desc = "A farmer’s dozen of smart cookies. Well, they aren’t really cookies per se, more like little bland condensed patties of your crop. Whatever they are, they’re undeniably smart.",
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_beautiful_material,
		str_name = "Beauty Spots",
		str_desc = "A small collection of severed beauty spots, mostly freckles and moles, that were presumably waiting for you if you had eaten your crops instead of milling them. Damn, what a missed opportunity!",
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_cute_material,
		str_name = "Cute Buttons",
		str_desc = "A wardrobe of cute buttons. You know you should probably be concerned that these lil’ guys were hiding in your crops, but honestly you’re overcome with emotion and feel utterly blessed. Lookit ‘em! They’re adorable! D’awww...",
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dyesolution,
		str_name = "Dye Solution",
		str_desc = "A small vial of salt, water, and vinegar. You can smelt this together with crop materials to make dyes.",
		price = 1000,
		vendors = [ewcfg.vendor_basedhardware]
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_textiles,
		str_name = "Textiles",
		str_desc = "A set of fabrics. You can smelt this together with crop materials to make exclusive cosmetics.",
		price = 1000,
		vendors = [ewcfg.vendor_basedhardware]
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_foodbase,
		str_name = "Food Base",
		str_desc = "A set of powders and chemicals. You can smelt this together with crop materials to make exclusive food items which take longer to expire.",
		price = 1000,
		vendors = [ewcfg.vendor_basedhardware]
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_poketubereyes,
		str_name = "Poketuber Eyes",
		str_desc = "The small stem buds of a Poketuber.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_poketubers],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_pulpgourdpulp,
		str_name = "Pulp Gourd Pulp",
		str_desc = "The pulp of a Pulp Gourd.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_pulpgourds],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_sourpotatoskins,
		str_name = "Sour Potato Skins",
		str_desc = "The skins of a Sour Potato.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_sourpotatoes],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_bloodcabbageleaves,
		str_name = "Blood Cabbage Leaves",
		str_desc = "The soft leaves of a Blood Cabbage.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_bloodcabbages],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_joybeanvines,
		str_name = "Joybean Vines",
		str_desc = "The severed vines on which Joybeans grow.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_joybeans],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_purplekilliflowerflorets,
		str_name = "Killiflower Florets",
		str_desc = "The bush-like appendages of a Killiflower plant.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_purplekilliflower],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_razornutshells,
		str_name = "Razornut Shells",
		str_desc = "The sharp and pointy shells of a Razornut.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_razornuts],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_pawpawflesh,
		str_name = "Pawpaw Flesh",
		str_desc = "The ground flesh of a Pawpaw.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_pawpaw],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_sludgeberrysludge,
		str_name = "Sludgeberry Sludge",
		str_desc = "The thick syrup of a Sludgeberry.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_sludgeberries],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_suganmanutfruit,
		str_name = "Suganmanut Fruit",
		str_desc = "The bright, multi-colored fruit off which Suganmanuts grow.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_suganmanuts],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_pinkrowddishroot,
		str_name = "Pink Rowddish Root",
		str_desc = "The thin, light-colored root of a Pink Rowddish.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_pinkrowddishes],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_dankwheatchaff,
		str_name = "Dankwheat Chaff",
		str_desc = "The scaly, protective casing on Dankwheat plants.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_dankwheat],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_brightshadeberries,
		str_name = "Brightshade Berries",
		str_desc = "The small blue berries that grow on Brightshade plants.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_brightshade],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_blacklimeade,
		str_name = "Black Limeade",
		str_desc = "The sweet and sour juice of a Black Lime.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_blacklimes],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_phosphorpoppypetals,
		str_name = "Phosphorpoppy Petals",
		str_desc = "The yellow-green petals of a Phosphorpoppy.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_phosphorpoppies],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_direapplestems,
		str_name = "Dire Apple Stems",
		str_desc = "The orange stems of a Dire Apple.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_direapples],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_rustealeafblades,
		str_name = "Rustea Leaf Blades",
		str_desc = "The razor-sharp blades attatched to the stems of Rustea Leaves.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_rustealeaves],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_metallicapheads,
		str_name = "Metallicap Heads",
		str_desc = "The bulbous head on the top of a Metallicap.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_metallicaps],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_steelbeanpods,
		str_name = "Steel Bean Pods",
		str_desc = "The long and hard pods that house Steel Beans.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_steelbeans],
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_aushuckstalks,
		str_name = "Aushuck Stalks",
		str_desc = "The lengthy stalks of an Aushuck plant.",
		acquisition = ewcfg.acquisition_milling,
		ingredients = [ewcfg.item_id_aushucks],
	),
	EwGeneralItem(
		id_item=ewcfg.item_id_civilianscalp,
		str_name="civilian's scalp",
		str_desc="It's the discarded scalp of an innocent NLACakaNM resident. You always wanted to kill one of these guys."
	),
	EwGeneralItem(
		id_item = "key",
		str_name = "Cabinet Key",
		str_desc = "It's a tiny key. Some idiot must've left this in the middle of the street, it's weathered down right out of the box.",
		context = "cabinetkey"
	),
	EwGeneralItem(
		id_item="filmreel",
		str_name="VHS Tape",
		str_desc="It's a VHS for one of Slimecorp's old training videos.",
		context="reelkey"
	),
	EwGeneralItem(
		id_item = "coordinatesheet",
		str_name = "Coordinates",
		str_desc = "It's a small slip of paper that reads: \"36.174435, -112.043243, N. Beach Depths\"",
		context = "droppable"
	),
	EwSeedPacket(
		id_item=ewcfg.item_id_gaiaseedpack_poketubers,
		cooldown=30,
		cost=50,
		str_name="Poketuber Gaiaslimeoid Seed Packet",
		str_desc="A seed packet for a Poketuber Gaiaslimeoid. It costs 50 gaiaslime to !plant one, and has a 30 second cooldown.",
		ingredients=[ewcfg.item_id_poketubereyes],
		enemytype="poketubers"
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_juvie,
		str_name = "Juvie Hunting Trophy",
		str_desc = "A hunting trophy flayed from the flesh of a still-living Juvenile. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_dinoslime,
		str_name = "Dinoslime Hunting Trophy",
		str_desc = "A hunting trophy pried from the sticky jaws of a Dinoslime. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_slimeadactyl,
		str_name = "Slimeadactyl Hunting Trophy",
		str_desc = "A hunting trophy ripped from the wing of a Slimeadactyl. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_microslime,
		str_name = "Microslime Hunting Trophy",
		str_desc = "A hunting trophy sampled from the body of a Microslime. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_slimeofgreed,
		str_name = "Slime of Greed Hunting Trophy",
		str_desc = "A hunting trophy found within the depths of a Slime of Greed. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_desertraider,
		str_name = "Desert Raider Hunting Trophy",
		str_desc = "A hunting trophy scalped from the head of a Desert Raider. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_mammoslime,
		str_name = "Mammoslime Hunting Trophy",
		str_desc = "A hunting trophy sawed from the tusk of a fallen Mammoslime. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_megaslime,
		str_name = "Megaslime Hunting Trophy",
		str_desc = "A hunting trophy extracted from the core of a Megaslime. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_srex,
		str_name = "Slimeasaurus Rex Hunting Trophy",
		str_desc = "A hunting trophy plucked from the toes of a vanquished Slimeasaurus Rex. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_dragon,
		str_name = "Green Eyes Slime Dragon Hunting Trophy",
		str_desc = "A hunting trophy yoinked from the talons of a fallen Green Eyes Slime Dragon. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_ufo,
		str_name = "UFO Hunting Trophy",
		str_desc = "A ███████ trophy ████ed from the ██████ of a UFO. Ahhh, the thrill of the ████...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_mammoslimebull,
		str_name = "Mammoslime Bull Trophy",
		str_desc = "A hunting trophy carved from the tusk of a fallen Mammoslime Bull. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_rivalhunter,
		str_name = "Rival Hunter Trophy",
		str_desc = "A hunting trophy \"borrowed\" from the head of a Rival Hunter. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_bustedrifle,
		str_name = "Busted Rifle",
		str_desc = "A hunting rifle snapped in twain. If only you could repair it somehow..."
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_repairkit,
		str_name = "Field Repair Kit",
		alias = ["repairkit", "fieldrepair"],
		str_desc = "A field repair kit for pantaloons, brunches, spyglasses and manners. Could be used to repair a hunting rifle too, in a pinch.",
		price = 500000,
		vendors = [ewcfg.vendor_bazaar]
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_spacecarp,
		str_name = "Space Carp Trophy",
		str_desc = "A hunting trophy wrenched from the mouth of a Space Carp. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_carpotoxin,
		str_name = "Carpotoxin",
		str_desc = "This stuff is incredibly poisonous. Good thing you're not going to drink it, hahah..."
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_moonrock,
		str_name = "Moon Rock",
		str_desc = "A piece of the Moon, now in your grubby little hands.",
		price = 100000
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_gull,
		str_name = "Gull Trophy",
		str_desc = "A hunting trophy snatched from the wings of a Gull. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_rainwing,
		str_name = "Rain Wing",
		str_desc = "A feather obtained from a gull. Folklore says this can be used to herald rain.",
		context  = "rain"
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_garfield,
		str_name = "Garfield Trophy",
		str_desc = "A hunting trophy sliced from the paws of Garfield. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_n400,
		str_name = "N400 Trophy",
		str_desc = "A hunting trophy requisitioned from N400. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_styx,
		str_name = "Styx Trophy",
		str_desc = "A hunting trophy shaved from Styx. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_prairieking,
		str_name = "Prairie King Trophy",
		str_desc = "A hunting trophy nabbed from the itty bitty hands of the Prarie King. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_wailord,
		str_name = "Wailord Trophy",
		str_desc = "A hunting trophy dredged from Wailord's blubber. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_phoenix,
		str_name = "Phoenix Trophy",
		str_desc = "A hunting trophy swept up from the ashes of the Phoenix. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_phoenixdown,
		str_name = "Phoenix Down",
		str_desc = "A feather plucked from a mythical Phoenix. Can be used to revive fallen slimeoids.",
		context = "slimeoidrevive"
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_pheromones,
		str_name = "Kinkfish Pheromones",
		str_desc = "A spray-on bottle of Kinkfish pheromones. Apparently, it attracts all sorts of things despite smelling like shit.",
		acquisition = ewcfg.acquisition_smelting,
		context = "pheromones",
		price = 10000
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_trophy_microgull,
		str_name = "Micro Gull Trophy",
		str_desc = "A miniscule hunting trophy snatched from the wings of a Micro Gull. Ahhh, the thrill of the hunt...",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	EwGeneralItem(
		id_item = ewcfg.item_id_feather,
		str_name = "Regular Feather",
		str_desc = "A perfectly normal feather. Nothing suspicious about this, nossir.",
		acquisition = ewcfg.acquisition_huntingtrophy
	),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_pulpgourds,
	# 	cooldown=45,
	# 	cost=100,
	# 	str_name="Pulp Gourds Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Pulp Gourds Gaiaslimeoid. It costs 100 gaiaslime to !plant one, and has a 45 second cooldown.",
	# 	ingredients=[ewcfg.item_id_pulpgourdpulp],
	# 	enemytype="pulpgourds"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_sourpotatoes,
	# 	cooldown=10,
	# 	cost=150,
	# 	str_name="Sour Potatoes Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Sour Potatoes Gaiaslimeoid. It costs 150 gaiaslime to !plant one, and has a 10 second cooldown.",
	# 	ingredients=[ewcfg.item_id_sourpotatoskins],
	# 	enemytype="sourpotatoes"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_bloodcabbages,
	# 	cooldown=10,
	# 	cost=125,
	# 	str_name="Blood Cabbages Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Blood Cabbages Gaiaslimeoid. It costs 125 gaiaslime to !plant one, and has a 10 second cooldown.",
	# 	ingredients=[ewcfg.item_id_bloodcabbageleaves],
	# 	enemytype="bloodcabbages"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_joybeans,
	# 	cooldown=120,
	# 	cost=100,
	# 	str_name="Joybeans Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Joybean Gaiaslimeoid. It costs 100 gaiaslime to !plant one, and has a 120 second cooldown.",
	# 	ingredients=[ewcfg.item_id_joybeanvines],
	# 	enemytype="joybeans"
	# ),
	EwSeedPacket(
		id_item=ewcfg.item_id_gaiaseedpack_purplekilliflower,
		cooldown=10,
		cost=100,
		str_name="Purple Killiflower Gaiaslimeoid Seed Packet",
		str_desc="A seed packet for a Purple Killiflower Gaiaslimeoid. It costs 100 gaiaslime to !plant one, and has a 10 second cooldown.",
		ingredients=[ewcfg.item_id_purplekilliflowerflorets],
		enemytype="purplekilliflower"
	),
	EwSeedPacket(
		id_item=ewcfg.item_id_gaiaseedpack_razornuts,
		cooldown=45,
		cost=50,
		str_name="Razornuts Gaiaslimeoid Seed Packet",
		str_desc="A seed packet for a Razornuts Gaiaslimeoid. It costs 50 gaiaslime to !plant one, and has a 45 second cooldown.",
		ingredients=[ewcfg.item_id_razornutshells],
		enemytype="razornuts"
	),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_pawpaw,
	# 	cooldown=45,
	# 	cost=150,
	# 	str_name="Pawpaw Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Pawpaw Gaiaslimeoid. It costs 150 gaiaslime to !plant one, and has a 45 second cooldown.",
	# 	ingredients=[ewcfg.item_id_pawpawflesh],
	# 	enemytype="pawpaw"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_sludgeberries,
	# 	cooldown=15,
	# 	cost=75,
	# 	str_name="Sludgeberries Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Sludgeberries Gaiaslimeoid. It costs 75 gaiaslime to !plant one, and has a 15 second cooldown.",
	# 	ingredients=[ewcfg.item_id_sludgeberrysludge],
	# 	enemytype="sludgeberries"
	# ),
	EwSeedPacket(
		id_item=ewcfg.item_id_gaiaseedpack_suganmanuts,
		cooldown=60,
		cost=125,
		str_name="Suganmanuts Gaiaslimeoid Seed Packet",
		str_desc="A seed packet for a Suganmanuts Gaiaslimeoid. It costs 125 gaiaslime to !plant one, and has a 60 second cooldown.",
		ingredients=[ewcfg.item_id_suganmanutfruit],
		enemytype="suganmanuts"
	),
	EwSeedPacket(
		id_item=ewcfg.item_id_gaiaseedpack_pinkrowddishes,
		cooldown=20,
		cost=150,
		str_name="Pink Rowddishes Gaiaslimeoid Seed Packet",
		str_desc="A seed packet for a Pink Rowddishes Gaiaslimeoid. It costs 150 gaiaslime to !plant one, and has a 20 second cooldown.",
		ingredients=[ewcfg.item_id_pinkrowddishroot],
		enemytype="pinkrowddishes"
	),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_dankwheat,
	# 	cooldown=30,
	# 	cost=200,
	# 	str_name="Dankwheat Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Dankwheat Gaiaslimeoid. It costs 200 gaiaslime to !plant one, and has a 30 second cooldown.",
	# 	ingredients=[ewcfg.item_id_dankwheatchaff],
	# 	enemytype="dankwheat"
	# ),
	EwSeedPacket(
		id_item=ewcfg.item_id_gaiaseedpack_brightshade,
		cooldown=10,
		cost=50,
		str_name="Brightshade Gaiaslimeoid Seed Packet",
		str_desc="A seed packet for a Brightshade Gaiaslimeoid. It costs 50 gaiaslime to !plant one, and has a 10 second cooldown.",
		ingredients=[ewcfg.item_id_brightshadeberries],
		enemytype="brightshade"
	),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_blacklimes,
	# 	cooldown=10,
	# 	cost=75,
	# 	str_name="Black Limes Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Black Limes Gaiaslimeoid. It costs 75 gaiaslime to !plant one, and has a 10 second cooldown.",
	# 	ingredients=[ewcfg.item_id_blacklimeade],
	# 	enemytype="blacklimes"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_phosphorpoppies,
	# 	cooldown=10,
	# 	cost=75,
	# 	str_name="Phosphorpoppies Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Phosphorpoppies Gaiaslimeoid. It costs 75 gaiaslime to !plant one, and has a 10 second cooldown.",
	# 	ingredients=[ewcfg.item_id_phosphorpoppypetals],
	# 	enemytype="phosphorpoppies"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_direapples,
	# 	cooldown=10,
	# 	cost=225,
	# 	str_name="Dire Apples Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Dire Apples Gaiaslimeoid. It costs 225 gaiaslime to !plant one, and has a 10 second cooldown.",
	# 	ingredients=[ewcfg.item_id_direapplestems],
	# 	enemytype="direapples"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_rustealeaves,
	# 	cooldown=10,
	# 	cost=100,
	# 	str_name="Rustea Leaves Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Rustea Leaves Gaiaslimeoid. It costs 100 gaiaslime to !plant one, and has a 10 second cooldown.",
	# 	ingredients=[ewcfg.item_id_rustealeafblades],
	# 	enemytype="rustealeaves"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_metallicaps,
	# 	cooldown=30,
	# 	cost=225,
	# 	str_name="Metallicaps Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Metallicaps Gaiaslimeoid. It costs 225 gaiaslime to !plant one, and has a 30 second cooldown.",
	# 	ingredients=[ewcfg.item_id_metallicapheads],
	# 	enemytype="metallicaps"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_steelbeans,
	# 	cooldown=90,
	# 	cost=150,
	# 	str_name="Steelbeans Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for a Steelbeans Gaiaslimeoid. It costs 150 gaiaslime to !plant one, and has a 90 second cooldown.",
	# 	ingredients=[ewcfg.item_id_steelbeanpods],
	# 	enemytype="steelbeans"
	# ),
	# EwSeedPacket(
	# 	id_item=ewcfg.item_id_gaiaseedpack_aushucks,
	# 	cooldown=120,
	# 	cost=175,
	# 	str_name="Aushucks Gaiaslimeoid Seed Packet",
	# 	str_desc="A seed packet for an Aushucks Gaiaslimeoid. It costs 175 gaiaslime to !plant one, and has a 120 second cooldown.",
	# 	ingredients=[ewcfg.item_id_aushuckstalks],
	# 	enemytype="auschucks"
	# ),
	EwTombstone(
		id_item=ewcfg.item_id_tombstone_defaultshambler,
		cost=300,
		brainpower=30,
		stock=20,
		str_name="Default Shambler Tombstone",
		str_desc="A tombstone for a Default Shambler. If you use it in a graveyard op, it'll add a cooldown of 30 seconds.",
		enemytype="defaultshambler",
	),
	EwTombstone(
		id_item=ewcfg.item_id_tombstone_bucketshambler,
		cost=500,
		brainpower=45,
		stock=20,
		str_name="Bucket Shambler Tombstone",
		str_desc="A tombstone for a Bucket Shambler. If you use it in a graveyard op, it'll add a cooldown of 45 seconds.",
		enemytype="bucketshambler",
	),
	EwTombstone(
		id_item=ewcfg.item_id_tombstone_juveolanternshambler,
		cost=700,
		brainpower=60,
		stock=20,
		str_name="Juve-O'-Lantern Shambler Tombstone",
		str_desc="A tombstone for a Juve-O'-Lantern Shambler. If you use it in a graveyard op, it'll add a cooldown of 60 seconds.",
		enemytype="juveolanternshambler",
	),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_flagshambler,
	# 	cost=200,
	# 	brainpower=60,
	# 	stock=10,
	# 	str_name="Flag Shambler Tombstone",
	# 	str_desc="A tombstone for a Flag Shambler. If you use it in a graveyard op, it'll add a cooldown of 60 seconds.",
	# 	enemytype="flagshambler",
	# ),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_shambonidriver,
	# 	cost=300,
	# 	brainpower=90,
	# 	stock=10,
	# 	str_name="Shamboni Driver Tombstone",
	# 	str_desc="A tombstone for a Shamboni. If you use it in a graveyard op, it'll add a cooldown of 90 seconds.",
	# 	enemytype="shambonidriver",
	# ),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_mammoshambler,
	# 	cost=500,
	# 	brainpower=90,
	# 	stock=1,
	# 	str_name="Mammoshambler Tombstone",
	# 	str_desc="A tombstone for a Mammoshambler. Acts as an upgrade to the Shamboni Driver tombstone. If you use it in a graveyard op, it'll add a cooldown of 90 seconds.",
	# 	enemytype="mammoshambler",
	# ),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_gigashambler,
	# 	cost=500,
	# 	brainpower=180,
	# 	stock=3,
	# 	str_name="Gigashambler Tombstone",
	# 	str_desc="A tombstone for a Gigashambler. If you use it in a graveyard op, it'll add a cooldown of 180 seconds.",
	# 	enemytype="gigashambler",
	# ),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_microshambler,
	# 	cost=300,
	# 	brainpower=60,
	# 	stock=1,
	# 	str_name="Microshambler Tombstone",
	# 	str_desc="A tombstone for a Microshambler. Acts as an upgrade to the Gigashambler tombstone. If you use it in a graveyard op, it'll add a cooldown of 60 seconds.",
	# 	enemytype="microshambler",
	# ),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_shamblersaurusrex,
	# 	cost=800,
	# 	brainpower=180,
	# 	stock=1,
	# 	str_name="Shamblesaurus Rex Tombstone",
	# 	str_desc="A tombstone for a Shamblesaurus. If you use it in a graveyard op, it'll add a cooldown of 180 seconds.",
	# 	enemytype="shamblesaurusrex",
	# ),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_shamblerdactyl,
	# 	cost=200,
	# 	brainpower=90,
	# 	stock=5,
	# 	str_name="Shamblerdactyl Tombstone",
	# 	str_desc="A tombstone for a Shamblerdactyl. If you use it in a graveyard op, it'll add a cooldown of 90 seconds.",
	# 	enemytype="shamblerdactyl",
	# ),
	EwTombstone(
		id_item=ewcfg.item_id_tombstone_dinoshambler,
		cost=150,
		brainpower=60,
		stock=5,
		str_name="Dinoshambler Tombstone",
		str_desc="A tombstone for a Dinoshambler. If you use it in a graveyard op, it'll add a cooldown of 60 seconds.",
		enemytype="dinoshambler",
	),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_ufoshambler,
	# 	cost=200,
	# 	brainpower=120,
	# 	stock=5,
	# 	str_name="UFO Shambler Tombstone",
	# 	str_desc="A tombstone for a UFO Shambler. If you use it in a graveyard op, it'll add a cooldown of 120 seconds.",
	# 	enemytype="ufoshambler",
	# ),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_brawldenboomer,
	# 	cost=150,
	# 	brainpower=60,
	# 	stock=10,
	# 	str_name="Brawlden Boomer Tombstone",
	# 	str_desc="A tombstone for a Brawlden Boomer. If you use it in a graveyard op, it'll add a cooldown of 60 seconds.",
	# 	enemytype="brawldenboomer",
	# ),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_juvieshambler,
	# 	cost=250,
	# 	brainpower=60,
	# 	stock=15,
	# 	str_name="Juvie Shambler Tombstone",
	# 	str_desc="A tombstone for a Juvie Shambler. If you use it in a graveyard op, it'll add a cooldown of 60 seconds.",
	# 	enemytype="juvieshambler",
	# ),
	EwTombstone(
		id_item=ewcfg.item_id_tombstone_shambleballplayer,
		cost=400,
		brainpower=60,
		stock=20,
		str_name="Shambleball Player Tombstone",
		str_desc="A tombstone for a Shambleball Player. If you use it in a graveyard op, it'll add a cooldown of 60 seconds.",
		enemytype="shambleballplayer",
	),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_shamblerwarlord,
	# 	cost=400,
	# 	brainpower=180,
	# 	stock=5,
	# 	str_name="Shambler Warlord Tombstone",
	# 	str_desc="A tombstone for a Shambler Warlord. If you use it in a graveyard op, it'll add a cooldown of 180 seconds.",
	# 	enemytype="shamblerwarlord",
	# ),
	# EwTombstone(
	# 	id_item=ewcfg.item_id_tombstone_shamblerraider,
	# 	cost=500,
	# 	brainpower=120,
	# 	stock=1,
	# 	str_name="Shambler Raider Tombstone",
	# 	str_desc="A tombstone for a Shambler Raider. Acts as an upgrade to the Shambler Warlord tombstone. If you use it in a graveyard op, it'll add a cooldown of 120 seconds.",
	# 	enemytype="shamblerraider",
	# ),
]
#item_list += ewdebug.debugitem_set

#debugitem = ewdebug.debugitem

# A map of id_item to EwGeneralItem objects.
item_map = {}

# A list of item names
item_names = []

# Populate item map, including all aliases.
for item in item_list:
	item_map[item.id_item] = item
	item_names.append(item.id_item)

	for alias in item.alias:
		item_map[alias] = item

# list of dyes you're able to saturate your Slimeoid with
dye_list = []
dye_map = {}
# seperate the dyes from the other normal items
for c in item_list:

	if c.context != "dye":
		pass
	else:
		dye_list.append(c)
		dye_map[c.str_name] = c.id_item
		
seedpacket_ingredient_list = []
seedpacket_material_map = {}
seedpacket_enemytype_map = {}
seedpacket_ids = []
for sp in item_list:
	if sp.context == ewcfg.context_seedpacket:
		seedpacket_ingredient_list.append(sp.ingredients[0])
		seedpacket_material_map[sp.ingredients[0]] = sp.id_item
		seedpacket_enemytype_map[sp.id_item] = sp.enemytype
		seedpacket_ids.append(sp.id_item)

tombstone_enemytype_map = {}
tombstone_fullstock_map = {}
tombstone_ids = []
for ts in item_list:
	if ts.context == ewcfg.context_tombstone:
		tombstone_enemytype_map[ts.id_item] = ts.enemytype
		tombstone_fullstock_map[ts.enemytype] = ts.stock
		tombstone_ids.append(ts.id_item)

slimexodia_parts = []

# Gather all parts of slimexodia.
for slimexodia in item_list:
	if slimexodia.context == 'slimexodia':
		slimexodia_parts.append(slimexodia)
	else:
		pass

prank_items_heinous = [] # common
prank_items_scandalous = [] # uncommon
prank_items_forbidden = [] # rare
swilldermuk_food = []

# Gather all prank items
for p in item_list:
	if p.context == ewcfg.context_prankitem and p.rarity == ewcfg.prank_rarity_heinous:
		prank_items_heinous.append(p)
	else:
		pass
for p in item_list:
	if p.context == ewcfg.context_prankitem and p.rarity == ewcfg.prank_rarity_scandalous:
		prank_items_scandalous.append(p)
	else:
		pass
for p in item_list:
	if p.context == ewcfg.context_prankitem and p.rarity == ewcfg.prank_rarity_forbidden:
		prank_items_forbidden.append(p)
	else:
		pass

# Pity-pies will also spawn across the map.
# for p in food_list:
# 	if p.acquisition == "swilldermuk":
# 		swilldermuk_food.append(p)
# 	else:
# 		pass

furniture_list = []
with open(os.path.join('json', 'furniture.json')) as f:
	furniture = json.load(f)
	for i in furniture:
		i = furniture[i]
		furniture_list.append(
			EwFurniture(
				id_furniture = i['id_furniture'],
				str_name = i['str_name'],
				str_desc = i['str_desc'],
				rarity = i['rarity'],
				acquisition = i['acquisition'],
				price = i['price'],
				vendors = i['vendors'],
				furniture_place_desc = i['furniture_place_desc'],
				furniture_look_desc = i['furniture_look_desc'],
				furn_set = i['furn_set'],
				hue = i['hue'],
				num_keys = i['num_keys']
			))

furniture_map = {}
furniture_names = []
furniture_lgbt = []
furniture_highclass = []
furniture_haunted = []
furniture_leather = []
furniture_church = []
furniture_pony = []
furniture_blackvelvet = []
furniture_slimecorp = []
furniture_seventies = []
furniture_shitty = []
furniture_instrument = []
furniture_specialhue = []

for furniture in furniture_list:
	furniture_map[furniture.id_furniture] = furniture
	furniture_names.append(furniture.id_furniture)
	if furniture.furn_set == "haunted":
		furniture_haunted.append(furniture.id_furniture)
	elif furniture.furn_set == "high class":
		furniture_highclass.append(furniture.id_furniture)
	elif furniture.furn_set == "lgbt":
		furniture_lgbt.append(furniture.id_furniture)
	elif furniture.furn_set == "leather":
		furniture_leather.append(furniture.id_furniture)
	elif furniture.furn_set == "church":
		furniture_church.append(furniture.id_furniture)
	elif furniture.furn_set == "pony":
		furniture_pony.append(furniture.id_furniture)
	elif furniture.furn_set == "blackvelvet":
		furniture_blackvelvet.append(furniture.id_furniture)
	elif furniture.furn_set == "seventies":
		furniture_seventies.append(furniture.id_furniture)
	elif furniture.furn_set == "slimecorp":
		furniture_slimecorp.append(furniture.id_furniture)
	elif furniture.furn_set == "shitty":
		furniture_shitty.append(furniture.id_furniture)
	elif furniture.furn_set == "instrument":
		furniture_instrument.append(furniture.id_furniture)
	elif furniture.furn_set == "specialhue":
		furniture_specialhue.append(furniture.id_furniture)
