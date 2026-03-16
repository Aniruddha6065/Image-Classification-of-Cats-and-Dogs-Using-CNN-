document.addEventListener("DOMContentLoaded", function() {

    const dropArea = document.getElementById("drop-area");
    const fileInput = document.getElementById("fileInput");

    dropArea.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropArea.style.background = "#333";
    });

    dropArea.addEventListener("dragleave", (e) => {
        dropArea.style.background = "rgba(26, 26, 29, 0.8)";
    });

    dropArea.addEventListener("drop", (e) => {
        e.preventDefault();
        dropArea.style.background = "rgba(26, 26, 29, 0.8)";
        fileInput.files = e.dataTransfer.files;
    });

});