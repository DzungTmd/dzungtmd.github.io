// var header = document.querySelector("h4")
// header.style.color = 'red'

// Conference -- Reverse button
// var Cpaper_Forward = document.querySelector("#C_forward");
// var Cpaper_Backward = document.querySelector("#C_backward");
// Cpaper_Forward.style.display = 'block';
// Cpaper_Backward.style.display = 'none';

// function C_Button() {
// var myButton = document.querySelector("#Button_C");
// if(myButton.attributes[4].value === 'true'){
//           Cpaper_Forward.style.display = 'none';
//           Cpaper_Backward.style.display = 'block';
// }else {
//           Cpaper_Forward.style.display = 'block';
//           Cpaper_Backward.style.display = 'none';
// }
//
// }

function C_Button() {
  var Cpaper_Backward = document.querySelector("#C_backward");
  var Cpaper_Forward = document.querySelector("#C_forward");
  Cpaper_Backward.classList.toggle('Chide');
  Cpaper_Forward.classList.toggle('Chide');
}

function J_Button() {
  var Jpaper_Backward = document.querySelector("#J_backward");
  var Jpaper_Forward = document.querySelector("#J_forward");
  Jpaper_Backward.classList.toggle('Jhide');
  Jpaper_Forward.classList.toggle('Jhide');
}
