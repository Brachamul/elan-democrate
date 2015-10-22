jQuery(function($) {

	var title_text = $('title').text() // On enregistre le titre pour pouvoir mettre des (1) quand il y a des notifications

	// Charger les notifs au premier chargement de la page
	$.get("/n/", function(data){
		// Récupérer le nombre de notification non vues pour les afficher dans la barre
		$('#loaded-notifications').html(data);
		$.get("/n/non_vues", function(data){ // Compter le nombre de notifs non vues
			$('.nombre-de-notifications-non-vues').html(data);
			if (data == '0') {
				$('.notificateur').addClass('tout-vu')
				$('title').text(title_text)
			} else {
				$('.notificateur').removeClass('tout-vu');
				$('title').text('(' + data + ') ' + title_text)
			};
		}); 
	});

	// Rafraichîr les notifications de la barre quand on clique sur le bouton de notifs
	$('#notification-loader').click(function(){
		$.get("/n/non_vues", function(nonvues){
			// Compte le nombre de notifs non-vues, pour voir s'il faut en récupérer de nouvelles
			if (nonvues != '0') {
				// Il y a de nouvelles notifications non-vues, on recharge
				$.get("/n/", function(data){
					// Récupérer le nombre de notification non vues pour les afficher dans la barre
					$('#loaded-notifications').html(data);
					$.get("/n/non_vues", function(data){ // Compter le nombre de notifs non vues
						$('.nombre-de-notifications-non-vues').html(data);
						$('.notificateur').removeClass('tout-vu');
						$('title').text('(' + data + ') ' + title_text)
						if (data == '0') {
							$('.notificateur').addClass('tout-vu')
							$('title').text(title_text)
						};
					});
				}); 
			};
		});
		$.get("/n/marquer_vues"); // marquer toutes les notifs en vues
	});

});


