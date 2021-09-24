# A. BENJAMIN TREGO
# GAME STORE - GAME NIGHT CALCULATOR
# CODECADEMY - OFF PLATFORM PROJECT

# EMPTY LIST TO STORE GAMER INFORMATION AND AVAILABILITY
gamers = []


# FUNCTION - ADD NEW GAMERS TO EXISTING LIST
def add_gamer(gamer, gamers_list):
    if "name" and "availability" in gamer:
        gamers_list.append(gamer)
    else:
        print("Missing input. Please try again.")
        
    return gamers_list


# CREATE LIST OF ALL GAMERS
kimberly = {"name":"Kimberly Warner","availability": ["Monday", "Tuesday", "Friday"]}

add_gamer(kimberly, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


# CREATE FREQUENCY TABLE
def build_daily_frequency_table():
    dict = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0,
                   "Friday": 0, "Saturday": 0, "Sunday":0}
    return dict


# STORE TABLE
count_availability = build_daily_frequency_table()


# FUNCTION TO CALCULATE AVAILABILITY 
def calculate_availability(gamers_list, available_frequency):
    
    for gamer in gamers_list:
            if "Monday" in gamer["availability"]:
                available_frequency["Monday"] += 1
            if "Tuesday" in gamer["availability"]:
                available_frequency["Tuesday"] += 1
            if "Wednesday" in gamer["availability"]:
                available_frequency["Wednesday"] += 1
            if "Thursday" in gamer["availability"]:
                available_frequency["Thursday"] += 1
            if "Friday" in gamer["availability"]:
                available_frequency["Friday"] += 1
            if "Saturday" in gamer["availability"]:
                available_frequency["Saturday"] += 1
            if "Sunday" in gamer["availability"]:
                available_frequency["Sunday"] += 1
                
    return available_frequency


# CALCULATE AVAILABILITY AND POPULATE TABLE
calculate_availability(gamers, count_availability)

print(count_availability)


# FUNCTION TO DETERMINE NIGHT WITH MOST AVAILABILITY
def find_best_night(availability_table):
    
    max_value = 0
    best_night = ""
    
    for key,value in availability_table.items():
        
        if value >= max_value:
            max_value = value
            best_night = key
            
    return best_night 


# DETERMINE BEST GAME NIGHT AND PRINT
game_night = find_best_night(count_availability)

print(game_night)


# FUNCTION TO CREATE LIST OF GAMERS AVAILABLE ON GIVEN NIGHT
def available_on_night(gamers_list, day): 
   
    gamers_available = []
    
    for dict in gamers_list:
        for key,value in dict.items():
              if day in value:
                gamers_available.append(dict["name"])
           
    return gamers_available

# DETERMINE GAMERS AVAILABLE ON GIVEN NIGHT AND PRINT LIST OF POTENTIAL ATTENDEES
attending_game_night = available_on_night(gamers, game_night)
print("List of potential attendees: ", attending_game_night)



name = "name"
game = "game"
day_of_week = "day"

form_email = "Hi, {}! {} will be played on {}. Hope to see you there!"

print(form_email.format(name, game, day_of_week))


##########################


def send_email(gamers_who_can_attend, day, game):
    message = ""
    for gamer in gamers_who_can_attend:
        message = (form_email.format(gamer, game, day))
        print(message)

send_email(attending_game_night, game_night, "Dragons and Demons")


###########################


unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer["availability"]]

second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)

second_night = find_best_night(second_night_availability)


###########################


available_second_game_night = available_on_night(gamers, second_night)

send_email(available_second_game_night, second_night, "Dragons and Demons")

