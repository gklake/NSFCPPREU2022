import csv
import random
import string


def get_list(filename):
    lis = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lis.append(row[0])
    
    return lis


def create_email_username(adjectives, nouns):
    adjective = adjectives[random.randint(0, len(adjectives)-1)]
    noun = nouns[random.randint(0, len(nouns)-1)]
    number = random.randint(0, 99)
    
    username = "%s_%s%02d" % (adjective, noun, number)
    email = username + "@gmail.com"
    
    return email, username
    

def create_password(characters, length):
    temp = random.sample(characters, length)
    password = "".join(temp)
    
    return password


def save_authentification(info):
    with open('authentification.txt', 'a') as file:
        file.write("%s,%s,%s,%s\n" % tuple(info))
    
    print('Done')


def main():
    adjectives = get_list('adjectives.txt')
    nouns = get_list('nouns.txt')
    
    email, username = create_email_username(adjectives, nouns)
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation.replace(',', '')
    all = lower + upper + num + symbols

    password = create_password(all, 16)
    
    site = input("Enter name of website: ")
    info = [site, email, username, password]

    save_authentification(info)


if __name__ == "__main__":
    main()







