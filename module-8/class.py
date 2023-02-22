class Phone:
    manufactured='china'
    def send_msg(self):
        print('hello')

new_phone=Phone()
new_phone.send_msg()
print(new_phone.manufactured)