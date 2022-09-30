/**
 * Copyright 2018, Google LLC
 * Licensed under the Apache License, Version 2.0 (the `License`);
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an `AS IS` BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

'use strict';

if (typeof firebase === 'undefined') {
  const msg = "0) Please paste the Firebase initialization snippet into index.html. See https://console.firebase.google.com > Overview > Add Firebase to your web app.";
  console.log(msg);
  alert(msg);
}

// [START gae_python38_auth_javascript]
// [START gae_python3_auth_javascript]
window.addEventListener('load', function () {
  document.getElementById('sign-out').onclick = function () {
    firebase.auth().signOut();
    location.href='../login/';
  };

  // FirebaseUI config.
  var uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function(authResult, redirectUrl) {
        // User successfully signed in.
        // Return type determines whether we continue the redirect automatically
        // or whether we leave that to developer to handle.
        return true;
      },
      uiShown: function() {
        // The widget is rendered.
        // Hide the loader.
        document.getElementById('loader').style.display = 'none';
      }
    },
    // singInFlow: 'popup',
    signInSuccessUrl: '/demo',
    signInOptions: [
      // Comment out any lines corresponding to providers you did not check in
      // the Firebase console.
      // firebase.auth.GoogleAuthProvider.PROVIDER_ID,
      // firebase.auth.EmailAuthProvider.PROVIDER_ID,
      //firebase.auth.FacebookAuthProvider.PROVIDER_ID,
      //firebase.auth.TwitterAuthProvider.PROVIDER_ID,
      //firebase.auth.GithubAuthProvider.PROVIDER_ID,
      {
        provider: firebase.auth.PhoneAuthProvider.PROVIDER_ID,
        recaptchaParameters: {
          type: 'image', // 'audio'
          size: 'invisible', // 'invisible' or 'compact' or 'normal'
          badge: 'bottomleft' //' bottomright' or 'inline' applies to invisible.
        },

        defaultCountry: 'KR', // Set default country to the United Kingdom (+44).
        // For prefilling the national number, set defaultNationNumber.
        // This will only be observed if only phone Auth provider is used since
        // for multiple providers, the NASCAR screen will always render first
        // with a 'sign in with phone number' button.
        // defaultNationalNumber: '1234567890',
        // You can also pass the full phone number string instead of the
        // 'defaultCountry' and 'defaultNationalNumber'. However, in this case,
        // the first country ID that matches the country code will be used to
        // populate the country selector. So for countries that share the same
        // country code, the selected country may not be the expected one.
        // In that case, pass the 'defaultCountry' instead to ensure the exact
        // country is selected. The 'defaultCountry' and 'defaultNationaNumber'
        // will always have higher priority than 'loginHint' which will be ignored
        // in their favor. In this case, the default country will be 'GB' even
        // though 'loginHint' specified the country code as '+1'.
        // loginHint: '+11234567890'
      }
    ],
    // Terms of service url.
    tosUrl: '/policy',
    privacyPolicyUrl: '/policy'
  };

  firebase.auth().onAuthStateChanged(function (user) {
    if (user) {
      // User is signed in, so display the "sign out" button and login info.
      document.getElementById('sign-out').hidden = false;
      document.getElementById('login-info').hidden = false;
      var logInfo = document.getElementById('login-info');
      logInfo.hidden = false;
      logInfo.innerHTML = 'Signed in ' + user.phoneNumber;
      console.log('Signed in:');
      console.log(user.phoneNumber);
      user.getIdToken().then(function (token) {
        // Add the token to the browser's cookies. The server will then be
        // able to verify the token against the API.
        // SECURITY NOTE: As cookies can easily be modified, only put the
        // token (which is verified server-side) in a cookie; do not add other
        // user information.
        document.cookie = "token=" + token;
      });
    } else {
      // User is signed out.
      // Initialize the FirebaseUI Widget using Firebase.
      var ui = new firebaseui.auth.AuthUI(firebase.auth());
      // var ui = new firebaseui.auth.AuthUI(auth)
      // Show the Firebase login button.
      ui.start('#firebaseui-auth-container', uiConfig);
      // Update the login state indicators.
      document.getElementById('sign-out').hidden = true;
      document.getElementById('login-info').hidden = true;
      // document.getElementById('sign-out2').hidden = false;
      // document.getElementById('login-info').hidden = true;
      // Clear the token cookie.
      document.cookie = "token=";
      console.log("### 6) onAuthStateChanged Cookie ");
      console.log(document.cookie);
    }

  }, function (error) {
    console.log(error);
    alert('Unable to log in: ' + error)
  });
});

// [END gae_python3_auth_javascript]
// [END gae_python38_auth_javascript]