#!/usr/bin/env python3
#Script Para Criar PenDrives Bootaveis

import os

os.system("sudo fdisk -l")
disc=input("Digite o disco exatamente: ")
os.system("sudo umount "+disc)
os.system("sudo mkfs.vfat -I"+disc)
img=input("Digite o local da imagem: ")
os.system("sudo dd if="+img+" of="+disc+" && sync")
