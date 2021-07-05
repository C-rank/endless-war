import asyncio
import random
import sys
import time

from ew.backend import item as bknd_item
from ew.backend import core as bknd_core
from ew.backend import hunting as bknd_hunt
from ew.backend import worldevent as bknd_worldevent

from ew.backend.item import EwItem
from ew.backend.hunting import EwOperationData
from ew.backend.worldevent import EwWorldEvent

from ew.static import cfg as ewcfg
from ew.static import items as static_items
from ew.static import poi as poi_static


from ew.utils import frontend as fe_utils
from ew.utils import core as ewutils
from ew.utils import hunting as hunt_utils
from ew.utils import item as itm_utils
from ew.utils import rolemgr as ewrolemgr


from ew.utils.combat import EwEnemy
from ew.utils.combat import EwUser
from ew.utils.district import EwDistrict

"""
    GVS COMMANDS
"""


async def gvs_print_grid(cmd):
    author = cmd.message.author
    user_data = EwUser(member=author)

    grid_map = hunt_utils.gvs_create_gaia_grid_mapping(user_data)

    debug = False
    if debug:
        blue_blank = ':blue_heart:'
        green_lawn = ':green_heart:'
        lime_lawn = ':yellow_heart:'
    else:
        blue_blank = ewcfg.emote_blankregional
        green_lawn = ewcfg.emote_greenlawn
        lime_lawn = ewcfg.emote_limelawn

    emote_set = []
    # print(grid_map)

    green_or_lime = lime_lawn
    for row in ewcfg.gvs_valid_coords_gaia:
        for coord in row:

            if green_or_lime == lime_lawn:
                green_or_lime = green_lawn
            else:
                green_or_lime = lime_lawn

            if coord in grid_map.keys():
                emote = ewcfg.gvs_enemy_emote_map[grid_map[coord]]

                if debug:
                    emote = ewcfg.gvs_enemy_emote_map_debug[grid_map[coord]]

                emote_set.append(emote)
            else:
                emote_set.append(green_or_lime)

    printed_grid_row_0 = "\n{}{}{}{}{}{}{}{}{}{}".format(
        blue_blank,
        ':one:',
        ':two:',
        ':three:',
        ':four:',
        ':five:',
        ':six:',
        ':seven:',
        ':eight:',
        ':nine:'
    )

    printed_grid_row_1 = "\n{}{}{}{}{}{}{}{}{}{}".format(
        ':regional_indicator_a:',
        emote_set[0],
        emote_set[1],
        emote_set[2],
        emote_set[3],
        emote_set[4],
        emote_set[5],
        emote_set[6],
        emote_set[7],
        emote_set[8],
    )

    printed_grid_row_2 = "\n{}{}{}{}{}{}{}{}{}{}".format(
        ':regional_indicator_b:',
        emote_set[9],
        emote_set[10],
        emote_set[11],
        emote_set[12],
        emote_set[13],
        emote_set[14],
        emote_set[15],
        emote_set[16],
        emote_set[17],
    )

    printed_grid_row_3 = "\n{}{}{}{}{}{}{}{}{}{}".format(
        ':regional_indicator_c:',
        emote_set[18],
        emote_set[19],
        emote_set[20],
        emote_set[21],
        emote_set[22],
        emote_set[23],
        emote_set[24],
        emote_set[25],
        emote_set[26],
    )

    printed_grid_row_4 = "\n{}{}{}{}{}{}{}{}{}{}".format(
        ':regional_indicator_d:',
        emote_set[27],
        emote_set[28],
        emote_set[29],
        emote_set[30],
        emote_set[31],
        emote_set[32],
        emote_set[33],
        emote_set[34],
        emote_set[35],
    )

    printed_grid_row_5 = "\n{}{}{}{}{}{}{}{}{}{}".format(
        ':regional_indicator_e:',
        emote_set[36],
        emote_set[37],
        emote_set[38],
        emote_set[39],
        emote_set[40],
        emote_set[41],
        emote_set[42],
        emote_set[43],
        emote_set[44],
    )

    full_grid_response = printed_grid_row_0 + printed_grid_row_1 + printed_grid_row_2 + printed_grid_row_3 + printed_grid_row_4 + printed_grid_row_5
    # print('Grid response length: {}'.format(len(full_grid_response)))

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, full_grid_response))


