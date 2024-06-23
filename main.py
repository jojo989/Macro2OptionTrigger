import tkinter as tk
from tkinter import filedialog

def makeTriggers(macro):
    objects = []
    for entry in macro:
        parts = entry.split('|')
        if len(parts) < 7:
            continue
        holdRelease = int(parts[1])
        p1xPos = float(parts[5])
        button = int(parts[2])
        
        if button == 1:
            inputValue = -1 if holdRelease == 1 else 1
            objectStr = f"1,2899,2,{p1xPos},3,105,155,1,36,1,165,{inputValue};"
            objects.append(objectStr)
    return objects

def main():
    root = tk.Tk()
    root.withdraw()

    macroFilePath = filedialog.askopenfilename(filetypes=(("XD Files", "*.xd"), ("All Files", "*.*")))
    
    with open(macroFilePath, 'r') as file:
        macroData = file.readlines()

    triggers = makeTriggers(macroData)
    
    triggersStr = ''.join(triggers)
    
    saveFilePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
    with open(saveFilePath, 'w') as saveFile:
        saveFile.write(triggersStr)

    print(f"Level string saved at {saveFilePath}")

if __name__ == "__main__":
    main()
