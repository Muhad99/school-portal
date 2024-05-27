const popup = document.querySelector('.chat-popup');
const chatBtn = document.querySelector('.chat-btn');
const submitBtn =document.querySelector('.submit');
const chatArea = document.querySelector('.chat-area');
const inputElm = document.querySelector('input');

const emojiBtn = document.querySelector('#emoji-btn');
const picker = new EmojiButton();

//Emoji Selector
window.addEventListener('DOMContentLoaded', () => {

	picker.on('emoji', emoji => {
		document.querySelector('input').value += emoji;
	});

 	emojiBtn.addEventListener('click', () => {
 		picker.togglePicker(emojiBtn);
 });
});

//chat button toggler

chatBtn.addEventListener('click', ()=>{
  console.log('2')
	popup.classList.toggle('show');
})

// Send message
submitBtn.addEventListener('click', ()=>{
	let userInput = inputElm.value; 
	
	let temp = `<div class="out-msg">
	<span class="my-msg">${userInput}</span>
	<img src="image/bg1.png" class="avatar">
	</div>`;

	chatArea.insertAdjacentHTML("beforeend", temp);
	inputElm.value = '';
})