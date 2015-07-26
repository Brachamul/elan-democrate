jQuery(function($) {



	// On garde en mémoire le score des commentaires et des posts

	$('[data-color="POS"]').each(function(){
		var health = parseInt($(this).data('health'), 10) - 1
		$(this).attr('data-health', health)
	})

	$('[data-color="NEG"]').each(function(){
		var health = parseInt($(this).data('health'), 10) + 1
		$(this).attr('data-health', health)
	})



	// On envoie un vote et on récupère la couleur du résultat (POS-NEU-NEG)

	$('.post .vote').click(function(){
		var post = $(this).closest('.post')
		var postId = post.data('postid')
		var voteColor = $(this).data('color')
		var url = '/p/' + postId + '/vote/' + voteColor
		var health = parseInt(post.attr('data-health'), 10)
		$.get(url, function(color){
			post.attr('data-color', color)
			if (color == "POS") { health = health + 1 } else if (color == "NEG") { health = health - 1 }
			post.find('.health').hide().html(health).fadeIn()
		})
	})

	$('.comment .vote').click(function(){
		var comment = $(this).closest('.comment')
		var commentId = comment.data('commentid')
		var voteColor = $(this).data('color')
		var url = '/p/comment/' + commentId + '/vote/' + voteColor
		var health = parseInt(comment.attr('data-health'), 10)
		$.get(url, function(color){
			comment.attr('data-color', color)
			if (color == "POS") { health = health + 1 } else if (color == "NEG") { health = health - 1 }
			comment.find('.health').hide().html(health).fadeIn()
		})
	})


	// Au chargement, on évalue la couleur attribuée par l'utilisateur aux commentaires
	$('.comment').each(function(){
		var comment = $(this)
		var url = '/p/comment/' + comment.data('commentid') + '/getcolor'
		var health = parseInt(comment.attr('data-health'), 10)
		$.get(url, function(color){
			comment.attr('data-color', color)
			if (color == "POS") { health = health + 1 } else if (color == "NEG") { health = health - 1 }
			comment.find('.health').hide().html(health).fadeIn()
		})
	})


	$('#postranker').click(function(){
		$.get('/p/rank_posts', function(result){
			$('#postranker-result').html(result)
		})
	})

	$('#commentmedic').click(function(){
		$.get('/p/comment_medic', function(result){
			$('#commentmedic-result').html(result)
		})
	})

	// Remplace les tags heading par des paragraphes dans les posts & commentaires en markdown
	$('.aggregateur .content').find('h1, h2, h3, h4, h5, h6').replaceWith(function() {
		return '<p>' + $(this).text() + '</p>'
	})

	$('.comment .hider, .comment-shower').click(function(){
		$(this).closest('.hiding-container').children('.comment').slideToggle()
		$(this).closest('.hiding-container').children('.comment-shower').slideToggle()
	})

	$('.comment .reply').click(function(){
		parent = $(this).data("comment")
		$('.comment-form[data-comment="' + parent + '"]').slideToggle().find('textarea').focus()
		$(this).toggleClass('active')
	})

	$('.comment .link.modify').click(function(){
		$(this).closest('.comment').children('form.modifier').slideToggle()
		$(this).closest('.comment').children('.content').slideToggle()
	})

	$('.root-commentor button.toggle').click(function(){
		$(this).toggleClass('btn-primary').toggleClass('btn-default')
		$(this).prev('form.nouveau_commentaire').slideToggle().find('textarea').focus()
	})



	// RÉACTIVITÉ

	$('#sidebar-toggle').click(function(){
		$('#aggregateur').toggleClass('sidebar-show')
	})

	$('.nouveau-post .panel-heading').click(function(){
		$(this).next('.panel-body').slideToggle()
	})


	


})
