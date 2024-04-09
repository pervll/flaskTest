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

function render_chess(data){
    var rows=data.split('?')[0].split('/')
    var current=data.split('?')[1]
    var j=0
    for (var row of rows) {
        var k=0;
        for (var i=0;i<row.length;i=i+2){
            var s=row.slice(i,i+2)
            if (s.charAt(1)!="o"){
                if (/^[a-z]$/.test(s.charAt(1))) {
                    draw_chess(s,"black/"+s.charAt(1)+".svg",j*128+7.75,k*128+7.75)
                } else {
                    draw_chess(s,"white/"+s.charAt(1)+".svg",j*128+7.75,k*128+7.75)
                }
                k++
            } else {
                k+=parseInt(s.charAt(1))
            }
        }
        j++
    }
}