function addToList() {
    const input = document.getElementById("input-section");
    const list = document.getElementById("list-section");
    const item = document.createElement("li");
    
    // Create text span
    const textSpan = document.createElement("span");
    textSpan.textContent = input.value;
    
    // Create delete button
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.onclick = function() {
        deleteItem(item);
    };
    
    // Append text and button to item
    item.appendChild(textSpan);
    item.appendChild(deleteBtn);
    
    list.insertBefore(item, list.firstChild);
    input.value = "";
}

function deleteItem(item) {
    item.remove();
}