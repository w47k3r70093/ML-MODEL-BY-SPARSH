# IMPORTING DIFFERENT MODULES

from tkinter import *
import pandas as pd
import numpy as np

# DEFINING OUR GUI WINDOW

root = Tk()
root.geometry("1600x900")  #SCREEN RESOLUTION

# MAIN FUNCTION

def CHECK():
    data_1 = entry_1.get()
    data_2 = entry_2.get()
    data_3 = entry_3.get()
    data_4 = entry_4.get()
    data_5 = entry_5.get()
    data_6 = entry_6.get()
    data_7 = entry_7.get()
    data_8 = entry_8.get()
    data_9 = entry_9.get()
    data_10 = entry_10.get()

    df = pd.DataFrame({'SNo':[1,2,3,4,5,6,7,8,9,10],'Data':[data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10]})

    X = df[['SNo']]
    Y = df[['Data']]

    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state = 0, test_size = 1/5)

    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()

    reg.fit(X_train, Y_train)
    Y_predict = reg.predict(X_test)

    Y_predict_val = reg.predict(np.array(11).reshape(1,1))
    # print(Y_predict_val)

    r2_score = reg.score(X_train,Y_train)
    # print(r2_score)
    accuracy = r2_score * 100



    predicted_value_label = Label(root, text = f"Value {Y_predict_val}\nAccuracy --> {accuracy}%", font = ('Corbel 20 bold underline'))
    predicted_value_label.place(x = 600, y = 650)
# --------------------------------------------------------------------------------------------------------------------------

# DEFINING MAIN HEADING ON THE GUI WINDOW

Title_Label = Label(root, text = "Machine Learning Prediction Model - By Sparsh", font = ('Algerian 25 bold underline'))
Title_Label.pack()

entry_label_1 = Label(root, text = "Data 1", font = ('Bahnschrift 15'))
entry_label_1.place(x = 700, y = 95)

# EMPTY FIELD TO ENTER FIRST DATA

entry_1 = Entry(root, width = 25)
entry_1.place(x = 770, y = 100)

entry_label_2 = Label(root, text = "Data 2", font = ('Bahnschrift 15'))
entry_label_2.place(x = 700, y = 145)

# EMPTY FIELD TO ENTER SECOND DATA

entry_2 = Entry(root, width = 25)
entry_2.place(x = 770, y = 150)

entry_label_3 = Label(root, text = "Data 3", font = ('Bahnschrift 15'))
entry_label_3.place(x = 700, y = 195)

# EMPTY FIELD TO ENTER THIRD DATA

entry_3 = Entry(root, width = 25)
entry_3.place(x = 770, y = 200)
#
entry_label_4 = Label(root, text = "Data 4", font = ('Bahnschrift 15'))
entry_label_4.place(x = 700, y = 245)

# EMPTY FIELD TO ENTER FOURTH DATA

entry_4 = Entry(root, width = 25)
entry_4.place(x = 770, y = 250)
#
entry_label_5 = Label(root, text = "Data 5", font = ('Bahnschrift 15'))
entry_label_5.place(x = 700, y = 295)

# EMPTY FIELD TO ENTER FIFTH DATA

entry_5 = Entry(root, width = 25)
entry_5.place(x = 770, y = 300)

entry_label_6 = Label(root, text = "Data 6", font = ('Bahnschrift 15'))
entry_label_6.place(x = 700, y = 345)

# EMPTY FIELD TO ENTER SIXTH DATA

entry_6 = Entry(root, width = 25)
entry_6.place(x = 770, y = 350)

entry_label_7 = Label(root, text = "Data 7", font = ('Bahnschrift 15'))
entry_label_7.place(x = 700, y = 395)

# EMPTY FIELD TO ENTER SEVENTH DATA

entry_7 = Entry(root, width = 25)
entry_7.place(x = 770, y = 400)

entry_label_8 = Label(root, text = "Data 8", font = ('Bahnschrift 15'))
entry_label_8.place(x = 700, y = 445)

# EMPTY FIELD TO ENTER EIGHTH DATA

entry_8 = Entry(root, width = 25)
entry_8.place(x = 770, y = 450)

entry_label_9 = Label(root, text = "Data 9", font = ('Bahnschrift 15'))
entry_label_9.place(x = 700, y = 495)

# EMPTY FIELD TO ENTER NINTH DATA

entry_9 = Entry(root, width = 25)
entry_9.place(x = 770, y = 500)

entry_label_10 = Label(root, text = "Data 10", font = ('Bahnschrift 15'))
entry_label_10.place(x = 700, y = 545)

# EMPTY FIELD TO ENTER TENTH DATA

entry_10 = Entry(root, width = 25)
entry_10.place(x = 770, y = 550)

# FINAL BUTTON TO CHECK

check_button = Button(root, text = "CHECK", bg = 'black', fg = 'white', activebackground = 'yellow', font = ('Bahnschrift 15 bold'), command = CHECK)
check_button.place(x = 770, y = 600)

root.mainloop()
