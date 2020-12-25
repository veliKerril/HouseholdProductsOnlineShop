// document.body.innerHTML = "This is some content";
document.getElementById('click-me').addEventListener('click', function() {
	document.querySelector('.bg-modal').style.display = 'flex';

});

document.querySelector('.close').addEventListener('click', function() {
	document.querySelector('.bg-modal').style.display = 'none';
});
