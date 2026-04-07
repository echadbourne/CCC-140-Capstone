const button = document.createElement('button')
button.innerText = 'Highlight Suspicious Emails'
button.id = 'mainButton'
button.addEventListener('click', () => {
  var emailRow = Array.from(document.querySelectorAll(".zA.yO"));
  var subject = Array.from(document.querySelectorAll(".bog"));
  for(i=0; i<emailRow.length; i++) {
    if(subject[i].innerText.includes("IT")) {
      emailRow[i].style.backgroundColor = "red";
    }
  }

})

document.body.appendChild(button);
// Button
