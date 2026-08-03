"""
Password storage demo — plaintext vs AES vs bcrypt vs SHA256
For educational use only. Never store real user passwords like this.
"""

import bcrypt
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# The demo password — pick something on the weaker side so the crack test
# actually finishes in a reasonable time. This is the whole point of the test.
PASSWORD = "Passw0rd123"

def store_plaintext(password):
    return password  # exactly what it looks like — the baseline of "wrong"

def store_aes(password):
    key = get_random_bytes(16)          # AES-128 key, kept in memory only for demo
    cipher = AES.new(key, AES.MODE_ECB) # ECB used here only to keep the demo simple
    ciphertext = cipher.encrypt(pad(password.encode(), AES.block_size))
    return ciphertext.hex(), key.hex()

def store_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def store_bcrypt(password):
    salt = bcrypt.gensalt(rounds=12)  # cost factor 12 — the industry-standard default
    return bcrypt.hashpw(password.encode(), salt).decode()

if __name__ == "__main__":
    print(f"Password: {PASSWORD}\n")

    print("1. Plaintext storage:")
    print(f"   {store_plaintext(PASSWORD)}\n")

    print("2. AES encryption:")
    ciphertext, key = store_aes(PASSWORD)
    print(f"   Ciphertext: {ciphertext}")
    print(f"   Key (never store this next to the ciphertext!): {key}\n")

    print("3. SHA256 hash (fast hash — for the crack comparison):")
    sha_hash = store_sha256(PASSWORD)
    print(f"   {sha_hash}\n")

    print("4. bcrypt hash (slow hash — for the crack comparison):")
    bcrypt_hash = store_bcrypt(PASSWORD)
    print(f"   {bcrypt_hash}\n")

    # Write hashes to files John the Ripper can consume directly
    with open("sha256_hash.txt", "w") as f:
        f.write(f"testuser:{sha_hash}\n")

    with open("bcrypt_hash.txt", "w") as f:
        f.write(f"testuser:{bcrypt_hash}\n")

    print("Wrote sha256_hash.txt and bcrypt_hash.txt for John the Ripper.")
