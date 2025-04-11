def get_user_info(users_data: list) -> None:
    for user in users:
        print(f"Twój znajomy {user['name']}! z miejscowości {user["location"]} opublikował {user['posts']} postów")