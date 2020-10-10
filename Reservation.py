import random


class Reservation(object):
    """ Base class to all reservation types.
    """

    def __init__(self, name):
        self._name = name

    def is_available(self, booking_class):
        return self.get_items(booking_class) > 0

    def make_reservation(self, customer, booking_class):
        if self.is_available(booking_class):
            self.decrement_items(booking_class)
            customer.get_customer_record()['Cost'] += self.get_price(booking_class)
            customer.get_customer_record()['Reservation_Id'][self._name] = \
                self.get_id_prefix() + '_' + booking_class + '_' + str(random.randrange(1000000, 2000000, 1))
            customer.subtract_from_budget(self.get_price(booking_class))
            customer.get_customer_record()['Budget'] = customer.get_budget()

    def get_items(self, booking_class):
        raise NotImplementedError

    def decrement_items(self, booking_class):
        raise NotImplementedError

    def get_id_prefix(self):
        raise NotImplementedError

    def get_price(self, booking_class):
        raise NotImplementedError


class Airline(Reservation):
    """ Class that encompasses the reservation of an airline seat.
    """

    # class level attributes of airline booking class types
    FIRST = 'First'
    BUSINESS = 'Business'
    ECONOMY = 'Economy'

    @staticmethod
    def get_booking_class_below(booking_class):
        """ class level method that returns all booking class at and below the a desire booking class.
        """
        if booking_class == Airline.FIRST:
            return [Airline.FIRST, Airline.BUSINESS, Airline.ECONOMY]
        elif booking_class == Airline.BUSINESS:
            return [Airline.BUSINESS, Airline.ECONOMY]
        else:
            return [Airline.ECONOMY]

    def __init__(self, name):
        super(Airline, self).__init__(name)

        if self._name == 'United':
            self.seats = {Airline.FIRST: 0, Airline.BUSINESS: 0, Airline.ECONOMY: 1200}
            self.prices = {Airline.FIRST: 1200, Airline.BUSINESS: 600, Airline.ECONOMY: 300}
        elif self._name == 'Spirit':
            self.seats = {Airline.FIRST: 0, Airline.BUSINESS: 0, Airline.ECONOMY: 100}
            self.prices = {Airline.FIRST: 0, Airline.BUSINESS: 0, Airline.ECONOMY: 200}
        else:
            raise Exception(f'{name} airline is not supported')

    def get_items(self, booking_class):
        """ Return the number of available seats for a particular booking class.
        :param booking_class: booking class
        :return: number of seats available
        """
        return self.seats[booking_class]

    def decrement_items(self, booking_class):
        """ Decrement the number of seats for a particular booking class
        :param booking_class:
        """
        self.seats[booking_class] -= 1

    def get_id_prefix(self):
        return str(self._name + '_').upper()

    def get_price(self, booking_class):
        return self.prices[booking_class]


class Hotel(Reservation):
    """ Class that encompasses the reservation of a hotel room.
    """

    # class level attributes of hotel booking class types
    PENTHOUSE = 'Penthouse'
    BUSINESS = 'Business'
    STANDARD = 'Standard'

    @staticmethod
    def get_booking_class_below(booking_class):
        """ class level method that returns all booking class at and below the a desire booking class.
        """
        if booking_class == Hotel.PENTHOUSE:
            return [Hotel.PENTHOUSE, Hotel.BUSINESS, Hotel.STANDARD]
        elif booking_class == Hotel.BUSINESS:
            return [Hotel.BUSINESS, Hotel.STANDARD]
        else:
            return [Hotel.STANDARD]

    def __init__(self, name):
        super(Hotel, self).__init__(name)

        if self._name == 'Four Seasons':
            self.seats = {Hotel.PENTHOUSE: 0, Hotel.BUSINESS: 4, Hotel.STANDARD: 10}
            self.prices = {Hotel.PENTHOUSE: 1200, Hotel.BUSINESS: 600, Hotel.STANDARD: 400}
        elif self._name == 'Marriott':
            self.seats = {Hotel.PENTHOUSE: 2, Hotel.BUSINESS: 12, Hotel.STANDARD: 40}
            self.prices = {Hotel.PENTHOUSE: 1000, Hotel.BUSINESS: 500, Hotel.STANDARD: 300}
        else:
            raise Exception(f'{name} hotel is not supported')

    def get_items(self, booking_class):
        return self.seats[booking_class]

    def decrement_items(self, booking_class):
        self.seats[booking_class] -= 1

    def get_id_prefix(self):
        return str(self._name + '_').upper()

    def get_price(self, booking_class):
        return self.prices[booking_class]

