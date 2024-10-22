let id = 0
const all = () => {
    let match = document.cookie.match(/_ga=.*[0-9]+\.[0-9]+;/)[0].split('.')
    id = `${match[2]}.${match[3].substr(0, match[3].length - 1)}`
    id = id?.split(';')[0]

    window.addEventListener('b24:form:init', (event) => {
    let form = event.detail.object;
   form.setProperty("param1", id);

    

});

}

const sourceSet =  () => {
    new URL(document.refferer).hostname()
let store = JSON.parse(localStorage.b24_crm_guest_utm)
if  (!store.list['utm_source']) {
    if (document.referrer.indexOf('google')>1){
console.log('google')
store.list['utm_source'] = 'google.by'
localStorage.b24_crm_guest_utm = JSON.stringify(store)

    }
    if ((document.referrer.indexOf('yandex')>1)||(document.referrer.indexOf('ya')>1)){
console.log('yandex')
store.list['utm_source'] = 'yandex.by'
localStorage.b24_crm_guest_utm = JSON.stringify(store)

    }

    if (document.referrer == '') {
console.log('direct')
store.list['utm_source'] = 'direct'
localStorage.b24_crm_guest_utm = JSON.stringify(store)

    }
} else {console.log('есть какието утм или они не пусты')}}

document.addEventListener("DOMContentLoaded", function(event) {
  setTimeout(sourceSet, 500)

});

document.addEventListener("DOMContentLoaded", function(event) {
  setTimeout(all, 500)
});

const getSuggestions = async () => {

  try{
      console.log(id)
     
const response = await fetch('https://tserashchuk.pythonanywhere.com/jsontest?client_id='+id, {cache: 'no-cache'});
    if(response.ok){
      const jsonResponse = await response.json()
    }
  }
  catch(error){
    console.log(error)
  }
}

//  document.addEventListener("DOMContentLoaded", function(event) {
//   setTimeout(getSuggestions, 600)
//  });


// let store = JSON.parse(localStorage.b24_crm_guest_utm)
// store.list['utm_source'] = 'newtest'
// localStorage.b24_crm_guest_utm = JSON.stringify(store)