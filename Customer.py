class Customer(object):
    """ Customer class, the users of the Reservation system.
    """

    # class attribute which has a unique id number
    __id = 0

    def __init__(self, first_name, last_name,
                 airline_class_preference, hotel_class_preference,
                 budget):
        """ Constructor.
        :param first_name: first name
        :param last_name: last name
        :param airline_class_preference: airline booking class preference
        :param hotel_class_preference: hotel booking class preference
        :param budget: available budget
        """
        Customer.__id += 1
        self.__id = Customer.__id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__airline_class_preference = airline_class_preference
        self.__hotel_class_preference = hotel_class_preference
        self.__budget = budget
        self.__cost = 0.0
        self.__customer_record = {'Name': self.__first_name + ' ' + self.__last_name,
                                  'Customer_Id': self.__id,
                                  'Cost': self.__cost,
                                  'Reservation_Id': {},
                                  'Budget': self.__budget
                                  }

    def get_name(self):
        return self.__first_name + ' ' + self.__last_name

    def get_airline_class_preference(self):
        return self.__airline_class_preference

    def get_hotel_class_preference(self):
        return self.__hotel_class_preference

    def get_budget(self):
        """ Return budget.
        :return: budget
        """
        return self.__budget

    def get_customer_record(self):
        """ Return the customer record.
        :return: customer record
        """
        return self.__customer_record

    def subtract_from_budget(self, expense):
        """ Subtract an expense from the budget.
        :param expense: expense to subtract
        :return: updated budget
        """
        self.__budget -= expense

    def check_budget(self, expense):
        """ Check whether the budget can accommodate an expense
        :param expense: expense
        :return: True if expense can be covered by the budget, and False, otherwise
        """
        return self.__budget - expense >= 0.0

    def print_record(self):
        """ Print the customer record with all reservation information.
        :return: customer record
        """
        record = ''
        for k, v in self.__customer_record.items():
            record += f'{k}:{v}\n'
        print(record)
