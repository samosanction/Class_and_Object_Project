class Building:
    def __init__(self, color, structure, owner):
        self.color = color
        self.structure = structure
        self.owner = owner

    def change_color(self):
        new_color = str(input('what is the new color you want? ...\n'))
        self.color = new_color
        print(f'Your Building Color has been updated to {self.color}')
        system_home()

    def change_structure(self):
        new_structure = input('what is the new structure you want? ...\n')
        self.structure = new_structure
        print(f'Your Building Structure has been updated to {self.structure}')
        system_home()

    def change_owner(self):
        new_owner = input('who is the new owner of the building? ...\n')
        self.owner = new_owner
        print(f'Your Building owner has been updated to {self.owner}')
        system_home()


building1 = Building('red', 'KingdomHall', 'Samuel ogogo')
building2 = Building('blue', 'school', 'David')
building3 = Building('green', 'store', 'Doris')

print(
    f'\nBuilding1 Color: {building1.color}, Owner: {building1.owner}, Structure: {building1.structure}')
print(
    f'\nBuilding1 Color: {building2.color}, Owner: {building2.owner}, Structure: {building2.structure}')
print(
    f'\nBuilding1 Color: {building3.color}, Owner: {building3.owner}, Structure: {building3.structure}')


# Selection of the building to be changed
def select_building():
    while True:
        try:
            print(
                'Please select your building .\n 1. Building1. \n 2. Building2 \n 3. Building3\n\n')
            building = int(input('Here..\n'))

            if building == 1:
                return 'building1'
            if building == 2:
                return 'building2'
            if building == 3:
                return 'building3'
            else:
                print('Wrong input!!!')
        except ValueError:
            print('Exception !!!')


def system_home():
    print('\n\nThings you can do to your house \n 1. Change color.\n 2. Change Owner. \n 3. Change Building Structure')
    print('\n********** Type \'end\' to STOP this program **********')
    print('\n********** Press 4 to view Current Building details this program **********')
    user_input_ = input('\n\nplease input 1, 2, or 3 to select any of the above task ....\n...')
    if user_input_ == '1':
        selected_building = select_building()
        if selected_building == 'building1':
            building1.change_color()
        if selected_building == 'building2':
            building2.change_color()
        if selected_building == 'building3':
            building3.change_color()
    elif user_input_ == '2':
        selected_building = select_building()
        if selected_building == 'building1':
            building1.change_owner()
        if selected_building == 'building2':
            building2.change_owner()
        if selected_building == 'building3':
            building3.change_owner()
    elif user_input_ == '3':
        selected_building = select_building()
        if selected_building == 'building1':
            building1.change_structure()
            system_home()
        if selected_building == 'building2':
            building2.change_structure()
            system_home()
        if selected_building == 'building3':
            building3.change_structure()
            system_home()
    elif user_input_ == 'end':
        exit()
    elif user_input_ == '4':
        print(
            f'\nBuilding1 Color: {building1.color}, Owner: {building1.owner}, Structure: {building1.structure}')
        print(
            f'\nBuilding1 Color: {building2.color}, Owner: {building2.owner}, Structure: {building2.structure}')
        print(
            f'\nBuilding1 Color: {building3.color}, Owner: {building3.owner}, Structure: {building3.structure}')
        system_home()
    else:
        print('Wrong input!!! pls try again. Select 1, 2, or 3 on your keyboard\n\n')
        system_home()


system_home()
