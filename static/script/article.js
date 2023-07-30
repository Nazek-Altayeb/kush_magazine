let comment_block;
let delete_block;
let bootstrap;

function comment() {
    comment_block = document.getElementById("comment_block");
    comment_block.style.display = "block";
}

function delete_article() {
    delete_block = document.getElementById("delete_block");
    delete_block.style.display = "block";
}

 setTimeout(function () {
            let messages = document.getElementById('msg');
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }, 2500);
