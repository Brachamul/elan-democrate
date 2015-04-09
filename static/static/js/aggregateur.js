jQuery(function($) {

	$('.post .vote.pos').click(function(){
		var postid;
		postid = $(this).attr("data-postid");
		postSelector = '#post-' + postid;
		var url;
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

	$('#postranker').click(function(){
		$.get('/p/rank_posts', function(result){
			$('#postranker-result').html(result);
		});
	});

});
