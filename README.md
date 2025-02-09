# chrome_open_local_video
**Google Chrome extension** that allows you to open video files from a link in a third-party video player.
Usually the **Google Chrome** does not allow you to open local files via a link **"file:///"**; you have to either manually copy the path and paste it into the explorer, or find other ways.
In fact, all we need is to get the local path and pass it to a third-party program.
This extension can be applied to any files, but in this example I used a video file.
In the instructions below I used **mpv** as video player, but you can use **VLC** or whatever you want.

# Installing manually (maybe i'll add install.bat later)
- git clone or download ZIP.
- Go to the **"C:\Users\USERNAME\AppData\Local\Google\Chrome\User Data\NativeMessagingHosts\"** If it doesn't exist then create it.
- Put in **"com.example.openfile.json"** from **"chrome_open_local_video/native/"**.
- Edit **"com.example.openfile.json"** with notepad, and find row:
   **"path": "C:\\chrome_open_local_video\\native\\start_app.bat"** - change path if needed.
- **Win + R** to open **cmd**.
  Then copy and paste this: **reg add HKCU\Software\Google\Chrome\NativeMessagingHosts\com.example.openfile /ve /t REG_SZ /d "%USERPROFILE%\AppData\Local\Google\Chrome\User Data\NativeMessagingHosts\com.example.openfile.json"**
- Open **chrome://extensions/** in browser. Enable **"Developer mode"**. Click **"Load unpacked"** and select the **"chrome_open_local_video/extension"** folder.
- Copy your **extension id**:
<img src="https://developer.chrome.com/static/docs/extensions/how-to/distribute/install-extensions/image/how-find-extension-id-v-5672686d70791.png" width=40% height=40%>

- Go to the **"C:\Users\USERNAME\AppData\Local\Google\Chrome\User Data\NativeMessagingHosts\"**. Edit **"com.example.openfile.json"** and paste your id here in place of **CHROME_EXTENSION_ID**:
   **"chrome-extension://CHROME_EXTENSION_ID/"**
- Edit **"chrome_open_local_video/native/open_file.py"** and change path to your external video player if needed (for me it's **"C:\\folder\\mpv.exe"**, you can paste your full path to exe or just type mpv if it is set in environment variables):
   **subprocess.run(["C:\\folder\\mpv.exe", file_path], shell=True)**
- Edit **start_app.bat** and change path to py file if needed:
   **python "C:\chrome_open_local_video\native\open_file.py" %***
- Restart **Chrome**, refresh the extension. That's all. After this, if you click on url that starts with **"file:///"** (like this **"file:///C:/folder/video.mp4"**) it will open in your external video player.

# Troubleshooting
If you have errors or nothing happened after click, check if the paths are correct. 
Try to restart chrome, refresh page and extension. 
Check if python is installed on your system. 
If an extension conflicts with others or causes errors in operation, simply turn it off and turn it on only when you need.  
