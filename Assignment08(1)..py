# ------------------------------------- #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot, 1.1.2030, Created started script
# RRoot, 1.1.2030, Added pseudo-code to start assignment 08
# Deborah Yenubari, March 8, Modified code to complete assignment 08
# --------------------------------------- #

# Data ----------------------------------- #
strFileName = 'Products.txt'
lstOfProductObjects = []


class Product(object):
    """Stores Data about a product:

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's standard price
    """
    #  Constructor
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price
        self.__lst_of_product_objects = lstOfProductObjects

    #  Properties
    @property
    def product_name(self):  # getter
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):  # setter
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isalpha() == False:
            self.__product_price = value
        else:
            raise Exception("Price may include numbers only")

    #  Methods
    def to_list(self):
        return self.__lst__()

    def __lst__(self):
        return self.__product_name[0] + "," + self.__product_price[1]


#  Processing ----------------------------- #
class FileProcessor(object):
    """ Processes data to and from a file and a list of product objects:
    methods:
        save_data-to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): ->(a list of product objects)
    """
    strFilename = 'Products.txt'
    lstOfProductObjects = []

    # Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """saves list data to a text file
                :param list_of_product_objects: (list) with rows of products
                :param file_name: (string) with the file name
                :return: lstOfProductObjects
        """
        file_name = open("Products.txt", "w")
        for lstRow in list_of_product_objects:
            file_name.write(lstRow[0] + "," + lstRow[1] + "\n")
        file_name.close()
        print("Data saved to file!")
        return list_of_product_objects

    # Add code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """ reads data from a text file into a list
                :param file_name: (string) with file name
                :param list_of_product_objects: (list) with rows of products
                :return:lstOfProductObjects
        """
        file = open("Products.txt", "r")
        fileData = file.read().splitlines()
        for line in file:
            print(fileData[0].strip() + "," + fileData[1].strip() + "\n")
        print("*** Data from file ***")
        print(list_of_product_objects)
        file.close()
        return list_of_product_objects


# Presentation(Input/Output) ------------- #
class IO:
    """Performs Input/Output tasks"""
    @staticmethod
    def print_menu_options():
        """ Displays a menu of choices to the user
        :return: nothing
        """
    print(""" 
    **** Menu of Options ****

    1. Show current Data in List 
    2. Add Data to the List 
    3. Save Current Data to File 
    4. Read Data from File
    5. Enter 'exit' to leave the program 
    """)

    #  Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform?( 1 to 5)-")).strip()
        print("-------------------------------------------------\n")
        return choice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message: An optional message you want to display
        :return:nothing
        """
        print(optional_message)
        input("Press the [Enter] key to continue.")

    # @staticmethod
    # def show_current_data(list_of_product_objects):
    #     """ Shows the current Tasks in the list of dictionaries rows
    #         #     :param list_of_rows: (list) of rows you want to display
    #         #     :return: lstOfProductObjects
    #      """
    #     Product.product_name = "Kiwis"
    #     Product.product_price = "$0.90"
    #     lstRow = [Product.product_name, Product.product_price]
    #     list_of_product_objects.append(lstRow)
    #     print("** Current Data: **")
    #     print(list_of_product_objects)
    #     return list_of_product_objects

    @staticmethod
    def load_initial_data(list_of_product_objects):
        """ Shows the current Tasks in the list of dictionaries rows
                :param list_of_product_objects: (list) of rows you want to display
                :return: lstOfProductObjects
         """
        Product.product_name = "Kiwis"
        Product.product_price = "$0.90"
        lstRow = [Product.product_name, Product.product_price]
        list_of_product_objects.append(lstRow)
        print("** Initial Data: **")
        print(list_of_product_objects)
        return list_of_product_objects

    @staticmethod
    def show_current_data(list_of_objects):
        temp = []
        for row in list_of_objects:
            if row not in temp:
                temp.append(row)
        list_of_objects = temp
        print(list_of_objects)
        return list_of_objects

    @staticmethod
    def add_data_to_list(list_of_product_objects):
        """ adds user input to the list of products
                product_name: (string) with the product's name
                product_price: (float) with the product's standard price
                list_of_product_objects: (list) with rows of products
                :return: list_of_product_objects
        """
        product_name = (input("Enter the name of a product: "))
        product_price = (input("Enter the price of the product: "))
        lstRow = [product_name, product_price]
        list_of_product_objects.append(lstRow)
        print("Data has been added to the List!")
        print(list_of_product_objects)


object1 = IO()
object1.load_initial_data(lstOfProductObjects)
while True:
    IO.print_menu_options()
    strChoice = IO.input_menu_choice()

    if strChoice == "1":
        object1 = IO()
        object1.show_current_data(lstOfProductObjects)
        IO.input_press_to_continue()
        continue

    elif strChoice == "2":
        object2 = IO()
        object2.add_data_to_list(lstOfProductObjects)
        IO.input_press_to_continue()
        continue

    elif strChoice == "3":
        object3 = FileProcessor()
        object3.save_data_to_file(strFileName, lstOfProductObjects)
        IO.input_press_to_continue()
        continue

    elif strChoice == "4":
        object4 = FileProcessor()
        object4.read_data_from_file(strFileName, lstOfProductObjects)
        IO.input_press_to_continue()
        continue

    else:
        print("GoodBye!")
        break

