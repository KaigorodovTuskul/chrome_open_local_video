chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "open_file") {
        chrome.runtime.sendNativeMessage("com.example.openfile", { url: message.url });
    }
});
