import asyncio
import time
import discord

import ewcfg
import ewutils
import ewitem

from ew import EwUser

class EwRole:
	id_server = ""
	id_role = ""
	name = ""

	def __init__(self, id_server = None, name = None, id_role = None):
		if id_server is not None and name is not None:
			self.id_server = id_server
			self.name = name


			data = ewutils.execute_sql_query("SELECT {id_role} FROM roles WHERE id_server = %s AND {name} = %s".format(
				id_role = ewcfg.col_id_role,
				name = ewcfg.col_role_name
			), (
				id_server,
				name
			))

			if len(data) > 0:  # if data is not empty, i.e. it found an entry
				# data is always a two-dimensional array and if we only fetch one row, we have to type data[0][x]
				self.id_role = data[0][0]
			else:  # create new entry
				ewutils.execute_sql_query("REPLACE INTO roles ({id_server}, {name}) VALUES (%s, %s)".format(
					id_server = ewcfg.col_id_server,
					name = ewcfg.col_role_name
				), (
					id_server,
					name
				))
		elif id_server is not None and id_role is not None:
			self.id_server = id_server
			self.id_role = id_role


			data = ewutils.execute_sql_query("SELECT {name} FROM roles WHERE id_server = %s AND {id_role} = %s".format(
				id_role = ewcfg.col_id_role,
				name = ewcfg.col_role_name
			), (
				id_server,
				id_role
			))

			if len(data) > 0:  # if data is not empty, i.e. it found an entry
				# data is always a two-dimensional array and if we only fetch one row, we have to type data[0][x]
				self.name = data[0][0]

	def persist(self):
		ewutils.execute_sql_query("REPLACE INTO roles (id_server, {id_role}, {name}) VALUES(%s, %s, %s)".format(
			id_role = ewcfg.col_id_role,
			name = ewcfg.col_role_name
		), (
			self.id_server,
			self.id_role,
			self.name
		))
			

"""
	Find relevant roles and save them to the database.
"""
def setupRoles(client = None, id_server = ""):
	
	roles_map = ewutils.getRoleMap(client.get_server(id_server).roles)
	for poi in ewcfg.poi_list:
		if poi.role in roles_map:
			try:
				role_data = EwRole(id_server = id_server, name = poi.role)
				role_data.id_role = roles_map[poi.role].id
				role_data.persist()
			except:
				ewutils.logMsg('Failed to set up role {}'.format(poi.role))
		
		if poi.major_role in roles_map:
			try:
				role_data = EwRole(id_server = id_server, name = poi.major_role)
				role_data.id_role = roles_map[poi.major_role].id
				role_data.persist()
			except:
				ewutils.logMsg('Failed to set up major role {}'.format(poi.major_role))
				
		if poi.minor_role in roles_map:
			try:
				role_data = EwRole(id_server = id_server, name = poi.minor_role)
				role_data.id_role = roles_map[poi.minor_role].id
				role_data.persist()
			except:
				ewutils.logMsg('Failed to set up minor role {}'.format(poi.minor_role))

	for faction_role in ewcfg.faction_roles:
		if faction_role in roles_map:
			try:
				role_data = EwRole(id_server = id_server, name = faction_role)
				role_data.id_role = roles_map[faction_role].id
				role_data.persist()
			except:
				ewutils.logMsg('Failed to set up role {}'.format(faction_role))

	for misc_role in ewcfg.misc_roles:
		if misc_role in roles_map:
			try:
				role_data = EwRole(id_server = id_server, name = misc_role)
				role_data.id_role = roles_map[misc_role].id
				role_data.persist()
			except:
				ewutils.logMsg('Failed to set up role {}'.format(misc_role))

