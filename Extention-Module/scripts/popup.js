async function runCommand(command) {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: toggleHighlight,
        args: [command]
    });
}
document.getElementById('On').addEventListener('click', () => runCommand('on'));
document.getElementById('Off').addEventListener('click', () => runCommand('off'));

function toggleHighlight(status) {
    var emailRows = Array.from(document.querySelectorAll('.zA.yO'));
    var subject = Array.from(document.querySelectorAll('.bog'));
    for (i = 0; i < emailRows.length; i++) {
        if (subject[i].innerText.includes('IT')) {
            emailRows[i].style.backgroundColor = (status === 'on') ? 'red' : '';
        }
    }
}