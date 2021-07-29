---
sidebar_position: 3
---

# Javascript

top 10 des librairies 2021 : https://medium.com/javascript-in-plain-english/top-10-most-popular-javascript-libraries-to-use-in-2021-5da60f187992

programmation fonctionnel : https://www.youtube.com/watch?v=mW_nLYvXyKk
programmation fonctionnel : https://www.youtube.com/watch?v=YZwilQqzdYA
programmation fonctionnel : https://www.youtube.com/watch?v=-Cdt-1tWJ3M


https://www.youtube.com/watch?v=Kp3HGwlXwCk
```js
// L'objet / JSON qui stocke ke formulaire
atDataForm = {
        user_firstname: null,
        user_lastname: null,
        user_email: null,
        user_subject: null,
        user_message: null
      }

// Fonction vérifie si l'object possède des clés dont la valeur est null 
function checkIfObjectContainsNullValue(object){
    let isObjectNullLess = true
    Object.entries(object).map(([k,v]) => !v ? isObjectNullLess = false : undefined )
    return isObjectNullLess
}

// Fonction métier, vérifie sur le formulaire est bien complété
function submitEmailForm(){
  if(checkIfObjectContainsNullValue(atDataForm)){
      emailjs.send(atDataForm)
      alert("Votre email a bien été envoyé")
  } else {
     alert("Veuillez correctement remplire le formulaire")
  }
} 

```