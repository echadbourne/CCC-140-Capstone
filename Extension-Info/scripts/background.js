chrome.runtime.onInstalled.addListener(() => {
  chrome.action.setBadgeText({
    text: "OFF",
  });
});

const gmail = 'https://mail.google.com/';

chrome.action.onClicked.addListener(async (tab) => {
  if (tab.url.startsWith(gmail)) {
    // Retrieve the action badge to check if the extension is 'ON' or 'OFF'
    const prevState = await chrome.action.getBadgeText({ tabId: tab.id });
    // Next state will always be the opposite
    const nextState = prevState === 'ON' ? 'OFF' : 'ON';

    // Set the action badge to the next state
    await chrome.action.setBadgeText({
      tabId: tab.id,
      text: nextState,
    });

    var yourEmailElements=document.getElementsByClassName("zA yO"); //eQXFj_IXXK

    if (nextState === "ON") {
      // Insert the CSS file when the user turns the extension on
      for(i = 0; i<yourEmailElements.length; i++){   
      if( yourEmailElements[i].innerText == "IT" ){
          yourEmailElements[i].style.backgroundcolor = "red"; 
       }
}
      //await chrome.scripting.insertJS({
       // files: ["highlight.js"],
       //target: { tabId: tab.id },
      //});
    } else if (nextState === "OFF") {
      // Remove the CSS file when the user turns the extension off
        yourEmailElements.style.backgroundcolor = ""; 
       
}
      //await chrome.scripting.removeJS({
        //files: ["highlight.js"],
        //target: { tabId: tab.id },
      //});
    }
});