async def gvs_print_lane(cmd):
    author = cmd.message.author
    user_data = EwUser(member=author)

    debug = False

    response = ""
    if cmd.tokens_count != 2:
        response = "Which lane do you want to check? Options are A, B, C, D, or E"
    else:
        chosen_lane = cmd.tokens[1].lower()
        lanes = ['a', 'b', 'c', 'd', 'e']

        if chosen_lane not in lanes:
            response = "That's not a valid lane, bitch."
        else:

            lane_index = lanes.index(chosen_lane)
            row_used = ewcfg.gvs_valid_coords_gaia[lane_index]

            coord_sets = hunt_utils.gvs_create_gaia_lane_mapping(user_data, row_used)

            counter = 0
            for coord_set in coord_sets:
                current_coord = row_used[counter]
                counter += 1

                response += "\n**{}**: (".format(current_coord)
                if len(coord_set) == 0:
                    response += "Empty"
                else:
                    for enemy_id in coord_set:
                        if enemy_id == 'frozen':
                            response += "FROZEN"
                        else:
                            enemy_data = EwEnemy(id_server=user_data.id_server, id_enemy=enemy_id)
                            props = enemy_data.enemy_props

                            if debug:
                                response += ewcfg.gvs_enemy_emote_map_debug[enemy_data.enemytype]
                                if props.get('joybean') == 'true':
                                    response += "-{}".format(ewcfg.gvs_enemy_emote_map_debug[ewcfg.enemy_type_gaia_joybeans])
                                if props.get('metallicap') == 'true':
                                    response += "-{}".format(ewcfg.gvs_enemy_emote_map_debug[ewcfg.enemy_type_gaia_metallicaps])
                                elif props.get('aushuck') == 'true':
                                    response += "-{}".format(ewcfg.gvs_enemy_emote_map_debug[ewcfg.enemy_type_gaia_aushucks])
                            else:
                                response += ewcfg.gvs_enemy_emote_map[enemy_data.enemytype]
                                if props.get('joybean') == 'true':
                                    response += "-{}".format(ewcfg.gvs_enemy_emote_map[ewcfg.enemy_type_gaia_joybeans])
                                if props.get('metallicap') == 'true':
                                    response += "-{}".format(ewcfg.gvs_enemy_emote_map[ewcfg.enemy_type_gaia_metallicaps])
                                elif props.get('aushuck') == 'true':
                                    response += "-{}".format(ewcfg.gvs_enemy_emote_map[ewcfg.enemy_type_gaia_aushucks])

                            response += " "

                response += ") "

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def gvs_incubate_gaiaslimeoid(cmd):
    user_data = EwUser(member=cmd.message.author)
    valid_material = False

    if user_data.poi != ewcfg.poi_id_og_farms:
        response = "You lack the proper equipment to create a Gaiaslimeoid. Head to the Atomic Forest in Ooze Gardens Farms!"
    else:
        if cmd.tokens_count < 2:
            material_counter = 0
            material_total = 0
            response = "Please specify the crop material you will use. Options are...\n"
            for material in static_items.seedpacket_ingredient_list:
                material_counter += 1
                material_total += 1
                response += "**{}**".format(material)
                if material_total != len(static_items.seedpacket_ingredient_list):
                    response += ", "

                if material_counter == 5:
                    material_counter = 0
                    response += "\n"
        else:
            material = ewutils.flattenTokenListToString(cmd.tokens[1:])

            for material_id in static_items.seedpacket_ingredient_list:
                if material in material_id or material == material_id:
                    valid_material = True
                    break

            if not valid_material:
                response = "That's not a crop material you can use, bitch."
            else:

                material_item = bknd_item.find_item(item_search=material, id_user=cmd.message.author.id, id_server=cmd.message.guild.id if cmd.message.guild is not None else None, item_type_filter=ewcfg.it_item)
                if material_item == None:
                    response = "You don't have that crop material in your inventory, bitch."
                else:

                    generated_seedpacket_id = static_items.seedpacket_material_map[material_id]
                    item = static_items.item_map.get(generated_seedpacket_id)

                    item_type = ewcfg.it_item
                    if item != None:
                        bknd_item.item_delete(id_item=material_item.get('id_item'))
                        name = item.str_name

                        item_props = itm_utils.gen_item_props(item)

                        generated_item_id = bknd_item.item_create(
                            item_type=item_type,
                            id_user=cmd.message.author.id,
                            id_server=cmd.message.guild.id,
                            item_props=item_props
                        )

                        response = "You insert your crop material into the patent-pending Garden Ganker Homunculifier-9000:tm: and pull down hard on the large metallic lever. After a bunch of bells, whistles, and flashing lights sound off, out pops a {}!".format(name)

                    else:
                        return ewutils.logMsg("ERROR: Could not produce seed packet for material {}.".format(material))

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def gvs_fabricate_tombstone(cmd):
    user_data = EwUser(member=cmd.message.author)

    if user_data.poi != ewcfg.poi_id_nuclear_beach_edge:
        response = "You lack the proper equipment to fabricate a Tombstone. Head to Dr. Downpour's Laboratory at the edge of Nuclear Beach!"
    else:
        if cmd.tokens_count < 2:
            tombstone_counter = 0
            tombstone_total = 0
            enemy_counter = 0
            response = "Please specify the tombstone you want to fabricate. Options are...\n"
            for tombstone in static_items.tombstone_enemytype_map.keys():
                tombstone_counter += 1
                tombstone_total += 1
                response += "**{}**".format(tombstone)
                if tombstone_total != len(static_items.tombstone_enemytype_map):
                    response += ", "

                if enemy_counter == 5:
                    enemy_counter = 0
                    response += "\n"
        else:
            tombstone = ewutils.flattenTokenListToString(cmd.tokens[1:])
            if tombstone not in static_items.tombstone_enemytype_map.keys():
                response = "That's not a valid tombstone you can make, bitch."
            else:

                brainz = user_data.gvs_currency
                generated_tombstone_id = tombstone
                item = static_items.item_map.get(generated_tombstone_id)
                if item != None:
                    cost = item.cost
                    name = item.str_name
                    item_type = ewcfg.it_item

                    if cost > brainz:
                        response = "A {} costs {} brainz to fabricate, and you only have {}.".format(name, cost, brainz)
                    else:
                        user_data.gvs_currency -= cost

                        item_props = itm_utils.gen_item_props(item)

                        generated_item_id = bknd_item.item_create(
                            item_type=item_type,
                            id_user=cmd.message.author.id,
                            id_server=cmd.message.guild.id,
                            item_props=item_props
                        )

                        response = "You insert {} of your hard earned brainz into the state of the art Downpour 3D Bio-printer, watching carefully as the squishy pink organs are transformed into a {} before your very eyes! You take it out of the machine and go on your merry way.".format(cost, name)

                        user_data.persist()

                else:
                    return ewutils.logMsg("ERROR: Could not produce tombstone for tombstone ID {}.".format(generated_tombstone_id))

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def gvs_join_operation(cmd):
    seedpackets = static_items.seedpacket_ids
    tombstones = static_items.tombstone_ids
    time_now = int(time.time())

    user_data = EwUser(member=cmd.message.author)
    poi = poi_static.id_to_poi.get(user_data.poi)
    district_data = EwDistrict(district=user_data.poi, id_server=user_data.id_server)

    response = ""

    if ewutils.channel_name_is_poi(cmd.message.channel.name) == False:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You must {} in a zone's channel.".format(cmd.tokens[0])))

    if district_data.time_unlock > time_now:

        if int((district_data.time_unlock - time_now) / 60) <= 1:
            time_remaining = district_data.time_unlock - time_now
            time_used = 'seconds'
        else:
            time_remaining = int((district_data.time_unlock - time_now) / 60)
            time_used = 'minutes'

        response = "The area is too scarred from recent battles between the Garden Gankers and the Shamblers. It needs {} more {} to heal before you can start an operation here.".format(time_remaining, time_used)
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    if not poi.is_district:
        response = "Oi, dumbass! You can't join an operation if you aren't in a district zone, first!"
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    if user_data.life_state == ewcfg.life_state_juvenile:
        faction = ewcfg.psuedo_faction_gankers
    elif user_data.life_state == ewcfg.life_state_shambler:
        faction = ewcfg.psuedo_faction_shamblers
    else:
        response = "Hey idiot, it's called *Gankers Vs. Shamblers!* No gangsters, ghosts, or SlimeCorp shills allowed!"
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    # if faction == ewcfg.psuedo_faction_gankers and district_data.degradation == 0:
    # 	response = "This place is already fully rejuvenated! You'll have to try somewhere else."
    # 	return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
    # elif faction == ewcfg.psuedo_faction_shamblers and district_data.degradation == ewcfg.district_max_degradation:
    # 	response = "This place is already fully shambled! You'll have to try somewhere else."
    # 	return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
    if poi.id_poi in [ewcfg.poi_id_juviesrow, ewcfg.poi_id_rowdyroughhouse, ewcfg.poi_id_copkilltown]:
        response = "This place is too heavily guarded. Trying to pull of an operation here strikes you as downright stupid."
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
    elif poi.id_poi == ewcfg.poi_id_thevoid:
        response = "Wow, great idea shithead, this sure is prime real estate you're trying to take over here in the middle of fucking nowhere. Try somewhere else."
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
    elif poi.id_poi in [ewcfg.poi_id_assaultflatsbeach, ewcfg.poi_id_oozegardens]:
        response = "It would be reckless to try and start an operation so close to the base of the {}. You'll have to try somewhere else.".format('Garden Gankers' if poi.id_poi == ewcfg.poi_id_oozegardens else 'Shamblers')
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    in_operation, op_poi = hunt_utils.gvs_check_if_in_operation(user_data)
    if in_operation:
        if op_poi != user_data.poi:
            response = "You're already in an operation! If you wanna add another {}, you'll have to head to {}, first!".format('seed packet' if faction == ewcfg.psuedo_faction_gankers else 'tombstone', op_poi)
            return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    if cmd.tokens_count < 2:
        response = "You need to select a {} first, dummy!".format('seed packet' if faction == ewcfg.psuedo_faction_gankers else 'tombstone')
    else:
        selected_item = ewutils.flattenTokenListToString(cmd.tokens[1:])

        # if faction == ewcfg.psuedo_faction_gankers:
        # 	choices = seedpackets
        # else:
        # 	choices = tombstones
        #
        # found_choice = False
        # for choice in choices:
        # 	if selected_item in choice:
        # 		selected_item = choice
        # 		found_choice = True
        # 		break
        # 	else:
        # 		response = "That's not a valid {} you can select, bitch.".format('seed packet' if faction == ewcfg.psuedo_faction_gankers else 'tombstone')
        #
        # if not found_choice:
        # 	return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

        item_sought = bknd_item.find_item(item_search=selected_item, id_user=user_data.id_user, id_server=user_data.id_server, item_type_filter=ewcfg.it_item)

        if item_sought != None:
            item = EwItem(id_item=item_sought.get('id_item'))
            item_props = item.item_props

            id_item = item_props.get('id_item')
            if id_item != None:
                if faction == ewcfg.psuedo_faction_gankers and id_item not in seedpackets:
                    response = "That's not a valid seed packet you can select, bitch."
                    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
                elif faction == ewcfg.psuedo_faction_shamblers and id_item not in tombstones:
                    response = "That's not a valid tombstone you can select, bitch."
                    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
            else:
                response = "That's not a valid {} you can select, bitch.".format('seed packet' if faction == ewcfg.psuedo_faction_gankers else 'tombstone')
                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

            if item_props.get('brainpower') != None:
                brainpower = int(item_props.get('brainpower'))  # Only for tombstones
            else:
                brainpower = 0

            enemytype = item_props.get('enemytype')

            is_duplicate = hunt_utils.gvs_check_operation_duplicate(user_data.id_user, user_data.poi, enemytype, faction)

            if is_duplicate:
                if faction == ewcfg.psuedo_faction_gankers:
                    response = "What the hell are you doing? You've already selected that seed packet!"
                else:
                    response = "Someone else already put down that tombstone."
                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

            if faction == ewcfg.psuedo_faction_shamblers:
                if district_data.horde_cooldown > time_now:
                    response = "You gotta wait another {} seconds before you can add another tombstone. Your zombie bones ain't what they used to be...".format(district_data.horde_cooldown - time_now)
                    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
                else:
                    district_data.horde_cooldown = time_now + brainpower
                    district_data.persist()

            limit_reached, current_limit = hunt_utils.gvs_check_operation_limit(user_data.id_user, user_data.poi, enemytype, faction)

            if limit_reached:
                if faction == ewcfg.psuedo_faction_gankers:
                    response = "You can't select more than 6 seed packets at a time!"
                else:
                    response = "There's not enough room for your tombstone! **(Current Tombstone Limit: {})**".format(current_limit)
                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

            # await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "Are you sure? **!accept** or **!refuse**."))

            # # Wait for an answer
            # accepted = False
            # try:
            # 	message = await cmd.client.wait_for_message(timeout=10, author=cmd.message.author, check=ewutils.check_accept_or_refuse)
            #
            # 	if message != None:
            # 		if message.content.lower() == "!accept":
            # 			accepted = True
            # 		if message.content.lower() == "!refuse":
            # 			accepted = False
            # except:
            # 	accepted = False
            accepted = True

            if accepted:

                # Lock juveniles into the district for garden ops
                if faction == ewcfg.psuedo_faction_gankers:
                    ewutils.moves_active[user_data.id_user] = 0
                    ewutils.active_restrictions[user_data.id_user] = 4

                # If there are no player-generated operations, then the bot will simply spawn in ones automatically.
                enemyfaction = ewcfg.psuedo_faction_gankers if faction == ewcfg.psuedo_faction_shamblers else ewcfg.psuedo_faction_shamblers
                opposing_ops = bknd_core.execute_sql_query("SELECT enemytype FROM gvs_ops_choices WHERE district = '{}' AND faction = '{}'".format(user_data.poi, enemyfaction))
                if len(opposing_ops) == 0:
                    hunt_utils.gvs_insert_bot_ops(user_data.id_server, user_data.poi, enemyfaction)
                # print('spawning in bot ops...')

                if in_operation:
                    if faction == ewcfg.psuedo_faction_gankers:
                        response = "You add your {} to the Garden Op".format(item_props.get('item_name'))
                    else:
                        response = "You add your {} to the Graveyard Op".format(item_props.get('item_name'))
                        response += "\n(You and your allies can add another one in {} seconds.)".format(brainpower)
                else:
                    if faction == ewcfg.psuedo_faction_gankers:
                        response = "You ready up for a Garden Op in {} with your {}. *Ready, set, PLANT!*".format(poi.str_name, item_props.get('item_name'))
                        district_data.gaiaslime += 50
                        district_data.persist()
                    else:
                        response = "You place down your {} in {} and get ready for a Graveyard Op. *Ready, set, BRRRRAAAAAIIINNNNZZZZ!*".format(item_props.get('item_name'), poi.str_name)
                        response += "\n(You and your allies can add another one in {} seconds.)".format(brainpower)

                # durability = int(item_props.get('durability'))

                if faction == ewcfg.psuedo_faction_shamblers:
                    shambler_stock = int(item_props.get('stock'))
                else:
                    shambler_stock = 0

                # if durability > 1:
                # 	item.item_props['durability'] = durability - 1
                # 	item.persist()
                # 	response += "\n(Your {}'s durability has been lowered)".format(item_props.get('item_name'))
                # else:
                # 	bknd_item.item_delete(item.id_item)
                # 	response += "\n(Your {} has been used up completely)".format(item_props.get('item_name'))

                op_data = EwOperationData(
                    id_user=user_data.id_user,
                    district=user_data.poi,
                    enemytype=enemytype,
                    faction=faction,
                    id_item=item_sought.get('id_item'),
                    shambler_stock=shambler_stock
                )
                op_data.persist()

            else:
                response = "Well, perhaps some other time, then."

        else:
            response = "Are you sure you have that {}? Try using **!inv**".format('seed packet' if faction == ewcfg.psuedo_faction_gankers else 'tombstone')

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def gvs_leave_operation(cmd):
    user_data = EwUser(member=cmd.message.author)

    if user_data.life_state == ewcfg.life_state_juvenile:
        faction = ewcfg.psuedo_faction_gankers
    elif user_data.life_state == ewcfg.life_state_shambler:
        faction = ewcfg.psuedo_faction_shamblers
    else:
        return

    in_operation, op_poi = hunt_utils.gvs_check_if_in_operation(user_data)
    if not in_operation:
        response = "You aren't even *in* an operation."
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "Are you sure? **!accept** or **!refuse**."))

    # Wait for an answer
    accepted = False
    try:

        message = await cmd.client.wait_for('message', timeout=30, check=lambda message: message.author == cmd.message.author and message.content.lower() in [ewcfg.cmd_accept, ewcfg.cmd_refuse])

        if message != None:
            if message.content.lower() == "!accept":
                accepted = True
            if message.content.lower() == "!refuse":
                accepted = False
    except:
        accepted = False

    if accepted:
        ewutils.active_restrictions[user_data.id_user] = 0

        items = bknd_core.execute_sql_query("SELECT id_item FROM gvs_ops_choices WHERE id_user = '{}'".format(user_data.id_user))
        bknd_core.execute_sql_query("DELETE FROM gvs_ops_choices WHERE id_user = '{}'".format(user_data.id_user))
        await bknd_hunt.delete_all_enemies(cmd=None, query_suffix="AND owner = '{}' AND poi = '{}'".format(user_data.id_user, user_data.poi), id_server_sent=user_data.id_server)

        response = "You drop out of your {} Op in {}.".format('Garden' if faction == ewcfg.psuedo_faction_gankers else 'Graveyard', op_poi)

        for item in items:
            item_data = EwItem(id_item=item)
            durability = int(item_data.item_props.get('durability'))

            if faction == ewcfg.psuedo_faction_gankers:
                if durability > 1:
                    item_data.item_props['durability'] = durability - 1
                    item_data.persist()
                    response += "\n(Your {}'s durability has been lowered)".format(item_data.item_props.get('item_name'))
                else:
                    bknd_item.item_delete(item)
                    response += "\n(Your {} has been used up completely)".format(item_data.item_props.get('item_name'))

            else:
                # To prevent shamblers from re-stocking operations with tombstones, they are destroyed upon leaving a graveyard op.
                bknd_item.item_delete(item)
                response += "\n(Your {} has been used up completely)".format(item_data.item_props.get('item_name'))

        response += "\nAll your Gaiaslimeoids in {} wilt and die.".format(op_poi) if faction == ewcfg.psuedo_faction_gankers else "All the shamblers belonging to your tombstone in {} fall apart and collapse onto the ground.".format(op_poi)

    else:
        response = "Well, perhaps some other time, then."

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def gvs_check_operations(cmd):
    if cmd.tokens_count == 1:
        operations = bknd_core.execute_sql_query("SELECT district, faction FROM gvs_ops_choices GROUP BY district;")

        response = "There are currently no Garden Ops or Graveyard Ops at this time."
        if len(operations) > 0:
            response = ""
            for op in operations:
                response += "\nThere are operations taking place in {}.".format(poi_static.id_to_poi.get(op[0]).str_name)

    elif cmd.tokens_count > 1:
        checked_district = ewutils.flattenTokenListToString(cmd.tokens[1:])
        district = poi_static.id_to_poi.get(checked_district)

        if district == None or not district.is_district:
            response = "That's not a valid district that you can check"
        else:
            operations = bknd_core.execute_sql_query("SELECT enemytype FROM gvs_ops_choices WHERE district = '{}' GROUP BY enemytype".format(district.id_poi))

            if len(operations) > 0:
                gaias = bknd_core.execute_sql_query("SELECT enemytype FROM gvs_ops_choices WHERE district = '{}' AND faction = 'gankers' GROUP BY enemytype".format(district.id_poi))
                shamblers = bknd_core.execute_sql_query("SELECT enemytype FROM gvs_ops_choices WHERE district = '{}' AND faction = 'shamblers' GROUP BY enemytype".format(district.id_poi))

                response = "In {}, the currently selected seed packets and tombstones include...\n".format(district.str_name)
                response += "**GAIASLIMEOIDS**"
                for gaia in gaias:
                    response += "\n{}".format(gaia[0])
                response += "\n**SHAMBLERS**"
                for shambler in shamblers:
                    response += "\n{}".format(shambler[0])

            else:
                response = "There aren't any operations going on in that district."

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def gvs_plant_gaiaslimeoid(cmd):
    seedpackets = static_items.seedpacket_ids
    time_now = int(time.time())

    user_data = EwUser(member=cmd.message.author)
    poi = poi_static.id_to_poi.get(user_data.poi)
    district_data = EwDistrict(district=user_data.poi, id_server=user_data.id_server)

    if not user_data.life_state == ewcfg.life_state_juvenile:
        response = "Only Juveniles of pure heart can lay down Gaiaslimeoids on the field."
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    if ewutils.channel_name_is_poi(cmd.message.channel.name) == False:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You must {} in a zone's channel.".format(cmd.tokens[0])))
    if not poi.is_district:
        response = "You can't plant a Gaiaslimeoid here, dummy!"
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    in_operation, op_poi = hunt_utils.gvs_check_if_in_operation(user_data)
    if not in_operation:
        response = "You aren't even *in* an operation."
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
    elif user_data.poi != op_poi:
        response = "You can't plant a Gaiaslimeoid here, dummy! Try heading to {}.".format(poi_static.id_to_poi.get(op_poi).str_name)
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    if cmd.tokens_count < 3:
        response = "You need to select a coordinate and seed packet, dummy!"
    else:
        coord = cmd.tokens[1].upper()
        selected_item = ewutils.flattenTokenListToString(cmd.tokens[2:])
        valid_coord = False

        for row in ewcfg.gvs_valid_coords_gaia:
            if coord in row:
                valid_coord = True
                break

        if not valid_coord:
            response = "That's not a valid coordinate, bitch."
            return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

        # choices = seedpackets
        #
        # found_choice = False
        # for choice in choices:
        # 	if selected_item in choice:
        # 		selected_item = choice
        # 		found_choice = True
        # 		break
        # 	else:
        # 		response = "That's not a valid seed packet you can select, bitch. (Hint: !plant [coord] [seed packet])"
        #
        # if not found_choice or invalid_coord:
        # 	return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

        item_sought = bknd_item.find_item(item_search=selected_item, id_user=cmd.message.author.id, id_server=user_data.id_server, item_type_filter=ewcfg.it_item)
        if item_sought != None:
            item = EwItem(id_item=item_sought.get('id_item'))
            item_props = item.item_props

            id_item = item_props.get('id_item')
            if id_item != None:
                if id_item not in seedpackets:
                    response = "That's not a valid seed packet you can select, bitch."
                    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
            else:
                response = "That's not a valid seed packet you can select, bitch."
                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

            enemytype = item_props.get('enemytype')
            cooldown = int(item_props.get('cooldown'))
            cost = int(item_props.get('cost'))
            time_nextuse = int(item_props.get('time_nextuse'))

            if cost > district_data.gaiaslime:
                response = "There's not enough Gaiaslime to go around! ({}/{})".format(district_data.gaiaslime, cost)
            elif time_nextuse > time_now:
                response = "You need to wait {} seconds before you can plant that Gaiaslimeoid down.".format(time_nextuse - time_now)
            else:
                item.item_props['time_nextuse'] = time_now + cooldown
                item.persist()

                gaias_in_coord = hunt_utils.gvs_get_gaias_from_coord(user_data.poi, coord)

                if len(gaias_in_coord) > 0:
                    for gaia in gaias_in_coord.keys():
                        enemy_data = EwEnemy(id_enemy=gaias_in_coord[gaia])

                        if enemytype == gaia:
                            if gaia in ewcfg.repairable_gaias:
                                enemy_data.slimes = enemy_data.initialslimes
                                district_data.gaiaslime -= cost
                                enemy_data.persist()
                                district_data.persist()

                                response = "The {} in {} was fully repaired!".format(enemy_data.display_name, enemy_data.gvs_coord)
                                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
                            else:
                                response = "There's already a {} in that coordinate!".format(enemy_data.display_name)
                                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
                        else:
                            if enemy_data.enemy_props.get('joybean') == 'true' and enemytype == ewcfg.enemy_type_gaia_joybeans:
                                response = "A Joybean has already been planted there."
                                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
                            elif enemy_data.enemy_props.get('metallicaps') == 'true' and enemytype == ewcfg.enemy_type_gaia_metallicaps:
                                response = "A Metallicap has already been planted there."
                                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
                            elif enemy_data.enemy_props.get('aushucks') == 'true' and enemytype == ewcfg.enemy_type_gaia_aushucks:
                                response = "An Aushuck has already been planted there."
                                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
                            else:
                                response = "There's already a {} in that coordinate!".format(enemy_data.display_name)
                                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

                    district_data.gaiaslime -= cost
                    district_data.persist()

                    resp_cont = hunt_utils.spawn_enemy(
                        id_server=user_data.id_server,
                        pre_chosen_type=enemytype,
                        pre_chosen_level=50,
                        pre_chosen_poi=user_data.poi,
                        pre_chosen_identifier='',
                        pre_chosen_faction=ewcfg.psuedo_faction_gankers,
                        pre_chosen_owner=user_data.id_user,
                        pre_chosen_coord=coord,
                        manual_spawn=True,
                    )

                    return await resp_cont.post()

                else:
                    if enemytype == ewcfg.enemy_type_gaia_metallicaps:
                        response = "Metallicaps must be planted on top of attacking Gaiaslimeoids."
                    elif enemytype == ewcfg.enemy_type_gaia_aushucks:
                        response = "Aushucks must first be planted on top of existing Gaiaslimeoids."
                    else:
                        district_data.gaiaslime -= cost
                        district_data.persist()

                        resp_cont = hunt_utils.spawn_enemy(
                            id_server=user_data.id_server,
                            pre_chosen_type=enemytype,
                            pre_chosen_level=50,
                            pre_chosen_poi=user_data.poi,
                            pre_chosen_identifier='',
                            pre_chosen_faction=ewcfg.psuedo_faction_gankers,
                            pre_chosen_owner=user_data.id_user,
                            pre_chosen_coord=coord,
                            manual_spawn=True,
                        )

                        return await resp_cont.post()

        else:
            response = "Are you sure you have that seed packet? Try using **!inv**"

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


