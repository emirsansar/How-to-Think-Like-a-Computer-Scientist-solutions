class SMS_store:

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, number, time, text):
        read_control = False
        self.inbox.append( [str(number), time, text, read_control] )

    def message_count(self):
        return "There are {0} messages in your inbox".format(len(self.inbox))

    def get_unread_indexes(self):
        unreaded_messages = []
        for i in range(0,len(self.inbox)):
            if self.inbox[i][3] == False:
                unreaded_messages.append(self.inbox[i])
        return "Unread messages: ", unreaded_messages

    def get_message(self,i):
        if i in range(0, len(self.inbox)):
            mesaj = self.inbox[i]
            mesaj[3] = True
            return self.inbox[i][:3]

    def delete(self, i):
        del self.inbox[i]
        return "Message was deleted.", i

    def clear(self):
        self.inbox = []
        return "The message box has been emptied."


a = SMS_store()
a.add_new_arrival(531,"01.02","acm")
a.add_new_arrival(532,"02.02","asd")
a.add_new_arrival(533,"03.02","qwe")
a.add_new_arrival(534,"04.02","zxc")

print(a.get_message(1))
print(a.message_count())
print(a.get_unread_indexes())
print(a.get_message(0))
print(a.get_unread_indexes())
print(a.delete(3))
print(a.message_count())
print(a.clear())
print(a.message_count())