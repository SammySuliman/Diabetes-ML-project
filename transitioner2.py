def Transitioner2(input_list):
    predict_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if input_list[0] == 'M':
        predict_list[0] = 0
    elif input_list[0] == 'F':
        predict_list[0] = 1 
    if input_list[1] == 'Y':
        predict_list[1] = 1
    elif input_list[1] == 'N':
        predict_list[1] = 0
    if type(input_list[2]) != 'float':
        predict_list[21] = float(input_list[2])
    else:
        predict_list[21] = input_list[2]
    if input_list[3] == 'Y':
        predict_list[2] = 1
    elif input_list[3] == 'N':
        predict_list[2] = 0
    if input_list[4] == 'Y':
        predict_list[3] = 1
    elif input_list[4] == 'N':
        predict_list[3] = 0
    if type(input_list[5]) != 'int':
        predict_list[22] = int(input_list[5])
    else:
        predict_list[22] = input_list[5]
    if type(input_list[6]) != 'int':
        predict_list[23] = int(input_list[6])
    else:
        predict_list[23] = input_list[6]
    if input_list[7] == 'Y':
        predict_list[4] = 1
    elif input_list[7] == 'N':
        predict_list[4] = 0
    if type(input_list[8]) != int:
        predict_list[24] == int(input_list[8])
    else:
        predict_list[24] == input_list[8]
    if input_list[9] == 'Y':
        predict_list[5] = 1
    elif input_list[9] == 'N':
        predict_list[5] = 0
    if input_list[10] == 'Y':
        predict_list[6] = 1
    elif input_list[10] == 'N':
        predict_list[6] = 0
    if int(input_list[11]) < 90:
        predict_list[7] = 1
        predict_list[8] = 0
    elif (int(input_list[11])) >= 90 and (int(input_list[11])) < 120:
        predict_list[7] = 0
        predict_list[8] = 1
    elif int(input_list[11]) >= 120:
        predict_list[7] = 0
        predict_list[8] = 1
    if (int(input_list[12])) <= 1 and (int(input_list[12])) >= 0: 
        predict_list[9] = 1
        predict_list[10] = 0
        predict_list[19] = 0
    elif (int(input_list[12])) <= 4 and (int(input_list[12])) >= 2:
        predict_list[9] = 0
        predict_list[10] = 1
        predict_list[19] = 0
    elif (int(input_list[12])) <= 8 and (int(input_list[12])) >= 5:
        predict_list[9] = 0
        predict_list[10] = 0
        predict_list[19] = 1
    elif (int(input_list[12])) <= 10 and (int(input_list[12])) >= 9:
        predict_list[9] = 0
        predict_list[10] = 0
        predict_list[19] = 0
    if input_list[13] == 'occasionally':
        predict_list[11] = 1
        predict_list[12] = 0
        predict_list[20] = 0
    elif input_list[13] == 'often':
        predict_list[11] = 0
        predict_list[12] = 1
        predict_list[20] = 0
    elif input_list[13] == 'very often':
        predict_list[11] = 0
        predict_list[12] = 0
        predict_list[20] = 1
    elif input_list[13] == 'always':
        predict_list[11] = 0
        predict_list[12] = 0
        predict_list[20] = 0
    if int(input_list[14]) == 0:
        predict_list[13] = 0
        predict_list[14] = 1
        predict_list[15] = 0
    elif (int(input_list[14])) < 30 and (int(input_list[14])) > 0:
        predict_list[13] = 0
        predict_list[14] = 0
        predict_list[15] = 0
    elif (int(input_list[14])) < 60 and (int(input_list[14])) >= 30:
        predict_list[13] = 1
        predict_list[14] = 0
        predict_list[15] = 0
    elif (int(input_list[14])) >= 60:
        predict_list[13] = 0
        predict_list[14] = 0
        predict_list[15] = 1
    if (int(input_list[15])) < 40:
        predict_list[16] = 0
        predict_list[17] = 0
        predict_list[18] = 1
    elif (int(input_list[15])) >= 40 and (int(input_list[15])) < 50:
        predict_list[16] = 0
        predict_list[17] = 0
        predict_list[18] = 0
    elif (int(input_list[15])) >= 50 and (int(input_list[15])) < 60:
        predict_list[16] = 1
        predict_list[17] = 0
        predict_list[18] = 0
    elif (int(input_list[15])) >= 60:
        predict_list[16] = 0
        predict_list[17] = 1
        predict_list[18] = 0
    return predict_list
