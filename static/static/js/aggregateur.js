jQuery(function($) {

	$('.post .vote.pos').click(function(){
		var postid;
		postid = $(this).attr("data-postid");
		postSelector = '#post-' + postid;
		var url;
		url = '/p/' + postid + '/vote/' + 'POS';
		$.get(url, function(color){
			if (color == "POS") {
				$(postSelector + ' .vote.pos').addClass("active");
				$(postSelector + ' .vote.neg').removeClass("active");
			} else if (color == "NEU") {
				$(postSelector + ' .vote').removeClass("active");
			} else if (color == "NEG") {
				$(postSelector + ' .vote.neg').addClass("active");
				$(postSelector + ' .vote.pos').removeClass("active");
			}
		})
	});

	$('.post .vote.neg').click(function(){
		var postid;
		postid = $(this).attr("data-postid");
		postSelector = '#post-' + postid;
		var url;
		url = '/p/' + postid + '/vote/' + 'NEG';
		$.get(url, function(color){
			if (color == "POS") {
				$(postSelector + ' .vote.pos').addClass("active");
				$(postSelector + ' .vote.neg').removeClass("active");
			} else if (color == "NEU") {
				$(postSelector + ' .vote').removeClass("active");
			} else if (color == "NEG") {
				$(postSelector + ' .vote.neg').addClass("active");
				$(postSelector + ' .vote.pos').removeClass("active");
			}
		})
	});

	$('.comment .vote.pos').click(function(){
		var commentid;
		commentid = $(this).attr("data-commentid");
		commentSelector = '#comment-' + commentid;
		var url;
		url = '/p/' + commentid + '/commentvote/' + 'POS';
		$.get(url, function(color){
			if (color == "POS") {
				$(commentSelector + ' > .healthbox .vote.pos').addClass("active");
				$(commentSelector + ' > .healthbox .vote.neg').removeClass("active");
			} else if (color == "NEU") {
				$(commentSelector + ' > .healthbox .vote').removeClass("active");
			} else if (color == "NEG") {
				$(commentSelector + ' > .healthbox .vote.neg').addClass("active");
				$(commentSelector + ' > .healthbox .vote.pos').removeClass("active");
			}
		})
	});

	$('.comment .vote.neg').click(function(){
		var commentid;
		commentid = $(this).attr("data-commentid");
		commentSelector = '#comment-' + commentid;
		var url;
		url = '/p/' + commentid + '/commentvote/' + 'NEG';
		$.get(url, function(color){
			if (color == "POS") {
				$(commentSelector + ' > .healthbox .vote.pos').addClass("active");
				$(commentSelector + ' > .healthbox .vote.neg').removeClass("active");
			} else if (color == "NEU") {
				$(commentSelector + ' > .healthbox .vote').removeClass("active");
			} else if (color == "NEG") {
				$(commentSelector + ' > .healthbox .vote.neg').addClass("active");
				$(commentSelector + ' > .healthbox .vote.pos').removeClass("active");
			}
		})
	});

	$('#postranker').click(function(){
		$.get('/p/rank_posts', function(result){
			$('#postranker-result').html(result);
		});
	});

	$('#commentmedic').click(function(){
		$.get('/p/comment_medic', function(result){
			$('#commentmedic-result').html(result);
		});
	});

	// Remplace les tags heading par des paragraphes dans les posts & commentaires en markdown
	$('.aggregateur .content').find('h1, h2, h3, h4, h5, h6').replaceWith(function() {
		return '<p>' + $(this).text() + '</p>';
	});


});
