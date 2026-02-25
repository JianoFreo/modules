function addToList() {
    const input = document.getElementById("input-section");
    const list = document.getElementById("list-section");
    const item = document.createElement("li");
    item.textContent = input.value;
    list.insertBefore(item, list.firstChild);  // Insert at beginning (stack behavior)
    input.value = "";
}