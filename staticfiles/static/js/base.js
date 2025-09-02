document.querySelector('#searchForm1 .search-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        document.getElementById('searchForm1').submit();
    }
});