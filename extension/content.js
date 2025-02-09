document.addEventListener("click", function (event) {
    let target = event.target.closest("a");
    if (!target) return;

    let url = target.href;
    if (url.startsWith("file:///")) {
        event.preventDefault();
        chrome.runtime.sendMessage({ action: "open_file", url: url });
    }
});