""" Lets shamblers start an event in DMs to get brains """


async def gvs_searchforbrainz(cmd):
    user_data = EwUser(member=cmd.message.author)

    if user_data.life_state != ewcfg.life_state_shambler:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You're not based enough to do that."))

    if user_data.poi != ewcfg.poi_id_slimesea:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You have to {} in the Slime Sea.".format(ewcfg.cmd_gvs_searchforbrainz)))

    time_now = int(time.time())

    if user_data.gvs_time_lastshambaquarium + ewcfg.cd_gvs_searchforbrainz >= time_now:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You'll have to rest for a while before searching for brainz again."))

    event_props = {}
    event_props['id_user'] = cmd.message.author.id
    event_props['brains_grabbed'] = 1
    event_props['captcha'] = ewutils.generate_captcha(length=1, user_data=user_data)
    event_props['channel'] = cmd.message.author.id

    # DM user
    response = poi_static.event_type_to_def.get(ewcfg.event_type_shambaquarium).str_event_start.format(ewcfg.cmd_gvs_grabbrainz, ewutils.text_to_regional_indicator(event_props['captcha']))
    try:
        await fe_utils.send_message(cmd.client, cmd.message.author, response)
    except fe_utils.discord.errors.Forbidden:
        response = "You have to allow ENDLESS WAR to DM you to search for brainz!"
        return await fe_utils.send_message(cmd.client, cmd.message.channel, response)

    user_data = EwUser(member=cmd.message.author)

    # check if the user's state hasn't changed just in case
    if user_data.life_state != ewcfg.life_state_shambler:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You're not based enough to do that."))

    if user_data.poi != ewcfg.poi_id_slimesea:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You have to {} in the Slime Sea.".format(ewcfg.cmd_gvs_searchforbrainz)))

    bknd_worldevent.create_world_event(
        id_server=user_data.id_server,
        event_type=ewcfg.event_type_shambaquarium,
        time_activate=time_now,
        time_expir=time_now + 60,  # 1 minute
        event_props=event_props
    )

    user_data.gvs_time_lastshambaquarium = time_now
    user_data.persist()


