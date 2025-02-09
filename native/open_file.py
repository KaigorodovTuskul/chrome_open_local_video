import sys
import json
import subprocess

def read_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        return None
    message_length = int.from_bytes(raw_length, byteorder="little")
    return json.loads(sys.stdin.read(message_length))

def send_response(response):
    response_json = json.dumps(response)
    sys.stdout.buffer.write(len(response_json).to_bytes(4, byteorder="little"))
    sys.stdout.write(response_json)
    sys.stdout.flush()

if __name__ == "__main__":
    message = read_message()
    if message and "url" in message:
        file_path = message["url"].replace("file:///", "").replace("/", "\\")  
        subprocess.run(["C:\\folder\\mpv.exe", file_path], shell=True)
    send_response({"status": "done"})
