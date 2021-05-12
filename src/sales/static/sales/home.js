console.log('Hello, World!');

const reportBtn = document.getElementById('report-btn');
const img = document.getElementById('img');
const modalBody = document.getElementById('modal-body');
const reportForm = document.getElementById('report-form');
const reportName = document.getElementById('id_name');
const reportRemarks = document.getElementById('id_remarks');
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;

if (img) {
  reportBtn.classList.remove('not-visible');
}

reportBtn.addEventListener('click', () => {
  img.setAttribute('class', 'w-100');
  modalBody.prepend(img);
  reportForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrf);
    formData.append('name', reportName.value);
    formData.append('remarks', reportRemarks.value);
    formData.append('image', img.src);

    $.ajax({
      type: 'POST',
      url: '/reports/save/',
      data: formData,
      success: (response) => console.log('response: ', response),
      error: (err) => console.log('err: ', err),
      processData: false,
      contentType: false,
    });
  });
});
