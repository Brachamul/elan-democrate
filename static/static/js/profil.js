jQuery(function($) {

	// Compte la longueur de la bio du profil
	var biolength = $('#bio-input').val().length
	$('#bio-counter').text(biolength);

	$('#bio-input').on('keyup',function() {
		var len = this.value.length;
		$('#bio-counter').text(len);
	});

});
