$(document).ready(function () {
	$(window).scroll(function(){
		var st = $(this).scrollTop();
		$('.container').css({
			'transform' : 'translate(0%, ' + st/2 + '%'
		});
	});
});