""" Command for shamblers to get brains in the shambaquarium event """


async def gvs_grabbrainz(cmd):
    if not isinstance(cmd.message.channel, fe_utils.discord.channel.DMChannel):
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You have to {} in DMs.".format(ewcfg.cmd_gvs_grabbrainz)))

    user_data = EwUser(id_user=cmd.message.author.id, id_server=cmd.guild.id)

    if user_data.life_state != ewcfg.life_state_shambler:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You're not based enough to do that."))

    if user_data.poi != ewcfg.poi_id_slimesea:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You have to {} in the Slime Sea.".format(ewcfg.cmd_gvs_grabbrainz)))

    # look for a shambaquarium event belonging to this player
    world_events = bknd_worldevent.get_world_events(id_server=cmd.guild.id)
    for id_event in world_events:
        if world_events.get(id_event) == ewcfg.event_type_shambaquarium:
            event_data = EwWorldEvent(id_event=id_event)
            if int(event_data.event_props.get('id_user')) == user_data.id_user:

                captcha = ewutils.flattenTokenListToString(cmd.tokens[1:]).lower()

                if event_data.event_props.get('captcha').lower() == captcha:
                    event_data.event_props['brains_grabbed'] = int(event_data.event_props['brains_grabbed']) + 1
                    captcha_length = int(event_data.event_props['brains_grabbed'])
                    event_data.event_props['captcha'] = ewutils.generate_captcha(length=captcha_length if captcha_length < 8 else 8, user_data=user_data)
                    event_data.persist()

                    user_data.gvs_currency += ewcfg.brainz_per_grab
                    user_data.persist()

                    response = "You grabbed {} brainz! Baaaaaased! New captcha: ".format(ewcfg.brainz_per_grab) + ewutils.text_to_regional_indicator(event_data.event_props['captcha'])
                    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

                else:
                    event_data.event_props['captcha'] = ewutils.generate_captcha(length=int(event_data.event_props['brains_grabbed']), user_data=user_data)
                    event_data.persist()
                    response = "Missed! That was pretty cringe dude... New captcha: " + ewutils.text_to_regional_indicator(event_data.event_props['captcha'])
                    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

            # break

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You have to {} before trying to grab any brainz!".format(ewcfg.cmd_gvs_searchforbrainz)))


