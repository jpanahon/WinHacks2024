var pythonData = JSON.parse(document.getElementById('python-data').textContent)

dataJSON = JSON.parse(pythonData)

$(document).ready(() => {
    $('.groceries-link').click((e) => {
        e.preventDefault();
        $.ajax({
            url: '/filtered/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ filtered: dataJSON["grocery_items"] }),
            success: function(response) {
                updateHTML(response)
            }
        });
    });

    $('.school-link').click((e) => {
        e.preventDefault();
        $.ajax({
            url: '/filtered/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ filtered: dataJSON["school_items"] }),
            success: function(response) {
                updateHTML(response)
            }
        });
    });

    function updateHTML(data) {
        // Implement your logic to update the HTML content
        // For example, you might update a specific element with the filtered data
        var divs = document.getElementsByClassName('items-desc')
        for (let i = 0; i < 3; i++) {
            let key = 'item' + (i+1)
            console.log(data['items'][key])
            divs[i].getElementsByTagName('h3')[0].innerText = data['items'][key]['name']
            divs[i].getElementsByTagName('p')[0].innerText = data['items'][key]['price']
            divs[i].getElementsByTagName('p')[1].innerText = data['items'][key]['desc']
            divs[i].getElementsByTagName('p')[2].innerText = data['items'][key]['quantity']
        }
    }
});
