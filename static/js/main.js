document.querySelector('input[placeholder="Search books..."]').addEventListener('keyup', (e) => {
    const term = e.target.value.toLowerCase();
    const books = document.querySelectorAll('.book-card');

    books.forEach(book => {
        const title = book.querySelector('h3').innerText.toLowerCase();
        if(title.indexOf(term) != -1) {
            book.style.display = 'block';
        } else {
            book.style.display = 'none';
        }
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchBar');
    
    if (searchInput) {
        searchInput.addEventListener('keyup', (e) => {
            const term = e.target.value.toLowerCase();
            const books = document.querySelectorAll('.book-card');

            books.forEach(book => {
                const title = book.querySelector('h3').innerText.toLowerCase();
                const author = book.querySelector('.author-name').innerText.toLowerCase();
                
                if (title.includes(term) || author.includes(term)) {
                    book.style.display = 'block';
                } else {
                    book.style.display = 'none';
                }
            });
        });
    }
});
// Search with a Fade-out/Fade-in animation
document.getElementById('searchBar').addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase();
    const books = document.querySelectorAll('.book-card');

    books.forEach(book => {
        const title = book.innerText.toLowerCase();
        if (title.includes(term)) {
            book.style.display = 'block';
            book.style.opacity = '1';
            book.style.transform = 'scale(1)';
        } else {
            book.style.opacity = '0';
            book.style.transform = 'scale(0.95)';
            setTimeout(() => {
                if(book.style.opacity === '0') book.style.display = 'none';
            }, 300);
        }
    });
});