""" Lets shamblers enter the slime sea"""


async def gvs_dive(cmd):
    user_data = EwUser(member=cmd.message.author)

    if user_data.life_state != ewcfg.life_state_shambler:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You're not based enough to do that."))

    if user_data.poi != ewcfg.poi_id_nuclear_beach_edge:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You have to {} at the edge of Nuclear Beach.".format(ewcfg.cmd_gvs_dive)))

    await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You begin swimming towards the Slime Sea."), delete_after=15)

    await asyncio.sleep(15)

    user_data = EwUser(member=cmd.message.author)
    user_data.poi = ewcfg.poi_id_slimesea
    user_data.persist()

    slimesea = poi_static.id_to_poi.get(ewcfg.poi_id_slimesea)
    sea_channel = fe_utils.get_channel(cmd.guild, slimesea.channel)
    await fe_utils.send_message(cmd.client, sea_channel, fe_utils.formatMessage(cmd.message.author, "You arrive in the Slime Sea."), delete_after=10)

    await ewrolemgr.updateRoles(client=cmd.client, member=cmd.message.author)


""" Lets shamblers exit the slime sea"""


async def gvs_resurface(cmd):
    user_data = EwUser(member=cmd.message.author)

    if user_data.life_state != ewcfg.life_state_shambler:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You're not based enough to do that."))

    if user_data.poi != ewcfg.poi_id_slimesea:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You have to {} at the Slime Sea.".format(ewcfg.cmd_gvs_resurface)))

    await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You begin swimming towards the Nuclear Beach."), delete_after=15)

    await asyncio.sleep(15)

    user_data = EwUser(member=cmd.message.author)
    user_data.poi = ewcfg.poi_id_nuclear_beach_edge
    user_data.persist()

    beach = poi_static.id_to_poi.get(ewcfg.poi_id_nuclear_beach_edge)
    beach_channel = fe_utils.get_channel(cmd.guild, beach.channel)
    await fe_utils.send_message(cmd.client, beach_channel, fe_utils.formatMessage(cmd.message.author, "You arrive in the Nuclear Beach."), delete_after=10)

    await ewrolemgr.updateRoles(client=cmd.client, member=cmd.message.author)


