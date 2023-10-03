import requests
import os, time
import json
import lzma

# Set up the Telegram bot
bot_token = os.getenv('bot_token')
chat_id = os.getenv('chat_id')
folder_path = "./mygreatshot"

def is_file_within_previous_minutes(file_path, minutes):
    file_modified_time = os.path.getmtime(file_path)
    current_time = time.time()
    time_difference = current_time - file_modified_time
    minutes_difference = time_difference / 60
    return minutes_difference <= minutes






class tele():

    def send_message(self,text):
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {'chat_id': chat_id, 'text':text}
        r = requests.post(url, data=data)

    def send_file(self, file_path):
        try:
            # Check if the file is a photo
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.jfif')):
                url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
                files = {'photo': open(file_path, 'rb')}
            # Check if the file is a video
            elif file_path.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
                url = f"https://api.telegram.org/bot{bot_token}/sendVideo"
                files = {'video': open(file_path, 'rb')}

            data = {'chat_id': chat_id}
            r = requests.post(url, files=files, data=data)
            # return print(r.text)
        except:
            pass

done_files = []
while True:
    folder_path = "./aliprod29"
    for filename in os.scandir(folder_path):
        if filename.is_file() and not filename.name.endswith(".json.xz"):
            if filename.path not in done_files:
                if is_file_within_previous_minutes(filename.path, 5):
                    print(filename.path)
                    done_files.append(filename.path)
                    tele().send_file(filename.path)
                    time.sleep(10)
                    # os.remove(filename.path)
                else:
                    pass
        elif filename.path not in done_files and filename.name.endswith('.json.xz'):
            if is_file_within_previous_minutes(filename.path, 5):
                # Path to the compressed JSON file
                file_path = filename.path
                # Read the compressed file
                with lzma.open(file_path, 'rt') as file:
                    # Load the JSON data
                    data = json.load(file)
                    try:
                        done_files.append(filename.path)
                        tele().send_message(data['node']['edge_media_to_caption']['edges'][0]['node']['text'])
                    except:pass
                # Access and process the data as needed
                # For example, print the value of a specific key
