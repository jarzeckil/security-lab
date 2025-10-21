import itertools
import string

def generate_passwords(lower, upper, output_filename="passwords.txt"):
    """
    Generuje wszystkie możliwe hasła o długości od lower do upper znaków,
    składające się z małych liter [a-z] i zapisuje je do pliku.
    """
    
    chars = string.ascii_letters + string.digits
    with open(output_filename, 'w') as f:
        for length in range(lower, upper+1):  # Dla długości od 1 do 5
            for combo in itertools.product(chars, repeat=length):
                password = "".join(combo)
                f.write(password + '\n')

if __name__ == "__main__":

    generate_passwords(1,4)

    print("Hasła zostały wygenerowane i zapisane w pliku passwords.txt")