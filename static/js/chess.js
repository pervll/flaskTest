/*var canvas=document.getElementById("board")
var ctx=canvas.getContext("2d")
var image=new Image();
image.onload = function() {
    canvas.style.position='absolute'
    canvas.setAttribute('width',image.width)
    canvas.setAttribute('height',image.height)
    ctx.drawImage(image,0,0,image.width,image.height)
};
image.src='/static/resources/chessboard.jpg'
*/
var c=document.createElement('img');
    c.id='board';
    c.style.position='absolute'
    c.style.top='0px';
    c.style.left='0px';
    c.setAttribute('width',1024);
    c.setAttribute('height',1024);
    c.setAttribute('src',"/static/resources/chessboard.jpg")
    document.body.appendChild(c);
function draw_chess(name,route,top,left) {
    var c=document.createElement('img');
    c.id=name;
    c.style.position='absolute'
    c.style.top=top.toString()+"px";
    c.style.left=left.toString()+"px";
    c.setAttribute('width',112.5);
    c.setAttribute('height',112.5);
    c.setAttribute('src',"/static/resources/"+route)
    document.body.appendChild(c);
}
