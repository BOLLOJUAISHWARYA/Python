//slideshow

let image=document.getElementById('smoothiehomeimg1');
let randomimgarray=["static/Home-images/slide.jpg","static/Home-images/slide1.jpg","static/Home-images/slide2.jpg"];
let length=randomimgarray.length;

function displayimg(){
    let imageindex=0;
    setInterval(function(){
        image.src=randomimgarray[imageindex];
        imageindex++;
        if(imageindex>=length){
            imageindex=0;
        }
    },2200);
}

displayimg();



