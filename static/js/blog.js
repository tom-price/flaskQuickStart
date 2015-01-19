$(document).ready(function(){
	var pagenumber = parseInt(location.hash.slice(1));

	if(isNaN(pagenumber)){
		pagenumber = 0;
	}

	var sections = $(".response1, .response2, .response3, .response4, .response5");

	sections.hide();
	$('.response' + pagenumber).show(0);
});

$(document).ready(function(){
	var button = document.querySelector('#methodsSelect');
	button.addEventListener('click', function(event) {
	    var target = document.querySelector(button.getAttribute('data-target'));
	    if (target.style.display == "none") {
	        target.style.display = "block";
	        button.innerHTML = "<h3 class='panel-title'>" + button.getAttribute('data-shown-text') + "</h3>";
	    } else {
	        target.style.display = "none";
	        button.innerHTML = "<h3 class='panel-title'>" + button.getAttribute('data-hidden-text') + "</h3>";
	    }
	});
});

$(document).ready(function(){
	var button = document.querySelector('#rulesSelect');
	button.addEventListener('click', function(event) {
	    var target = document.querySelector(button.getAttribute('data-target'));
	    if (target.style.display == "none") {
	        target.style.display = "block";
	        button.innerHTML = "<h3 class='panel-title'>" + button.getAttribute('data-shown-text') + "</h3>";
	    } else {
	        target.style.display = "none";
	        button.innerHTML = "<h3 class='panel-title'>" + button.getAttribute('data-hidden-text') + "</h3>";
	    }
	});
});
