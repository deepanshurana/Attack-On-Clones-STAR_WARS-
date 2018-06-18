import random 
import textwrap


def show_message(dotted_line,width):

    print(dotted_line)
    print("\033[1m"+ "Attack of clones:" + "\033[0m")

    message = (
        "The war between humans and their arch enemies , Clones was in the offing. Obi-Wan, one of the brave Jedi on his way ," 
        "he spotted a small isolated settlement .Tired and hoping to replenish his food stock , he decided to take a detour." 
        "As he approached the village, he saw five residence , there was no one to be seen around.He decided to enter" )
    print(textwrap.fill(message, width = width))

def show_mission(dotted_line):
    print("\033[1m"+ "Mission:" + "\033[0m")
    print('\t Choose the hit where Obi wan can rest...')
    print("\033[1m"+ "TIP:" + "\033[0m")
    print("Be careful as there are Stormtroopers lurking around!")
    print(dotted_line)


def occupy_huts():
    huts = []

    while len(huts) < 5:
        random_choice = random.choice(occupants)
        huts.append(random_choice)
    return huts



def process_user_choice(): 
     message = "\033[1m"+ "Choose the hut to enter (1-5) " + "\033[0m"
     uc = input("\n" + message)
     index = int(uc)
     return index

   


def reveal_occcupants(index,huts,dotted_line):

    
    print("Revealing the occupants...")
    msg = ""
    for i in range (len(huts))  :
        occupant_info = "|%d : %s|" % (i + 1, huts[i])
        msg += occupant_info + " "
    print(msg + "\t")
    print(dotted_line)


def printbold(message, end = '\n'):
    print("\033[1m" + message +"\033[0m")

def attack(health_meter):
    hit_list = 4*['Jedi'] + 6*['clones']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10,15)
    health_meter[injured_unit] = max(hit_points - injury , 0)
    printbold("ATTACK!")
    show_health(health_meter)
            
def show_health(health_meter,bold = True):
    printbold("HEALTH :  Obi Wan: %d StormTrooper: %d " % (health_meter['Jedi'],health_meter['clones']))

def reset_meter(health_meter):
    health_meter['Jedi'] = 40
    health_meter['clones'] = 30


def enter_huts(index,huts,dotted_line): 
    print("\033[1m"+ "Entering Hut %d ..." %index + "\033[0m")
    reset_meter(health_meter)
    if huts[index - 1] != 'Stormtrooper':
        print("\033[1m"+ "Obi Wan Is Safe..." + "\033[0m")
    else:
        printbold('STORMTROOPER SIGHTED!')
        show_health (health_meter, bold = True)
        continue_attack = True
        while continue_attack:
            continue_attack = raw_input("....continue attack (y/n): ")
            if continue_attack == 'n':
                printbold("RUNNING AWAY WITH FOLLOWING HEALTH STATUS...")
                show_health(health_meter, bold = True)
                printbold("Game Over!")
                break
            attack(health_meter)

            if health_meter['clones'] <= 0:
                printbold("The Force Is Strong With You ...Victory!")
                break
            if health_meter['Jedi'] <= 0:
                printbold("I find your lack of faith disturbing...You Lose!")
                break
    print(dotted_line)


def run():
    keep_playing = 'y'
    global health_meter
    health_meter = {}
    global occupants 
    occupants = ['Stormtrooper','Jedi Hideout']
    width = 70
    dotted_line = '-' * width

    show_message(dotted_line, width)
    show_mission(dotted_line)

    while keep_playing == 'y':
         huts = occupy_huts()
         index = process_user_choice()
         reveal_occcupants(index,huts,dotted_line)
         enter_huts(index,huts,dotted_line)
         keep_playing = raw_input("Play Again?(y/n)")
         

if __name__ == '__main__':
    run()
 




