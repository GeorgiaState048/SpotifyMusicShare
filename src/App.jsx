/* eslint-disable linebreak-style */
/* eslint-disable react/button-has-type */
/* eslint-disable react/jsx-one-expression-per-line */
/* eslint-disable no-param-reassign */
/* eslint-disable camelcase */

import './App.css';
import {
  useEffect, React,
} from 'react';
import UserProfile from './components/UserProfile';

// import { FunFact } from './FunFact';

const CLIENT_ID = '00d15048d06349268d294078fdd59e1d'; // insert your client id here from spotify
const SPOTIFY_AUTHORIZE_ENDPOINT = 'https://accounts.spotify.com/authorize';
const REDIRECT_URL_AFTER_LOGIN = 'http://192.168.1.82:8000/';
const SPACE_DELIMITER = '%20';
const SCOPES = [
  'user-read-currently-playing',
  'user-read-playback-state',
];
const SCOPES_URL_PARAM = SCOPES.join(SPACE_DELIMITER);
/*
http://192.168.1.82:8000/#access_token=BQBE4IwOP9gMx5rMd2bPvfin7W5AV3u4P1RFSbyX85NuEZwVT_c7mM-7jAeKAXp2K5jN6s_IIhBa3a33QxM8Bb_9Mue1y3XPq1KuWj2VF2vVQaKF-TuF5NUuxjXqScQ29_iAT34rSb9bs3WVUTJuZTq9kF8X_ZUV&token_type=Bearer&expires_in=3600
*/
const getReturnedParamsFromSpotifyAuth = (hash) => {
  const stringAfterHashtag = hash.substring(1);
  const paramsInUrl = stringAfterHashtag.split('&');
  const paramsSplitUp = paramsInUrl.reduce((accumulater, currentValue) => {
    const [key, value] = currentValue.split('=');
    accumulater[key] = value;
    return accumulater;
  }, {});
  return paramsSplitUp;
};

function App() {
  useEffect(() => {
    if (window.location.hash) {
      const {
        access_token,
        // expiresIn,
        // tokenType,
      } = getReturnedParamsFromSpotifyAuth(window.location.hash);
      localStorage.clear();

      localStorage.setItem('access_token', access_token);
      console.log('This is the App localStorage test', localStorage.getItem('access_token'));
    }
  });
  function handleLogin() {
    window.location = `${SPOTIFY_AUTHORIZE_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URL_AFTER_LOGIN}&scope=${SCOPES_URL_PARAM}&response_type=token&show_dialog=true`;
  }
  return (
    <body>
      <h1>Click Below to Login to your Spotify Account!</h1>
      <button onClick={handleLogin}>log in to spotify</button>
      <button onClick={handleLogin}>log in as a different user</button>
      <UserProfile />
    </body>
  );
}

export default App;
