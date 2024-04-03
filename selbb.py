import tkinter as tk
from tkinter import GROOVE, LabelFrame, filedialog
from tkinter import font
import traceback
from turtle import bgcolor
from PIL import Image, ImageTk
import easyocr
import pyautogui
import pytesseract
def submit_form():
    try:
        FileNumber_val = entry_File_number.get()
        FormNumber_val = entry_form_number.get()
        Title_val = entry_title.get()
        FirstName_val = entry_first_name.get()
        LastName_val = entry_last_name.get()
        Initial_val = entry_initial.get()
        MailID_val = entry_mail_id.get()
        FatherName_val = entry_father_name.get()
        DateofBirth_val = entry_date_of_birth.get()
        Gender_val = entry_gender.get()
        Profession_val = entry_profession.get()
        MailingStreet_val = entry_mailing_street.get()
        Mailingcity_val = entry_mailing_city.get()
        PostalCode_val = entry_postal_code.get()
        MailingCountry_val = entry_mailing_country.get()
        ServiceProvider_val = entry_service_provider.get()
        ReffrenceNumber_val = entry_reference_number.get()
        Simnumber_val = entry_sim_number.get()
        fileNumber_val = entry_file_number.get()
        TypeofNetwork_val = entry_type_of_network.get()
        CellModel_val = entry_cell_model.get()
        IMMEI1_val = entry_imei1.get()
        IMMEi2_val = entry_imei2.get()
        Typeofplan_val = entry_type_of_plan.get()
        Typeofcreditcard_val = entry_type_of_credit_card.get()
        ContactValue_val = entry_contact_value.get()
        Dateofissue_val = entry_date_of_issue.get()
        Dateofrenewal_val = entry_date_of_renewal.get()

        # PyAutoGUI code with the obtained values
        pyautogui.time.sleep(10)
        pyautogui.click(305, 321)
        pyautogui.write(FileNumber_val, interval=0.25)  # File Number
        pyautogui.click(415, 320)
        pyautogui.write(FormNumber_val, interval=0.25)  # Form Number
        pyautogui.click(529, 324)
        pyautogui.write(Title_val, interval=0.25)  # Title
        pyautogui.click(652, 326)
        pyautogui.write(FirstName_val, interval=0.25)  # First Name
        pyautogui.click(880, 325)
        pyautogui.write(LastName_val, interval=0.25)  # Last Name
        pyautogui.click(1118, 325)
        pyautogui.write(Initial_val, interval=0.25)  # Initial
        pyautogui.click(1240, 342)
        pyautogui.write(MailID_val, interval=0.25)  # Mail ID
        pyautogui.click(1471, 339)
        pyautogui.write(FatherName_val, interval=0.25)  # Father Name
        pyautogui.click(284, 405)
        pyautogui.write(DateofBirth_val, interval=0.25)  # Date of Birth
        pyautogui.click(518, 400)
        pyautogui.write(Gender_val, interval=0.25)  # Gender
        pyautogui.click(761, 403)
        pyautogui.write(Profession_val, interval=0.25)  # Profession
        pyautogui.click(1044, 412)
        pyautogui.write(MailingStreet_val, interval=0.25)  # Mailing Street
        pyautogui.click(1225, 396)
        pyautogui.write(Mailingcity_val, interval=0.25)  # Mailing city
        pyautogui.click(1481, 419)
        pyautogui.write(PostalCode_val, interval=0.25)  # Postal Code
        pyautogui.click(284, 475)
        pyautogui.write(MailingCountry_val, interval=0.25)  # Mailing Country
        pyautogui.click(615, 479)
        pyautogui.write(ServiceProvider_val, interval=0.25)  # Service Provider
        pyautogui.click(870, 484)
        pyautogui.write(fileNumber_val, interval=0.25)  # file Number
        pyautogui.click(1019, 474)
        pyautogui.write(ReffrenceNumber_val, interval=0.25)  # Reference Number
        pyautogui.click(1218, 481)
        pyautogui.write(Simnumber_val, interval=0.25)  # sim number
        pyautogui.click(1448, 475)
        pyautogui.write(TypeofNetwork_val, interval=0.25)  # Type of Network
        pyautogui.click(293, 550)
        pyautogui.write(CellModel_val, interval=0.25)  # Cell Model
        pyautogui.click(517, 547)
        pyautogui.write(IMMEI1_val, interval=0.25)  # IMEI1
        pyautogui.click(750, 553)
        pyautogui.write(IMMEi2_val, interval=0.25)  # IMEI2
        pyautogui.click(982, 550)
        pyautogui.write(Typeofplan_val, interval=0.25)  # Type of plan
        pyautogui.click(1208, 547)
        pyautogui.write(Typeofcreditcard_val, interval=0.25)  # Type of credit card
        pyautogui.click(1452, 549)
        pyautogui.write(ContactValue_val, interval=0.25)  # Contact Value
        pyautogui.click(291, 623)
        pyautogui.write(Dateofissue_val, interval=0.25)  # Date of issue
        pyautogui.click(531, 623)
        pyautogui.write(Dateofrenewal_val, interval=0.25)  # Date of renewal
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()
def clear_form():
    try:
        # Clear all entry fields
        for entry in entry_fields:
            entry.delete(0, tk.END)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

def image_to_text_with_tesseract(image_path):
    try:
        # Use Tesseract to perform OCR on the image
        result_text = pytesseract.image_to_string(Image.open(image_path))

        return result_text.strip()

    except Exception as e:
        print(f"Error: {e}")
        return None

def select_image():
    # Open a file dialog to choose an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    
    if file_path:
        # Update the image and perform OCR
        update_image(file_path)
        perform_ocr(file_path)

