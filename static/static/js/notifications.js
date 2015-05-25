jQuery(function($) {

	$('#notification_loader').click(function(){
		$.getJSON("/n/json/all", function(data){ // On chope les dernière notifications
			$('.notification').remove(); // On supprime les notifications
			for (notification in data) {
				var notification = [ // On créé le code d'affichage sur la base du JSON dans le data
					"<li class='notification'><a href='#'>",
					data[notification].acteur,
					data[notification].action,
					"</a></li>"
					].join(" ")
				$('#loaded_notifications').append(notification); // On rajoute tout ça au conteneur
			}
		});
	});

});
