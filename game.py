import pyautogui 
from pathlib import Path
import pytesseract
PROJECT_ROOT = Path(__file__).parent
import pyscreeze
#from pyscreeze import ImageNotFoundException
import time
pyautogui.useImageNotFoundException()
from PIL import Image
'''
pyautogui.moveTo(100, 550)

pyautogui.PAUSE = 0.01
pyautogui.click(clicks=5000)'''

'''
#im = pyautogui.screenshot(region=(0,0, 300, 400))
loc2 =  pyautogui.locateOnScreen((str(PROJECT_ROOT) + "/" + 'seven.png'), 
                                 confidence=0.5, region=(0,0, 700, 1000),
                                 grayscale=True)


print(loc2)
location = pyautogui.center(loc2)'''
'''
pic_dic = {"one.png": [], "two.png":[], "three.png":[], "four.png":[], "five.png":[], "six.png":[], "seven.png":[], "eight.png":[]}

pic_list = list(pic_dic)
for i in range(len(pic_list)):
    try:
        x,y = pyautogui.locateCenterOnScreen(
            str(PROJECT_ROOT) + "/" + pic_list[i], 
            confidence= 0.8,
            grayscale= False)
    except pyautogui.ImageNotFoundException:
        x,y = 0,0

    pic_dic[pic_list[i]].append([x/2,y/2])
    #pic_dicx[pic_list[i]].append(x)

#x,y = pic_dic["four.png"][0]
#pyautogui.moveTo(x/2,y/2) 
#print(x/2,y/2)
#print(pic_dic)'''

