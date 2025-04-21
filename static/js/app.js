const fileInput = document.getElementById('image');
const fileLabel = document.querySelector('label[for="image"]');

fileInput.addEventListener('change', function () {
  if (fileInput.files.length > 0) {
    fileLabel.textContent = fileInput.files[0].name;
  } else {
    fileLabel.textContent = 'Choose Image';
  }
});