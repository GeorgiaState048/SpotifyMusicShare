/* eslint-disable linebreak-style */
/* eslint-disable react/button-has-type */
/* eslint-disable react/jsx-one-expression-per-line */
import './App.css';
// import {
//   useEffect, useState, React, useRef,
// } from 'react'
import React from 'react';
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
function App() {
  function handleLogin() {
    window.location = `${SPOTIFY_AUTHORIZE_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URL_AFTER_LOGIN}&scope=${SCOPES_URL_PARAM}&response_type=token&show_dialog=true`;
  }
  return (
    <body>
      <h1>Click Below to Login to your Spotify Account!</h1>
      <button onClick={handleLogin}>login to spotify</button>
    </body>
  );
}

export default App;
