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

    $('.devices-link').click((e) => {
        e.preventDefault();
        $.ajax({
            url: '/filtered/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ filtered: dataJSON["electronic_items"] }),
            success: function(response) {
                updateHTML(response)
            }
        });
    });

    $('.clothes-link').click((e) => {
        e.preventDefault();
        $.ajax({
            url: '/filtered/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ filtered: dataJSON["clothes_items"] }),
            success: function(response) {
                updateHTML(response)
            }
        });
    });

    function updateHTML(data) {
        // Implement your logic to update the HTML content
        // For example, you might update a specific element with the filtered data
        const divs = document.getElementsByClassName('items-desc')
        const itemBoxes = document.getElementsByClassName('item')

        for (let i = 0; i < 3; i++) {
            let key = 'item' + (i+1)
            divs[i].getElementsByTagName('h3')[0].innerText = data['items'][key]['name']
            divs[i].getElementsByTagName('p')[0].innerText = data['items'][key]['price']
            divs[i].getElementsByTagName('p')[1].innerText = data['items'][key]['desc']
            divs[i].getElementsByTagName('p')[2].innerText = data['items'][key]['quantity']
        }

        for (let i = 3; i < 9; i++) {
            itemBoxes[i].style.display = 'none'
            divs[i].style.display = 'none'
        }
    }
});
