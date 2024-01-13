# This is my GitHub repository file for EncryptVault started 1-7-2024

''' this is the original programming for the EncryptVault system. 
It has been my, (John M.P. Santi Sr.) dream for the last 2 years 4-2022. 
I have been learning about programming and computer systems for the 
last two years to get to this point of being able to program this 
application. The goal of this programm is to allow users to safely,
digitally, store their seed phrases, and passwords.'''

''' 1. We make 2 USB keys, one for encrypting which is green, and one 
for decrypting which is red. This is likely best done with secure
USB drives that are called Apricorn, which have security pins. 

    2. Encrypting your data.
Enter your encryption USB (Green). The program encrypts the data and 
returns both the encrypted data (to be stored) and a QR representation 
(of the encrypted data), which can be stored anywhere safely: 
    -online
    -on the cloud
    -at moms or sisters house, in a safe, computer, or phone. '''

''' ***Note- 
    A. The program should promt you to save both the encrypted file and 
    the encrypted data QR code in multiple locations. 

    B. The program should also check the data that is saved against the 
    original file, and against each other for errors. 

    Theoretically one could save a photo of 10 QR codes created by EV and 
make one QR code representing the lot, which could then be decrypted with 
a two step decryption process. 

    This program accesses your camera to photograph the QR code, and then 
Decrypts it into the original data which is safely displayed on the 
EncryptVault device.

    The idea is that the static encryption and decryption keys are split and 
encrypted with a common EncryptVault cipher and then stored immutably on the 
blockchain. some function of verification by the user and the decryption from 
centralized EV system gets the key returned to the customer in 2 distinct 
parts in such a way that EV cannot actually regenerate the key, only the 
customer on thier perspective device'''

# establish latest version
# test for update availability
# offer update

#----------------------------------------------------------------------------------------
#-----------------------Beginning of Code------------------------------------------------

# ----------code block A---define the variable 'usb_status' with a random number----------

'''this following code block is temporary and will be replaced with a "search" 
and return the actual ev version which installed on the actual device'''

# import random
# numbers = [1.1, 2.0, 3.1, 4.2, 5.0]  # Defined set of numbers
# ev_version = random.choice(numbers)
# print("Random number:", ev_version)
# print()
#^^^^^end code block A^^^^^define the variable 'usb_status' with a random number^^^^^^^^^^^^^^^^
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# welcome intro

GREEN = "\033[92m"  # Text color = Bright Green
BLUE = "\033[94m"                   # example: print(f"{GREEN}This text will be green.{RESET}")
RED = "\033[91m"    # Text color = Red
ITALIC = "\033[3m"
RESET = "\033[0m"   # Reset to default color
YELLOW = "\033[93m" # Text color = Yellow


#*>>>>>>>>>
def intro():
    print(f"\n{BLUE}{ITALIC}<----------------------------------------------------------------->\n"
        f"Welcome, my dear friend, to EncryptVault!\nThis is your place to "
        f"safely, digitally, store all of your crypto-wallet seed phrases and private keys.{RESET}")
    
    slow_type(f"{GREEN}{ITALIC}\n\"Never, ever, lose access to your crypto seed phrases and wallets, ever ,"
        f"no matter what\"** -J. Santi\n{RESET}", delay=0.01)

    # print("EncryptVault Version-",ev_version)
    # # if ev_version = latest_ev_version, print("You are running the latest version of EncryptVault")
    # if ev_version >= 4:
    #     print("(You are running the most current version of EncryptVault)\n") 
    # else:
    #     print("         ***Warning! You are not currently running the latest version of EncryptVault***")
    #     print("            For security reasons, please update by clicking here: <Update Now>\n")
        
    
    slow_type(f"I will be your guide through this process.\nLet's begin...", delay=0.01)  # future functionality, allow user to hover over words for definitions and explanations
    

    # future functionality...
    # call usb drive for status on your usb stick. 0 = none inserted, 1 = non-password protected USB inserted, 
    # 2 = valid encryption drive Green, 3 = valid decryption drive Red

'''prompt check USB'''
#print("Let's start by checking the status of your USB:")

