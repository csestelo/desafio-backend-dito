document.onreadystatechange = function () {
    if (document.readyState === 'complete') {
        let inputElement = document.getElementById('searchTerm');
        inputElement.oninput = function () {
            if (inputElement.value.length > 1) {
                let inputVal = inputElement.value;
                let myHeaders = new Headers({'Content-Type': 'application/json'});
                // gambi, modificar após implementar CORS
                let myInit = {method: 'GET', headers: myHeaders, mode: 'no-cors'};
                let url = 'http://localhost:5000/events?event_startswith=' + inputVal;
                let myRequest = new Request(url, myInit);

                fetch(myRequest).then(function (response) {
                    response.json().then(function (json) {
                            console.log(json)
                    })
                })
            }
        }
    }
};
