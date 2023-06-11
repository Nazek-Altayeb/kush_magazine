document.addEventListener('DOMContentLoaded', () => {
    event.preventDefault();
    add_comment_button = document.getElementById('add_comment');
    comment_block = document.getElementById('comment_block');
    add_comment_button.addEventListener('click', function () {
        comment_block.style.display = block;
    });
});