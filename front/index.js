document.onreadystatechange = function () {
    if (document.readyState === 'complete') {
        let inputElement = document.getElementsByClassName('searchTerm')[0];
        inputElement.onchange = function () {
            console.log(arguments)
        }
    }
};