"""
	Hide the names of poi roles behind a uniform alias
"""
async def hideRoleNames(cmd):
	id_server = cmd.message.server.id
	client = ewutils.get_client()
	
	server = client.get_server(id_server)
	roles_map = ewutils.getRoleMap(server.roles)

	poi_counter = 0
	for poi in ewcfg.poi_list:
		
		if (not poi.is_subzone) and (not poi.is_district):
			continue
		
		# Slow down just a bit every 20 POIs
		poi_counter += 1
		if poi_counter == 20:
			poi_counter = 0
			await asyncio.sleep(2)
		
		try:
			if poi.role in roles_map:
				role = roles_map[poi.role]
				await client.edit_role(server = server, role = role, name = ewcfg.generic_role_name)
		except:
			ewutils.logMsg('Failed to hide role name for {}'.format(poi.role))
			
		try:
			if poi.major_role in roles_map:
				major_role = roles_map[poi.major_role]
				await client.edit_role(server = server, role = major_role, name = ewcfg.generic_role_name)
		except:
			ewutils.logMsg('Failed to hide role name for {}'.format(poi.major_role))
			
		try:
			if poi.minor_role in roles_map:
				minor_role = roles_map[poi.minor_role]
				await client.edit_role(server = server, role = minor_role, name = ewcfg.generic_role_name)
		except:
			ewutils.logMsg('Failed to hide role name for {}'.format(poi.minor_role))

"""
	Restore poi roles to their original names
"""
async def restoreRoleNames(cmd):

	member = cmd.message.author
	
	if not member.server_permissions.administrator:
		return
	
	client = cmd.client
	server = member.server
	for poi in ewcfg.poi_list:
		try:
			role_data = EwRole(id_server = server.id, name = poi.role)
			for role in server.roles:
				if role.id == role_data.id_role:
					await client.edit_role(server = server, role = role, name = role_data.name)
		except:
			ewutils.logMsg('Failed to restore role name for {}'.format(poi.role))
			
		try:
			major_role_data = EwRole(id_server = server.id, name = poi.major_role)
			for role in server.roles:
				if role.id == major_role_data.id_role:
					await client.edit_role(server = server, role = role, name = major_role_data.name)
		except:
			ewutils.logMsg('Failed to restore role name for {}'.format(poi.major_role))
			
		try:
			minor_role_data = EwRole(id_server = server.id, name = poi.minor_role)
			for role in server.roles:
				if role.id == minor_role_data.id_role:
					await client.edit_role(server = server, role = role, name = minor_role_data.name)
		except:
			ewutils.logMsg('Failed to restore role name for {}'.format(poi.minor_role))
			
"""
	Creates all POI roles from scratch. Ideally, this is only used in test servers.
"""
async def recreateRoles(cmd):
	member = cmd.message.author
	
	if not member.server_permissions.administrator:
		return
	
	client = cmd.client
	server = client.get_server(cmd.message.server.id)
	
	server_role_names = []
	
	for role in server.roles:
		server_role_names.append(role.name)
		
	# print(server_role_names)
	roles_created = 0
	
	for poi in ewcfg.poi_list:

		# if poi.role != None:
		# 
		# 	if poi.role not in server_role_names:
		# 		await client.create_role(server=server, name=poi.role)
		# 		ewutils.logMsg('created role {} for poi {}'.format(poi.role, poi.id_poi))
		# 
		# 		roles_created += 1

		if poi.major_role != None and poi.major_role != ewcfg.role_null_major_role:

			if poi.major_role not in server_role_names:
				
				if poi.is_district:
					#print(poi.major_role)
					await client.create_role(server=server, name=poi.major_role)
					ewutils.logMsg('created major role {} for poi {}'.format(poi.major_role, poi.id_poi))
	
					roles_created += 1

		if poi.minor_role != None and poi.minor_role != ewcfg.role_null_minor_role:

			if poi.minor_role not in server_role_names:
				
				if poi.is_district or poi.is_street:
					await client.create_role(server=server, name=poi.minor_role)
					ewutils.logMsg('created minor role {} for poi {}'.format(poi.minor_role, poi.id_poi))
	
					roles_created += 1
				
	print('{} roles were created in recreateRoles.'.format(roles_created))
		
