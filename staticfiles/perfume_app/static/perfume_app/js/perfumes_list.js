document.querySelectorAll('#searchForm input[type="checkbox"]').forEach(checkbox => {
    checkbox.addEventListener('change', event => {
         event.stopPropagation();
         document.getElementById('searchForm').submit();
    });
});

document.getElementById('clearCheckboxes').addEventListener('click', () => {
    document.querySelectorAll('#searchForm input[type="checkbox"]').forEach(cb => cb.checked = false);
    document.getElementById('searchForm').submit();
});