""" Sell a potted gaiaslimeoid to Hortisolis """


async def gvs_sell_gaiaslimeoid(cmd):
    user_data = EwUser(member=cmd.message.author)

    if user_data.life_state == ewcfg.life_state_shambler:
        response = "You lack the higher brain functions required to {}.".format(cmd.tokens[0])
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    # Only at the Atomic Forest
    if user_data.poi != ewcfg.poi_id_og_farms:
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, "You have to be in the Atomic Forest to sell your Gaiaslimeoids."))

    item_search = ewutils.flattenTokenListToString(cmd.tokens[1:])
    item_sought = bknd_item.find_item(item_search=item_search, id_user=cmd.message.author.id, id_server=cmd.guild.id, item_type_filter=ewcfg.it_item)

    if item_sought:
        gaiaslimeoid = EwItem(id_item=item_sought.get('id_item'))

        if gaiaslimeoid.item_props.get('id_item') != ewcfg.item_id_gaiaslimeoid_pot:
            response = "Hortisolis politely refuses that item. He informs you that it is not a potted Gaiaslimeoid."
            return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

        slime_gain = 20000 * int(gaiaslimeoid.item_props.get('size'))

        gaia_type = gaiaslimeoid.item_props.get('gaiaslimeoid')

        response = 'Hortisolis speaks in a boisterous manner:\n"FOR THOUST {} GAIASLIMEOID, I SUBMIT {} SLIME. DO YOU {}, OR WOULD YOU RATHER {}?"'.format(gaia_type, slime_gain, ewcfg.cmd_accept, ewcfg.cmd_refuse)
        await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

        # Wait for an answer
        accepted = False
        try:
            msg = await cmd.client.wait_for('message', timeout=30, check=lambda message: message.author == cmd.message.author and message.content.lower() in [ewcfg.cmd_accept, ewcfg.cmd_refuse])

            if msg != None:
                if msg.content == ewcfg.cmd_accept:
                    accepted = True
        except:
            accepted = False

        gaiaslimeoid = EwItem(id_item=item_sought.get('id_item'))
        # cancel deal if the gaiaslimeoid is no longer in user's inventory
        if gaiaslimeoid.id_owner != str(user_data.id_user):
            accepted = False

        if accepted:
            user_data = EwUser(member=cmd.message.author)
            user_data.change_slimes(slime_gain)
            user_data.persist()

            bknd_item.item_delete(gaiaslimeoid.id_item)

            response = "Hortisolis gives you {} slime for your {} Gaiaslimeoid.".format(slime_gain, gaiaslimeoid.item_props.get('gaiaslimeoid'))

        else:
            response = '"A PITY, PERHAPS YOU WILL FIND SOME USE FOR IT ELSEWHERE. PRITHEE BE CAREFUL!"'

    else:
        response = "Are you sure you have that Gaiaslimeoid?"

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


