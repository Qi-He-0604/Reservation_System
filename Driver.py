from Customer import *
from Reservation import *


def driver():
    """ Mainline driver of the Reservation system
    """

    # instantiate Airline objects and store within a list
    airlines = [Airline('Spirit'), Airline('United')]

    # instantiate Hotel objects and store within a list
    hotels = [Hotel('Four Seasons'), Hotel('Marriott')]

    # instantiate Customer objects and store within a list
    customers = [Customer('George', 'Washington', Airline.ECONOMY, Hotel.PENTHOUSE, 2000.0),
                 Customer('Thomas', 'Jefferson', Airline.FIRST, Hotel.STANDARD, 2400.0),
                 Customer('James', 'Madison', Airline.FIRST, Hotel.BUSINESS, 2000.0),
                 Customer('Andrew', 'Jackson', Airline.BUSINESS, Hotel.PENTHOUSE, 1000.0),
                 Customer('Abraham', 'Lincoln', Airline.BUSINESS, Hotel.STANDARD, 2000.0),
                 Customer('Theodore', 'Roosevelt', Airline.ECONOMY, Hotel.PENTHOUSE, 12000.0),
                 Customer('Woodrow', 'Wilson', Airline.FIRST, Hotel.PENTHOUSE, 1600.0),
                 Customer('Franklin', 'Roosevelt', Airline.BUSINESS, Hotel.STANDARD, 1800.0),
                 Customer('Harry', 'Truman', Airline.BUSINESS, Hotel.STANDARD, 2000.0),
                 Customer('John', 'Kennedy', Airline.ECONOMY, Hotel.BUSINESS, 1200.0)]

    # iterate over customers
    #
    for customer in customers:

        print(f'\nAttempting to Book Reservation(s) for {customer.get_name()}')

        booking_class_preferred_airline = customer.get_airline_class_preference()
        booking_class_preferred_hotel = customer.get_hotel_class_preference()

        # check to see if a reservation can be made with airline and hotel preferences
        #
        is_reservation_fulfilled = False
        for airline in airlines:
            for hotel in hotels:
                if airline.is_available(booking_class_preferred_airline) and \
                        hotel.is_available(booking_class_preferred_hotel):
                    # check budget
                    if customer.check_budget(airline.get_price(booking_class_preferred_airline) +
                                             hotel.get_price(booking_class_preferred_hotel)):
                        airline.make_reservation(customer, booking_class_preferred_airline)
                        hotel.make_reservation(customer, booking_class_preferred_hotel)
                        is_reservation_fulfilled = True
                        break
                    elif customer.check_budget(airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                             hotel.get_price(booking_class_preferred_hotel)):
                        airline.make_reservation(customer, airline.get_booking_class_below(booking_class_preferred_airline)[1])
                        hotel.make_reservation(customer, booking_class_preferred_hotel)
                        is_reservation_fulfilled = True
                        break
                    elif customer.check_budget(airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                             hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[1])):
                        airline.make_reservation(customer, airline.get_booking_class_below(booking_class_preferred_airline)[1])
                        hotel.make_reservation(customer, hotel.get_booking_class_below(booking_class_preferred_hotel)[1])
                        is_reservation_fulfilled = True
                        break
                    elif customer.check_budget(airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                             hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                        airline.make_reservation(customer, airline.get_booking_class_below(booking_class_preferred_airline)[1])
                        hotel.make_reservation(customer, hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                        is_reservation_fulfilled = True
                        break
                    elif customer.check_budget(airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                             hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                        airline.make_reservation(customer, airline.get_booking_class_below(booking_class_preferred_airline)[2])
                        hotel.make_reservation(customer, hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                        is_reservation_fulfilled = True
                        break

            if is_reservation_fulfilled:
                break

        # could not make reservations with airline and hotel preferences
        #
        while not is_reservation_fulfilled:
            #print('No reservation can be made.')
            #pass
            for airline in airlines:
                for hotel in hotels:
                    if len(airline.get_booking_class_below(booking_class_preferred_airline)) > 1 and \
                            airline.is_available(
                                airline.get_booking_class_below(booking_class_preferred_airline)[1]) and \
                            hotel.is_available(booking_class_preferred_hotel):
                        # check budget
                        if customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                hotel.get_price(booking_class_preferred_hotel)):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         1])
                            hotel.make_reservation(customer, booking_class_preferred_hotel)
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[1])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         1])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[1])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         1])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break

                    elif len(airline.get_booking_class_below(booking_class_preferred_airline)) > 1 and \
                            len(hotel.get_booking_class_below(booking_class_preferred_hotel)) > 1 and \
                            airline.is_available(
                                airline.get_booking_class_below(booking_class_preferred_airline)[1]) and \
                            hotel.is_available(hotel.get_booking_class_below(booking_class_preferred_hotel)[1]):
                        # check budget
                        if customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[1])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         1])
                            hotel.make_reservation(customer, hotel.get_booking_class_below(booking_class_preferred_hotel)[1])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         1])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break

                    elif len(airline.get_booking_class_below(booking_class_preferred_airline)) > 1 and \
                            len(hotel.get_booking_class_below(booking_class_preferred_hotel)) > 2 and \
                            airline.is_available(
                                airline.get_booking_class_below(booking_class_preferred_airline)[1]) and \
                            hotel.is_available(hotel.get_booking_class_below(booking_class_preferred_hotel)[2]):
                        # check budget
                        if customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         1])
                            hotel.make_reservation(customer, hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break

                    elif len(airline.get_booking_class_below(booking_class_preferred_airline)) > 2 and \
                            airline.is_available(
                                airline.get_booking_class_below(booking_class_preferred_airline)[2]) and \
                            hotel.is_available(booking_class_preferred_hotel):
                        # check budget
                        if customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(booking_class_preferred_hotel)):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer, booking_class_preferred_hotel)
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[1])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[1])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break

                    elif len(airline.get_booking_class_below(booking_class_preferred_airline)) > 2 and \
                            len(hotel.get_booking_class_below(booking_class_preferred_hotel)) > 1 and \
                            airline.is_available(
                                airline.get_booking_class_below(booking_class_preferred_airline)[2]) and \
                            hotel.is_available(hotel.get_booking_class_below(booking_class_preferred_hotel)[1]):
                        # check budget
                        if customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[1])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer, hotel.get_booking_class_below(booking_class_preferred_hotel)[1])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break

                    elif len(hotel.get_booking_class_below(booking_class_preferred_hotel)) > 1 and \
                            airline.is_available(booking_class_preferred_airline) and \
                            hotel.is_available(hotel.get_booking_class_below(booking_class_preferred_hotel)[1]):
                        # check budget
                        if customer.check_budget(
                                airline.get_price(booking_class_preferred_airline) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[1])):
                            airline.make_reservation(customer, booking_class_preferred_airline)
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[1])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[1])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         1])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[1])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[1])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[1])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break

                    elif len(hotel.get_booking_class_below(booking_class_preferred_hotel)) > 2 and \
                            airline.is_available(booking_class_preferred_airline) and \
                            hotel.is_available(hotel.get_booking_class_below(booking_class_preferred_hotel)[2]):
                        # check budget
                        if customer.check_budget(
                                airline.get_price(booking_class_preferred_airline) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer, booking_class_preferred_airline)
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[1]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         1])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break
                        elif customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer,
                                                   hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break

                    elif len(airline.get_booking_class_below(booking_class_preferred_airline)) > 2 and \
                            len(hotel.get_booking_class_below(booking_class_preferred_hotel)) > 2 and \
                            airline.is_available(
                                airline.get_booking_class_below(booking_class_preferred_airline)[2]) and \
                            hotel.is_available(hotel.get_booking_class_below(booking_class_preferred_hotel)[2]):
                        # check budget
                        if customer.check_budget(
                                airline.get_price(airline.get_booking_class_below(booking_class_preferred_airline)[2]) +
                                hotel.get_price(hotel.get_booking_class_below(booking_class_preferred_hotel)[2])):
                            airline.make_reservation(customer,
                                                     airline.get_booking_class_below(booking_class_preferred_airline)[
                                                         2])
                            hotel.make_reservation(customer, hotel.get_booking_class_below(booking_class_preferred_hotel)[2])
                            is_reservation_fulfilled = True
                            break

                if is_reservation_fulfilled:
                    break

        customer.print_record()


if __name__ == '__main__':
    driver()