# insert call for USB status here. We must make a protocol for 
# identifying a properly formatted EncryptVault USB drive and distinguishing 
# between a Green encryption and Red decryption drive. It would be nice to
# be able to verify the encryption key size on the USB, e.g.-256, 512

import os    # This allows us to run operating system commands from within the python script
import sys   # This allows us to verify that a library has been
             # imported after calling it with the import command
import cryptography    # This allows us to use the cryptography library

import subprocess   #This allows us to run a command line command from within the python script
import random    #This allows us to generate random numbers
import string   #This allows us to generate random strings

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

import time  #This allows us to use the time function to create a delay 


#*>>>>>>>>>
def slow_type(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # for newline after the typing effect

                # Example usage
                # type_like_effect("Hello, this is being 'typed' out!", delay=0.1)

#*>>>>>>>>>
def generate_rsa_keys():        # before we generate keys we prompt the user and ask if they want to make keys
    # Generate a 4096-bit RSA private key
    
    #* Let user know that generating keys may take a bit of time
    print(f"{GREEN}OK, you chose yes to generate new public and private keys:{RESET}\n")
    print(f"{YELLOW}It takes a bit to create these extremely long and secure keys")
    print(f"Please be patient and allow the keys to generate without exiting the program.")
    print(f"I will give you a tone when the keys are ready.{RESET}")
    
    
    #* Private key inserted into variable with parameters
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )

    #* Get the public key from the private key and insert into variable
    public_key = private_key.public_key()
    
    return private_key, public_key
    
    #* Serialize private key to PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    #* Serialize public key to PEM format
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    #* Save the private key to a file
    with open("private_key.pem", "wb") as f:
        f.write(private_key_pem)

    #* Save the public key to a file
    with open("public_key.pem", "wb") as f:
        f.write(public_key_pem)

       
    print("\n\nCongratulations! Your keys have been generated and saved to file.")
    
    #* Print the private key
    print("\n<----------------------------------------------------------------->")
    print(f"{RED}{ITALIC}WARNING! Never let anyone see this code that you don't want "
          f"to have FULL ACCESS to your crypto wallet.\nDo not take photos of this "
          f"code nor save it to the web.\nThere are significants risks in saving and "
          f"printing this code{RESET}")
    print(f"\n{RED}<------------------Beginning of Private Key------------------------------>\n")
    print(private_key_pem.decode())
    print(f"\n{RED}<------------------End of Private Key------------------------------>\n{RESET}")
    
    #* Print the public key
    print("\n<----------------------------------------------------------------->")
    print(f"{GREEN}{ITALIC}This is your public key for encryption."
          f"\nIt may be shared with anyone you wish,\nand stored anywhere as text or QR code.")
    print(f"\n<------------------Beginning of Public Key------------------------------>\n")
    print(public_key_pem.decode())
    print(f"\n<------------------End of Public Key------------------------------>\n{RESET}")
 
    
# !!!!!!!!Make sure that the files cannot be overwritten and that there is a 4 digit random string serial identifyer for the corresponding KEY pairs. Since Private KEY-A only decrypts Public KEY-A, we cannot get the KEY files confused or the data can be lost!!!!!!!!!

 


#*<<<<<<<<<<<<<<<<<<<####################>>>>>>>>>>>>>>>>>>>>
# Start program

user_response_enter = input("\nWould you like to enter EncryptVault? (y/n): ")
if user_response_enter == "y":
    intro()
else:
    print("OK, Goodbye\n\n")
    exit()
    
        
print("\n\nWould you like to generate new Public and Private 4096 RSA keys and save to file?")
print(f"{YELLOW}Warning! the keys will display on the screen when created and saved, be sure that you have neccessary privacy{RESET}")
user_response_generate = input("Please enter y/n: ")
if user_response_generate == "y":
    generate_rsa_keys()
    
    
    

#print("Clear to 221")


''' PUBLIC & PRIVATE KEY generation'''
#------code block B-----Prompt user for Public and Private KEY generation---------------------------------
#--------------------------------------------------------------------------------------------------------
# Prompt user if they wish to create a new Public and Private Key
print("Would you like to create a new Public and Private KEY?")

