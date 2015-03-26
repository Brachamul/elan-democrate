jQuery(function($) {

	$('.post .vote.pos').click(function(){
		var postid;
		postid = $(this).attr("data-postid");
		postSelector = '#post-' + postid;
		arrowSelector = postSelector + ' .vote.pos';
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

});
