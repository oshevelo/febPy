//-------Aux functions------------
const spinner = document.querySelector('#spinner');

function addSpinner() {
  spinner.classList.add("spinner--shown");
}

function removeSpinner() {
  spinner.classList.remove("spinner--shown");
}

function getCookieCsrf(){
  const value = `; ${document.cookie}`;
  const parts = value.split(`; csrftoken=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
async function getTextFromResponseBody(resp) {
    return await resp.text();
}

function getRequestHandlerDecorator(apiUrl, fillFunc, idInput=null){
    return function (evt){
        evt.preventDefault();
        addSpinner();
        const fullApiUrl = idInput===null? apiUrl : apiUrl + idInput.value;
        window.fetch(fullApiUrl)
        .then(response => {
          if (response.ok) {
            return response.json();
          }
          throw new Error(`${response.status}: ${response.errors}`);
        })
        .then(obj => {
            removeSpinner();
            fillFunc(obj)})
        .catch(error => {
          removeSpinner();
          alert(error);
        });
    }
}

function pppRequestHandlerDecorator(method, apiUrl, getBodyFunc, fillFunc, idInput=null, alertText=null, errorAlertText=null){
    return function (evt){
            evt.preventDefault();
            const body = getBodyFunc(evt);

            if (typeof body === 'string') {
                alert(body);
                return;
            }

            addSpinner();
            const fullApiUrl = idInput===null? apiUrl : apiUrl + idInput.value;
            window.fetch(fullApiUrl,
                {
                    method: method,
                    headers:{'Content-Type': 'application/json',
                            'X-CSRFTOKEN': getCookieCsrf()},
                    body: JSON.stringify(body),
                })
            .then(response => {
              if (response.ok) {
                return response.json();
              }
              throw response.text();
            })
            .then(obj => {
                removeSpinner();
                fillFunc(obj);
                if (alertText!==null){
                    alert(alertText);
                    }
                })
            .catch(error => {
                removeSpinner();
                (async () =>{
                    error_text = await error;
                    alert(`${errorAlertText}\n${error_text}`);
                    })();
                });

    };
}

//----------------User Profile---------------------
const apiProfileUrl = 'http://127.0.0.1:8000/api/userprofile/';



//--------------Filling functions--------------------
function getDataFromUserProfileForm(evt) {
        const body = {};
    body['username'] = document.querySelector('#user-profile-form #username').textContent;
    body['first_name'] = document.querySelector('#user-profile-form [name="first_name"]').value;
    body['last_name'] = document.querySelector('#user-profile-form [name="last_name"]').value;
    body['date_of_birth'] = document.querySelector('#user-profile-form [name="date_of_birth"]').value;
    body['sex'] = document.querySelector('#user-profile-form [name="sex"]').value;
    body['preferable_language'] = document.querySelector('#user-profile-form [name="preferable_language"]').value;

    const addr_info = document.querySelector('#user-profile-form #addresses');
    if (addr_info.children.length > 0){
        const addr_array = [];
        for (let i = 0; i < addr_info.children.length; i++) {
            addr_array.push(addr_info.children[i].value)
        }
        body['addresses_of_delivery'] = addr_array;
    }
    else{
        body['addresses_of_delivery'] = null;
    }

    const tel_info = document.querySelector('#user-profile-form #telephones');
    if (tel_info.children.length > 0){
        const tel_array = [];
        for (let i = 0; i < tel_info.children.length; i++) {
            tel_array.push(tel_info.children[i].value)
        }
        body['telephones'] = tel_array;
    }
    else{
        body['telephones'] = null;
    }

    const email_info = document.querySelector('#user-profile-form #add-emails');
    if (email_info.children.length > 0){
        const email_array = [];
        for (let i = 0; i < email_info.children.length; i++) {
            email_array.push(email_info.children[i].value)
        }
        body['additional_emails'] = email_array;
    }
    else{
        body['additional_emails'] = null;
    }
    return body;
}
function fillUserProfileForm(obj){
    // console.log(obj);
    const form = document.querySelector('#user-profile-form');
    const username = document.querySelector('#user-profile-form #username');
    username.textContent = obj.username;
    const first_name = document.querySelector('#user-profile-form [name="first_name"]');
    first_name.value = obj.first_name;
    const last_name = document.querySelector('#user-profile-form [name="last_name"]');
    last_name.value = obj.last_name;
    const date_of_birth = document.querySelector('#user-profile-form [name="date_of_birth"]');
    date_of_birth.value = obj.date_of_birth;
    const sex = document.querySelector('#user-profile-form [name="sex"]');
    sex.value = obj.sex;
    const preferable_language = document.querySelector('#user-profile-form [name="preferable_language"]');
    preferable_language.value = obj.preferable_language;

    const addr_info = document.querySelector('#user-profile-form #addresses');
    addr_info.innerHTML = "";
    if (obj.addresses_of_delivery) {
        obj.addresses_of_delivery.forEach((addr, idx) => {
                                                        const inp = document.createElement("input");
                                                        inp.setAttribute("name", `address-${idx}`);
                                                        inp.setAttribute("pattern", ".{3,100}");
                                                        inp.value = addr;
                                                        addr_info.appendChild(inp);
                                                        })
    }

    const tel_info = document.querySelector('#user-profile-form #telephones');
    tel_info.innerHTML = "";
    if (obj.telephones) {
        obj.telephones.forEach((tel, idx) => {
                                                        const inp = document.createElement("input");
                                                        inp.setAttribute("name", `tel-${idx}`);
                                                        inp.setAttribute("type", "tel");
                                                        inp.setAttribute("pattern", "^\\+?[0-9-]{7,16}");
                                                        inp.value = tel;
                                                        tel_info.appendChild(inp);
                                                        })
    }

    const add_email_info = document.querySelector('#user-profile-form #add-emails');
    add_email_info.innerHTML = "";
    if (obj.additional_emails) {
        obj.additional_emails.forEach((email, idx) => {
                                                        const inp = document.createElement("input");
                                                        inp.setAttribute("name", `email-${idx}`);
                                                        inp.setAttribute("type", "email");
                                                        inp.setAttribute("pattern", "\\w+@.+\\..+");
                                                        inp.setAttribute("maxlength", "50");
                                                        inp.value = email;
                                                        add_email_info.appendChild(inp);
                                                        })
    }

}
function getDataFromSignupForm(evt){
    const body = {}
    body['username'] = document.querySelector('#signup-form [name="username"]').value;
    body['email'] = document.querySelector('#signup-form [name="email"]').value;
    body['password'] = document.querySelector('#signup-form #password').value;
    const confirmPassword = document.querySelector('#signup-form #confirmPassword').value;

    if (body['password'] === confirmPassword ){
        document.querySelector('#signup-form').reset();
        return body;
    }
    else{
        return 'Password should be equal in both inputs!'
    }
}
function respondToSignUp(obj){
    console.log('respondToSignUp');
}

//----------------Create listeners-----------------
const getUserInfo = getRequestHandlerDecorator(apiProfileUrl, fillUserProfileForm);
const putUserInfo = pppRequestHandlerDecorator('PUT', apiProfileUrl, getDataFromUserProfileForm,
    fillUserProfileForm, null, 'User\'s profile updated', 'Update user error:');

const signupUser = pppRequestHandlerDecorator('POST',
    apiProfileUrl+'create/', getDataFromSignupForm, respondToSignUp, null, 'New user created!\nPlease find the activation link', 'Registration error:');

//-----------------Adding listeners------------------------
const userProfileTab = document.querySelector("#pills-profile-tab");
if (userProfileTab){
    userProfileTab.addEventListener('click', getUserInfo)
}

const userProfileForm = document.querySelector('#user-profile-form');
if (userProfileForm){
    userProfileForm.addEventListener('submit', putUserInfo);
    }

const signupForm = document.querySelector('#signup-form');
if (signupForm){
    signupForm.addEventListener('submit', signupUser);
    }