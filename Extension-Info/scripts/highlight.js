var yourEmailElements=doc.getElementsByClassName("eQXFj_IXXK");

for(i = 0; i<yourEmailElements.length; i++){   
      if( yourEmailElements[i].innerText == "what you are looking for" ){
          yourEmailElements[i].turnRed(); 
       }
}