let gameArea = {
    canvas : document.createElement("canvas"),
    init : function() {
        this.canvas.width = 640;
        this.canvas.height = 640;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
    }
}
function component(width, height, input, x, y, type) {
    this.type = type;
    if (type == "image") {
        this.image = new Image();
        this.image.src = input;
    }
    this.width = width;
    this.height = height; 
    this.x = x;
    this.y = y;    
    this.update = function() {
        ctx = myGameArea.context;
            ctx.drawImage(this.image, 
                this.x, 
                this.y,
                this.width, this.height);
    }
}
let chessPiece = {b:{P:[[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2]],R:[[1,1],[8,1]],
    N:[[2,1],[7,1]],B:[[3,1],[6,1]],Q:[[4,1]],K:[[5,1]]},w:{P:[[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7]],R:[[1,8],[8,8]],
        N:[[2,8],[7,8]],B:[[3,8],[6,8]],Q:[[4,8]],K:[[5,8]]}
}
function create_piece(){
    for (let i in chessPiece){
        for (let j in i){
            for (k=0;k<j.length;k++){
                let (i+j+k) = new component(60,60,"/resources/"+(i+j)+".jpg",(k[0]-1)*80,(k[1]-1)*80,image)
            }
        }
    }
}
function create_scene(){
    let board = new component(640,640,"/resources/chessboard.jpg",0,0,image)
    create_piece()
}
function init(){
    gameArea.init()
    create_scene()
}
 function render(){
 }
init()