"""
	Deletes all POI roles of a desired type. Ideally, this is only used in test servers.
"""
async def deleteRoles(cmd):
	member = cmd.message.author

	if not member.server_permissions.administrator:
		return

	client = cmd.client
	server = client.get_server(cmd.message.server.id)
	
	delete_target = ""
	
	if cmd.tokens_count > 1:
		if cmd.tokens[1].lower() == 'roles':
			delete_target = 'roles'
		elif cmd.tokens[1].lower() == 'minorroles':
			delete_target = 'minorroles'
		elif cmd.tokens[1].lower() == 'majorroles':
			delete_target = 'majorroles'
		elif cmd.tokens[1].lower() == 'hiddrenroles':
			delete_target = 'hiddenroles'
		else:
			return
	else:
		return
		
	roles_map = ewutils.getRoleMap(server.roles)

	server_role_names = []

	for role in server.roles:
		server_role_names.append(role.name)
		
	roles_deleted = 0

	if delete_target == 'roles':
		for poi in ewcfg.poi_list:
			if poi.role in server_role_names:
				await client.delete_role(server=server, role=roles_map[poi.role])
				roles_deleted += 1
			
	elif delete_target == 'majorroles':
		for poi in ewcfg.poi_list:
			if poi.is_district:
				if poi.major_role in server_role_names:
					await client.delete_role(server=server, role=roles_map[poi.major_role])
					roles_deleted += 1
		
	elif delete_target == 'minorroles':
		for poi in ewcfg.poi_list:
			if poi.is_district or poi.is_street:
				if poi.minor_role in server_role_names:
					await client.delete_role(server=server, role=roles_map[poi.minor_role])
					roles_deleted += 1
				
	elif delete_target == 'hiddenroles':
		for generic_role in server.roles:
			if generic_role.name == ewcfg.generic_role_name:
				await client.delete_role(server=server, role=generic_role)
				roles_deleted += 1

	print('{} roles were deleted in deleteRoles.'.format(roles_deleted))


