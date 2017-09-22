def main():
    print 'woop woop, its the sound of the police!'
    speed = 95
    
    mood = 'good'
    if speed >= 80:
        print 'License and registration please'
        if mood == 'terrible' or speed >= 100:
            print 'You have the right to remain silent!!!!!'
        elif mood == 'bad' or speed >= 90:
            print "I'm going to have to write you a ticket."
            write_ticket(speed)
        else:
            print "Let's try to keep it under 80 ok bro!"

def write_ticket(s):
    print 'You gots to pay 1,000 galleon cause you was doing' , s , 'thats to fast boy'


if __name__ == '__main__':
    main()