# Prompts y/n question, returns True/False
#*>>>>>>>>>
def ask_yes_no_question(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n']:
            return response == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

answer_make_keys = ask_yes_no_question("Please enter y/n: ")

if answer_make_keys:  # Equivalent to if answer_make_keys == True:
    
    # else argument skips generate Asymetric KEYS
   

    '''generate Asymetric KEYS'''
    #----code block B.2----------generate RSA Keys and store in PEM format----------------------
    #---------------------------------------------------------------------------------------
     
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import rsa


    
        
    # Generate a 4096-bit RSA private 
    #*>>>>>>>>>
    def generate_rsa_keys():
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
    )
        
        # Export RSA public/private KEY in PEM format
        red_private_key = key.exportKey('PEM').decode('utf-8')
        print("This is your Red Pill Private Key:\n", red_private_key)

        green_public_key = key.publickey().exportKey('PEM').decode('utf-8')
        print("This is your Green Pill Public Key:\n", green_public_key)
    
    

    ''' before we save our crypto keys we have to make sure that the files cannot be overwritten
    and that there is a 4 digit random string serial identifyer for the corresponding KEY
    pairs. Since Private KEY-A only decrypts Public KEY-A, we cannot get the KEY files confused or 
    the data can be lost!'''
    

    '''<<<<<<<<<<This code adds upper and lower case letters to the 4 digit serial code ensuring less chance of duplicates>>>>>>>>'''
    # import random
    # import string

    #*<<<<<<<< Generate a 4-digit random alphanumeric string >>>>>>>>>>>>>
    CHARACTERS = string.ascii_letters + string.digits
    SERIAL_NUMBER = ''.join(random.choices(CHARACTERS, k=4))

    #*<<<<<<<< Save PEM KEY into the file >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # red_private_key save to file
    red_private_filename = f'/tmp/EV_private_key_ser-{SERIAL_NUMBER}.pem'
    with open(red_private_filename, 'x') as file:
        file.write(red_private_key)
    # Set file permissions to read-only
    os.chmod(red_private_filename, 0o400)

    # green_public_key save to file
    green_public_filename = f'/tmp/EV_public_key_ser-{SERIAL_NUMBER}.pem'
    with open(green_public_filename, 'x') as file:
        file.write(green_public_key)

    # Set file permissions to read-only
    os.chmod(green_public_filename, 0o400)
    
else:
    print("\033[32mYou chose 'no'. Skipping the KEY generation process.\033[0m\n")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^End Code Block B^^^^^generate RSA Keys and store in PEM format^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    

# print("\nOK -> Line 148\n")

#print("We have made it past the KEY encryption block")



'''module working properly'''
#^----code block C-----Check if USB is inserted---------------------------------------------
#^------------------------------------------------------------------------------------------
import subprocess
import sys

#*>>>>>>>>>
def check_usb_drive():
    out = subprocess.check_output('wmic logicaldisk get DriveType, caption', shell=True)

    usb_detected = False

    for drive in str(out).strip().split('\\r\\r\\n'):
        if '2' in drive:
            drive_letter = drive.split(':')[0]
            drive_type = drive.split(':')[1].strip()
            
            if drive_type == '2':
                usb_detected = True
                # Change text color to green
                print("\033[32mYes, USB drive detected.\033[0m")
                break

    if not usb_detected:
        print("No USB drive detected")

#*>>>>>>>>>
def prompt_continue():
    response = input("Would you like to check again for the presence of a USB drive? (y/n) ")
    return response.lower() == 'y'

#*>>>>>>>>>
def main():
    check_usb = input("Would you like to check for the presence of an inserted USB drive? (y/n) ")
    if check_usb.lower() == 'y':
        check_usb_drive()
    else:
        print("Skipping USB drive check.")

    check_again = prompt_continue()

    while check_again:
        check_usb_drive()
        check_again = prompt_continue()

    response = input("Do you want to continue with the program or quit? (c/q) ")
    if response.lower() == 'q':
        sys.exit()
    else:
        # Change text color to green
        print("\033[32mOk, let's continue...\n\033[0m")
        #print("Ok, let's continue.\n") regular color

print("Start 'Check for USB' subroutine\n")
main()
print("End 'Check for USB' subroutine\n")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^End Code Block C^^^^^Check if USB is inserted^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# print("\nOK -> Line 208\n")



