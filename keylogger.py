import pynput.keyboard #Считываем онли с клавы

def process_key_press (key):     #содержит клавишу пользователя
    print (key)

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press) # функция обратного вызова (сработка только когда нажимается кллавиша)
with keyboard_listener:
    keyboard_listener.join() #Запуск 