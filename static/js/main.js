$(document).ready(function(){
 
	$( "#clickme" ).click(function() {
		$( "#book" ).slideDown( "slow", function() {
		// Animation complete.
		});
	});

});