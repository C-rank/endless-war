import asyncio

from ew.static import cfg as ewcfg
from ew.static import poi as poi_static
from ew.utils import core as ewutils
from ew.utils import frontend as fe_utils
from ew.utils import rolemgr as ewrolemgr
from ew.utils.combat import EwUser
from ew.utils.district import EwDistrict

"""
	Informs the player about their current zone's capture progress
"""


async def capture_progress(cmd):
    user_data = EwUser(member=cmd.message.author)
    response = ""

    poi = poi_static.id_to_poi.get(user_data.poi)
    response += "**{}**: ".format(poi.str_name)

    if not user_data.poi in poi_static.capturable_districts:
        response += "This zone cannot be captured."
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    district_data = EwDistrict(id_server=user_data.id_server, district=user_data.poi)

    if district_data.controlling_faction != "":
        response += "{} control this district. ".format(district_data.controlling_faction.capitalize())
    elif district_data.capturing_faction != "" and district_data.cap_side != district_data.capturing_faction:
        response += "{} are de-capturing this district. ".format(district_data.capturing_faction.capitalize())
    elif district_data.capturing_faction != "":
        response += "{} are capturing this district. ".format(district_data.capturing_faction.capitalize())
    else:
        response += "Nobody has staked a claim to this district yet."

    response += "\n\n**Current influence: {:,}**\nMinimum influence: {:,}\nMaximum influence: {:,}\nPercentage to maximum influence: {:,}%".format(abs(district_data.capture_points), int(ewcfg.min_influence[district_data.property_class]), int(ewcfg.limit_influence[district_data.property_class]),
                                                                                                                                                   round((abs(district_data.capture_points) * 100 / (ewcfg.limit_influence[district_data.property_class])), 1))

    # if district_data.time_unlock > 0:

    # response += "\nThis district cannot be captured currently. It will unlock in {}.".format(ewutils.formatNiceTime(seconds = district_data.time_unlock, round_to_minutes = True))
    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


