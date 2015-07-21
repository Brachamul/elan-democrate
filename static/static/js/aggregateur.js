jQuery(function($) {

	$('.post[data-color="POS"]').each(function(){
		var health = parseInt($(this).data('health'), 10) - 1
		$(this).attr('data-health', health)
	})

	$('.post[data-color="NEG"]').each(function(){
		var health = parseInt($(this).data('health'), 10) + 1
		$(this).attr('data-health', health)
	})

	$('.post .vote.pos').click(function(){
		var url = '/p/' + $(this).data('postid') + '/vote/' + 'POS'
		var post = $(this).closest('.post')
		var health = parseInt(post.attr('data-health'), 10)
		$.get(url, function(color){
			post.attr('data-color', color)
			if (color == "POS") { health = health + 1 } else if (color == "NEG") { health = health - 1 }
			post.find('.health').hide().html(health).fadeIn()
		})
	})

	$('.post .vote.neg').click(function(){
		var url = '/p/' + $(this).data('postid') + '/vote/' + 'NEG'
		var post = $(this).closest('.post')
		var health = parseInt(post.attr('data-health'), 10)
		$.get(url, function(color){
			post.attr('data-color', color)
			if (color == "POS") { health = health + 1 } else if (color == "NEG") { health = health - 1 }
			post.find('.health').hide().html(health).fadeIn()
		})
	})


	$('.post .vote.neg').click(function(){
		var url = '/p/' + $(this).data('postid') + '/vote/' + 'NEG'
		var post = $(this).closest('.post') 
		$.get(url, function(color){
			post.attr('data-color', color)
		})
		var health = parseInt(post.attr('data-health'), 10)
		if (post.attr('data-color') == "POS") {
			health = health + 1	
		} else if (post.attr('data-color') == "NEG") {
			health = health - 1
		}
		post.find('.health').html(health)
	})

	$('.comment .vote.pos').click(function(){
		var commentid = $(this).attr("data-commentid")
		var commentSelector = '#comment-' + commentid
		var url = '/p/' + commentid + '/commentvote/' + 'POS'
		$.get(url, function(color){
			if (color == "POS") {
				$(commentSelector + ' > .healthbox .vote.pos').addClass("active")
				$(commentSelector + ' > .healthbox .vote.neg').removeClass("active")
			} else if (color == "NEU") {
				$(commentSelector + ' > .healthbox .vote').removeClass("active")
			} else if (color == "NEG") {
				$(commentSelector + ' > .healthbox .vote.neg').addClass("active")
				$(commentSelector + ' > .healthbox .vote.pos').removeClass("active")
			}
		})
	})

	$('.comment .vote.neg').click(function(){
		var commentid = $(this).attr("data-commentid")
		var commentSelector = '#comment-' + commentid
		var url = '/p/' + commentid + '/commentvote/' + 'NEG'
		$.get(url, function(color){
			if (color == "POS") {
				$(commentSelector + ' > .healthbox .vote.pos').addClass("active")
				$(commentSelector + ' > .healthbox .vote.neg').removeClass("active")
			} else if (color == "NEU") {
				$(commentSelector + ' > .healthbox .vote').removeClass("active")
			} else if (color == "NEG") {
				$(commentSelector + ' > .healthbox .vote.neg').addClass("active")
				$(commentSelector + ' > .healthbox .vote.pos').removeClass("active")
			}
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

	$('.comment .reply').click(function(){
		parent = $(this).data("comment")
		$('.comment-form[data-comment="' + parent + '"]').slideToggle().find('textarea').focus()
		$(this).toggleClass('active')
	})

	$('.root-commentor button.toggle').click(function(){
		$(this).toggleClass('btn-primary').toggleClass('btn-default')
		$(this).prev('form.nouveau_commentaire').slideToggle().find('textarea').focus()
	})


})
