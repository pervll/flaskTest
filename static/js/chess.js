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
    /*var c=document.createElement('img');
    c.id=name;
    c.style.position='absolute'
    c.style.top=top.toString()+"px";
    c.style.left=left.toString()+"px";
    c.setAttribute('width',112.5);
    c.setAttribute('height',112.5);
    c.setAttribute('src',"/static/resources/"+route)
    document.body.appendChild(c);*/
    var canvas=document.getElementById('board')
    var ctx=canvas.getContext("2d")
    var image=new Image();
    image.src='/static/resources/'+route
    image.onload = function() {
        ctx.drawImage(image,left,top,112.5,112.5)
    };
}

function render_chess(data){
    var rows=data.split('?')[0].split('/')
    var current=data.split('?')[1]
    var j=0
    for (var row of rows) {
        var k=0;
        for (var i=0;i<row.length;){
            var s=row[i]
            if (/^[a-z]$/.test(s)) {
                draw_chess(s,"black/"+s+".jpg",j*128+7.75,k*128+7.75)
            } 
            if (/^[A-Z]$/.test(s)) {
                draw_chess(s,"white/"+s+".jpg",j*128+7.75,k*128+7.75)
            }
            if (/^[1-9]$/.test(s)) {
                var s=row.slice(i,i+2)
                k+=parseInt(s.charAt(0))-1
                i++
            }
            k++
            i++
        } 
        j++   
    }
        
}
