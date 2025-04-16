def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}! z miejscowości {user["location"]} opublikował {user['posts']} postów")

def add_user(users_data: list) -> None:
    user_name = input("podaj imię nowego użytkownika: ")
     user_location = input("podaj lokalizacje nowego znajomego: ")
      user_posts = int(input("podaj liczbę postów "))
       users_data.append({"name": user_name, "location": user_location, "posts": user_posts})