"""
	Fix the Discord roles assigned to this member.
"""
async def updateRoles(
	client = None,
	member = None,
	server_default = None,
	#refresh_perms = False,
	refresh_perms = True,
):
	time_now = int(time.time())

	if server_default != None:
		user_data = EwUser(id_user=member.id, id_server = server_default)
	else:
		user_data = EwUser(member=member)

	id_server = user_data.id_server
	
	if member == None:
		return ewutils.logMsg("error: member was not supplied for updateRoles")

	#roles_map = ewutils.getRoleMap(member.server.roles)
	roles_map_user = ewutils.getRoleIdMap(member.roles)

	if user_data.life_state != ewcfg.life_state_kingpin and ewcfg.role_kingpin in roles_map_user:
		# Fix the life_state of kingpins, if somehow it wasn't set.
		user_data.life_state = ewcfg.life_state_kingpin
		user_data.persist()

	elif user_data.life_state != ewcfg.life_state_grandfoe and ewcfg.role_grandfoe in roles_map_user:
		# Fix the life_state of a grand foe.
		user_data.life_state = ewcfg.life_state_grandfoe
		user_data.persist()

	faction_roles_remove = [
		ewcfg.role_juvenile,
		ewcfg.role_juvenile_active,
		ewcfg.role_juvenile_pvp,
		ewcfg.role_rowdyfuckers,
		ewcfg.role_rowdyfuckers_pvp,
		ewcfg.role_rowdyfuckers_active,
		ewcfg.role_copkillers,
		ewcfg.role_copkillers_pvp,
		ewcfg.role_copkillers_active,
		ewcfg.role_corpse,
		ewcfg.role_corpse_pvp,
		ewcfg.role_corpse_active,
		ewcfg.role_kingpin,
		ewcfg.role_grandfoe,
		ewcfg.role_slimecorp,
		ewcfg.role_tutorial,
		ewcfg.role_shambler,
	]

	# Manage faction roles.
	faction_role = ewutils.get_faction(user_data = user_data)

	faction_roles_remove.remove(faction_role)

	pvp_role = None
	active_role = None
	if faction_role in ewcfg.role_to_pvp_role:

		if user_data.time_expirpvp >= time_now:
			pvp_role = ewcfg.role_to_pvp_role.get(faction_role)
			faction_roles_remove.remove(pvp_role)

		# if ewutils.is_otp(user_data):
		# 	active_role = ewcfg.role_to_active_role.get(faction_role)
		# 	faction_roles_remove.remove(active_role)

	tutorial_role = None
	if user_data.poi in ewcfg.tutorial_pois:
		tutorial_role = ewcfg.role_tutorial
		faction_roles_remove.remove(tutorial_role)

	# Manage location roles.
	user_poi = ewcfg.id_to_poi.get(user_data.poi)
	#print(user_poi.id_poi)
	if user_poi != None:
		# poi_role = user_poi.role
		poi_major_role = user_poi.major_role
		poi_minor_role = user_poi.minor_role
		poi_permissions = user_poi.permissions
	else:
		# poi_role = None
		poi_major_role = None
		poi_minor_role = None
		poi_permissions = None


	poi_permissions_remove = []
	for poi in ewcfg.poi_list:
		if poi.permissions != None and poi.permissions != poi_permissions:
			poi_permissions_remove.append(poi.id_poi)

	poi_roles_remove = []
	for poi in ewcfg.poi_list:
		if poi.major_role != None and poi.major_role != poi_major_role:
			poi_roles_remove.append(poi.major_role)
		if poi.minor_role != None and poi.minor_role != poi_minor_role:
			poi_roles_remove.append(poi.minor_role)

	misc_roles_remove = [
		ewcfg.role_gellphone,
		ewcfg.role_slimernalia
	]

	# Remove user's gellphone role if they don't have a phone
	role_gellphone = None
	gellphones = ewitem.find_item_all(item_search = ewcfg.item_id_gellphone, id_user = user_data.id_user, id_server = user_data.id_server, item_type_filter = ewcfg.it_item)
	gellphone_active = False

	for phone in gellphones:
		phone_data = ewitem.EwItem(id_item = phone.get('id_item'))
		if phone_data.item_props.get('active') == 'true':
			gellphone_active = True
			break
		
	if gellphone_active == True:
		role_gellphone = ewcfg.role_gellphone
		misc_roles_remove.remove(ewcfg.role_gellphone)

	role_slimernalia = None
	#if user_data.slimernalia_kingpin == True:
	#	role_slimernalia = ewcfg.role_slimernalia
	#	misc_roles_remove.remove(ewcfg.role_slimernalia)


	role_ids = []
	for role_id in roles_map_user:

		try:
			role_data = EwRole(id_server = id_server, id_role = role_id)
			roleName = role_data.name
			if roleName != None and roleName not in faction_roles_remove and roleName not in misc_roles_remove and roleName not in poi_roles_remove:
				role_ids.append(role_data.id_role)
		except:
			ewutils.logMsg('error: couldn\'t find role with id {}'.format(role_id))

	
	try:
		role_data = EwRole(id_server = id_server, name = faction_role)
		if not role_data.id_role in role_ids:
			role_ids.append(role_data.id_role)
			#ewutils.logMsg('found role {} with id {}'.format(role_data.name, role_data.id_role))
	except:
		ewutils.logMsg('error: couldn\'t find role {}'.format(faction_role))

	try:
		role_data = EwRole(id_server = id_server, name = pvp_role)
		if not role_data.id_role in role_ids:
			role_ids.append(role_data.id_role)
			#ewutils.logMsg('found role {} with id {}'.format(role_data.name, role_data.id_role))
	except:
		ewutils.logMsg('error: couldn\'t find role {}'.format(pvp_role))

	try:
		role_data = EwRole(id_server = id_server, name = active_role)
		if not role_data.id_role in role_ids:
			role_ids.append(role_data.id_role)
			#ewutils.logMsg('found role {} with id {}'.format(role_data.name, role_data.id_role))
	except:
		ewutils.logMsg('error: couldn\'t find role {}'.format(active_role))

	try:
		role_data = EwRole(id_server = id_server, name = tutorial_role)
		if not role_data.id_role in role_ids:
			role_ids.append(role_data.id_role)
			#ewutils.logMsg('found role {} with id {}'.format(role_data.name, role_data.id_role))
	except:
		ewutils.logMsg('error: couldn\'t find role {}'.format(tutorial_role))
		
	try:
		major_role_data = EwRole(id_server = id_server, name = poi_major_role)
		if not major_role_data.id_role in role_ids:
			role_ids.append(major_role_data.id_role)
			#ewutils.logMsg('found role {} with id {}'.format(role_data.name, role_data.id_role))
	except:
		ewutils.logMsg('error: couldn\'t find role {}'.format(poi_major_role))

	try:
		minor_role_data = EwRole(id_server = id_server, name = poi_minor_role)
		if not minor_role_data.id_role in role_ids:
			role_ids.append(minor_role_data.id_role)
			#ewutils.logMsg('found role {} with id {}'.format(role_data.name, role_data.id_role))
	except:
		ewutils.logMsg('error: couldn\'t find role {}'.format(poi_minor_role))

	try:
		role_data = EwRole(id_server = id_server, name = role_gellphone)
		if not role_data.id_role in role_ids:
			role_ids.append(role_data.id_role)
			#ewutils.logMsg('found role {} with id {}'.format(role_data.name, role_data.id_role))
	except:
		ewutils.logMsg('error: couldn\'t find role {}'.format(role_gellphone))

	try:
		role_data = EwRole(id_server = id_server, name = role_slimernalia)
		if not role_data.id_role in role_ids:
			role_ids.append(role_data.id_role)
			#ewutils.logMsg('found role {} with id {}'.format(role_data.name, role_data.id_role))
	except:
		ewutils.logMsg('error: couldn\'t find role {}'.format(role_slimernalia))

	# if faction_role not in role_names:
	# 	role_names.append(faction_role)
	# if poi_role != None and poi_role not in role_names:
	# 	role_names.append(poi_role)

	#replacement_roles = []
	#for name in role_names:
	#	role = roles_map.get(name)

	#	if role != None:
	#		replacement_roles.append(role)
	#	else:
	#		ewutils.logMsg("error: role missing \"{}\"".format(name))

	#ewutils.logMsg('looking for {} roles to replace'.format(len(role_ids)))
	replacement_roles = []

	for role in member.server.roles:
		if role.id in role_ids:
			#ewutils.logMsg('found role {} with id {}'.format(role.name, role.id))
			replacement_roles.append(role)

	#ewutils.logMsg('found {} roles to replace'.format(len(replacement_roles)))
	
	try:
		await client.replace_roles(member, *replacement_roles)
	except:
		ewutils.logMsg('error: failed to replace roles for {}'.format(member.display_name))

	if refresh_perms:
		await refresh_user_perms(client = client, id_server = id_server, used_member = member)

	#try:
	#	await client.replace_roles(member, *replacement_roles)
	#except:
	#	ewutils.logMsg('error: failed to replace roles for {}'.format(member.display_name))