def update_image(image_path):
    # Open and display the selected image
    img = Image.open(image_path)
    img.thumbnail((700, 600))  # Resize image to fit in the window
    img = ImageTk.PhotoImage(img)

    # Update the image label
    image_label.config(image=img)
    image_label.image = img
def perform_ocr(image_path):
    # Perform OCR on the selected image
    result_text = image_to_text_with_tesseract(image_path)

    # Clear previous text
    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)

    # Insert new text at the beginning of the Text widget
    text_widget.insert("1.0", result_text)

    # Disable editing
    text_widget.config(state="disabled")

try:
    # Create the main window
    root = tk.Tk()
    root.title("PyAutoGUI Form Filler with EasyOCR")
    F1 = LabelFrame(root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="#191970") 
    F1.place(x=0, y=20)
    F2 = LabelFrame(root, text="Image to text converter", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="#191970") 
    F2.place(x=500, y=50)
    entry_File_number = tk.Entry(F1)
    entry_form_number = tk.Entry(F1)
    entry_title = tk.Entry(F1)
    entry_first_name = tk.Entry(F1)
    entry_last_name = tk.Entry(F1)
    entry_initial = tk.Entry(F1)
    entry_mail_id = tk.Entry(F1)
    entry_father_name = tk.Entry(F1)
    entry_date_of_birth = tk.Entry(F1)
    entry_gender = tk.Entry(F1)
    entry_profession = tk.Entry(F1)
    entry_mailing_street = tk.Entry(F1)
    entry_mailing_city = tk.Entry(F1)
    entry_postal_code = tk.Entry(F1)
    entry_mailing_country = tk.Entry(F1)
    entry_service_provider = tk.Entry(F1)
    entry_reference_number = tk.Entry(F1)
    entry_sim_number = tk.Entry(F1)
    entry_file_number = tk.Entry(F1)
    entry_type_of_network = tk.Entry(F1)
    entry_cell_model = tk.Entry(F1)
    entry_imei1 = tk.Entry(F1)
    entry_imei2 = tk.Entry(F1)
    entry_type_of_plan = tk.Entry(F1)
    entry_type_of_credit_card = tk.Entry(F1)
    entry_contact_value = tk.Entry(F1)
    entry_date_of_issue = tk.Entry(F1)
    entry_date_of_renewal = tk.Entry(F1)

    # Store entry fields in a list for easy clearing
    entry_fields = [
        entry_File_number, entry_form_number, entry_title, entry_first_name,
        entry_last_name, entry_initial, entry_mail_id, entry_father_name,
        entry_date_of_birth, entry_gender, entry_profession, entry_mailing_street,
        entry_mailing_city, entry_postal_code, entry_mailing_country,
        entry_service_provider, entry_reference_number, entry_sim_number,
        entry_file_number, entry_type_of_network, entry_cell_model, entry_imei1,
        entry_imei2, entry_type_of_plan, entry_type_of_credit_card,
        entry_contact_value, entry_date_of_issue, entry_date_of_renewal
    ]

    labels = [
        "File Number", "Form Number", "Title", "First Name", "Last Name", "Initial",
        "Mail ID", "Father Name", "Date of Birth", "Gender", "Profession",
        "Mailing Street", "Mailing City", "Postal Code", "Mailing Country",
        "Service Provider", "Reference Number", "Sim Number", "file Number",
        "Type of Network", "Cell Model", "IMEI 1", "IMEI 2", "Type of Plan",
        "Type of Credit Card", "Contact Value", "Date of Issue", "Date of Renewal"
    ]

    # Arrange widgets in two columns
    row_num = 0
    col_num = 0
    for label, entry_field in zip(labels, entry_fields):
        tk.Label(F1, text=label).grid(row=row_num, column=col_num, sticky=tk.E)
        entry_field.grid(row=row_num, column=col_num + 1, padx=5, pady=5)
        row_num += 1
        if row_num % 15 == 0:
            row_num = 0
            col_num += 2

    # Create and place the submit button
    button_submit = tk.Button(F1, text="Submit", command=submit_form)
    button_submit.grid(row=row_num, column=col_num, pady=10, padx=10, columnspan=2)

    # Create and place the clear button
    button_clear = tk.Button(F1, text="Clear", command=clear_form)
    button_clear.grid(row=row_num + 1, column=col_num, pady=10, padx=10, columnspan=2)

    # Create a button to select an image
    select_button = tk.Button(F1, text="Select Image", command=select_image)
    select_button.grid(row=row_num + 2, column=col_num, pady=10, padx=10, columnspan=2)

    # Create labels for image and text
    image_label = tk.Label(F2)
    image_label.grid(row=0, column=0, columnspan=2, pady=10)
    custom_font = font.Font(family="Arial", size=10)
    text_widget = tk.Text(F2, wrap="word", height=20, width=70,font=custom_font)
    text_widget.grid(row=5, column=0, padx=10)
    def set_min_max_size():
        root.minsize(400, 300)  # Set the minimum size to 400x300 pixels
        root.maxsize(1920, 1080)  # Set the maximum size to 1000x800 pixels

    # Add a vertical scrollbar to the Text widget
    scrollbar = tk.Scrollbar(F2, orient="vertical", command=text_widget.yview)
    scrollbar.grid(row=5, column=16, sticky="ns")
    text_widget.config(yscrollcommand=scrollbar.set)

    # Adjust column and row weights to move widgets to the right
    root.columnconfigure(0, weight=1)
    root.columnconfigure(15, weight=1)
    root.geometry("1366x600")
    # Call a function to set minimum and maximum sizes
    set_min_max_size()
    root.resizable(True, True)  # Allow resizing in both directions
    root.mainloop()
except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()