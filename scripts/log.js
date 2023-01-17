
let key
login = document.getElementById('login');
logup = document.getElementById('logup');
logout = document.getElementById('logout');
my_profile = document.getElementById('my_profile');
let user
let writers
let rooms
log.style.visibility = "hidden";
function vision(){
if (key){
  logout.style.visibility = "visible";
  my_profile.style.visibility = "visible";
  login.style.visibility = "hidden";
  logup.style.visibility = "hidden"
}else{
  login.style.visibility = "visible";
  logup.style.visibility = "visible";
  logout.style.visibility = "hidden";
  my_profile.style.visibility = "hidden";
 }
}
vision()

 login.addEventListener('click', () => {
 log.style.visibility = "visible";
  log.innerHTML=`<form class="form" method="POST" name="login" >
    <h2 class="form__title">Введите данные</h2>
       <hr>
      <label class="label">
      <span class="label__title">Почта:</span>
      <input class="label__input" name="email" type="email" placeholder="email@domain.com" required>
         </label>
               <br><br>
    <label class="label">
      <span class="label__title">Пароль:</span>
      <input class="label__input" name="password" type="password" placeholder="пароль" required>
          </label>
                 <br><br>
        <button type="button" id='submit' class="form__submit" >Войти</button>
  </form>`;

  submit.addEventListener('click', async() =>{
let formLogin = document.forms.login
let email = formLogin.email.value;
let password = formLogin.password.value;
let body = {
email: email,
password: password
}

let options = {
  method: 'POST', // выбор метода запроса
  mode: 'cors', // режим работы запроса
  headers: { // дополнительные заголовки для запроса
    'Content-Type': 'application/json',
 'Authorization': key,
  },
  body: JSON.stringify(body)
}

if (body['email'] && body['password']) {
let response = await fetch('http://127.0.0.1:8000/dj-rest-auth/login/', options)
let data = response.json();
localStorage.setItem('key', data['key']);
 key =localStorage.getItem('key');
if(key) {
    vision();
     log.innerHTML=``;
     log.style.visibility = "hidden";

 options = {
  method: 'GET',
    headers: {
     'Authorization': `${key}`,
  },
  }

response = await fetch('http://127.0.0.1:8000/apiwriters/', options)
data = await response.json();
writers = data['results'];

response = await fetch('http://127.0.0.1:8000/apirooms/', options)
data = await response.json();
rooms = data['results'];
for (let key in rooms) {
    let li = document.createElement('li');
    li.innerHTML = `${rooms[key]['name']}`
    roomsUl.appendChild(li)
}

for (let key in rooms) {
    let li = document.createElement('li');
    li.innerHTML = `${writers[key]['name']}`
    chattersUl.appendChild(li)
}

}
}
})
})


 logout.addEventListener('click', () => {
  const options = {
  method: 'POST',
    headers: {
     'Authorization': `${key}`,
  },
  }
fetch('http://127.0.0.1:8000/dj-rest-auth/logout/', options)
.then(() => {
localStorage.removeItem('key')
key = null;
user = null;
writers = null;
rooms = null;
roomsUl.innerHTML ='';
chattersUl.innerHTML ='';

vision();
})
return false;
})
