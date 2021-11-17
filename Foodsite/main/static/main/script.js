let teg_num_cart = document.getElementById("num_cart_p")

num = 0;
for(let i=0; i < localStorage.length; i++){
   key = localStorage.key(i)
   num += Number(localStorage.getItem(key))
}
teg_num_cart.innerHTML = num;

function add(id){
   let conut = 1
   for(let i=0; i < localStorage.length; i++){
      key = localStorage.key(i)
      if(key == id){
         conut = Number(localStorage.getItem(key)) + 1
         localStorage.removeItem(key);
      }
   }
   localStorage.setItem(id, conut);
   teg_num_cart.innerHTML = ++num;

   console.log(window.localStorage)
}

function buy(){
   localStorage.clear();
   let container = document.getElementById("container")
   container.innerHTML = ""
   teg_num_cart.innerHTML = "";
}