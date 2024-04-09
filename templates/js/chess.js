document.getElementById("test").innerHTML = "chess online"
var chessing = false
//define object acting as canvas
var gameArea = {
    canvas : document.getElementById("board"),
    init : function() {
        this.canvas.width = 1024;
        this.canvas.height = 1024;
        this.context = this.canvas.getContext("2d");
        //document.body.insertBefore(this.canvas, document.body.childNodes[0]);
    }
}
//define object acting as chesspiece
function component(width, height, input, x, y, type , name) {
    this.type = type;
    this.name = name
    if (type == "image") {
        this.image = new Image(width,height);
        this.image.src = input;
    }
    this.width = width;
    this.height = height; 
    this.x = x;
    this.y = y;    
<<<<<<< Updated upstream:templates/js/chess.js
    this.update = function() {
        ctx = myGameArea.context;
=======
    this.draw = function() {
        ctx = gameArea.context;
>>>>>>> Stashed changes:static/js/chess2.js
            ctx.drawImage(this.image, 
                this.x, 
                this.y,
                this.width, this.height);
    }
}
//piece positions to send
var chessPiecePos = {black:{p:[[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2]],r:[[1,1],[8,1]],
    n:[[2,1],[7,1]],b:[[3,1],[6,1]],q:[[4,1]],k:[[5,1]]},white:{p:[[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7]],r:[[1,8],[8,8]],
        n:[[2,8],[7,8]],b:[[3,8],[6,8]],q:[[4,8]],k:[[5,8]]}
}
//create chesspiece objects
function create_piece(){
    var chessPiece = []
    let path = ""
    let newOb
    for (let i in chessPiecePos){
        for (let j in i){
            for (k=0;k<j.length;k++){
<<<<<<< Updated upstream:templates/js/chess.js
                let (i+j+k) = new component(60,60,"/resources/"+(i+j)+".jpg",(k[0]-1)*80,(k[1]-1)*80,image)
=======
                path = "/static/resources/" + toString(i) + "/" + toString(j) + ".jpg"
                newOb =  new component(96,96,path,((k[0]-1)*128+64),((k[1]-1)*128+64),image ,(i+j+k))
                chessPiece.push(newOb)
>>>>>>> Stashed changes:static/js/chess2.js
            }
        }
    }
}
<<<<<<< Updated upstream:templates/js/chess.js
function create_scene(){
    let board = new component(640,640,"/resources/chessboard.jpg",0,0,image)
    create_piece()
=======
//main game loop after init
function mainloop(){
    while (chessing){
        render()
    }
>>>>>>> Stashed changes:static/js/chess2.js
}
function init(){
    chessing = true
    gameArea.init()
<<<<<<< Updated upstream:templates/js/chess.js
    create_scene()
}
init()
=======
    let board = new component(1024,1024,"/static/resources/chessboard.jpg",0,0,image)
    create_piece()
    mainloop()
}
//draw everything for every frame
function render(){
    board.draw()
    for (let i in chessPiece){
        i.draw()
    }
}
//start initalization upon loaded
document.addEventListener("load",init())
>>>>>>> Stashed changes:static/js/chess2.js
