function previewImage(event) {
    var input = event.target;
    var reader = new FileReader();
    reader.onload = function(){
        var imgElement = document.getElementById('previewImg');
        imgElement.src = reader.result;
    };
    reader.readAsDataURL(input.files[0]);
}

document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault();
    let formData = new FormData();
    formData.append('image', document.getElementById('image').files[0]);

    // Fetch the CSRF token from the meta tag
    let csrfToken = document.head.querySelector('meta[name="csrf-token"]').content;

    let response = await fetch('/api/upload/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken  // Set the CSRF token in the headers
        },
        body: formData
    });

    let result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
};