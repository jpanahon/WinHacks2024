// Sorry
let itemsNumber = 1;

function addItem() {
    itemsNumber++;

    let items = document.getElementById("items");
    let newItem = document.createElement("input");

    newItem.setAttribute("type", "text");
    newItem.setAttribute("name", "item-name");

    // Tailwind classes
    newItem.classList.add("border-black");
    newItem.classList.add("border-2");
    newItem.classList.add("p-2");

    let itemLabel = document.createElement("label");
    document.createElement("br");

    itemLabel.setAttribute("for", "item-name");
    itemLabel.innerHTML = `<br> <br>Item #${itemsNumber} Name <br>`;
    itemLabel.classList.add("font-semibold");
    itemLabel.classList.add("text-xl");

    items.appendChild(itemLabel);
    items.appendChild(newItem);

    let itemPrice = document.createElement("input");
    itemPrice.setAttribute("type", "number");
    itemPrice.setAttribute("name", `item-price-${itemsNumber}`);
    itemPrice.required = true;

    document.createElement("br");

    itemPrice.classList.add("border-black");
    itemPrice.classList.add("border-2");
    itemPrice.classList.add("p-2");

    let itemPriceTag = document.createElement("label");
    document.createElement("br");

    itemPriceTag.setAttribute("for", `item-price-${itemsNumber}`);
    itemPriceTag.innerHTML = `<br> <br>Item #${itemsNumber} Price<span class="text-red-600">*</span><br>`;
    itemPriceTag.classList.add("font-semibold");
    itemPriceTag.classList.add("text-xl");

    document.createElement("br");

    items.appendChild(itemPriceTag);
    items.appendChild(itemPrice);
}

function removeItem() {
    itemsNumber--;

    let itemList = document.getElementById("items");
    let items = itemList.getElementsByTagName("input");
    let labels = itemList.getElementsByTagName("label");

    if (items.length > 2) {
        itemList.removeChild(items[items.length - 1]);
        itemList.removeChild(items[items.length - 1]);
        itemList.removeChild(labels[labels.length - 1]);
        itemList.removeChild(labels[labels.length - 1]);
    }
}

function calculate() {
    let items = document.getElementById("items");
}
