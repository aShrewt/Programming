#Change generator

pikachuhp = 50
count = 0

while pikachuhp > 0:
    angdmg = int(input("How much damage does angel do? "))
    pikachuhp -= angdmg
    print("pikachu has",angdmg,"done to it and only has",pikachuhp,"hp left!")
    count = count+1
print("Pikachu has fainted")
print("It took",count,"attacks to faint")