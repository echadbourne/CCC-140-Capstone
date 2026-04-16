async function runCommand(command) {
    const url = 'http://localhost:5984/phishphilter/_all_docs?include_docs=true&descending=true&limit=5';
    const response = await fetch(url, {
        method: 'GET',
        mode: 'cors',
        credentials: 'include',
        headers: {
            'Authorization': 'Basic ' + btoa("phish:philter"),
            'Accept': 'application/json'
        }
    });
    const data = await response.json();
    let emails = [];
    data.rows.forEach(row => {
        if (row.doc.Subject){
            const docSubject = Object.values(row.doc.Subject);
            emails = emails.concat(docSubject);
        }
    });
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: toggleHighlight,
        args: [command, emails]
    });
}
document.getElementById('On').addEventListener('click', () => runCommand('on'));
document.getElementById('Off').addEventListener('click', () => runCommand('off'));


function toggleHighlight(status, emails) {
    var emailRows = Array.from(document.querySelectorAll('.zA'));
    var subject = Array.from(document.querySelectorAll('.bog'));
    for (i = 0; i < emailRows.length; i++) {
        if (emails.some(phish => subject[i].innerText.toLowerCase() === phish.toLowerCase())) {
            emailRows[i].style.backgroundColor = (status === 'on') ? 'red' : '';
        }
    }
}