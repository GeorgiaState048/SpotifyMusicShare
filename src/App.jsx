/* eslint-disable linebreak-style */
/* eslint-disable react/button-has-type */
/* eslint-disable react/jsx-one-expression-per-line */
/* eslint-disable no-param-reassign */
/* eslint-disable camelcase */
// test
import './App.css';
import {
  useEffect, React,
} from 'react';
import env from 'react-dotenv';
import UserProfile from './components/UserProfile';
// import { FunFact } from './FunFact';

const SPOTIFY_KEY = env.CLIENT_ID; // insert your client id here from spotify
const SPOTIFY_AUTHORIZE_ENDPOINT = 'https://accounts.spotify.com/authorize';
const REDIRECT_URL_AFTER_LOGIN = 'http://10.250.34.208:8000/';
const SPACE_DELIMITER = '%20';
const SCOPES = [
  'user-read-currently-playing',
  'user-read-playback-state',
];
const SCOPES_URL_PARAM = SCOPES.join(SPACE_DELIMITER);
console.log(SPOTIFY_KEY);

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
    window.location = `${SPOTIFY_AUTHORIZE_ENDPOINT}?client_id=${SPOTIFY_KEY}&redirect_uri=${REDIRECT_URL_AFTER_LOGIN}&scope=${SCOPES_URL_PARAM}&response_type=token&show_dialog=true`;
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
