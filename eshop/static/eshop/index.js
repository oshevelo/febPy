

const spinner = document.querySelector('#spinner');


//----------Template request function---------------
function templateFunc (func, inputs, textToOutput, outputField) {
  return function (evt) {
    evt.preventDefault();
    addSpinner();

    const values = inputs.map(item => item.value.trim());
    func.apply(null, values)

    .then(data => {
      removeSpinner();
      outputField.innerHTML = `<p>${textToOutput}</p><pre>${data}</pre>`;
    })
    .catch(error => {
      removeSpinner();
      outputField.innerHTML = `<p>${error}</p>`;
    });
    this.reset();
  }
}

//---------User profile-------------------
const apiProfileUrl = 'http://127.0.0.1:8000/api/userprofiles/';

const getUserProfileForm = document.querySelector('#getUserProfileForm');
const userID = document.querySelector('#getUserProfileForm input[name="userID"]')


const userProfileOutputField = document.querySelector('#userProfileOutputField');

function getUserProfile(id) {

  return window.fetch(apiProfileUrl + id)
    .then(response => {
      if (response.ok) {
        return response.json();
      }
      throw new Error(`${response.status}: ${response.errors}`);
    })
    .then(data => {
        return JSON.stringify(data, null, 2);
        })
}

const handleGetUserProfileFormSubmit = templateFunc(getUserProfile,
                                                [
                                                    userID
                                                ],
                                                'User profile info has been fetched',
                                                userProfileOutputField);
getUserProfileForm.addEventListener('submit', handleGetUserProfileFormSubmit);




//-------Aux functions------------

function addSpinner() {
  spinner.classList.add("spinner--shown");
}

function removeSpinner() {
  spinner.classList.remove("spinner--shown");
}