# cmd = input()
#
# match cmd:
#     case "top" | "Top" | "TOP":
#         print('Команда top')
#     case "bottom" | "Bottom" | "BOTTOM":
#         print('Команда bottom')
#     case "right" | "Right" | "RIGHT":
#         print('Команда right')
#     case "left" | "Left" | "LEFT":
#         print('Команда left')


# def get_data(value):
#     match value:
#         case str(value):
#             return value
#         case int(value):
#             return value
#         case float(value):
#             return value
#
#     return None


def get_data(value):
    match value:
        case int(value) if value > 0:
            return value
        case float(value) if -100 <= value <= 100:
            return value
        case str(value):
            return value


    return None
