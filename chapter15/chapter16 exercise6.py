# Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone:
import time

class SMS_store:
    def __init__(self):
        self.inbox = []     # boş liste

    def add_new_arrival(self, from_number, text_of_sms, read_status = False):
        number = str(from_number)
        time_received = time.strftime("%D %T")      # zamanı string e çevirir ½D ay,gün,yıl  %T saat,dakika,saniye
        self.inbox.append([time_received, number, text_of_sms, read_status])

    def message_count(self):
        return "There are {0} messages in your Inbox".format(len(self.inbox))

    def get_unread_indexes(self):
        unread = []     # okunmamaışlar için liste
        for index, message in enumerate(self.inbox):        # enumerate, index numaraları ile sıralar.
            if False in message:
                unread.append(index)
        return "Unread Messages in:", unread

    def get_message(self, index):
        message = self.inbox[index]
        message[3] = "Read"        # read_status u Okunmuş olarak işaretler
        return message[ : 3]

    def delete(self, index):
        del self.inbox[index]
        return "Deleted Message", index

    def clear(self):
        self.inbox = []     # listeyi sıfırlar.
        return "Empty Inbox"

a =SMS_store()
a.add_new_arrival(531,"acm")
a.add_new_arrival(532,"asd")
a.add_new_arrival(533,"qwe")
a.add_new_arrival(534,"zxc")

print(a.get_message(1))
print(a.message_count())
print(a.get_unread_indexes())
print(a.get_message(0))
print(a.get_unread_indexes())
print(a.delete(3))
print(a.message_count())
print(a.clear())
print(a.message_count())