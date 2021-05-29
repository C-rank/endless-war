import random

from . import cfg as ewcfg
from ..model.hunting import EwAttackType


# Attacking type effects
def atf_fangs(ctn = None):
	# Reskin of dual pistols

	aim = (random.randrange(10) + 1)
	#ctn.sap_damage = 1

	if aim == (1 + int(10 * ctn.hit_chance_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0
	elif aim == (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_talons(ctn = None):
	# Reskin of katana

	ctn.miss = False
	ctn.slimes_damage = int(0.85 * ctn.slimes_damage)
	#ctn.sap_damage = 0
	#ctn.sap_ignored = 10

	if (random.randrange(10) + 1) == (10 + int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2.1

def atf_raiderscythe(ctn = None):
	# Reskin of scythe

	ctn.enemy_data.change_slimes(n = (-ctn.slimes_spent * 0.33), source = ewcfg.source_self_damage)
	ctn.slimes_damage = int(ctn.slimes_damage * 1.25)
	aim = (random.randrange(10) + 1)
	#ctn.sap_damage = 0
	#ctn.sap_ignored = 5

	if aim <= (2 + int(10 * ctn.hit_chance_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0
	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_gunkshot(ctn = None):
	# Reskin of rifle

	aim = (random.randrange(10) + 1)
	#ctn.sap_damage = 2

	if aim <= (2 + int(10 * ctn.hit_chance_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0
	elif aim >= (9 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_tusks(ctn = None):
	# Reskin of bat

	aim = (random.randrange(21) - 10)
	#ctn.sap_damage = 3
	if aim <= (-9 + int(21 * ctn.hit_chance_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0

	ctn.slimes_damage = int(ctn.slimes_damage * (1 + (aim / 10)))

	if aim >= (9 - int(21 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage = int(ctn.slimes_damage * 1.5)

def atf_molotovbreath(ctn = None):
	# Reskin of molotov

	dmg = ctn.slimes_damage
	ctn.slimes_damage = int(ctn.slimes_damage * 0.75)
	#ctn.sap_damage = 0
	#ctn.sap_ignored = 10

	aim = (random.randrange(10) + 1)

	#ctn.bystander_damage = dmg * 0.5

	if aim == (3 + int(10 * ctn.hit_chance_mod)):
		ctn.miss = True
		ctn.slimes_damage = 0

	elif aim == (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2

def atf_armcannon(ctn = None):
	dmg = ctn.slimes_damage
	#ctn.sap_damage = 2

	aim = (random.randrange(20) + 1)

	if aim <= (2 + int(20 * ctn.hit_chance_mod)):
		ctn.miss = True

	if aim == (20 - int(20 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 3


def atf_axe(ctn=None):
	ctn.slimes_damage *= 0.7
	aim = (random.randrange(10) + 1)

	if aim <= (4 + int(10 * ctn.hit_chance_mod)):
		ctn.miss = True

	if aim == (10 - int(10 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2


def atf_hooves(ctn=None):
	ctn.slimes_damage *= 0.4
	aim = (random.randrange(30) + 1)

	if aim <= (5 + int(30 * ctn.hit_chance_mod)):
		ctn.miss = True

	if aim > (25 - int(30 * ctn.crit_mod)):
		ctn.crit = True
		ctn.slimes_damage *= 2
		
def atf_body(ctn=None):
	ctn.slimes_damage *= 0.5
	aim = (random.randrange(10) + 1)

	if aim <= 2:
		ctn.miss = True

	if aim == 10:
		ctn.crit = True
		ctn.slimes_damage *= 2
def atf_smallclaws(ctn=None):
	chance = random.randrange(3)
	if chance <= 1:
		ctn.miss = True
	if chance == 2:
		strikes = random.randrange(5)
		ctn.strikes = strikes
		ctn.slimes_damage *= 0.05
	if chance == 3:
		ctn.slimes_damage *= 0.3
		ctn.crit = True
def atf_gvs_basic(ctn=None):
	pass

# All enemy attacking types in the game.
enemy_attack_type_list = [
	EwAttackType( # 1
		id_type = "fangs",
		str_crit = "**Critical Hit!** {name_enemy} sinks their teeth deep into {name_target}!",
		str_miss = "**{name_enemy} missed!** Their maw snaps shut!",
		#str_trauma_self = "You have bite marks littered throughout your body.",
		#str_trauma = "They have bite marks littered throughout their body.",
		str_kill = "{name_enemy} opens their jaw for one last bite right on {name_target}'s juicy neck. **CHOMP**. Blood gushes out of their arteries and onto the ground. {emote_skull}",
		str_killdescriptor = "mangled",
		str_damage = "{name_target} is bitten on the {hitzone}!!",
		fn_effect = atf_fangs
	),
	EwAttackType( # 2
		id_type = "talons",
		str_crit = "**Critical hit!!** {name_target} is slashed across the chest!!",
		str_miss = "**{name_enemy} missed!** Their wings flap in the air as they prepare for another strike!",
		#str_trauma_self = "A large section of scars litter your abdomen.",
		#str_trauma = "A large section of scars litter their abdomen.",
		str_kill = "In a fantastic display of avian savagery, {name_enemy}'s talons grip {name_target}'s stomach, rip open their flesh and tear their intestines to pieces. {emote_skull}",
		str_killdescriptor = "disembowled",
		str_damage = "{name_target} has their {hitzone} clawed at!!",
		fn_effect = atf_talons
	),
	EwAttackType( # 3
		id_type = "scythe",
		str_crit = "**Critical hit!!** {name_target} is carved by the wicked curved blade!",
		str_miss = "**MISS!!** {name_enemy}'s swings miss wide of the target!",
		#str_trauma_self = "You are wrapped tightly in bandages that hold your two halves together.",
		#str_trauma = "They are wrapped tightly in bandages that hold their two halves together.",
		str_kill = "**SLASHH!!** {name_enemy}'s scythe cleaves the air, and {name_target} staggers. A moment later, {name_target}'s torso topples off their waist. {emote_skull}",
		str_killdescriptor = "sliced in twain",
		str_damage = "{name_target} is cleaved through the {hitzone}!!",
		fn_effect = atf_raiderscythe
	),
	EwAttackType( # 4
		id_type = "gunkshot",
		str_crit = "**Critical hit!!** {name_target} is covered in a thick, gelatenous ooze!",
		str_miss = "**MISS!!** {name_enemy}'s gunk shot just barely missed the target!",
		#str_trauma_self = "Several locations on your body have decayed from the aftermath of horrific radiation.",
		#str_trauma = "Several locations on their body have decayed from the aftermath of horrific radiation.",
		str_kill = "**SPLOOSH!!** {name_enemy}'s gunk shot completely envelops {name_target}, boiling their flesh alive in a radiation that rivals the Elephant's Foot. Nothing but a charred husk remains. {emote_skull}",
		str_killdescriptor = "slimed on",
		str_damage = "{name_target} is coated in searing, acidic radiation on their {hitzone}!!",
		fn_effect = atf_gunkshot
	),
	EwAttackType( # 5
		id_type = "tusks",
		str_crit = "**Critical hit!!** {name_target} is smashed hard by {name_enemy}'s tusks!",
		str_miss = "**{name_enemy} missed!** Their tusks strike the ground, causing it to quake underneath!",
		#str_trauma_self = "You have one large scarred-over hole on your upper body.",
		#str_trauma = "They have one large scarred-over hole on their upper body.",
		str_kill = "**SHINK!!** {name_enemy}'s tusk rams right into your chest, impaling you right through your back! Moments later, you're thrusted out on to the ground, left to bleed profusely. {emote_skull}",
		str_killdescriptor = "pierced",
		str_damage = "{name_target} has tusks slammed into their {hitzone}!!",
		fn_effect = atf_tusks
	),
	EwAttackType( # 6
		id_type = "molotovbreath",
		# str_backfire = "**Oh the humanity!!** {name_enemy} tries to let out a breath of fire, but it combusts while still inside their maw!!",
		str_crit = "**Critical hit!!** {name_target} is char grilled by {name_enemy}'s barrage of molotov breath!",
		str_miss = "**{name_enemy} missed!** Their shot hits the ground instead, causing embers to shoot out in all directions!",
		#str_trauma_self = "You're wrapped in two layers of bandages. What skin is showing appears burn-scarred.",
		#str_trauma = "They're wrapped in two layers of bandages. What skin is showing appears burn-scarred.",
		str_kill = "In a last ditch effort, {name_enemy} breathes in deeply for an extra powerful shot of fire. Before you know it, your body is cooked alive like a rotisserie chicken. {emote_skull}",
		str_killdescriptor = "exploded",
		str_damage = "{name_target} is hit by a blast of fire on their {hitzone}!!",
		fn_effect = atf_molotovbreath
	),
	EwAttackType( # 7
		id_type = "armcannon",
		str_crit = "**Critical hit!!** {name_target} has a clean hole shot through their chest by {name_enemy}'s bullet!",
		str_miss = "**{name_enemy} missed their target!** The stray bullet cleaves right into the ground!",
		#str_trauma_self = "There's a deep bruising right in the middle of your forehead.",
		#str_trauma = "There's a deep bruising right in the middle of their forehead.",
		str_kill = "{name_enemy} readies their crosshair right for your head and fires without hesitation. The force from the bullet is so powerful that when it lodges itself into your skull, it rips your head right off in the process. {emote_skull}",
		str_killdescriptor = "sniped",
		str_damage = "{name_target} has a bullet zoom right through their {hitzone}!!",
		fn_effect = atf_armcannon
	),
	EwAttackType( # 8
		id_type = "axe",
		str_crit = "**Critical hit!!** {name_target} is thoroughly cleaved by {name_enemy}'s axe!",
		str_miss = "**{name_enemy} missed!** The axe gives a loud **THUD** as it strikes the earth!",
		#str_trauma_self = "There's a hefty amount of bandages covering the top of your head",
		#str_trauma = "There's a hefty amount of bandages covering the top of their head",
		str_kill = "{name_enemy} lifts up their axe for one last swing. The wicked edge buries itself deep into your skull, cutting your brain in twain. {emote_skull}",
		str_killdescriptor = "axed",
		str_damage = "{name_target} is swung at right on their {hitzone}!!",
		fn_effect = atf_axe
	),
	EwAttackType( # 9
		id_type = "hooves",
		str_crit = "**Critical hit!!** {name_enemy} lays a savage hind-leg kick into {name_target}'s chest!",
		str_miss = "**WHOOSH!** {name_enemy}'s hooves just barely miss you!",
		#str_trauma_self = "Your chest is somewhat concave.",
		#str_trauma = "Their chest is somewhat concave.",
		str_kill = "{name_enemy} gallops right over your head, readying their hind legs just after landing. Before you can even ready your weapon, their legs are already planted right onto your chest. Your heart explodes. {emote_skull}",
		str_killdescriptor = "stomped",
		str_damage = "{name_target} is stomped all over their {hitzone}!!",
		fn_effect = atf_hooves
	),
	EwAttackType( # 10
		id_type = "body",
		str_crit = "**OOF!!** {name_enemy} lands a critical strike onto {name_target}'s torso with the sheer impact of their body weight!",
		str_miss = "**MISS!** {name_enemy} flails their body around to try and attack {name_target}, but nothing happens...",
		#str_trauma_self = "Your have deep bruising on your torso.",
		#str_trauma = "They have deep bruising on their torso.",
		str_kill = "{name_enemy} throws every once of force they can at you with your body. The impact is so strong that you're slammed into the ground, shattering your skull. {emote_skull}",
		str_killdescriptor = "pushed around",
		str_damage = "{name_target} gets bumped around a bit on their {hitzone}!",
		fn_effect = atf_body
	),
	EwAttackType(  # 11
		id_type="amateur",
		str_crit="**AIIIIEEE!!** {name_enemy} screams in abject fear, lunging at {name_target}'s with a {civ_weapon} in hand! Fuck, they actually got you!",
		str_miss="**MISS!** {name_enemy} trips and falls facefirst on the ground. {name_target} is holding back their laughter at how goddamn stupid this all is.",
		# str_trauma_self = "Your have deep bruising on your torso.",
		# str_trauma = "They have deep bruising on their torso.",
		str_kill="{name_enemy} is thrown into an adrenaline rush! They brandish their {civ_weapon} and throw it in a perfect spiral, directly through {name_target}'s skull. {emote_skull}",
		str_killdescriptor="felled",
		str_damage="{name_enemy} bludgeons {name_target} in the {hitzone}! At least they try to...",
		fn_effect=atf_body
	),
	EwAttackType(  # 11
		id_type="stomp",
		str_crit="**OH FUCK!** The titanoslime reels back onto its hind legs, stomping {name_target} deeper and deeper into the asphalt!",
		str_miss="**MISS!** {name_target} jumps barely out of the way of a stomp!",
		# str_trauma_self = "Your have deep bruising on your torso.",
		# str_trauma = "They have deep bruising on their torso.",
		str_kill="**CRUNCH!!** The titanoslime locks its teeth into your flesh, snapping you clean in half and swallowing all but your legs! You can feel the creatures stomach acid stinging on your face before you rapidly lose consciousness.{emote_skull}",
		str_killdescriptor="vored",
		str_damage="{name_enemy} swings it's car width legs full speed into {name_target}!",
		fn_effect=atf_tusks
	),
	EwAttackType(  # 11
		id_type="stompn6",
		str_crit="**YIPPIE KI YAY MOTHER FUCKERS!!!** N6 pulls back the reins, reeling the Titanoslime up and stomping {name_target} deeper and deeper into the asphalt!",
		str_miss="**MISS!** {name_target} jumps barely out of the way of a stomp! You can hear N6 cursing from atop her steed.",
		# str_trauma_self = "Your have deep bruising on your torso.",
		# str_trauma = "They have deep bruising on their torso.",
		str_kill="N6 pulls out some kind of laser pistol and aims it directly at you. **FOOM!** You don't see the next moment because your eyes are now a fine powder. You bleed out the sockets for a few minutes before collapsing dead in the street.{emote_skull}",
		str_killdescriptor="disintegrated",
		str_damage="{name_enemy} swings it's car width legs full speed into {name_target}! N6 laughs and watches you eat shit on the pavement!",
		fn_effect=atf_tusks
	),
	EwAttackType(  # 12
		id_type="gnash",
		str_crit="**GNASH GNASH GNASH!!!** The {name_enemy} opens it's mouth as wide it can go and chomps down on {name_target}! OOF!",
		str_miss="**MISS!** {name_target} barely sidesteps the {name_enemy}'s lunging bite!",
		str_kill="**GNASH!!!** The {name_enemy} catches you in it's mouth and flails you around a little, for effect. The world fades from view as the venom takes over. {emote_skull}",
		str_killdescriptor="gnashed",
		str_damage="{name_enemy} chomps into {name_target}! {name_target} is looking a little woozy!",
		fn_effect=atf_fangs
	),
	EwAttackType(  # 13
		id_type="beak",
		str_crit="**PECK PECK PECK!!!** The {name_enemy} rips you to shreds! {name_target} is bleeding profusely!",
		str_miss="**SWOOSH!** {name_target} barely misses {name_enemy} and swoops around for another shot!",
		str_kill="**PECK PECK!!!** The {name_enemy} swoops at you with malice in their eyes. {name_target} never had a chance as their skin is ripped off, piece by piece. {emote_skull}",
		str_killdescriptor="pecked",
		str_damage="{name_enemy} pecks at {name_target}! They draw blood!",
		fn_effect=atf_talons
	),
	# If str_trauma and str_trauma_self make a return, consider filling GvS attacktypes out in these attributes.
	EwAttackType( # GvS - 1
		id_type = "g_seeds",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s seeds completely miss {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "{name_enemy}'s seeds land right inside {name_target}'s skull, killing them instantly. {emote_skull}",
		str_killdescriptor = "seeded",
		str_damage = "{name_target} is pummeled with seeds on their {hitzone}!",
		str_groupattack = "{name_target} pummels a whole group of shamblers with their seeds!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 1.5
			id_type = "g_appleacid",
			str_crit = "NULL",
			str_miss = "**MISS!** {name_enemy}'s acid completely misses {name_target}!",
			#str_trauma_self = "NULL", 
			#str_trauma = "NULL,
			str_kill = "{name_enemy} hurls a glob of acid straight onto {name_target}'s chest, melting down their insides. {emote_skull}",
			str_killdescriptor = "melted down to the bone",
			str_damage = "{name_target} is drenched with acid on their {hitzone}!",
			str_groupattack = "{name_target} drenches a group of shamblers with their acid!",
			fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 2
		id_type = "g_bloodshot",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s bloodshot dissipates in mid-air as it fails to seek out {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "{name_enemy} turns {name_target} into a shriveled up husk! {emote_skull}",
		str_killdescriptor = "drained",
		str_damage = "{name_target} has their life essence drained away by {name_enemy}!",
		str_groupattack = "{name_enemy} sucks the life force out of a group of shamblers!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 3
		id_type = "g_nuts",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s nuts don't even come close to hitting {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "{name_enemy}'s nuts knock {name_target}'s head clean off! {emote_skull}",
		str_killdescriptor = "conked on the head",
		str_damage = "{name_enemy}'s nuts bonk {name_target} on their {hitzone}!",
		str_groupattack = "{name_enemy}'s nuts richochet off of a group of shamblers!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 4
		id_type = "g_chompers",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s gaping maw snaps shut!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**CHOMP!** {name_enemy} devours {name_target}, killing them instantly. {emote_skull}",
		str_killdescriptor = "chomped",
		str_damage = "{name_enemy}'s chompers take a bite out of {name_target}!",
		str_groupattack = "{name_enemy} is running wild!! Their chompers lay waste to a group of shamblers!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 5
		id_type = "g_fists",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy} thrashes about, but fails to hit {name_target}.",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "{name_enemy} deals a devastating strike to {name_target}! The impact causes their heart to stop. {emote_skull}",
		str_killdescriptor = "punched to death",
		str_damage = "{name_enemy}'s fists deal savage blows to {name_target}!",
		str_groupattack = "{name_enemy} rushes down a group of shamblers with their fists!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 6
		id_type = "g_brainwaves",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s Binaural Brainwaves completely miss {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "{name_enemy} hypnotizes {name_target} into walking off of the Slime's End cliffs. {emote_skull}",
		str_killdescriptor = "mind broken",
		str_damage = "{name_enemy}'s Binaural Brainwaves give {name_target} a massive headache!",
		str_groupattack = "{name_enemy} is firing on all cylinders! Their Binaural Brainwaves impact multiple shamblers!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 7
		id_type = "g_vapecloud",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_target} completely avoids {name_enemy}'s vape cloud!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "{name_target} has inhaled too much of {name_enemy}'s toxic vape cloud! {emote_skull}",
		str_killdescriptor = "vaped to death",
		str_damage = "{name_enemy} completely covers {name_target} in a toxic vape cloud!",
		str_groupattack = "{name_enemy} spreads its toxic vape cloud to a group of shamblers!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 8
		id_type = "g_hotbox",
		str_crit = "NULL",
		str_miss = "**MISS!** weed",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = " {emote_skull}",
		str_killdescriptor = "forced to smoke too much weed",
		str_damage = "weed",
		str_groupattack = "weed",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 9
		id_type = "g_blades",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_target} manages to avoid getting cut on {name_enemy}'s blades!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**SHINK!!** {name_enemy}'s blades sink deep into {name_target}! {emote_skull}",
		str_killdescriptor = "cut and stabbed",
		str_damage = "{name_enemy} cuts {name_target} with their sharpened blades!",
		str_groupattack = "{name_enemy} slices and dices a group of shamblers with their blades!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 10
		id_type = "g_explosion",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s explosion doesn't even come close to hitting {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**KABOOM!!** {name_enemy} sacrifices itself to blow {name_target} apart! {emote_skull}",
		str_killdescriptor = "blown to smithereens",
		str_damage = "*BOOM!* {name_enemy}'s explosion puts a dent into {name_target}!",
		str_groupattack = "{name_enemy} takes down a group of shamblers with it!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 11
		id_type = "s_shamboni",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy} drives right past {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "{name_enemy}'s wheels completely flatten {name_target}! {emote_skull}",
		str_killdescriptor = "run over",
		str_damage = "{name_enemy}'s wheels run over {name_target}!",
		str_groupattack = "{name_enemy} runs over a group of gaiaslimeoids!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 12
		id_type = "s_teeth",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s bite doesn't even graze {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**CRUNCH!** {name_enemy} devours {name_target} with their teeth! {emote_skull}",
		str_killdescriptor = "bitten all over",
		str_damage = "{name_enemy} bites {name_target} on their {hitzone}!",
		str_groupattack = "{name_enemy}'s appetite knows no bounds! They bite into several gaiaslimeoids!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 13
		id_type = "s_tusks",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_targets}'s tusks fail to hit {name_target}, and give a loud *THUD* as they strike the ground!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**SLAM!** {name_target} is flattened by {name_enemy}'s tusks. {emote_skull}",
		str_killdescriptor = "slammed into the ground",
		str_damage = "{name_enemy} bashes {name_target}'s {hitzone} with their tusks!",
		str_groupattack = "{name_enemy} slams its tusks into several gaiaslimeoids!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 14
		id_type = "s_fangs",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s jaws snap shut! It failed to eat {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**GULP!** {name_enemy} swallows {name_target} whole! {emote_skull}",
		str_killdescriptor = "vored to death",
		str_damage = "",
		str_groupattack = "NULL",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 15
		id_type = "s_talons",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy} couldn't get a grip on {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**YOINK!** {name_enemy} picks up {name_target} and carries them off into the sunset... {emote_skull}",
		str_killdescriptor = "spirited away",
		str_damage = "**SLASH!** {name_enemy} couldn't carry {name_target} away, but scratched them up nonetheless!",
		str_groupattack = "{name_enemy} attacks a group of gaiaslimeoids with their talons!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 16
		id_type = "s_molotovbreath",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_target} managed to avoid {name_enemy}'s hellfire!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**FWOOOOOOOSHHHHH!!** {name_enemy} burns {name_target} to a crisp! {emote_skull}",
		str_killdescriptor = "burnt to ash",
		str_damage = "{name_enemy} spits a ball of fire at {name_target} and burns their {hitzone}!",
		str_groupattack = "{name_enemy} absolutely incinerates a group of gaiaslimeoids with their molotov breath!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 17
		id_type = "s_cudgel",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s cudgel misses {name_target} and goes down with a *THUD*.",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**OOF!!** {name_enemy}'s cudgel whacks {name_target} so hard, it buries them far beneath the ground. {emote_skull}",
		str_killdescriptor = "flattened",
		str_damage = "**BAM!** {name_enemy} strikes {name_target}'s {hitzone} with their cudgel!",
		str_groupattack = "NULL",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 18
		id_type = "s_raiderscythe",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy}'s scythe breezes past {name_target}!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "{name_enemy} cleaves {name_target} in two. {emote_skull}",
		str_killdescriptor = "cut in twain",
		str_damage = "{name_enemy} slices {name_target} with its scythe!",
		str_groupattack = "{name_enemy} slashes a group of gaiaslimeoids with its scythe!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType( # GvS - 19
		id_type = "s_grenadecannon",
		str_crit = "NULL",
		str_miss = "**MISS!** {name_enemy} couldn't land a hit on {name_target} with its grenade cannon!",
		#str_trauma_self = "NULL", 
		#str_trauma = "NULL,
		str_kill = "**KABAM!!** {name_enemy}'s grenade cannon lands a direct hit on {name_target}! {emote_skull}",
		str_killdescriptor = "blown apart",
		str_damage = "{name_target} is caught in the blast zone of {name_enemy}'s grenades!",
		str_groupattack = "{name_enemy} blows up a group of gaiaslimeoids with its grenades!",
		fn_effect = atf_gvs_basic
	),
	EwAttackType(  #
		id_type="titanoslime",
		str_crit="NULL",
		str_miss="**MISS!** {name_target} barely jumps out of the way of {name_enemy}'s foot!",
		# str_trauma_self = "NULL",
		# str_trauma = "NULL,
		str_kill="**WRYYYYYYYY!!!!!** {name_enemy}'s collossal jowls slice {name_target} completely in half! As they lose conciousness, {name_target} can feel the burn of the acid on their face as they sink helplessly into its churning stomach. {emote_skull}",
		str_killdescriptor="vored",
		str_damage="{name_target} takes the brunt of {name_enemy}'s stomp!",
		str_groupattack="{name_enemy} tailsweeps a horde of gaiaslimeoids!",
		fn_effect=atf_tusks
	),
]

# A map of id_type to EwAttackType objects.
attack_type_map = {}

# Populate attack type map.
for attack_type in enemy_attack_type_list:
	attack_type_map[attack_type.id_type] = attack_type
