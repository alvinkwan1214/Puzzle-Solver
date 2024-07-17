import pyautogui 
from pathlib import Path
import pytesseract
PROJECT_ROOT = Path(__file__).parent
import pyscreeze
#from pyscreeze import ImageNotFoundException
import time
pyautogui.useImageNotFoundException()
from PIL import Image
from math import sqrt 
import statistics
runs  = 0 
time_list = []
while runs < 1000000:
    print("Run:", 1+runs)
    def image_search(number):
            index = {"one":"Game2_12.png", "two":"Game2_22.png"}
            picture  = index[number]
            pic_dic = {"Game2_12.png": [], "Game2_22.png":[]}
            pic_list = list(pic_dic)
            for i in range(len(pic_list)):
                try:
                    location = pyautogui.locateAllOnScreen(
                        str(PROJECT_ROOT) + "/" + pic_list[i], 
                        confidence= 0.85,
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

    def clean_bigdic(big_dic):
        key  = list(big_dic)
        value_list = []
        for i in range(len(key)):
            value = (big_dic[key[i]])[1]
            value_list.append(value)
        
        result = dict(zip(key, value_list))

        return result
    
    def num_dic_create():
        '''numbers = ["one", "two"]
        loc_list = []
        x_list = []
        y_list = []
        for i in range(len(numbers)):
            loc = image_search(numbers[i])
            for j in range(len(loc)):
                x, y = loc[j]
                x_list.append(x)
                y_list.append(y)

                x_list.sort()
                y_list.sort()
            #loc_list.append(loc)
        #numbers_dic = dict(zip(numbers, loc_list))
        print(x_list)
        print(y_list)'''

        num_dic = {"one":[], "two":[]}
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

        mew = []
        while len(column_list) != 0:
            column = column_list[0]
            m_column = column_list[-1]

            if len(column_list) == 1:
                mew.append(column)
                column_list.remove(column)
            else:
                mew.append([column,m_column])
                #mew.append(m_column)

                column_list.remove(column)
                column_list.remove(m_column)

        row_list = list(set(y_list))
        row_list.sort()
        mew.reverse()
        even_col= []
        odd_col = []
        for i in range(2):
            row = mew[0 + i*2]
            even_col.append(row)

        for i in range(2):
            row = mew[1 + i*2]
            odd_col.append(row)
        
        even_col_flat = []
        for i in range(len(even_col)):
            loc = even_col[i]
            if isinstance(loc, list):
                for j in range(len(loc)):
                    loc2 = loc[j]
                    even_col_flat.append(loc2)
            else:
                even_col_flat.append(loc)
                    
        odd_col_flat = []
        for i in range(len(odd_col)):
            loc = odd_col[i]
            if isinstance(loc, list):
                for j in range(len(loc)):
                    loc2 = loc[j]
                    odd_col_flat.append(loc2)
            else:
                odd_col_flat.append(loc)

        beven_list = []
        bodd_list =[]
        for i in range(len(row_list)):
            if i % 2 == 0:
                #assign to even number column
                if len(beven_list) < 1:
                    beven_list.append((even_col_flat[0], row_list[i]))
                elif len(beven_list) > 15:
                    beven_list.append((even_col_flat[0], row_list[i]))
                else:
                    for j in range(len(even_col_flat)):
                        beven_list.append((even_col_flat[j], row_list[i]))


            else: 
                if len(bodd_list) < 2:
                    bodd_list.append((odd_col_flat[0], row_list[i]))
                    bodd_list.append((odd_col_flat[1], row_list[i]))
                elif len(beven_list) > 14:
                    bodd_list.append((odd_col_flat[0], row_list[i]))
                    bodd_list.append((odd_col_flat[1], row_list[i]))
                else:
                    for j in range(len(odd_col_flat)):
                        bodd_list.append((odd_col_flat[j], row_list[i]))




        all_cord_list = bodd_list + beven_list
        odd_col_flat.sort()
        even_col_flat.sort()
        all_col_list = odd_col_flat + even_col_flat
        all_col_list.sort()
        new_cord_list = []


        for x_cord in all_col_list:

            for cord in all_cord_list:
                x,y = cord
                if x == x_cord:
                    new_cord_list.append((x,y))


        #for x in new_cord_list:
        #  pyautogui.moveTo(x)

        circle_list = ["11", "12", "13", "14",
                    "21", "22", "23", "24", "25",
                    "31", "32", "33", "34", "35", "36",
                    "41", "42", "43", "44", "45", "46", "47",
                    "51", "52", "53", "54", "55", "56",
                    "61", "62", "63", "64", "65",
                    "71", "72", "73", "74"
                    ]
        big_list = []

        list_to_check1 = num_dic["one"]
        list_to_check2 = num_dic["two"]


        '''for k in range(len(new_cord_list)):
            x_1, y_1 = new_cord_list[k]

            if new_cord_list[k] in list_to_check1:
                number = 1
                big_list.append([(x_1,y_1), number])
            elif new_cord_list[k] in list_to_check2:
                number = 2
                big_list.append([(x_1,y_1), number])
            else:
                number = 0
                big_list.append([(x_1,y_1), number])'''

        for k in range(len(new_cord_list)):
            x_1, y_1 = new_cord_list[k]
            for i in range(len(num_dic_key)):
                number = num_dic_key[i]
                list_to_check = num_dic[number]
                value = i + 1
                for j in range(len(list_to_check)):
                    x, y = list_to_check[j]
                    if abs(x-x_1) < 1 and abs(y - y_1) < 1:
                        big_list.append([(x_1,y_1), value])


        structure = dict(zip(circle_list, big_list))
        
        return(structure)


    big_dic = num_dic_create()
    #print(big_dic)
    def calculate(clicking_circle):
        a11 = {"11":0, "12":0, "21": 0,"22": 0}
        a12 = {"11":0, "12":0, "13":0, "22": 0,"23": 0}
        a13 = {"12":0, "13":0, "14":0, "23": 0,"24": 0}
        a14 = {"13":0, "14":0, "24": 0,"25": 0}

        a21 = {"11":0, "21":0, "22": 0,"31": 0,"32": 0}
        a22 = {"11":0, "12":0, "21":0, "22": 0,"23": 0,"32": 0,"33": 0 }
        a23 = {"12":0, "13":0, "22":0, "23": 0,"24": 0,"33": 0,"34": 0 }
        a24 = {"13":0, "14":0, "23":0, "24": 0,"25": 0,"34": 0,"35": 0 }
        a25 = {"14":0, "24":0, "25": 0,"35": 0,"36": 0}

        a31 = {"21":0, "31":0, "32": 0,"41": 0,"42": 0}
        a32 = {"21":0, "22":0, "31":0, "32": 0,"33": 0,"42": 0,"43": 0 }
        a33 = {"22":0, "23":0, "32":0, "33": 0,"34": 0,"43": 0,"44": 0 }
        a34 = {"23":0, "24":0, "33":0, "34": 0,"35": 0,"44": 0,"45": 0 }
        a35 = {"24":0, "25":0, "34":0, "35": 0,"36": 0,"45": 0,"46": 0 }
        a36 = {"25":0, "35":0, "36": 0,"46": 0,"47": 0}

        a41 = {"31":0, "41":0, "42": 0,"51": 0}
        a42 = {"31":0, "32":0, "41":0, "42": 0,"43": 0,"51": 0,"52": 0 }
        a43 = {"32":0, "33":0, "42":0, "43": 0,"44": 0,"52": 0,"53": 0 }
        a44 = {"33":0, "34":0, "43":0, "44": 0,"45": 0,"53": 0,"54": 0 }
        a45 = {"34":0, "35":0, "44":0, "45": 0,"46": 0,"54": 0,"55": 0 }
        a46 = {"35":0, "36":0, "45":0, "46": 0,"47": 0,"55": 0,"56": 0 }
        a47 = {"36":0, "46":0, "47": 0,"56": 0}

        a51 = {"61":0, "51":0, "52": 0,"41": 0,"42": 0}
        a52 = {"61":0, "62":0, "51":0, "52": 0,"53": 0,"42": 0,"43": 0 }
        a53 = {"62":0, "63":0, "52":0, "53": 0,"54": 0,"43": 0,"44": 0 }
        a54 = {"63":0, "64":0, "53":0, "54": 0,"55": 0,"44": 0,"45": 0 }
        a55 = {"64":0, "65":0, "54":0, "55": 0,"56": 0,"45": 0,"46": 0 }
        a56 = {"65":0, "55":0, "56": 0,"46": 0,"47": 0}

        a61 = {"71":0, "61":0, "62": 0,"51": 0,"52": 0}
        a62 = {"71":0, "72":0, "61":0, "62": 0,"63": 0,"52": 0,"53": 0 }
        a63 = {"72":0, "73":0, "62":0, "63": 0,"64": 0,"53": 0,"54": 0 }
        a64 = {"73":0, "74":0, "63":0, "64": 0,"65": 0,"54": 0,"55": 0 }
        a65 = {"74":0, "64":0, "65": 0,"55": 0,"56": 0}

        a71 = {"71":0, "62":0, "61": 0,"62": 0}
        a72 = {"71":0, "72":0, "73":0, "62": 0,"63": 0}
        a73 = {"72":0, "73":0, "74":0, "63": 0,"64": 0}
        a74 = {"73":0, "74":0, "64": 0,"65": 0}

        circle_list = ["11", "12", "13", "14",
                        "21", "22", "23", "24", "25",
                        "31", "32", "33", "34", "35", "36",
                        "41", "42", "43", "44", "45", "46", "47",
                        "51", "52", "53", "54", "55", "56",
                        "61", "62", "63", "64", "65",
                        "71", "72", "73", "74"
                        ]
        affect_list = [a11, a12, a13, a14, a21, a22, a23, a24, a25, a31, a32, a33, 
                    a34, a35, a36, a41, a42, a43, a44, a45, a46, a47, a51, a52,
                    a53, a54, a55, a56, a61, a62, a63, a64, a65, a71, a72, a73,
                    a74]



        affect_dic = dict(zip(circle_list, affect_list))
        changed_dic = affect_dic[clicking_circle]
        changed_dic_list = list(changed_dic)
        for i in range(len(changed_dic_list)):
            changed_dic[changed_dic_list[i]] += 1

        return changed_dic
            

    big_dic_value = list(big_dic.values())



    circle_list = ["11", "12", "13", "14",
                        "21", "22", "23", "24", "25",
                        "31", "32", "33", "34", "35", "36",
                        "41", "42", "43", "44", "45", "46", "47",
                        "51", "52", "53", "54", "55", "56",
                        "61", "62", "63", "64", "65",
                        "71", "72", "73", "74"
                        ]

    value_list = []

    for x in big_dic_value: 
        value_list.append(x[1])

    coord_list = []

    for x in big_dic_value: 
        coord_list.append(x[0])

    coord_to_cir = dict(zip(coord_list, circle_list))

    action_cord = []
    #print(clean_bigdic(big_dic))
    i = 0
    while i <= 32:
        if i <= 3:
            target = circle_list[i]
            target_value = (big_dic[target])[1]
            if target_value != 1:
                button_to_click = circle_list[i+5]
                clicking_coord = (big_dic[button_to_click])[0]
                clicking_circle = coord_to_cir[clicking_coord]
                changes_in_buttons = calculate(clicking_circle)
                action_cord.append(clicking_coord)

                changes_in_buttons_list = list(changes_in_buttons)
                for j in range(len(changes_in_buttons_list)):
                    name = changes_in_buttons_list[j]
                    change_by = changes_in_buttons[name]
                    (big_dic[(name)])[1]+= change_by
                    if (big_dic[(name)])[1] > 2:
                        (big_dic[(name)])[1] -= 2
            i += 1
            #print(i)
                
        if i > 3 and i <= 8:
            target = circle_list[i]
            target_value = (big_dic[target])[1]
            if target_value != 1:
                button_to_click = circle_list[i+6]
                clicking_coord = (big_dic[button_to_click])[0]
                clicking_circle = coord_to_cir[clicking_coord]
                changes_in_buttons = calculate(clicking_circle)
                
                action_cord.append(clicking_coord)
                changes_in_buttons_list = list(changes_in_buttons)
                for j in range(len(changes_in_buttons_list)):
                    name = changes_in_buttons_list[j]
                    change_by = changes_in_buttons[name]
                    (big_dic[(name)])[1]+= change_by
                    if (big_dic[(name)])[1] > 2:
                        (big_dic[(name)])[1] -= 2
            i += 1
            #print(i)
        if i > 8 and i <= 14:
            target = circle_list[i]
            target_value = (big_dic[target])[1]
            if target_value != 1:
                button_to_click = circle_list[i+7]
                clicking_coord = (big_dic[button_to_click])[0]
                clicking_circle = coord_to_cir[clicking_coord]
                changes_in_buttons = calculate(clicking_circle)
                
                action_cord.append(clicking_coord)
                changes_in_buttons_list = list(changes_in_buttons)
                for j in range(len(changes_in_buttons_list)):
                    name = changes_in_buttons_list[j]
                    change_by = changes_in_buttons[name]
                    (big_dic[(name)])[1]+= change_by
                    if (big_dic[(name)])[1] > 2:
                        (big_dic[(name)])[1] -= 2
        
            i += 1
            #print(i)

        if i == 14:
            next7_list = []
            num_list = []
            for j in range(7):
                next_7 = circle_list[i+j+1]
                next7_list.append(next_7)

            for k in range(len(next7_list)): 
                num_list.append((big_dic[next7_list[k]])[1])
                no_2 = num_list.count(2)
            if no_2 % 2 == 0:
                continue
            else:
                #print("odd")
                for n in range(len(next7_list)):
                    clicking_coord = (big_dic[next7_list[n]])[0]
                    
                    action_cord.append(clicking_coord)
                    changes_in_buttons = calculate(next7_list[n])
                
                    changes_in_buttons_list = list(changes_in_buttons)
                    for j in range(len(changes_in_buttons_list)):
                        name = changes_in_buttons_list[j]
                        change_by = changes_in_buttons[name]
                        (big_dic[(name)])[1]+= change_by
                        if (big_dic[(name)])[1] > 2:
                            (big_dic[(name)])[1] -= 2
            #print(big_dic)


        if i > 14 and i <= 21:
            target = circle_list[i]
            target_value = (big_dic[target])[1]
            if target_value != 1:
                button_to_click = circle_list[i+7]
                clicking_coord = (big_dic[button_to_click])[0]
                clicking_circle = coord_to_cir[clicking_coord]
                changes_in_buttons = calculate(clicking_circle)
                
                action_cord.append(clicking_coord)
                changes_in_buttons_list = list(changes_in_buttons)
                for j in range(len(changes_in_buttons_list)):
                    name = changes_in_buttons_list[j]
                    change_by = changes_in_buttons[name]
                    (big_dic[(name)])[1]+= change_by
                    if (big_dic[(name)])[1] > 2:
                        (big_dic[(name)])[1] -= 2
            i += 1
            #print(i)

        if i == 21:
            next6_list = []
            num_list = []
            for j in range(6):
                next_6 = circle_list[i+j+1]
                next6_list.append(next_6)

            for k in range(len(next6_list)): 
                num_list.append((big_dic[next6_list[k]])[1])
                no_2 = num_list.count(2)


            if no_2 % 2 == 0:
                continue
            else:
                #print("odd")
        
                for n in range(5):
                    
                    clicking_coord = (big_dic[circle_list[4 + n]])[0]
                    cricle = coord_to_cir[clicking_coord]
                    action_cord.append(clicking_coord)
                    changes_in_buttons = calculate(cricle)
                
                    changes_in_buttons_list = list(changes_in_buttons)
                    for j in range(len(changes_in_buttons_list)):
                        name = changes_in_buttons_list[j]
                        change_by = changes_in_buttons[name]
                        (big_dic[(name)])[1]+= change_by
                        if (big_dic[(name)])[1] > 2:
                            (big_dic[(name)])[1] -= 2
                
                i = 4

            
        if i > 21 and i <= 27:
            target = circle_list[i]
            target_value = (big_dic[target])[1]
            if target_value != 1:
                button_to_click = circle_list[i+6]
                clicking_coord = (big_dic[button_to_click])[0]
                clicking_circle = coord_to_cir[clicking_coord]
                changes_in_buttons = calculate(clicking_circle)
                
                action_cord.append(clicking_coord)
                changes_in_buttons_list = list(changes_in_buttons)
                for j in range(len(changes_in_buttons_list)):
                    name = changes_in_buttons_list[j]
                    change_by = changes_in_buttons[name]
                    (big_dic[(name)])[1]+= change_by
                    if (big_dic[(name)])[1] > 2:
                        (big_dic[(name)])[1] -= 2
            i += 1
            #print(i)

        if i == 27:
            next6_list = []
            num_list = []
            for j in range(5):
                next_6 = circle_list[i+j+1]
                next6_list.append(next_6)

            for k in range(len(next6_list)): 
                num_list.append((big_dic[next6_list[k]])[1])
                no_2 = num_list.count(2)


            if no_2 % 2 == 0:
                continue
            else:
                #print("odd")
        
                for n in range(6):
        
                    clicking_coord = (big_dic[circle_list[9 + n]])[0]
                    cricle = coord_to_cir[clicking_coord]
                    action_cord.append(clicking_coord)
                    changes_in_buttons = calculate(cricle)
                
                    changes_in_buttons_list = list(changes_in_buttons)
                    for j in range(len(changes_in_buttons_list)):
                        name = changes_in_buttons_list[j]
                        change_by = changes_in_buttons[name]
                        (big_dic[(name)])[1]+= change_by
                        if (big_dic[(name)])[1] > 2:
                            (big_dic[(name)])[1] -= 2
                i = 9
        
        if i > 27 and i <= 32:
            target = circle_list[i]
            target_value = (big_dic[target])[1]
            if target_value != 1:
                button_to_click = circle_list[i+5]
                clicking_coord = (big_dic[button_to_click])[0]
                clicking_circle = coord_to_cir[clicking_coord]
                changes_in_buttons = calculate(clicking_circle)
                
                action_cord.append(clicking_coord)
                changes_in_buttons_list = list(changes_in_buttons)
                for j in range(len(changes_in_buttons_list)):
                    name = changes_in_buttons_list[j]
                    change_by = changes_in_buttons[name]
                    (big_dic[(name)])[1]+= change_by
                    if (big_dic[(name)])[1] > 2:
                        (big_dic[(name)])[1] -= 2
            i += 1
            #print(i)

    #print(clean_bigdic(big_dic))
    pyautogui.PAUSE = 0
    start = time.time()
    for i in range(len(action_cord)):
        if runs == 0:
            if i == 0:
                #pyautogui.moveTo(action_cord[i])
                pyautogui.click(action_cord[i],clicks = 2)
                
            else:
                #pyautogui.moveTo(action_cord[i])
                pyautogui.click(action_cord[i],clicks = 1)

        else:
            #pyautogui.moveTo(action_cord[i])
            pyautogui.click(action_cord[i],clicks = 1)




    end = time.time()
    elapsed_time = end - start
    time_list.append(elapsed_time)
    
    print("this run runtime:",elapsed_time,"s")

    average_time = statistics.fmean(time_list)
    print("average runtime:",average_time,"s")



    x,y = pyautogui.locateCenterOnScreen(
                    str(PROJECT_ROOT) + "/" + "great22.png", 
                    confidence= 0.5,
                    grayscale= False)
    #pyautogui.moveTo(x/2,y/2)
    pyautogui.click(x/2,y/2,clicks = 1)
    
    runs += 1







