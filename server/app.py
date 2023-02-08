from flask import Flask, request
app = Flask(__name__)
list_of_messages = []


@app.route('/')
def hello_world():
    return 'Messanger Flask server is running! ' \
           '<br> <a href="/status">Check status</a>'


@app.route('/status')
def status():
    return {
        'messages_count': len(list_of_messages)
    }


@app.route("/api/Messanger", methods=['POST'])
def send_message():
    message = request.json
    print(message)
    list_of_messages.append(message)
    message_text = f"{message['UserName']} <{message['TimeStamp']}>: {message['MessageText']}"
    print(f"Всего сообщений: {len(list_of_messages)} Посланное сообщение: {message_text}")
    return f"Сообщение отослано успешно. Всего сообщений: {len(list_of_messages)} ", 200


@app.route("/api/Messanger/<int:message_id>")
def get_message(message_id: int):
    print(message_id)
    if 0 <= message_id < len(list_of_messages):
        print(list_of_messages[message_id])
        return list_of_messages[message_id], 200
    else:
        return "Not found", 400


if __name__ == '__main__':
    app.run()

