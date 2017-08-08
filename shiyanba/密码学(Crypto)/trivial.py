#!/usr/bin/env python
import sys

alphaL = "abcdefghijklnmopqrstuvqxyz"
alphaU = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
num    = "0123456789"
keychars = num+alphaL+alphaU

# if len(sys.argv) != 3:
#   print "Usage: %s SECRET_KEY PLAINTEXT"%(sys.argv[0])
#   sys.exit()

key = 'T0pS3cre7key'#sys.argv[1]
# if not key.isalnum():
#   print "Your key is invalid, it may only be alphanumeric characters"
#   sys.exit()

plaintext = ''#sys.argv[2]

ciphertext = "Bot kmws mikferuigmzf rmfrxrwqe abs perudsf! Nvm kda ut ab8bv_w4ue0_ab8v_DDU"
for i in range(len(ciphertext)):
  rotate_amount = keychars.index(key[i%len(key)])
  if ciphertext[i] in alphaL:
    enc_char = ord('a') + (ord(ciphertext[i])-ord('a')-rotate_amount)%26
  elif ciphertext[i] in alphaU:
    enc_char = ord('A') + (ord(ciphertext[i])-ord('A')-rotate_amount)%26
  elif ciphertext[i] in num:
    enc_char = ord('0') + (ord(ciphertext[i])-ord('0')-rotate_amount)%10
  else:
    enc_char = ord(ciphertext[i])
  plaintext = plaintext + chr(enc_char)

print plaintext