for runs in range(100):
#block_dic = {"one": [], "two":[], "three":[], "four":[], "five":[], "six":[], "seven":[], "eight":[]}
    print("RUN:", runs+1)
    '''def check():
        pic_dic = {"one.png": [], "two.png":[], "three.png":[], "four.png":[], "five.png":[], "six.png":[], "seven.png":[], "eight.png":[]}
        pic_list = list(pic_dic)
        for i in range(len(pic_list)):
            try:
                x,y = pyautogui.locateCenterOnScreen(
                    str(PROJECT_ROOT) + "/" + pic_list[i], 
                    confidence= 0.8,
                    grayscale= False)
            except pyscreeze.ImageNotFoundException:
                x,y = 0,0


            pic_dic[pic_list[i]].append([x/2,y/2])

        pic_dic2 = {"one.png": [], "two.png":[], "three.png":[], "four.png":[], "five.png":[], "six.png":[], "seven.png":[], "eight.png":[]}
        pic_list2 = list(pic_dic)
        x,y = pyautogui.locateCenterOnScreen(
                str(PROJECT_ROOT) + "/" + "giveup.png", 
                confidence= 0.8,
                grayscale= False)

        pyautogui.moveTo(x/2,y/2)
        pyautogui.click()

        x,y = pyautogui.locateCenterOnScreen(
                str(PROJECT_ROOT) + "/" + "restart.png", 
                confidence= 0.6,
                grayscale= False)
        pyautogui.moveTo(x/2,y/2)
        pyautogui.click()
        for i in range(len(pic_list2)):
            try:
                x,y = pyautogui.locateCenterOnScreen(
                    str(PROJECT_ROOT) + "/" + pic_list2[i], 
                    confidence= 0.8,
                    grayscale= False)
            except pyautogui.ImageNotFoundException:
                x,y = 0,0

            pic_dic2[pic_list2[i]].append([x/2,y/2])
        
        coord_list1 = list(pic_dic.values())
        coord_list2= list(pic_dic2.values())

        table = []
        for i in range(len(coord_list1)):
            check = coord_list1[i]
            for j in range(len(coord_list2)):
                if check != coord_list2[j]:
                    missing = check

        return missing'''
            

    def image_search(number):
        index = {"one":"a1.png", "two":"a2.png", "three":"a3.png", "four":"a4.png"}
        picture  = index[number]
        pic_dic = {"a1.png": [], "a2.png":[], "a3.png":[], "a4.png":[]}
        pic_list = list(pic_dic)
        for i in range(len(pic_list)):
            try:
                location = pyautogui.locateAllOnScreen(
                    str(PROJECT_ROOT) + "/" + pic_list[i], 
                    confidence= 0.83,
                    grayscale= False)
            except pyautogui.ImageNotFoundException:
                x,y = 0,0

            pic_dic[pic_list[i]].append(list(location))


        loc_list = (pic_dic[picture])[0]
        for i in range(len(loc_list)):
            x,y = pyautogui.center((loc_list)[i])
            (loc_list)[i] = x/2, y/2
        for i in range(len(loc_list)):
            x,y = (loc_list)[i]
            new_list = loc_list
            for j in range(len(new_list)):
                check_value = new_list[j]
                x2, y2 = check_value
                if abs(x-x2) < 2 and abs(y -y2) < 2:
                    new_list[j] = x,y

        final_list = list(set(new_list))
        print("number of",number, "is" , len(final_list))
        #for i in range(len(final_list)):
        #pyautogui.moveTo(final_list[i])
        return final_list


    def num_dic_create():
        num_dic = {"one":[], "two":[], "three":[],"four":[]}
        num_dic_key = list(num_dic)
        raw_list = []
        for i in range(len(num_dic_key)):
            coord = image_search(num_dic_key[i])
            num_dic[num_dic_key[i]] = coord
            raw_list.append(coord)
        

        x_list =[]
        y_list =[]
        for i in range(len(raw_list)):
            for j in range(len(raw_list[i])):
                x,y = (raw_list[i])[j]

                x_list.append(x)
                for k in range(len(x_list)):
                        x = (x_list)[k]
                        xnew_list = x_list
                        for l in range(len(xnew_list)):
                            check_value = xnew_list[l]
                            x2 = check_value
                            if abs(x-x2) < 2:
                                xnew_list[l] = x
                y_list.append(y)
                for m in range(len(y_list)):
                        y = (y_list)[m]
                        ynew_list = y_list
                        for n in range(len(ynew_list)):
                            check_value = ynew_list[n]
                            y2 = check_value
                            if abs(y-y2) < 2:
                                ynew_list[n] = y
            
        column_list = list(set(x_list))
        column_list.sort()
        row_list = list(set(y_list))
        row_list.sort()


        coord_list = []
        for i in range(len(row_list)):
            y = row_list[i]
            for j in range(len(column_list)):
                x =  column_list[j]
                coord_list.append((x,y))

        square_list = ["11", "12", "13","14",
                    "21", "22", "23","24",
                    "31", "32", "33", "34",
                    "41", "42", "43","44"]
        value_on_screen_list = []



    
        for i in range(len(coord_list)):
            trial_coord = coord_list[i]
    

            num_dic_value = list(num_dic.values())

            for k in range(len(num_dic_key)):
                name = num_dic_key[k]
                value = num_dic[name]
                for j in range(len(value)):
                    number_coords = value[j]
                    numx, numy = number_coords
                    x,y = trial_coord

                    if abs(x  - numx) < 1 and abs(y- numy)<1: 
                        number_on_screen = num_dic_key[k]

            ass_value = {"one":1 , "two":2, "three": 3, "four": 4}
            value_on_screen = ass_value[number_on_screen]

            info = [value_on_screen, trial_coord]

            

            value_on_screen_list.append(info)


        square_dic = dict(zip(square_list, value_on_screen_list))
        return square_dic



    def num_dic_clean(square_dic):
        keys = list(square_dic)
        location_list= []
        for i in range(len(keys)):
            value = square_dic[keys[i]]
            number = value[0]
            location_list.append(number)
        

        return location_list

    square_dic = num_dic_create()
    

    def num_dic_override(square_dic):
        userinput = 4413122443342234
        userinput_list = [int(x) for x in str(userinput)]

        keys = list(square_dic)
        location_list= []
        for i in range(len(keys)):
            value = square_dic[keys[i]]
            (square_dic[keys[i]])[0] = userinput_list[i]

        return square_dic

    #square_dic = num_dic_override(square_dic)

    print("original:", num_dic_clean(square_dic))

    copy_of_square_dic = num_dic_clean(square_dic)


    keys = list(square_dic.keys())

    square_list = list(square_dic.values())
    coord_list = []


    for i in range(len(square_list)):
        clicking_circle_1 = square_list[i]
        finding_clicking_circle_coord = clicking_circle_1[1]
        coord_list.append(finding_clicking_circle_coord)


    coord_dict = dict(zip(coord_list, keys))


    def calculation(changes, clicking_circle_coord):
        affect_button = coord_dict[clicking_circle_coord]

        affect_dic11 = {"11":0, "12": 0,
                        "21":0,"22":0}

        affect_dic12 = {"11":0, "12": 0, "13":0,
                        "21":0,"22":0, "23":0}

        affect_dic13 = {"12":0, "13": 0, "14":0,
                        "22":0,"23":0, "24":0}

        affect_dic14 = {"13":0, "14": 0,
                        "23":0,"24":0}

        affect_dic21 = {"11":0, "12": 0, 
                        "21":0,"22":0, 
                        "31":0, "32":0}

        affect_dic22 = {"11":0, "12":0, "13":0,
                        "21":0,"22":0, "23":0,
                        "31":0, "32":0, "33":0}

        affect_dic23 = {"12":0, "13":0, "14":0,
                        "22":0,"23":0, "24":0,
                        "32":0, "33":0, "34":0}

        affect_dic24 = {"13":0, "14": 0, 
                        "23":0,"24":0, 
                        "33":0, "34":0}

        affect_dic31 = {"21":0, "22": 0, 
                        "31":0,"32":0, 
                        "41":0, "42":0}

        affect_dic32 = {"21":0, "22":0, "23":0,
                        "31":0,"32":0, "33":0,
                        "41":0, "42":0, "43":0}

        affect_dic33 = {"22":0, "23":0, "24":0,
                        "32":0,"33":0, "34":0,
                        "42":0, "43":0, "44":0}

        affect_dic34 = {"23":0, "24": 0, 
                        "33":0,"34":0, 
                        "43":0, "44":0}

        affect_dic41 = {"31":0, "32": 0,
                        "41":0,"42":0}

        affect_dic42 = {"31":0, "32": 0, "33":0,
                        "41":0,"42":0, "43":0}

        affect_dic43 = {"32":0, "33": 0, "34":0,
                        "42":0,"43":0, "44":0}

        affect_dic44 = {"33":0, "34": 0,
                        "43":0,"44":0}

        big_dic = {"11":affect_dic11, "12":affect_dic12, "13": affect_dic13, "14":affect_dic14,
                "21":affect_dic21, "22":affect_dic22, "23": affect_dic23, "24":affect_dic24,
                "31":affect_dic31, "32":affect_dic32, "33": affect_dic33, "34":affect_dic34,
                "41":affect_dic41, "42":affect_dic42, "43": affect_dic43, "44":affect_dic44,}
        
        dic_to_change = big_dic[affect_button]
        neigbour = list(dic_to_change)
        for i in range(len(neigbour)):
            dic_to_change[neigbour[i]]+= changes
        
        big_dic[affect_button] = dic_to_change

        return dic_to_change 

    def num_click(value_to_change): 
        value = value_to_change
        if value ==  1: 
            num_taps = 0
        elif value  == 4:
            num_taps = 2
        else: 
            num_taps = 6 - value
        #pyautogui.moveTo(click_coord)
        ##pyautogui.click(clicks=num_taps)
        return num_taps

    action_list = []

    for i in range(16): 
        if i < 3:
            square_list = list(square_dic.values())
            target_circle = square_list[i]
            target_circle_value= target_circle[0]

            clicking_circle = square_list[i+5]
            clicking_circle_coord = clicking_circle[1]
            if target_circle_value ==  1: 
                changes = 0
            else: 
                changes = 5 - target_circle_value
            
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            #click_times = num_click(target_circle_value)
            '''if i > 0:
                click_times = num_click(target_circle_value) - 1
                if click_times < 0:
                    click_times = 0 '''

            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)

        if i == 3:
            compare_value = (square_dic[keys[i]])[0]
            clicking_circle_coord = (square_dic[keys[i+2]])[1]

            changes = compare_value - 1

            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4


            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)

            if compare_value ==  1: 
                    changes = 0
            else: 
                    changes = 5 - compare_value

            clicking_circle_coord = (square_dic[keys[i-3]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            clicking_circle_coord = (square_dic[keys[i]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4
        
            print("after first layer:", num_dic_clean(square_dic))
        if i > 3 and i < 7:
            square_list = list(square_dic.values())
            target_circle = square_list[i]
            target_circle_value= target_circle[0]

            clicking_circle = square_list[i+5]
            clicking_circle_coord = clicking_circle[1]
            if target_circle_value ==  1: 
                changes = 0
            else: 
                changes = 5 - target_circle_value
            
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)


        if i == 7:
            compare_value = (square_dic[keys[i]])[0]
            clicking_circle_coord = (square_dic[keys[i+2]])[1]

            changes = compare_value - 1

            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4


            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)

            if compare_value ==  1: 
                    changes = 0
            else: 
                    changes = 5 - compare_value

            clicking_circle_coord = (square_dic[keys[i+1]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            clicking_circle_coord = (square_dic[keys[i+4]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4
            print("after second layer:", num_dic_clean(square_dic))




        if i > 7 and i < 11:
            square_list = list(square_dic.values())
            target_circle = square_list[i]
            target_circle_value= target_circle[0]

            clicking_circle = square_list[i+5]
            clicking_circle_coord = clicking_circle[1]
            if target_circle_value ==  1: 
                changes = 0
            else: 
                changes = 5 - target_circle_value
            
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)


        if i == 11:
            compare_value = (square_dic[keys[i]])[0]
            clicking_circle_coord = (square_dic[keys[i+2]])[1]

            changes = compare_value - 1

            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4


            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)

            if compare_value ==  1: 
                    changes = 0
            else: 
                    changes = 5 - compare_value

            clicking_circle_coord = (square_dic[keys[i+1]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            clicking_circle_coord = (square_dic[keys[i+4]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4
            print("after third layer:", num_dic_clean(square_dic))
        

        if i == 12:
            compare_value = (square_dic[keys[i+1]])[0]
            clicking_circle_coord = (square_dic[keys[i-8]])[1]

            changes = compare_value - 1

            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4


            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)

            if compare_value ==  1: 
                    changes = 0
            else: 
                    changes = 5 - compare_value

            clicking_circle_coord = (square_dic[keys[0]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            clicking_circle_coord = (square_dic[keys[i]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4
        
            print("after 3.5 layer:", num_dic_clean(square_dic))

        if i == 13:
            compare_value = (square_dic[keys[i+1]])[0]
            clicking_circle_coord = (square_dic[keys[7]])[1]

            changes = compare_value - 1

            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4


            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)

            if compare_value ==  1: 
                    changes = 0
            else: 
                    changes = 5 - compare_value

            clicking_circle_coord = (square_dic[keys[3]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            clicking_circle_coord = (square_dic[keys[15]])[1]
            current_action = [clicking_circle_coord, changes]
            action_list.append(current_action)
            affected_buttons_dic = calculation(changes, clicking_circle_coord)
            affected_buttons_list = list(affected_buttons_dic)
            for j in range(len(affected_buttons_list)):
                affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                if (square_dic[affected_buttons_list[j]])[0] > 4:
                    (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4
        
            print("after 3.5 layer:", num_dic_clean(square_dic))

        if i == 14:
            print("doing corners")
            coord_order = [(square_dic[keys[6]])[1],
                            (square_dic[keys[14]])[1],
                            (square_dic[keys[2]])[1],
                            (square_dic[keys[4]])[1],
                            (square_dic[keys[7]])[1],
                            (square_dic[keys[0]])[1],
                            (square_dic[keys[3]])[1],
                            (square_dic[keys[12]])[1],
                            (square_dic[keys[15]])[1]]
            
            compare_value = (square_dic[keys[12]])[0]
            taps_list = [0,0,0,0,0,0,0,0,0]
            if compare_value == 4:
                taps_list = [1,3,3,3,3,1,1,1,1]
                print(4)
            if compare_value == 2:
                taps_list = [3,1,1,1,1,3,3,3,3]
                print(2)
            if compare_value == 3:
                taps_list = [2,2,2,2,2,2,2,2,2]
                print(3)
            algo = []

            for coordindates in range(len(coord_order)):
                taps = taps_list[coordindates]
                coord_alg = coord_order[coordindates]
                current_action = [coord_alg, taps]
                action_list.append(current_action)
            


                affected_buttons_dic = calculation(taps, coord_alg)
                affected_buttons_list = list(affected_buttons_dic)
                for j in range(len(affected_buttons_list)):
                    affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                    (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                    if (square_dic[affected_buttons_list[j]])[0] > 4:
                        (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            print("after 3.75 layer:", num_dic_clean(square_dic))
            

        if i == 15:
            print("doing corners")
            coord_order = [(square_dic[keys[5]])[1],
                            (square_dic[keys[13]])[1],
                            (square_dic[keys[1]])[1],
                            (square_dic[keys[7]])[1],
                            (square_dic[keys[4]])[1],
                            (square_dic[keys[0]])[1],
                            (square_dic[keys[3]])[1],
                            (square_dic[keys[12]])[1],
                            (square_dic[keys[15]])[1]]
            
            compare_value = (square_dic[keys[15]])[0]
            taps_list = [0,0,0,0,0,0,0,0,0]
            if compare_value == 4:
                taps_list = [1,3,3,3,3,1,1,1,1]
                print(4)
            if compare_value == 2:
                taps_list = [3,1,1,1,1,3,3,3,3]
                
                print(2)
            if compare_value == 3:
                taps_list = [2,2,2,2,2,2,2,2,2]
                print(3)
            algo = []

            for coordindates in range(len(coord_order)):
                taps = taps_list[coordindates]
                coord_alg = coord_order[coordindates]
                current_action = [coord_alg, taps]
                action_list.append(current_action)
            
                affected_buttons_dic = calculation(taps, coord_alg)
                affected_buttons_list = list(affected_buttons_dic)
                for j in range(len(affected_buttons_list)):
                    affected_buttons_change_by = affected_buttons_dic[affected_buttons_list[j]]
                    (square_dic[affected_buttons_list[j]])[0] +=  affected_buttons_change_by
                    if (square_dic[affected_buttons_list[j]])[0] > 4:
                        (square_dic[affected_buttons_list[j]])[0] = (square_dic[affected_buttons_list[j]])[0] - 4

            print("after 4 layer:", num_dic_clean(square_dic))
        

    pyautogui.PAUSE = 0
    def solving(action_list):
        times_list = []
        for i in range(len(action_list)):
            times = (action_list[i])[1]
            times_list.append(times)
        for k in range(len(times_list)):
            times = times_list[k] 
            if runs == 0:
                if times == 0:
                    times_list[k] += 0
                else: 
                    times_list[k] += 1
                    break
            else:
                times_list[k] += 0
        
        start = time.time()
        for j in range(len(action_list)):
            if times_list[j] == 0:
                continue
            x,y = (action_list[j])[0]
            #pyautogui.moveTo(to_click)

            times = times_list[j]
            pyautogui.click(x,y,times)
  
        end = time.time()
        elapsed_time = end - start
        return elapsed_time
    
    elapsed_time = solving(action_list)
    
    results = [copy_of_square_dic,elapsed_time]

    print("total time used:",elapsed_time,"s")
    while True:
        try:
            x,y = pyautogui.locateCenterOnScreen(
                    str(PROJECT_ROOT) + "/" + "great.png", 
                    confidence= 0.6,
                    grayscale= False)
            break
        except:
            x,y = pyautogui.locateCenterOnScreen(
                    str(PROJECT_ROOT) + "/" + "give.png", 
                    confidence= 0.8,
                    grayscale= False)
            pass
    #pyautogui.moveTo(x/2,y/2)
    pyautogui.click(x/2,y/2,clicks = 1)

    

''' x,y = pyautogui.locateCenterOnScreen(
                str(PROJECT_ROOT) + "/" + "great.png", 
                confidence= 0.8,
                grayscale= False)


if pyautogui.ImageNotFoundException():
    x,y = pyautogui.locateCenterOnScreen(
                str(PROJECT_ROOT) + "/" + "give.png", 
                confidence= 0.8,
                grayscale= False)
    '''



    




'''
trial1 = {'one.png': [[129.0, 625.0]], 'two.png': [[129.0, 452.5]], 'three.png': [[128.5, 798.0]], 'four.png': [[301.5, 452.5]], 'five.png': [[474.0, 625.0]], 'six.png': [[474.0, 452.5]], 'seven.png': [[474.0, 797.5]], 'eight.png': [[301.5, 625.0]]}

trial2 = {'one.png': [[129.0, 797.5]], 'two.png': [[474.5, 625.0]], 'three.png': [[301.5, 452.5]], 'four.png': [[129.0, 452.5]], 'five.png': [[474.0, 798.0]], 'six.png': [[301.5, 797.5]], 'seven.png': [[301.5, 625.0]], 'eight.png': [[474.0, 452.5]]}

coord_list1 = list(trial1.values())
coord_list2= list(trial2.values())



table = []
for i in range(len(coord_list1)):
    check = coord_list1[i]
    for j in range(len(coord_list2)):
        if check != coord_list2[j]:
            missing = check

            
print(missing)

print(coord_list1[0])
print(coord_list2[0])'''
#new_list = list(set(coord_list).difference(coord_list2))

#print(coord_list)


#x,y = location
#text = pytesseract.image_to_string((str(PROJECT_ROOT) + "/" + 'trial.png'),lang='eng')

#print(text)#
#print(im)


