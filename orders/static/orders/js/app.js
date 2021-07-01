document.addEventListener("DOMContentLoaded",  () => {
    let limit = 0; //set limit

    checkboxes = document.querySelectorAll('.toppings'); //select all checkboxes

    function checker(elem) {
        if (elem.checked) { //if checked, increment counter
            limit++;
        } else {
            limit--; //else, decrement counter
        }

        for (i = 0; i < checkboxes.length; i++) { // loop through all 

            if (limit == 5) {
            if (!checkboxes[i].checked) {
                checkboxes[i].disabled = true; // and disable unchecked checkboxes

            }

            } else { //if limit is less than two

            if (!checkboxes[i].checked) {
                checkboxes[i].disabled = false; // enable unchecked checkboxes
            }

            }
        }

    }

        for (i = 0; i < checkboxes.length; i++) {
        checkboxes[i].onclick = function() { //call function on click and send current element as param
            checker(this);
        }
    }
});