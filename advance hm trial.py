import datetime
import time
from tkinter import *
from tabulate import tabulate
import cv2
import mysql.connector as con
import pyttsx3 as pt
from PIL import Image

# Establish a connection to the MySQL database
mycon = con.connect(host="localhost", user="root", passwd="amartyapaul123", database="menu")

# Check if the connection is successful
if mycon.is_connected():
    print("Welcome:")

# Create a cursor object to execute SQL queries
cursor = mycon.cursor()

def text_animation(text, delay=0.03):
    """
    Function to display text with animation effect.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Initialize the text-to-speech engine
engine = pt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)

# Initialize global variables to keep track of amounts
amt = 0
tamt = 0
amt1 = 0
tamt1 = 0
amt2 = 0
tamt2 = 0

# Rest of the code...

def wishMe():
    """
    Function to greet the user based on the current time.
    """
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        text_animation("Good morning:")
        speak("Good morning:")
    elif hour <= 16:
        text_animation("Good afternoon:")
        speak("Good morning:")
    else:
        text_animation("Good evening:")
        speak("Good evening:")

    text_animation("I am Ashley. I am here to assist you?")
    speak("I am Ashley. I am here to assist you?")


def speak(audio):
    """
    Function to speak the given text using the text-to-speech engine.
    """
    engine.say(audio)
    engine.runAndWait()

def veg_menu():
    """
    Function to display and process the vegetarian menu.
    """
    global amt, tamt

    cursor.execute("SELECT * FROM veg")
    data = cursor.fetchall()
    speak("This is the menu:")
    print("Veg menu:")
    headers = ["Serial Number", "Item", "Price"]
    table_data = []
    for item in data:
        table_data.append(item)

    beautiful_table = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
    print(beautiful_table)
    choice = "Y"
    while choice == "Y":
        speak("Enter the serial number of the item you want to eat:")
        a = int(input("Enter the serial number of the item you want to eat:"))
        speak("Enter the quantity:")
        qty1 = int(input("Enter the quantity:"))

        if a == 1:
            amt += qty1 * 150
        elif a == 2:
            amt += qty1 * 100
        elif a == 3:
            amt += qty1 * 80
        elif a == 4:
            amt += qty1 * 200
        elif a == 5:
            amt += qty1 * 70
        elif a == 6:
            amt += qty1 * 200
        elif a == 7:
            amt += qty1 * 80
        elif a == 8:
            amt+=qty1*120
        elif a == 9:
            amt+=qty1*110
        elif a == 10:
            amt+=qty1*250
        elif a == 11:
            amt+=qty1*180
        elif a == 12:
            amt+=qty1*180
        else:
            amt+=qty1*80

        tamt = amt

        speak("Do you want to enter more items?")
        choice = input("Do you want to enter more items? (Y/N):")

def nonveg_menu():
    """
    Function to display and process the non-vegetarian menu.
    """
    global amt1, tamt1

    cursor.execute("SELECT * FROM nonveg")
    data = cursor.fetchall()
    speak("Welcome to the non-veg counter:")
    print("Welcome to the non-veg counter:")
    headers = ["Serial Number", "Item", "Price"]
    table_data = []
    for item in data:
        table_data.append(item)

    beautiful_table = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
    print(beautiful_table)
    choice = "Y"
    while choice == "Y":
        valid_serials = [str(i+1) for i in range(len(data))]
        valid_serials.append("0")  # Allow user to exit the loop by entering 0

        speak("Enter the serial number:")
        b = input("Enter the serial number of the item you want to eat:")

        if b not in valid_serials:
            text_animation("Invalid serial number! Please try again.")
            continue

        if b == "0":
            break

        b = int(b)
        speak("Enter the quantity:")
        qty2 = int(input("Enter the quantity:"))

        if b == 1:
            amt1 += qty2 * 150
        elif b == 2:
            amt1 += qty2 * 200
        elif b == 3:
            amt1 += qty2 * 300
        elif b == 4:
            amt1 += qty2 * 300
        elif b == 5:
            amt1 += qty2 * 350
        elif b == 6:
            amt1 += qty2 * 400
        elif b == 7:
            amt1 += qty2 * 350
        elif b == 8:
            amt1 += qty2 * 280
        elif b == 9:
            amt1 += qty2 * 380
        elif b == 10:
            amt1 += qty2 * 450
        elif b == 11:
            amt1 += qty2 * 480
        else:
            amt1 += qty2 * 500

        tamt1 = amt1

        speak("Do you want to order more?")
        choice = input("Do you want to order more? (Y/N):")


def dessert_menu():
    """
    Function to display and process the dessert menu.
    """
    global amt2, tamt2

    cursor.execute("SELECT * FROM dessert")
    data = cursor.fetchall()
    speak("Welcome to the dessert counter:")
    print("Welcome to the dessert counter:")
    headers = ["Serial Number", "Item", "Price"]
    table_data = []
    for item in data:
        table_data.append(item)

    beautiful_table = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
    print(beautiful_table)
    choice = "Y"
    while choice == "Y":
        speak("Enter the serial number of the item you want to eat:")
        c = int(input("Enter the serial number of the item you want to eat:"))
        speak("Enter the quantity:")
        qty3 = int(input("Enter the quantity:"))

        if c == 1:
            amt2 += qty3 * 120
        elif c == 2:
            amt2 += qty3 * 100
        elif c == 3:
            amt2 += qty3 * 120
        elif c == 4:
            amt2 += qty3 * 100
        elif c == 5:
            amt2 += qty3 * 90
        elif c == 6:
            amt2 += qty3 * 110
        elif c == 7:
            amt2 += qty3 * 110
        elif c == 8:
            amt2 += qty3 * 110
        elif c == 9:
            amt2 += qty3 * 120
        elif c == 10:
            amt2 += qty3 * 80
        elif c == 11:
            amt2 += qty3 * 80
        else:
            amt2 += qty3 * 120

        tamt2 = amt2

        speak("Do you want to order more?")
        choice = input("Do you want to order more? (Y/N):")

def generate_bill():
    """
    Function to generate the final bill and display it using a Tkinter GUI.
    """
    global tamt, tamt1, tamt2

    speak("Please wait, the camera is opening:")
    speak("Press 'g' to click a photo:")
    cap = cv2.VideoCapture(0)
    a = datetime.datetime.now()
    while True:
        ret, video_data = cap.read()
        cv2.imshow("User's Image " + str(a), video_data)
        cv2.imwrite("User.png", video_data)
        if cv2.waitKey(1) == ord('g'):
            break
    IMGE = Image.open("User.png")
    resized_img = IMGE.resize((160, 150))
    resized_img.save("user.png")
    cap.release()
    cv2.destroyAllWindows()

    tot = tamt + tamt1 + tamt2
    gst = tot * 0.05
    gtotal = tot + gst

    text_animation("Generating the final bill...")
    time.sleep(1)

    root = Tk()
    root.title("CUSTOMER'S BILL")
    root.geometry("600x700")
    f1 = Frame(root, bg="grey", borderwidth="6", relief=SUNKEN)
    f1.pack(side=TOP)
    frame_label = Label(f1, text="Here's Your Bill", font="bold", fg="red", padx="100", pady="5")
    label2 = Label(text="*******************\Apshereton\****************", font="bold", fg="blue")
    photo = PhotoImage(file="user.png")
    Photo_label = Label(image=photo)
    label3 = Label(text="******************Veg*******************", font="bold", fg="blue")
    label4 = Label(text="Total cost of veg:         " + str(tamt), font="bold", fg="blue")
    label5 = Label(text="**************Non Veg****************", font="bold", fg="blue")
    label6 = Label(text="Total cost of nonveg:      " + str(tamt1), font="bold", fg="blue")
    label7 = Label(text="Gst:                        " + str(gst), font="bold", fg="blue")
    label7b = Label(text="******************Dessert*******************", font="bold", fg="blue")
    label7a = Label(text="Total cost of dessert:      " + str(tamt2), font="bold", fg="blue")
    label8 = Label(text="Amount to be paid:         " + str(gtotal), font="bold", fg="blue")
    speak("Your Pleasure our comfort:")
    label9 = Label(text="Your Pleasure our comfort!", font="bold", fg="blue")
    label10 = Label(text="*************Visit again************", font="bold", fg="blue")
    Photo_label.pack()
    frame_label.pack(side=TOP, fill="x")
    label2.pack()
    label3.pack()
    label4.pack(anchor="nw")
    label5.pack()
    label6.pack(anchor="nw")
    label7.pack(anchor="nw")
    label7b.pack(anchor="nw")
    label7a.pack(anchor="nw")
    label8.pack(anchor="nw")
    label9.pack()
    label10.pack()

    root.mainloop()

if __name__ == '__main__':
    text_animation("Welcome to the Restaurant Management System...")
    time.sleep(1)
    wishMe()
    while True:
        speak("Option Window:")
        print("Options:")
        print("1. Enter the vegetarian counter")
        print("2. Enter the non-vegetarian counter")
        print("3. Enter the dessert counter")
        print("4. Generate bill")
        print("5. Exit")
        ch = int(input("Enter your choice (1-5):"))

        if ch == 1:
            veg_menu()
        elif ch == 2:
            nonveg_menu()
        elif ch == 3:
            dessert_menu()
        elif ch == 4:
            generate_bill()
        elif ch == 5:
            break
        else:
            text_animation("Invalid choice! Please try again.")

    speak("Thank you for visiting us. Have a nice day!")
