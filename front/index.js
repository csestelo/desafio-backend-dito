document.onreadystatechange = function () {
    if (document.readyState === 'complete') {
        let inputElement = document.getElementById('searchTerm');
        inputElement.oninput = async function () {
            if (inputElement.value.length > 1) {
                await callEventsApi(inputElement.value);
            }
            else removePreviousValue()
        }
    }
};

async function callEventsApi(inputVal) {
    let url = 'http://localhost:5000/events?event_startswith=' + inputVal;
    let myRequest = new Request(url);
    let resp = await fetch(myRequest);
    await handleResponse(resp)
}

async function handleResponse(resp) {
    removePreviousValue();

    if (resp.status === 404) {
        return ['Sem sugestões ...'].forEach(createElements)
    }
    else {
        let content = await resp.json();
        content['events'].forEach(createElements)
    }
}

function removePreviousValue() {
    let listItems = document.getElementById('listItems');
    if (listItems.children.length !== 0) {
        while (listItems.firstChild) {
            listItems.removeChild(listItems.firstChild);
        }
    }
}

function createElements(value, index, ar) {
    let newItem = document.createElement('option');
    let newContent = document.createTextNode(value);
    newItem.appendChild(newContent);

    let listItems = document.getElementById('listItems');
    listItems.appendChild(newItem);
}
