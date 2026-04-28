password = input("Enter your password: ")

password_tamanho = len(password)

has_at = '@' in password
has_hashtag = '#' in password
has_exclamation = '!' in password

if  password_tamanho >= 8 and (has_at or has_hashtag or has_exclamation):
    print("Your password is ok")
has_exclamation("Your password is very weak")
