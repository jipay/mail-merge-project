#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", "r") as f:
    base = f.read()
    with open("./Input/Names/invited_names.txt", "r") as f1:
        guest = f1.readlines()
        for g in guest:
            name = g.strip()
            with open(f"./Output/ReadyToSend/{name}_letter.txt", "w") as f2:
                f2.write(base.replace("[name]", f"{name}"))