# Old capping CMD
"""async def annex(cmd):
	user_data = EwUser(member = cmd.message.author)
	if user_data.life_state == ewcfg.life_state_shambler:
		response = "You lack the higher brain functions required to {}.".format(cmd.tokens[0])
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	response = ""
	resp_cont = ewutils.EwResponseContainer(id_server = cmd.guild.id)
	time_now = int(time.time())

	poi = poi_static.id_to_poi.get(user_data.poi)

	if user_data.life_state == ewcfg.life_state_corpse:
		response = "You ineffectively try shaking your can of spraypaint to whip up some sick graffiti. Alas, you’re all outta slime. " \
                   "They should really make these things compatible with ectoplasm."
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	if not (len(user_data.faction) > 0 and user_data.life_state == ewcfg.life_state_enlisted):
		response = "Juveniles are too chickenshit to make graffiti and risk getting busted by the cops. Fuckin’ losers."
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	if user_data.poi in [ewcfg.poi_id_rowdyroughhouse, ewcfg.poi_id_copkilltown]:
		response = "There’s no point, the rest of your gang has already covered this place in spraypaint. Focus on exporting your graffiti instead."
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	if user_data.poi == ewcfg.poi_id_juviesrow:
		response = "Nah, the Rowdys and Killers have both agreed this is neutral ground. You don’t want to start a diplomatic crisis, " \
                   "just stick to spraying down sick graffiti and splattering your rival gang across the pavement in the other districts."
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	if not user_data.poi in poi_static.capturable_districts:
		response = "This zone cannot be captured."
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	district_data = EwDistrict(id_server = user_data.id_server, district = user_data.poi)


	if district_data.is_degraded():
		response = "{} has been degraded by shamblers. You can't {} here anymore.".format(poi.str_name, cmd.tokens[0])
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
	if district_data.time_unlock > 0:
		response = "You can’t spray graffiti here yet, it’s too soon after your rival gang extended their own cultural dominance over it. Try again in {}.".format(ewutils.formatNiceTime(seconds = district_data.time_unlock, round_to_minutes = True))
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	if district_data.all_neighbors_friendly():
		response = "What the hell are you doing, dude? You can’t put down any graffiti here, it’s been completely overrun by your rival gang. " \
                   "You can only spray districts that have at least one unfriendly neighbor, duh!"
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	users_in_district = district_data.get_players_in_district(
		life_states = [ewcfg.life_state_enlisted],
		ignore_offline = True,
		pvp_only = True
	)

	allies_in_district = district_data.get_players_in_district(
		factions = [user_data.faction],
		life_states = [ewcfg.life_state_enlisted],
		ignore_offline = True,
		pvp_only = True
	)

	if len(users_in_district) > len(allies_in_district):
		response = "Holy shit, deal with your rival gangsters first! You can’t spray graffiti while they’re on the prowl!"
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	mutations = user_data.get_mutations()

	slimes_spent = ewutils.getIntToken(tokens = cmd.tokens, allow_all = True)
	capture_discount = 1

	if ewcfg.mutation_id_lonewolf in mutations:
		if user_data.time_expirpvp > time_now:
			if len(users_in_district) == 1:
				capture_discount *= 0.8
		else:
			if len(users_in_district) == 0:
				capture_discount *= 0.8

	if ewcfg.mutation_id_patriot in mutations:
		capture_discount *= 0.8

	if slimes_spent == None:
		response = "How much slime do you want to spend on spraying graffiti in this district?"
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	if slimes_spent < 0:
		slimes_spent = user_data.slimes

	if slimes_spent > user_data.slimes:
		response = "You don't have that much slime, retard."
		return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

	num_lock = len(allies_in_district)
	if user_data.time_expirpvp < time_now:
		num_lock += 1

	if (district_data.controlling_faction not in ["", user_data.faction]) or (district_data.capturing_faction not in ["", user_data.faction]):
		slimes_decap = min(district_data.capture_points, int(slimes_spent / capture_discount))
		decap_resp = district_data.change_capture_points(
			progress = -slimes_decap,
			actor = user_data.faction,
			num_lock = num_lock
		)
		resp_cont.add_response_container(decap_resp)

		user_data.change_slimes(n = -slimes_decap * capture_discount, source = ewcfg.source_spending)
		slimes_spent -= slimes_decap * capture_discount

	slimes_cap = min(district_data.max_capture_points - district_data.capture_points, int(slimes_spent / capture_discount))
	cap_resp = district_data.change_capture_points(
		progress = slimes_cap,
		actor = user_data.faction,
		num_lock = num_lock
	)
	resp_cont.add_response_container(cap_resp)

	user_data.change_slimes(n = -slimes_cap * capture_discount, source = ewcfg.source_spending)

	# Flag the user for PvP
	# user_data.time_expirpvp = ewutils.calculatePvpTimer(user_data.time_expirpvp, ewcfg.time_pvp_annex, True)

	user_data.persist()
	district_data.persist()
	await ewrolemgr.updateRoles(client = cmd.client, member = cmd.message.author)

	return await resp_cont.post()
"""


async def change_spray(cmd):
    user_data = EwUser(member=cmd.message.author)
    newspray = cmd.message.content[(len(ewcfg.cmd_changespray)):].strip()

    if newspray == "":
        response = "You need to add an image link to change your spray."
    elif len(newspray) > 400:
        response = "Fucking christ, are you painting the Sistine Chapel? Use a shorter link."
    else:
        response = "Got it. Spray set."
        user_data.spray = newspray
        user_data.persist()

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def tag(cmd):
    user_data = EwUser(member=cmd.message.author)

    if user_data.life_state in (ewcfg.life_state_enlisted, ewcfg.life_state_kingpin):
        response = user_data.spray
    else:
        response = "Save the spraying for the gangsters. You're either too gay or dead to participate in this sort of thing."
    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
