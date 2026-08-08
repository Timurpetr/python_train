class Message:
    def __init__(self, text: str, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    msgs = {}

    @classmethod
    def add_message(cls, msg):
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        key = id(msg)
        if key in cls.msgs:
            cls.msgs.pop(key)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)


msg = Message("Всем привет!")
print(msg.text, msg.fl_like)
store = Viber()
store.add_message(msg)
