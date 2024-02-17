var pythonData = JSON.parse(document.getElementById('python-data').textContent)

dataJSON = JSON.parse(pythonData)

$(document).ready(() => {
    $('.groceries-link').click(() => {
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: dataJSON["grocery_items"],
            success: function(res) {
                console.log('success')
            }
        })
    })

    $('.school-link').click(() => {
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: dataJSON["school_items"],
            success: function(res) {
                console.log('success')
            }
        })
    })
})