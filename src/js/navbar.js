$(document).ready(function () {
	$('.menu-btn').on('click', function(){
		event.preventDefault();
		$('.menu').toggleClass('menu_active');
		$('.contant').toggleClass('contant_active')
	})
});