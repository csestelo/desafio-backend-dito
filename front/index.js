document.onreadystatechange = function () {
    if (document.readyState === 'complete') {
        let inputElement = document.getElementById('searchTerm');
        inputElement.oninput = function () {
            if (inputElement.value.length > 1) {
                let inputVal = inputElement.value;
                let url = 'http://localhost:5000/events?event_startswith=' + inputVal;
                let myRequest = new Request(url);

                fetch(myRequest)
                    .then(function (response) {
                        return response.json();
                    })
                    .then(function (content) {
                        console.log(content);
                    })
            }
        }
    }
};
