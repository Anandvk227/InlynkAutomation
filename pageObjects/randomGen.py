import random
import string

class randomGen:
    @staticmethod
    def random_email(size=7, chars=string.ascii_lowercase + string.digits):
        prefix = random.choice(string.ascii_lowercase)  # Ensure the first character is an alphabet
        prefix += ''.join(random.choice(chars) for _ in range(size - 1))  # Generate remaining characters
        suffix = "@yopmail.com"
        return prefix + suffix

    @staticmethod
    def random_first_name():
        random_part = ''.join(random.choice(string.ascii_letters) for _ in range(5))  # Random part after "test"
        return f"Test{random_part}"  # Prefix "test" to the random part

    @staticmethod
    def random_company_name():
        first_part = randomGen.random_first_name()  # Access the random_first_name method using the class
        second_part = ['Technologies', 'Solutions', 'Innovations', 'Systems', 'Services', 'Creators']
        third_part = ['Private Limited', 'Inc.', 'LLC', 'Enterprises', 'Group']

        # Randomly choose words for the second and third parts of the company name
        company_name = first_part + ' ' + random.choice(second_part) + ' ' + random.choice(third_part)
        return company_name

    @staticmethod
    def random_phone_number():
        prefixes = ['6', '7', '8', '9']  # Valid starting digits for Indian mobile numbers

        prefix = random.choice(prefixes)
        remaining_digits = ''.join(random.choice('0123456789') for _ in range(9))

        return f'{prefix}{remaining_digits}'

    @staticmethod
    def random_Emp_Id():
        prefix = '9'  # Assuming '9' as the fixed prefix
        remaining_digits = ''.join(random.choice('0123456789') for _ in range(4))  # Generating 4 random digits

        return f'{prefix}{remaining_digits}'

