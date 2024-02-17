document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("add_field").addEventListener("click", function () {
        let items = document.getElementById("items");
        let newField = document.createElement("input");
        newField.setAttribute("type", "text");
        newField.setAttribute("name", "item-name");
        items.appendChild(newField);
    });
});