'''module appears to be working properly'''
#-----code block D-----Format USB drive in NTFS format and label drive later----------------------
#-------------------------------------------------------------------------------------------------
import subprocess
import sys

#*>>>>>>>>>
def get_usb_drive_letter():
    out = subprocess.check_output('wmic logicaldisk get DriveType, Caption', shell=True)
    drives = str(out).strip().split('\\r\\r\\n')
    for drive in drives:
        if '2' in drive:
            drive_letter = drive.split(':')[0].strip()
            return drive_letter

    return None

#*>>>>>>>>>
def format_usb_drive(usb_drive):
    # Prompt the user to confirm if they want to format the USB drive
    format_confirmation = input(f"\n\033[31m!!!Warning!!! The following action will erase all information on\nthe USB drive inserted in drive: {usb_drive}, and is IRREVERSIBLE!!!\033[0m\n  \033[33mDo you want to format the USB drive located at drive: {usb_drive}? (y/n) \033[0m")

    if format_confirmation.lower() != "y":
        print("\n\033[32mSkipping the format USB module.\033[0m\n")
        return

    # Format the USB drive with the NTFS file system
    format_command = f"format {usb_drive}: /fs:ntfs /q"
    subprocess.run(format_command, shell=True)

    # Prompt the user to provide a drive label
    drive_label = input("Please enter a drive label of \033[34mEncryptVault_Red_DC\033[0m or \033[34mEncryptVault_Green_EC: \033[0m")

    # Set the drive label for the formatted USB drive
    label_command = f"label {usb_drive}: {drive_label}"
    subprocess.run(label_command, shell=True)

    print(f"\033[32mUSB drive {usb_drive} formatted successfully with label:\033[0m\033[34m '{drive_label}'.\033[0m")

#*>>>>>>>>>
def format_USB_main():
    usb_drive = get_usb_drive_letter()

    if usb_drive is None:
        print("No USB drive detected.")
        return

    print(f"USB drive detected in drive: {usb_drive}")

    # Prompt the user to format the USB drive
    format_usb_drive(usb_drive)
    return                                      #<<<<-Change: added this 5/26/23 1:46pm<<<<<<

format_USB_main()
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^^^^End code block D^^^^^Format USB drive in NTFS format and label drive later^^^^^^^^^^^^^^^^^^^^^^^^^^^




#-----Code Block E-----This bit of code is to save the KEY files to the USB drive--------------------------
#--------------------------------------------------------------------------------------------------------
import os
import shutil
import tkinter as tk
from tkinter import filedialog
import platform
import psutil

#*>>>>>>>>>
def get_usb_drive_letter():
    if platform.system() == 'Windows':
        drives = psutil.disk_partitions()
        for drive in drives:
            if 'removable' in drive.opts and drive.mountpoint:
                return drive.mountpoint
    elif platform.system() == 'Darwin':
        drives = psutil.disk_partitions(all=True)
        for drive in drives:
            if 'removable' in drive.opts and drive.mountpoint:
                return drive.mountpoint

    return None

#*>>>>>>>>>
def save_file_to_usb():
    while True:
        # Create a new root window
        root = tk.Tk()
        root.withdraw()

        # Prompt the user to browse and select a file
        print("Select an EncryptVault KEY file to save to your USB")
        file_path = filedialog.askopenfilename()

        # Check if a file was selected
        if not file_path:
            print("No file selected.")
            break

        # Get the file name from the file path
        file_name = os.path.basename(file_path)

        # Get the USB drive letter
        usb_drive = get_usb_drive_letter()

        if usb_drive is None:
            print("No USB drive detected.")
            break

        print(f"USB drive detected at {usb_drive}")

        # Create the destination directory if it doesn't exist
        destination_dir = os.path.join(usb_drive, "EncryptVault")
        os.makedirs(destination_dir, exist_ok=True)

        # Construct the destination path
        destination = os.path.join(destination_dir, file_name)

        # Copy the file to the USB drive
        try:
            shutil.copy2(file_path, destination)  # Use shutil.copy2 for preserving metadata
            print(f"\033[32mFile '{file_name}' saved to USB drive {usb_drive}.\033[0m\n")
        except Exception as e:
            print(f"Failed to save file to USB drive: {e}")
            break

        # Destroy the root window
        root.destroy()

        # Prompt the user if they want to insert another backup drive
        backup_confirmation = input("Do you want to insert another backup drive? (y/n) ")

        if backup_confirmation.lower() != "y":
            # Prompt the user if they want to exit the program
            exit_confirmation = input("Do you want to exit the program? (y/n) ")

            if exit_confirmation.lower() == "y":
                break

