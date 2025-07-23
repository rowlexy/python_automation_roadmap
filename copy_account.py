import sys, pyperclip
profiles = {
    "work": "rowland.elegbede@chrobinson.com",
    "gmail": "rowlandelegbede@gmail.com",
    "yahoo": "rowlexy_2009@yahoo.com"
}

if len(sys.argv) < 2:
    print('Fewer arguments, usage: python3 copy_password.py [account]')
    sys.exit()

account = sys.argv[1]


if account in profiles:
    print(f'{account.title()} email address copied successfully')
    pyperclip.copy(profiles[account])
else:
    print(f'Account does not exist')
