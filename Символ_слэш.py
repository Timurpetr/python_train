# значения этих переменных в программе не менять
DEBUG = 10, "DEBUG"
INFO = 20, "INFO"
WARNING = 30, "WARNING"
ERROR = 40, "ERROR"
CRITICAL = 50, "CRITICAL"


# здесь объявляйте функцию
def log_event(
    timestamp, message, *, level=INFO, format_log="[%(time)] %(levelname) - %(message)"
):
    if level[0] <= INFO[0]:
        return None
    result = format_log
    result = result.replace("%(time)", str(timestamp))
    result = result.replace("%(message)", message)
    result = result.replace("%(levelname)", level[1])
    result = result.replace("%(levelno)", str(level[0]))
    return result


log_time = int(input())
log_msg = input()

# здесь продолжайте программу


log_item = log_event(
    log_time, log_msg, level=WARNING, format_log="%(levelname) - (%(time)) %(message)"
)
print(log_item)
