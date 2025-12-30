from ps4b import Message 
from ps4b import PlaintextMessage
from ps4b import CiphertextMessage

if __name__ == '__main__':
     # ===== MESSAGE CLASS TESTS =====
      
      try:
            Cipher = CiphertextMessage("pmttw, ewztl!")
            decrypted = Cipher.decrypt_message()
            assert decrypted == (18, "hello, world!")
            print(f"Test Case, {decrypted[1]}, shifted {decrypted[0]} times passes")
      except AssertionError:
            print(f"{decrypted[1]} failed")

      
      try:
            Cipher = CiphertextMessage("W vohs Cpxsqh cfwsbhohsr dfcufoaawbu")
            decrypted = Cipher.decrypt_message()
            assert decrypted == (12, "I hate Object orientated programming")
            print(f"Test Case, {decrypted[1]}, shifted {decrypted[0]} times passes")
      except AssertionError:
            print(f"{decrypted[1]} failed")