# Removes and updates user permissions. It's got a fair amount of debuggers, sorry about the mess!
async def refresh_user_perms(client, id_server, used_member = None, startup = False):
	#try:
	server = client.get_server(id_server)
	
	member_list = []
	#subzone_member_list = []

	if not startup:
		for poi in ewcfg.poi_list:
			channel = ewutils.get_channel(server, poi.channel)
			if channel == None:
				ewutils.logMsg('Error: In refresh_user_perms, could not get channel for {}'.format(poi.channel))
				# Second try
				channel = ewutils.get_channel(server, poi.channel)
				if channel == None:
					continue
					
			#print('{} overwrites: {}'.format(poi.id_poi, channel.overwrites))
			member_count = 0
			for tuple in channel.overwrites:
				#print('tuplevar: {}'.format(tuple[0]) + '\n\n')
				if tuple[0] not in server.roles:
					member = tuple[0]
					member_list.append(tuple[0])
					
					# If we dont have the right member supplied in the function call, don't modify its permissions
					if member != used_member:
						continue
					
					user_data = EwUser(member=member)
					
					if user_data.poi != poi.id_poi:
	
						# Every 20 members, slow down a  bit
						member_count += 1
						if member_count == 20:
							member_count = 0
							await asyncio.sleep(2)
						
						# Incorrect overwrite found for user
						time_now_start = int(time.time())
	
						for i in range(ewcfg.permissions_tries):
							await client.delete_channel_permissions(channel, member)
	
						time_now_end = int(time.time())
	
						#print('took {} seconds to delete channel permissions'.format(time_now_end - time_now_start))
							
						#print('\ndeleted overwrite in {} for {}\n'.format(channel, member))
					
					#elif user_data.poi == poi.id_poi:
						correct_poi = ewcfg.id_to_poi.get(user_data.poi)
						
						correct_channel = ewutils.get_channel(server, correct_poi.channel)
						#correct_lan_channel = "{}-LAN-connection".format(correct_channel)
						
						permissions_dict = correct_poi.permissions
						overwrite = discord.PermissionOverwrite()
						overwrite.read_messages = True if ewcfg.permission_read_messages in permissions_dict[user_data.poi] else False
						overwrite.send_messages = True if ewcfg.permission_send_messages in permissions_dict[user_data.poi] else False
						
						# wall_overwrite = None
						# if user_data.poi in [ewcfg.poi_id_mine, ewcfg.poi_id_cv_mines, ewcfg.poi_id_tt_mines]:
						# 	wall_overwrite = discord.PermissionOverwrite()
						# 	wall_channel = ewutils.get_channel(server, correct_channel.name + '-wall')
						# 	overwrite.read_messages = True
						
						#print(permissions_dict[user_data.poi])
						time_now_start = int(time.time())
	
						for i in range(ewcfg.permissions_tries):
							await client.edit_channel_permissions(correct_channel, member, overwrite)
							# if wall_overwrite != None:
							# 	await client.edit_channel_permissions(wall_channel, member, wall_overwrite)
							#await client.edit_channel_permissions(correct_lan_channel, member, overwrite)
	
						time_now_end = int(time.time())
	
						#print('took {} seconds to update channel permissions'.format(time_now_end - time_now_start))
	
						#print('updated permissions for {} in {}'.format(member, user_data.poi))
						
						
						
					else:
						pass
						# print(member)
						# print(poi.str_name)
				
		if used_member not in member_list:
		# Member has no overwrites -- fix this:
			user_data = EwUser(member=used_member)
	
			# User might not have their poi set to downtown when they join the server.
			if user_data.poi == None:
				correct_poi = ewcfg.id_to_poi.get('downtown')
			else:
				correct_poi = ewcfg.id_to_poi.get(user_data.poi)
			
			#print(user_data.poi)
			
			correct_channel = ewutils.get_channel(server, correct_poi.channel)
	
			permissions_dict = correct_poi.permissions
			overwrite = discord.PermissionOverwrite()
			overwrite.read_messages = True if ewcfg.permission_read_messages in permissions_dict[user_data.poi] else False
			overwrite.send_messages = True if ewcfg.permission_send_messages in permissions_dict[user_data.poi] else False

			# wall_overwrite = None
			# if user_data.poi in [ewcfg.poi_id_mine, ewcfg.poi_id_cv_mines, ewcfg.poi_id_tt_mines]:
			# 	wall_overwrite = discord.PermissionOverwrite()
			# 	wall_channel = ewutils.get_channel(server, correct_channel.name + '-wall')
			# 	overwrite.read_messages = True
		
			time_now_start = int(time.time())
	
			for i in range(ewcfg.permissions_tries):
				await client.edit_channel_permissions(correct_channel, used_member, overwrite)
				# if wall_overwrite != None:
				# 	await client.edit_channel_permissions(wall_channel, used_member, wall_overwrite)
				#await client.edit_channel_permissions(correct_lan_channel, used_member, overwrite)

			time_now_end = int(time.time())
	
			#print('took {} seconds to generate channel permissions'.format(time_now_end - time_now_start))

			# print('corrected overwrite in {} for {}'.format(correct_channel, member))
			#print('\ngenerated permissions for {} in {}\n'.format(used_member, user_data.poi))
					
	# if used_member != None:
	# 	
	# 	

	# if startup:
	# 	# On startup, give out permissions where necessary. This should only need to be done once, when the update goes live.
	# 	
	# 	conn_info = ewutils.databaseConnect()
	# 	conn = conn_info.get('conn')
	# 	cursor = conn.cursor();
	# 
	# 	cursor.execute(
	# 		"SELECT id_user, poi FROM users WHERE id_server = %s".format(
	# 		), (
	# 			id_server,
	# 		))
	# 
	# 	users = cursor.fetchall()
	# 
	# 	user_count = 0
	# 	for user in users:
	# 		
	# 
	# 		current_member = server.get_member(user[0])
	# 		
	# 		#print(member)
	# 		#print('member list: {}'.format(member_list))
	# 		
	# 		user_poi = ewcfg.id_to_poi.get(user[1])
	# 
	# 		if current_member == None:
	# 			# Second try.
	# 			current_member = server.get_member(user[0])
	# 			if current_member == None:
	# 				continue
	# 				
	# 		# Every 20 users, slow down a bit
	# 		user_count += 1
	# 		if user_count == 20:
	# 			user_count = 0
	# 			await asyncio.sleep(2)
	# 				
	# 		if current_member in member_list:
	# 			# Member might have the wrong overwrite if the bot shut down/crashed right after persisting user data
	# 			user_data = EwUser(member=current_member)
	# 
	# 			for poi in ewcfg.poi_list:
	# 
	# 				channel = ewutils.get_channel(server, poi.channel)
	# 				if channel == None:
	# 					# Second try
	# 					channel = ewutils.get_channel(server, poi.channel)
	# 					if channel == None:
	# 						continue
	# 
	# 				# print('{} overwrites: {}'.format(poi.id_poi, channel.overwrites))
	# 				for tuple in channel.overwrites:
	# 					# print('tuplevar: {}'.format(tuple[0]) + '\n\n')
	# 					if tuple[0] not in server.roles:
	# 						member = tuple[0]
	# 
	# 						# If we dont have the right member in the member list, skip it.
	# 						if member != current_member:
	# 							continue
	# 
	# 						user_data = EwUser(member=member)
	# 
	# 						if user_data.poi != poi.id_poi:
	# 
	# 							# Incorrect overwrite found for user
	# 							time_now_start = int(time.time())
	# 
	# 							for i in range(ewcfg.permissions_tries):
	# 								await client.delete_channel_permissions(channel, current_member)
	# 
	# 							time_now_end = int(time.time())
	# 
	# 							#print('took {} seconds to delete channel permissions'.format(time_now_end - time_now_start))
	# 
	# 							#print('\ndeleted overwrite in {} for {}\n'.format(channel, current_member))
	# 							
	# 							# Only remove the current member once before moving on to the next code block.
	# 							if current_member in member_list:
	# 								member_list.remove(current_member)
	# 			
	# 		if current_member not in member_list:
	# 			# Member has no overwrite -- fix this:
	# 			user_data = EwUser(member=current_member)
	# 			correct_poi = ewcfg.id_to_poi.get(user_data.poi)
	# 
	# 			if correct_poi != None:
	# 				permissions_dict = user_poi.permissions
	# 			else:
	# 				continue
	# 			
	# 			correct_channel = ewutils.get_channel(server, correct_poi.channel)
	# 			#correct_lan_channel = "{}-LAN-connection".format(correct_channel)
	# 
	# 			#print(user_data.poi)
	# 			
	# 			overwrite = discord.PermissionOverwrite()
	# 			overwrite.read_messages = True if ewcfg.permission_read_messages in permissions_dict[user_data.poi] else False
	# 			overwrite.send_messages = True if ewcfg.permission_send_messages in permissions_dict[user_data.poi] else False
	# 			#overwrite.connect = True if ewcfg.permission_connect_to_voice in permissions_dict[user_data.poi] else False
	# 
	# 			wall_overwrite = None
	# 			if user_data.poi in [ewcfg.poi_id_mine, ewcfg.poi_id_cv_mines, ewcfg.poi_id_tt_mines]:
	# 				wall_overwrite = discord.PermissionOverwrite()
	# 				wall_channel = ewutils.get_channel(server, correct_channel.name + '-wall')
	# 				overwrite.read_messages = True
	# 			
	# 			time_now_start = int(time.time())
	# 
	# 			for i in range(ewcfg.permissions_tries):
	# 				await client.edit_channel_permissions(correct_channel, current_member, overwrite)
	# 				if wall_overwrite != None:
	# 					await client.edit_channel_permissions(wall_channel, current_member, wall_overwrite)
	# 				#await client.edit_channel_permissions(correct_lan_channel, current_member, overwrite)
	# 			
	# 			time_now_end = int(time.time())
	# 			
	# 			#print('took {} seconds to add channel permissions'.format(time_now_end - time_now_start))
	# 
	# 			# print('corrected overwrite in {} for {}'.format(correct_channel, member))
	# 			print('added permissions for {} in {}'.format(current_member, user_data.poi))

	#except:
		#ewutils.logMsg('caught exception while refreshing permissions')