""" Dig up a gaiaslimeoid """


async def dig(cmd):  # TODO  zen garden functionality

    if cmd.tokens_count < 2:
        response = 'Specify which coordinate you want to dig up.'
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    user_data = EwUser(member=cmd.message.author)

    if user_data.life_state == ewcfg.life_state_shambler:
        response = "You lack the higher brain functions required to {}.".format(cmd.tokens[0])
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    weapon_item = EwItem(id_item=user_data.weapon)

    if weapon_item.item_props.get("weapon_type") != ewcfg.weapon_id_shovel:
        response = "You can't dig Gaiaslimeoids without a shovel, dumbass. Buy one from Hortisolis at the Atomic Forest in Ooze Gardens Farms!"
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    coord = cmd.tokens[1].upper()
    is_garden = False

    # Look for gaiaslimeoid
    gaias = hunt_utils.gvs_get_gaias_from_coord(user_data.poi, coord)

    dig_low_priority = [ewcfg.enemy_type_gaia_rustealeaves]
    dig_mid_priority = []
    dig_high_priority = [ewcfg.enemy_type_gaia_steelbeans]

    # ID of gaiaslimeoid found
    dig_target = None

    for enemy_id in ewcfg.gvs_enemies_gaiaslimeoids:
        if enemy_id not in dig_low_priority and enemy_id not in dig_high_priority:
            dig_mid_priority.append(enemy_id)

    type_to_id_map = {}
    for id in gaias.keys():
        type = gaias[id]
        type_to_id_map[type] = id

    for target in dig_high_priority:
        if target in type_to_id_map.keys():
            dig_target = type_to_id_map[target]

    for target in dig_mid_priority:
        if target in type_to_id_map.keys():
            dig_target = type_to_id_map[target]

    for target in dig_low_priority:
        if target in type_to_id_map.keys():
            dig_target = type_to_id_map[target]

    # is_garden = if it was a garden

    if dig_target is None:
        response = "There are no Gaiaslimeoids here."
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    if not is_garden:

        enemy = EwEnemy(id_server=user_data.id_server, id_enemy=dig_target)
        bknd_hunt.delete_enemy(enemy)

        if random.random() < 0.8:  # 90% chance to fail
            response = "You dig up a {} Gaiaslimeoid."
            return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

        bknd_item.item_create(
            item_type=ewcfg.it_item,
            id_user=cmd.message.author.id,
            id_server=cmd.guild.id,
            item_props={
                'id_item': ewcfg.item_id_gaiaslimeoid_pot,
                'item_name': "Pot containing a {} Gaiaslimeoid".format(enemy.display_name),
                'item_desc': "It's a pot with a {} foot-tall {} Gaiaslimeoid. You can place it in a zen garden or sell it to Hortisolis.".format("{size}", enemy.display_name),
                'time_lastslimed': int(time.time()),
                'size': 1,
                'gaiaslimeoid': enemy.enemytype
            }
        )

        response = "You dig up a {} Gaiaslimeoid and place it in a pot!".format(enemy.display_name)

    else:
        response = "Placeholder zen garden dig"
    # change owner

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def gvs_progress(cmd):
    op_districts = []
    response = ""

    for poi in poi_static.poi_list:
        # if poi.is_district and not poi.id_poi in [ewcfg.poi_id_rowdyroughhouse, ewcfg.poi_id_copkilltown, ewcfg.poi_id_juviesrow, ewcfg.poi_id_oozegardens, ewcfg.poi_id_assaultflatsbeach, ewcfg.poi_id_thevoid]:
        if poi.is_district:
            op_districts.append(poi.id_poi)

    degradation_data = bknd_core.execute_sql_query("SELECT district, degradation FROM districts WHERE district IN {} AND id_server = {}".format(tuple(op_districts), cmd.message.guild.id))

    non_degraded_districts = []
    degraded_districts = []

    for district in degradation_data:
        if district[1] == 0:
            non_degraded_districts.append(district[0])
        elif district[1] == ewcfg.district_max_degradation:
            degraded_districts.append(district[0])

    # non_degraded_districts = set(non_degraded_districts)
    # degraded_districts = set(degraded_districts)

    counter = 0
    response += "\n**Rejuvenated Districts**"
    for non_deg in non_degraded_districts:
        if counter % 5 == 0:
            response += "\n"

        poi = poi_static.id_to_poi.get(non_deg)
        counter += 1

        if counter != len(non_degraded_districts):
            response += "{}, ".format(poi.str_name)
        else:
            response += "and {}.".format(poi.str_name)

    counter = 0
    response += "\n**Shambled Districts**"
    for deg in degraded_districts:
        if counter % 5 == 0:
            response += "\n"

        poi = poi_static.id_to_poi.get(deg)
        counter += 1

        if counter != len(degraded_districts):
            response += "{}, ".format(poi.str_name)
        else:
            response += "and {}.".format(poi.str_name)

    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def gvs_gaiaslime(cmd):
    user_data = EwUser(member=cmd.message.author)

    district_data = EwDistrict(district=user_data.poi, id_server=user_data.id_server)

    if district_data.gaiaslime > 0:
        response = "This district houses {} gaiaslime.".format(district_data.gaiaslime)
    else:
        response = "There is no gaiaslime to be found here."
    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def gvs_brainz(cmd):
    user_data = EwUser(member=cmd.message.author)

    response = "You have {} brainz.".format(user_data.gvs_currency)
    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

