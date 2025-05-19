import hashlib

target_hash = "3cc6520a6890b92fb55a6b3d657fd1f6" 

def bruteforce(hash):
    for i in range(1000000):
        password = f"{i:06d}"
        hashed = hashlib.md5(password.encode()).hexdigest()
        if hashed == hash:
            return "Great Success " + f"{hashed} "+ f"{password}"
    return "Failure"

print(bruteforce(target_hash))