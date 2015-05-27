jQuery(function($) {

	// Rafraichîr les notifications de la barre
	$('#notification-loader').click(function(){
		$.get("/n/", function(data){
			// Récupérer le nombre de notification non vues pour les afficher dans la barre
			$('#loaded-notifications').html(data);
			$.get("/n/marquer_vues"); // marquer toutes les notifs en vues
			$.get("/n/non_vues", function(data){ // Compter le nombre de notifs non vues
				$('#non-vues').html(data);
				$('#notifications').removeClass('tout-vu');
				if (data == '0') {
					$('#notifications').addClass('tout-vu')
				};
			}); 
		});
	});

	// Compter le nombre de notifs non vues
	$.get("/n/non_vues", function(data){
		$('#non-vues').html(data);
		$('#notifications').removeClass('tout-vu');
		if (data == '0') {
			$('#notifications').addClass('tout-vu')
		};
	}); 

});