async def shamble(cmd):
    user_data = EwUser(member=cmd.message.author)

    if user_data.life_state != ewcfg.life_state_shambler and user_data.poi != ewcfg.poi_id_assaultflatsbeach:
        response = "You have too many higher brain functions left to {}.".format(cmd.tokens[0])
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
    elif user_data.life_state in [ewcfg.life_state_juvenile, ewcfg.life_state_enlisted] and user_data.poi == ewcfg.poi_id_assaultflatsbeach:
        response = "You feel an overwhelming sympathy for the plight of the Shamblers and decide to join their ranks."
        await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

        await asyncio.sleep(5)

        user_data = EwUser(member=cmd.message.author)
        user_data.life_state = ewcfg.life_state_shambler
        user_data.degradation = 100

        ewutils.moves_active[user_data.id_user] = 0

        user_data.poi = ewcfg.poi_id_nuclear_beach_edge
        user_data.persist()

        member = cmd.message.author

        base_poi_channel = fe_utils.get_channel(cmd.message.guild, 'nuclear-beach-edge')

        response = 'You arrive inside the facility and are injected with a unique strain of the Modelovirus. Not long after, a voice on the intercom chimes in.\n**"Welcome, {}. Welcome to Downpour Laboratories. It\'s safer here. Please treat all machines and facilities with respect, they are precious to our cause."**'.format(member.display_name)

        await ewrolemgr.updateRoles(client=cmd.client, member=member)
        return await fe_utils.send_message(cmd.client, base_poi_channel, fe_utils.formatMessage(cmd.message.author, response))

    else:
        pass

# Rest in fucking pieces

# if poi is None:
# 	return
# elif not poi.is_district:
# 	response = "This doesn't seem like an important place to be shambling. Try a district zone instead."
# 	return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
# elif poi.id_poi == ewcfg.poi_id_oozegardens:
# 	response = "The entire district is covered in Brightshades! You have no business shambling this part of town!"
# 	return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
#
# in_operation, op_poi = ewutils.gvs_check_if_in_operation(user_data)
# if in_operation:
# 	if op_poi != user_data.poi:
# 		response = "You aren't allowed to !shamble this district, per Dr. Downpour's orders.\n(**!goto {}**)".format(op_poi)
# 		return await fe_utils.send_message(cmd.client, cmd.message.channel,  fe_utils.formatMessage(cmd.message.author, response))
# else:
# 	response = "You aren't even in a Graveyard Op yet!\n(**!joinops [tombstone]**)"
# 	return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
#
# if (time_now - user_data.time_lasthaunt) < ewcfg.cd_shambler_shamble:
# 	response = "You know, you really just don't have the energy to shamble this place right now. Try again in {} seconds.".format(int(ewcfg.cd_shambler_shamble-(time_now-user_data.time_lasthaunt)))
# 	return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
#
# district_data = EwDistrict(district = poi.id_poi, id_server = cmd.guild.id)
#
# if district_data.degradation < poi.max_degradation:
# 	district_data.degradation += 1
# 	# user_data.degradation += 1
# 	user_data.time_lasthaunt = time_now
# 	district_data.persist()
# 	user_data.persist()
#
# 	response = "You shamble {}.".format(poi.str_name)
# 	await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
#
# 	if district_data.degradation == poi.max_degradation:
# 		response = ewcfg.str_zone_degraded.format(poi = poi.str_name)
# 		await fe_utils.send_message(cmd.client, cmd.message.channel, response)

async def rejuvenate(cmd):
    user_data = EwUser(member=cmd.message.author)

    if user_data.life_state == ewcfg.life_state_shambler and user_data.poi != ewcfg.poi_id_oozegardens:
        response = "You lack the higher brain functions required to {}.".format(cmd.tokens[0])
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
    elif user_data.life_state == ewcfg.life_state_shambler and user_data.poi == ewcfg.poi_id_oozegardens:
        response = "You decide to change your ways and become one of the Garden Gankers in order to overthrow your old master."
        await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

        await asyncio.sleep(5)

        user_data = EwUser(member=cmd.message.author)
        user_data.life_state = ewcfg.life_state_juvenile
        user_data.degradation = 0
        # user_data.gvs_currency = 0

        ewutils.moves_active[user_data.id_user] = 0

        user_data.poi = ewcfg.poi_id_og_farms
        user_data.persist()

        client = ewutils.get_client()
        server = client.get_guild(user_data.id_server)
        member = server.get_member(user_data.id_user)

        base_poi_channel = fe_utils.get_channel(cmd.message.guild, ewcfg.channel_og_farms)

        response = "You enter into Atomic Forest inside the farms of Ooze Gardens and are sterilized of the Modelovirus. Hortisolis gives you a big hug and says he's glad you've overcome your desire for vengeance in pursuit of deposing Downpour."

        await ewrolemgr.updateRoles(client=cmd.client, member=member)
        return await fe_utils.send_message(cmd.client, base_poi_channel, fe_utils.formatMessage(cmd.message.author, response))

    else:
        pass

