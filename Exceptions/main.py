while True:
    try:
        number = int(input('Whats your fav number?\n'))
        # number == (18/number)
        break
    except ValueError:
        print('Make sure to input a number')
    except ZeroDivisionError:
        print("Don't pick 0")
    # Below not recommended since it will hide all errors
    except:
        break
    # Occurs every single time
    finally:
        print('loop complete')
