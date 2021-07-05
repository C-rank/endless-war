import asyncio
import random
import sys
import time

from ew.backend import item as bknd_item

from ew.backend.item import EwItem

from ew.static import cfg as ewcfg

from ew.utils import frontend as fe_utils
from ew.utils import core as ewutils

from ew.utils.combat import EwUser


"""
    SLIMERNALIA COMMANDS
"""


# Show a player's festivity
async def festivity(cmd):
    if cmd.mentions_count == 0:
        user_data = EwUser(member=cmd.message.author)
        response = "You currently have {:,} festivity.".format(user_data.get_festivity())

    else:
        member = cmd.mentions[0]
        user_data = EwUser(member=member)
        response = "{} currently has {:,} festivity.".format(member.display_name, user_data.get_festivity())

    # Send the response to the player.
    await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def wrap(cmd):
    if cmd.tokens_count != 4:
        response = 'To !wrap a gift, you need to specify a recipient, message, and item, like so:\n```!wrap @munchy#6443 "Sample text." chickenbucket```'
        return await fe_utils.send_message(cmd.client, cmd.message.channel, response)

    if cmd.mentions_count == 0:
        response = "Who exactly are you giving your gift to?"
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    if cmd.mentions_count > 1:
        response = "Back it up man, the rules are one gift for one person!"
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    recipient = cmd.mentions[0]
    recipient_data = EwUser(member=recipient)

    member = cmd.message.author
    user_data = EwUser(member=cmd.message.author)

    if recipient_data.id_user == user_data.id_user:
        response = "C'mon man, you got friends, don't you? Try and give a gift to someone other than yourself."
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    paper_sought = bknd_item.find_item(item_search="wrappingpaper", id_user=cmd.message.author.id, id_server=cmd.guild.id, item_type_filter=ewcfg.it_item)

    if paper_sought:
        paper_item = EwItem(id_item=paper_sought.get('id_item'))

    if paper_sought and paper_item.item_props.get('context') == ewcfg.context_wrappingpaper:
        paper_name = paper_sought.get('name')
    else:
        response = "How are you going to wrap a gift without any wrapping paper?"
        return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))

    gift_message = cmd.tokens[2]

    item_search = ewutils.flattenTokenListToString(cmd.tokens[3:])
    item_sought = bknd_item.find_item(item_search=item_search, id_user=cmd.message.author.id, id_server=cmd.guild.id)

    if item_sought:
        item = EwItem(id_item=item_sought.get('id_item'))
        if item.item_type == ewcfg.it_item:
            if item.item_props.get('id_item') == "gift":
                response = "It's already wrapped."
                return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))
        if item.soulbound:
            response = "It's a nice gesture, but trying to gift someone a Soulbound item is going a bit too far, don't you think?"
        elif bknd_item.check_inv_capacity(user_data=user_data, item_type=ewcfg.it_item):
            response = ewcfg.str_generic_inv_limit.format(ewcfg.it_item)
        else:
            gift_name = "Gift"

            gift_address = 'To {}, {}. From, {}'.format(recipient.display_name, gift_message, member.display_name, )

            gift_desc = "A gift wrapped in {}. Wonder what's inside?\nThe front of the tag reads '{}'\nOn the back of the tag, an ID number reads **({})**.".format(paper_name, gift_address, item.id_item)

            response = "You shroud your {} in {} and slap on a premade bow. Onto it, you attach a note containing the following text: '{}'.\nThis small act of kindness manages to endow you with Slimernalia spirit, if only a little.".format(item_sought.get('name'), paper_name, gift_address)

            bknd_item.item_create(
                id_user=cmd.message.author.id,
                id_server=cmd.guild.id,
                item_type=ewcfg.it_item,
                item_props={
                    'item_name': gift_name,
                    'id_item': "gift",
                    'item_desc': gift_desc,
                    'context': gift_address,
                    'acquisition': "{}".format(item_sought.get('id_item')),
                    # flag indicating if the gift has already been given once so as to not have people farming festivity through !giving
                    'gifted': "false"
                }
            )
            bknd_item.give_item(id_item=item_sought.get('id_item'), id_user=str(cmd.message.author.id) + "gift", id_server=cmd.guild.id)
            bknd_item.item_delete(id_item=paper_item.id_item)

            user_data.festivity += ewcfg.festivity_on_gift_wrapping

            user_data.persist()
    else:
        if item_search == "" or item_search == None:
            response = "Specify the item you want to wrap."
        else:
            response = "Are you sure you have that item?"
    return await fe_utils.send_message(cmd.client, cmd.message.channel, fe_utils.formatMessage(cmd.message.author, response))


async def yoslimernalia(cmd):
    await fe_utils.send_message(cmd.client, cmd.message.channel, '@everyone Yo, Slimernalia!', filter_everyone=False)

