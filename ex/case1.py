cmd = input()
match cmd.lower():
    case "Top" | "top" | "TOP": print("Команда top")
    case "Bottom" | "bottom" | "BOTTOM": print("Команда bottom")
    case "Left" | "left" | "LEFT": print("Команда letf")
    case "Right" | "right" | "RIGHT": print("Команда right") 
    case _: print("Неверная команда")