btns = document.querySelectorAll(".btn");

let text = ''

for (let i =0; i<btns.length; i++){
    btns[i].addEventListener('click', function onClick() {
        btns[i].style.backgroundColor = 'salmon';
        btns[i].style.color = 'white';
        console.log(btns[i]);
        a =1;
        post( "/postmethod", {
          a
        })
        
      });


}
console.log(btns);