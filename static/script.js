var activeButton = null;

function toggleFilter(buttonId) {
    var button = document.getElementById(buttonId);
    var selectedFilterInput = document.getElementById('selectedFilter');

    if (button === activeButton) {
        button.classList.remove("active");
        activeButton = null;
        selectedFilterInput.value = "";  // No filter selected
    } else {
        if (activeButton) {
            activeButton.classList.remove("active");
        }
        button.classList.add("active");
        activeButton = button;
        selectedFilterInput.value = buttonId;  // Set the selected filter
    }
}
