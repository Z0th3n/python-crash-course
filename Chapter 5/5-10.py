# Checking usernames
current_users = ['John', 'Pedro', 'Manolo', 'Michael', 'Pepe']
new_users = ['pedro', 'juanjo', 'maría', 'miguelito', 'pepe']

# Checking used nicknames
for new_user in new_users:
    if new_user.title() in current_users:
        print("Sorry amigo, pero " + new_user + " ya existe.")
    else:
        print("Ok, aceptamos " + new_user + " como nuevo usuario.")
