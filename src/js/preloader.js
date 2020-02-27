






var	images = document.images;
var	images_total_count= images.length;
var	images_loaded_count=0;
var	preloader = document.getElementById('page-preloader');
var	perc_display=document.getElementById('loader_perc');

for (i=0; i<images_total_count; i++)
{
	image_clone=new Image();
	image_clone.onload = image_loaded;
	image_clone.onerror = image_loaded;
	image_clone.src = images[i].src;
}
function image_loaded()
{
	images_loaded_count++;
	perc_display.innerHTML = (( (100 / images_total_count) * images_loaded_count )<<0) +'%' ;


	if (images_loaded_count >= images_total_count)
	{
		setTimeout(function () {
			if (!preloader.classList.contains('prealoader-done')) {
				preloader.classList.add('preloader-done')
			}
		}, 1000);
	}
}























