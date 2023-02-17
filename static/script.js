const nextButtons = document.querySelectorAll('.next');
for (let i = 0; i < nextButtons.length; i++) {
  nextButtons[i].addEventListener('click', function() {
	const currentFieldset = this.parentElement;
	const nextFieldset = currentFieldset.nextElementSibling;
	if (nextFieldset !== null) {
	  currentFieldset.style.display = 'none';
	  nextFieldset.style.display = 'block';
	}
  });
}

const previousButtons = document.querySelectorAll('.previous');
for (let i = 0; i < previousButtons.length; i++) {
  previousButtons[i].addEventListener('click', function() {
	const currentFieldset = this.parentElement;
	const previousFieldset = currentFieldset.previousElementSibling;
	if (previousFieldset !== null) {
	  currentFieldset.style.display = 'none';
	  previousFieldset.style.display = 'block';
	}
  });
}