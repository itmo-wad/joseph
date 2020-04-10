// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var Img = document.getElementById("img");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
document.addEventListener('click',showModal);
function showModal() {
	if (event.target.id == "myBtn") {
  	modal.style.display = "block";
		Img.src = event.target.parentNode.children[0].src;
	}
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