save_file_to_usb()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^End Code Block E^^^^^This bit of code is to save the KEY files to the USB drive^^^^^^^^^^^^^^^^^^^^^

input("At line 356, press any key to continue...")

#-----code block F-----This bit of code is to get input and encrypt data-------------------------------------
#----------------------------------------------------------------------------------------------------------
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

#*>>>>>>>>>
def generate_rsa_key_pair():
    # Generate a new RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    # Get the corresponding public key
    public_key = private_key.public_key()

    return private_key, public_key

#*>>>>>>>>>
def save_key_to_file(key, filename):
    # Save the key to a file in PEM format
    with open(filename, "wb") as key_file:
        key_file.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

#*>>>>>>>>>
def load_key_from_file(filename):
    # Load a private key from a file in PEM format
    with open(filename, "rb") as key_file:
        key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return key

#*>>>>>>>>>
def encrypt_data(public_key, data):
    # Encrypt the data using the public key
    encrypted_data = public_key.encrypt(
        data.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data

#*>>>>>>>>>
def save_data_to_file(data, filename):
    # Save the data to a file
    with open(filename, 'wb') as file:
        file.write(data)

#*>>>>>>>>>
def main_module_encrypt_data():
    # Prompt user for input data to be encrypted
    data = input("Enter data to be encrypted: ")

    # Load public key from the USB file
    usb_filename = "/path/to/usb/public_key.pem"  # Replace with the actual USB file path
    public_key = load_key_from_file(usb_filename)

    # Encrypt the data using the public key
    encrypted_data = encrypt_data(public_key, data)

    # Prompt user to save the file to the device
    device_filename = input("Enter a filename to save the encrypted data to the device: ")
    save_data_to_file(encrypted_data, device_filename)

    # Prompt user to save the file to the USB
    usb_save_filename = "/path/to/usb/encrypted_data.txt"  # Replace with the actual USB file path
    save_data_to_file(encrypted_data, usb_save_filename)

    print("\033[92mEncryption and file saving completed successfully!\033[0m")

if __name__ == '__main__':
    main_module_encrypt_data()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^End Code Block F^^^^^This bit of code is to get input and encrypt data^^^^^^^^^^^^^^^^^^^^^^^^^^

input("At line 421, press any key to continue...")


#-----code block G-----This bit of code is to decrypt data and display it-------------------------------------
#----------------------------------------------------------------------------------------------------------
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

#*>>>>>>>>>
def load_key_from_file(filename):
    with open(filename, "rb") as key_file:
        key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return key
#*>>>>>>>>>
def decrypt_data(private_key, encrypted_data):
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data.decode('utf-8')

#*>>>>>>>>>
def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

#*>>>>>>>>>
def main():
    # Prompt user to plug in the USB drive
    input("Please plug in the USB drive containing the decryption key file and press Enter to continue...")
    
    # Prompt user to choose the file with the data to be decrypted
    device_filename = input("Enter the filename of the encrypted data on the device: ")
    
    # Prompt user to choose the file with the decryption key on the USB
    usb_filename = input("Enter the filename of the decryption key file on the USB: ")
    private_key = load_key_from_file(usb_filename)
    
    # Read encrypted data from the file
    with open(device_filename, 'rb') as file:
        encrypted_data = file.read()
    
    # Decrypt the data using the private key
    decrypted_data = decrypt_data(private_key, encrypted_data)
    
    # Prompt user to save the decrypted data to the device
    save_device = input("Do you want to save the decrypted data to the device? (yes/no): ")
    if save_device.lower() == 'yes':
        device_save_filename = input("Enter a filename to save the decrypted data to the device: ")
        save_data_to_file(decrypted_data, device_save_filename)
    
    # Prompt user to save the decrypted data to the USB
    save_usb = input("Do you want to save the decrypted data to the USB? (yes/no): ")
    if save_usb.lower() == 'yes':
        usb_save_filename = input("Enter a filename to save the decrypted data to the USB: ")
        save_data_to_file(decrypted_data, usb_save_filename)
    
    print("Decryption and file saving completed successfully!")

if __name__ == '__main__':
    main()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^End Code Block G^^^^^This bit of code is to decrypt data and display it^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




#-----code block H-----This bit of code is to turn encrypted data to a QR code-------------------------------------
#----------------------------------------------------------------------------------------------------------------
import os
from PIL import Image, ImageDraw
import qrcode
import tkinter as tk
from tkinter import filedialog

#*>>>>>>>>>
def capture_qr_code():
    root = tk.Tk()
    root.withdraw()
    
    # Prompt user to select the file with the encrypted data
    file_path = filedialog.askopenfilename(title="Select the file with the encrypted data")
    
    # Read the QR code image
    qr_code_image = Image.open(file_path)
    
    # Decode the QR code to retrieve the encrypted data
    qr_code = qrcode.QRCode()
    qr_code.add_data(qr_code_image)
    qr_code.make(fit=True)
    decrypted_data = qr_code.data
    
    return decrypted_data

#*>>>>>>>>>
def label_qr_code(qr_code_image, label_text):
    # Add label text above the QR code
    qr_code_width, qr_code_height = qr_code_image.size
    qr_code_with_label = Image.new("RGB", (qr_code_width, qr_code_height + 30), color="white")
    qr_code_with_label.paste(qr_code_image, (0, 0))
    
    draw = ImageDraw.Draw(qr_code_with_label)
    label_width, label_height = draw.textsize(label_text)
    label_x = (qr_code_width - label_width) // 2
    label_y = qr_code_height
    draw.text((label_x, label_y), label_text, fill="black")
    
    return qr_code_with_label

#*>>>>>>>>>
def save_qr_code(qr_code_image, filename):
    qr_code_image.save(filename, "JPEG")

#*>>>>>>>>>
def main():
    # Prompt user to capture the QR code
    print("Please capture the QR code containing the encrypted data.")
    input("Press Enter to continue...")
    
    # Capture the encrypted data from the QR code
    decrypted_data = capture_qr_code()
    
    # Prompt user to provide a label for the QR code
    label_text = input("Enter the label for the QR code: ")
    
    # Create the labeled QR code image
    qr_code_image = qrcode.make(decrypted_data)
    qr_code_with_label = label_qr_code(qr_code_image, label_text)
    
    # Prompt user to save the labeled QR code as a JPEG file
    save_filename = input("Enter a filename to save the labeled QR code (with .jpeg extension): ")
    save_qr_code(qr_code_with_label, save_filename)
    
    # Prompt user whether to revert the QR code to data
    revert_qr_code = input("Do you want to revert a QR code to data? (yes/no): ")
    
    if revert_qr_code.lower() == 'yes':
        # Prompt user to select the QR code image file
        root = tk.Tk()
        root.withdraw()
        qr_code_file = filedialog.askopenfilename(title="Select the QR code image file")
        
        # Read the QR code image
        qr_code_image = Image.open(qr_code_file)
        
        # Decode the QR code to retrieve the data
        qr_code = qrcode.QRCode()
        qr_code.add_data(qr_code_image)
        qr_code.make(fit=True)
        data = qr_code.data.decode('utf-8')
        
        print("Decoded data: ", data)
        
        # Prompt user whether to save the data as a file to the device
        save_data_device = input("Do you want to save the data as a file to the device? (yes/no): ")
        if save_data_device.lower() == 'yes':
            save_filename_device = input("Enter a filename to save the data to the device: ")
            with open(save_filename_device, 'w') as file:
                file.write(data)
        
        # Prompt user whether to save the data to the USB drive
        save_data_usb = input("Do you want to save the data to the USB drive? (yes/no): ")
        if save_data_usb.lower() == 'yes':
            usb_filename = input("Enter a filename to save the data to the USB drive: ")
            with open(usb_filename, 'w') as file:
                file.write(data)
    
    print("Program completed successfully!")

if __name__ == '__main__':
    main()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^End Code Block H^^^^This bit of code is to turn encrypted data to a QR code^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