# Change all permissions for POI channels
async def change_perms(cmd):
	member = cmd.message.author
	client = ewutils.get_client()

	if not member.server_permissions.administrator:
		return

	user_data = EwUser(member=member)

	allow_or_deny = None
	if cmd.tokens_count > 1:
		allow_or_deny = cmd.tokens[1].lower()

		if allow_or_deny == 'allow':
			allow_or_deny = True
			response = "DEBUG: ALLOWED READ AND SEND ACCESS TO ALL POI CHANNELS/CATEGORIES."
			await ewutils.send_message(client, cmd.message.channel, ewutils.formatMessage(member, response))
		elif allow_or_deny == 'deny':
			allow_or_deny = False
			response = "DEBUG: DENIED READ AND SEND ACCESS TO ALL POI CHANNELS/CATEGORIES."
			await ewutils.send_message(client, cmd.message.channel, ewutils.formatMessage(member, response))
		elif allow_or_deny == 'nuetral':
			allow_or_deny = 'None'
			response = "DEBUG: SET READ AND SEND ACCESS FOR ALL POI CHANNELS/CATEGORIES TO NEUTRAL."
			await ewutils.send_message(client, cmd.message.channel, ewutils.formatMessage(member, response))
		else:
			response = "ERROR: INVALID ANSWER."
			return await ewutils.send_message(client, cmd.message.channel, ewutils.formatMessage(member, response))

	server = client.get_server(id=user_data.id_server)

	for poi in ewcfg.poi_list:
		channel = ewutils.get_channel(server, poi.channel)
		
		if channel == None:
			print(poi.id_poi)
			continue
		
		role = discord.utils.get(server.roles, name='@everyone')

		overwrite = discord.PermissionOverwrite()
		
		if allow_or_deny == True:
			overwrite.read_messages = True
			overwrite.send_messages = True
		elif allow_or_deny == False:
			overwrite.read_messages = False
			overwrite.send_messages = False
		elif allow_or_deny == 'None':
			overwrite.read_messages = None
			overwrite.send_messages = None
			
		overwrite.read_message_history = None
		
		if allow_or_deny == True or allow_or_deny == False or allow_or_deny == 'None':
			
			for i in range(ewcfg.permissions_tries):
				await client.edit_channel_permissions(channel, role, overwrite)

			print('set read/send perms in {} to {}'.format(channel, allow_or_deny))
			
	print('got through all channels in changeperms')

# Remove all user overwrites in the server's POI channels
async def remove_user_overwrites(cmd):
	
	if not cmd.message.author.server_permissions.administrator:
		return
	
	server = cmd.message.server
	client = ewutils.get_client()
	
	for poi in ewcfg.poi_list:
		
		searched_channel = poi.channel
		
		channel = ewutils.get_channel(server, searched_channel)
		
		if channel == None:
			# Second try
			channel = ewutils.get_channel(server, searched_channel)
			if channel == None:
				continue
				
		# print('{} overwrites: {}'.format(poi.id_poi, channel.overwrites))
		for tuple in channel.overwrites:
			# print('tuplevar: {}'.format(tuple[0]) + '\n\n')
			if tuple[0] not in server.roles:
				member = tuple[0]
				
				print('removed overwrite in {} for {}'.format(channel, member))

				for i in range(ewcfg.permissions_tries):
					await client.delete_channel_permissions(channel, member)
		

	response = "DEBUG: ALL USER OVERWRITES DELETED."
	return await ewutils.send_message(client, cmd.message.channel, ewutils.formatMessage(cmd.message.author, response))